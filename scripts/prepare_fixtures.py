"""Create explicitly synthetic contract fixtures and the privacy-safe source record."""
import hashlib
import json
from pathlib import Path

from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]


def main():
    source = ROOT / "sources/edi_ff180_final.local.pdf"
    reader = PdfReader(source)
    excerpt = "# Privacy-safe synopsis excerpt\n\nSource pages 3-12, excluding header-only page 11. This is extracted source text, not a new claim of approval.\n\n"
    for index in list(range(2, 10)) + [11]:
        excerpt += f"## Source page {index + 1}\n\n{reader.pages[index].extract_text()}\n\n"
    excerpt = "\n".join(line.rstrip() for line in excerpt.splitlines()).rstrip() + "\n"
    (ROOT / "sources/synopsis-excerpt.md").write_text(excerpt, encoding="utf-8")
    manifest = {
        "source_name": "edi_ff180_final.pdf",
        "pages": len(reader.pages),
        "sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "review_date": "2026-10-12",
        "original_storage": "local-only; excluded from Git due to personal contact data",
        "tracked_excerpt_pages": list(range(3, 11)) + [12],
        "technical_figures": [8, 9],
        "figure_9_limit": "source image cropped on right and bottom",
        "source_rendering": "Poppler compressed-stream warnings; page review completed",
        "publication_rights": "not established for public redistribution"
    }
    (ROOT / "sources/manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    entities = [{"id": name, "label": label, "layer": layer} for name, label, layer in [
        ("lamp", "Illustrative lamp", "product"),
        ("thermal", "Illustrative thermal path", "subsystem"),
        ("interface", "Illustrative interface layer", "component"),
        ("material", "Synthetic material", "material"),
        ("conduction", "Steady conduction principle", "principle"),
        ("eq", "Illustrative layer thermal model", "model")]]
    parameters = [{"id": name, "entity_id": entity, "quantity_kind": kind, "unit": unit} for name, entity, kind, unit in [
        ("L", "interface", "length", "m"), ("A", "interface", "area", "m^2"),
        ("k", "material", "thermal_conductivity", "W/(m*K)"),
        ("Q", "thermal", "heat_flow", "W"), ("dT", "interface", "temperature_difference", "K")]]
    evidence = [{"id": "synthetic", "title": "Invented planning fixture; no scientific validation",
                 "source_type": "synthetic", "locator": "docs/reasoning-spec.md illustrative calculation",
                 "review": "unreviewed", "reuse": "Project-authored synthetic fixture"}]
    relations = [{"id": "r1", "source_id": "interface", "target_id": "thermal", "category": "structural", "predicate": "part_of", "origin": "manual", "review": "unreviewed", "evidence_ids": ["synthetic"]}]
    model = {"id": "model-1", "entity_id": "eq", "registry_key": "illustrative_conduction_drop_v1",
             "input_slots": ["L", "A", "k", "Q"], "output_slots": ["dT"],
             "assumptions": ["steady_state", "one_dimensional", "constant_k"],
             "evidence_ids": ["synthetic"], "review": "unreviewed"}
    application = {"id": "app-1", "model_id": "model-1", "configuration_id": "synthetic-config-1",
                   "inputs": {k: k for k in model["input_slots"]}, "outputs": {"dT": "dT"},
                   "required_conditions": model["assumptions"]}
    values = {key: {"value": value, "unit": unit, "origin": "synthetic"} for key, value, unit in [
        ("L", .001, "m"), ("A", .001, "m^2"), ("k", 1, "W/(m*K)"), ("Q", 2, "W") ]}
    # Unreviewed model is deliberately unresolved in all fixture scenarios.
    scenarios = [{"id": "forward-unreviewed", "configuration_id": "synthetic-config-1", "direction": "forward",
                  "values": values, "conditions": {k: True for k in model["assumptions"]}, "expected_state": "unresolved"},
                 {"id": "missing-k", "configuration_id": "synthetic-config-1", "direction": "forward",
                  "values": {k: v for k, v in values.items() if k != "k"}, "conditions": {"steady_state": None}, "expected_state": "unresolved"},
                 {"id": "backward-unreviewed", "configuration_id": "synthetic-config-1", "direction": "backward",
                  "values": {k: v for k, v in values.items() if k != "k"}, "conditions": {k: True for k in model["assumptions"]},
                  "target": {"parameter_id": "dT", "operator": "<=", "value": 1, "unit": "K"}, "expected_state": "unresolved"}]
    pack = {"id": "synthetic-thermal-fixture", "version": "0.1.0", "status": "synthetic_fixture", "entities": entities,
            "parameters": parameters, "evidence": evidence, "relations": relations, "models": [model], "applications": [application], "scenarios": scenarios}
    (ROOT / "examples/synthetic-domain-pack.json").write_text(json.dumps(pack, indent=2) + "\n", encoding="utf-8")
    print("Prepared manifest, privacy-safe excerpt, and synthetic contract fixture.")


if __name__ == "__main__":
    main()
