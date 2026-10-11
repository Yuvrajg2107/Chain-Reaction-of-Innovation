"""Verify planning artifacts. This does not test a product or engineering model."""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
# Optional temporary installation used on the authoring host.
if (ROOT / "tmp/doc-deps").exists():
    sys.path.insert(0, str(ROOT / "tmp/doc-deps"))
from jsonschema import Draft202012Validator, FormatChecker
from pypdf import PdfReader


def check_pack(pack):
    collections = ["entities", "parameters", "evidence", "relations", "models", "applications", "scenarios"]
    for collection in collections:
        ids = [record["id"] for record in pack[collection]]
        assert len(ids) == len(set(ids)), f"Duplicate IDs in {collection}"
    entity_ids = {record["id"] for record in pack["entities"]}
    parameter_ids = {record["id"] for record in pack["parameters"]}
    evidence_ids = {record["id"] for record in pack["evidence"]}
    models = {record["id"]: record for record in pack["models"]}
    for parameter in pack["parameters"]:
        assert parameter["entity_id"] in entity_ids
        if "minimum" in parameter and "maximum" in parameter:
            assert parameter["minimum"] <= parameter["maximum"]
    for relation in pack["relations"]:
        assert relation["source_id"] in entity_ids and relation["target_id"] in entity_ids
        assert set(relation["evidence_ids"]) <= evidence_ids
    for model in pack["models"]:
        assert model["entity_id"] in entity_ids
        assert set(model["evidence_ids"]) <= evidence_ids
        assert not set(model["input_slots"]) & set(model["output_slots"])
    for application in pack["applications"]:
        model = models[application["model_id"]]
        assert set(application["inputs"]) == set(model["input_slots"])
        assert set(application["outputs"]) == set(model["output_slots"])
        assert set(application["inputs"].values()) <= parameter_ids
        assert set(application["outputs"].values()) <= parameter_ids
        assert set(model["assumptions"]) <= set(application["required_conditions"])
    for scenario in pack["scenarios"]:
        assert set(scenario["values"]) <= parameter_ids
        if "target" in scenario:
            assert scenario["target"]["parameter_id"] in parameter_ids
    if pack["status"] == "synthetic_fixture":
        assert all(scenario["expected_state"] == "unresolved" for scenario in pack["scenarios"])
        assert all(model["review"] == "unreviewed" for model in pack["models"])


def main():
    errors = []
    md_files = [ROOT / "README.md", ROOT / "AGENTS.md"] + list((ROOT / "docs").rglob("*.md")) + list((ROOT / "sources").glob("*.md")) + list((ROOT / "examples").glob("*.md"))
    for path in md_files:
        content = path.read_text(encoding="utf-8")
        for target in re.findall(r"!?\[[^\]]*\]\(([^)]+)\)", content):
            if target.startswith(("http:", "https:", "mailto:")):
                continue
            target = target.split("#")[0]
            if target and not (path.parent / target).resolve().exists():
                errors.append(f"Broken local link: {path.relative_to(ROOT)} -> {target}")
        # Contact data copied from the supplied roster is not needed in tracked prose.
        if re.search(r"\b(?:7498186674|8482926363|9604651265|9156406879|9970944211)\b|@vit\.edu", content):
            errors.append(f"Personal contact data in {path.relative_to(ROOT)}")
    schema = json.loads((ROOT / "schemas/domain-pack.schema.json").read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    fixtures = list((ROOT / "examples").glob("*.json"))
    for path in fixtures:
        pack = json.loads(path.read_text(encoding="utf-8"))
        for error in validator.iter_errors(pack):
            errors.append(f"Schema violation {path.name}: {error.message}")
        check_pack(pack)
    report = ROOT / "reports/ChainReaction_Analysis_and_Plan.pdf"
    reader = PdfReader(report)
    text = "\n".join(page.extract_text() or "" for page in reader.pages)
    for required in ["Product requirements document", "Evaluation protocol", "Novelty assessment", "Source register", "Implementation plan"]:
        if required not in text:
            errors.append(f"Missing report section: {required}")
    if any(not (page.extract_text() or "").strip() for page in reader.pages):
        errors.append("Blank PDF page")
    if errors:
        print("\n".join(errors))
        raise SystemExit(1)
    print(json.dumps({"markdown_files": len(md_files), "contract_fixtures": len(fixtures), "report_pages": len(reader.pages),
                      "report_words": len(text.split()), "broken_local_links": 0, "contact_data_hits": 0,
                      "scope": "documentation and schema checks only"}, indent=2))


if __name__ == "__main__":
    main()
