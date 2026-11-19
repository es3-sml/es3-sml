"""
<!-- ********************************************************************************
 * Copyright (c) 2026 Schwarz Digits Cloud GmbH & Co. KG
 *
 * This program and the accompanying materials are made available under the
 * terms of the Creative Commons Attribution-ShareAlike 4.0 International Public License
 * which is available at https://creativecommons.org/licenses/by-sa/4.0/.
 *
 * SPDX-License-Identifier: CC-BY-SA-4.0
 *
 * Contributors:
 *   Andy Riexinger - initial contribution
 ******************************************************************************* -->
 """
#!/usr/bin/env python3
"""
ES³ SML Framework — MkDocs Generator from Master JSON (v7 Edition)
==================================================================
Generates MkDocs documentation pages from the master JSON file (`sml_data.json`).
Features:
  - Exact formatting matching SDC specifications
  - Horizontal divider (`---`) at the end of each Control Objective block
  - Automatic generation of the summary mapping table at the end of each dimension
    ("Mapping of the Objectives to the corresponding Sovereignty Maturity Level")
    derived from the `requirements` field of each control.
"""

import sys
import os
import json
import re
import argparse
from pathlib import Path

DIMENSION_SLUGS = {
    "SML 1": "sml1-strategic",
    "SML 2": "sml2-legal",
    "SML 3": "sml3-data",
    "SML 4": "sml4-operational",
    "SML 5": "sml5-supply-chain",
    "SML 6": "sml6-technology",
    "SML 7": "sml7-security",
    "SML 8": "sml8-environmental",
    "SML 9": "sml9-ai",
}

COPYRIGHT_HEADER = """<!-- ********************************************************************************
 * Copyright (c) 2026 Schwarz Digits Cloud GmbH & Co. KG
 *
 * This program and the accompanying materials are made available under the
 * terms of the Creative Commons Attribution-ShareAlike 4.0 International Public License
 * which is available at https://creativecommons.org/licenses/by-sa/4.0/.
 *
 * SPDX-License-Identifier: CC-BY-SA-4.0
 *
 * Contributors:
 *   Andy Riexinger - initial contribution
 ******************************************************************************* -->"""

SML2_INFO_BOX = """!!! note "Approved Jurisdictions List (AJL)"
    Please find an example for an Approved Jurisdictions List (AJL) [here](https://es3-sml.github.io/es3-sml/schema/)"""

def clean_id(raw_id: str) -> str:
    m = re.match(r"^(SML\s*\d+\.CO\s*\d+(\.C\s*\d+)?)", raw_id.strip())
    if m:
        return m.group(1).strip()
    return raw_id.split("(")[0].strip()

def extract_level_from_id(raw_id: str) -> str:
    m = re.search(r"\(([^)]+)\)", raw_id)
    if m:
        return m.group(1).replace("&", "&").strip()
    return "Governance & Operations"

def clean_co_title(raw_title: str) -> tuple[str, str]:
    cleaned = re.sub(r"\(SML\s*\d+\.CO\s*\d+\)", "", raw_title).strip()
    if " - " in cleaned:
        parts = cleaned.split(" - ", 1)
        return parts[0].strip(), parts[1].strip()
    elif ":" in cleaned:
        parts = cleaned.split(":", 1)
        return parts[0].strip(), parts[1].strip()
    return cleaned, ""

def generate_markdown(catalog_data: dict, docs_dir: Path, overview_file: str = "overview.md", check_only: bool = False) -> bool:
    dim_dir = docs_dir / "dimensions"
    dim_dir.mkdir(parents=True, exist_ok=True)
    all_synced = True
    all_dimensions_data = []

    items = catalog_data.items() if isinstance(catalog_data, dict) else enumerate(catalog_data)

    for key, dim_info in items:
        if not isinstance(dim_info, dict):
            continue

        raw_name = str(key)
        m = re.match(r"^(SML\s*\d+)", raw_name)
        dim_prefix = m.group(1) if m else raw_name
        slug = DIMENSION_SLUGS.get(dim_prefix, dim_prefix.lower().replace(" ", "-"))
        target_file = dim_dir / f"{slug}.md"

        dim_title = dim_info.get("dimension_title", dim_info.get("name", raw_name))
        dim_desc = dim_info.get("dimension_desc", dim_info.get("description", ""))

        if not dim_title.startswith("SML"):
            h1_title = f"{dim_prefix} — {dim_title}"
        else:
            h1_title = dim_title

        md = []
        md.append(COPYRIGHT_HEADER)
        md.append("")
        md.append(f"# {h1_title}\n")
        if dim_desc:
            md.append(f"*{dim_desc}*\n")
        md.append("---\n")

        # SML 2 specific Info Box (Admonition)
        if dim_prefix == "SML 2":
            md.append(SML2_INFO_BOX)
            md.append("")
            md.append("---\n")

        objectives = dim_info.get("objectives", dim_info.get("control_objectives", []))
        controls_for_table = []

        for obj in objectives:
            co_id = obj.get("id", "").strip()
            co_raw_title = obj.get("title", co_id)
            short_name, extracted_target = clean_co_title(co_raw_title)

            target_state = obj.get("objective", obj.get("target_state", extracted_target))
            sovereignty_contribution = obj.get("sovereignty_contribution", "")

            md.append(f"## {co_id} {short_name}\n")
            if target_state:
                md.append(f"**Objective:** {target_state}  ")
            if sovereignty_contribution:
                md.append(f"*Sovereignty Contribution:* {sovereignty_contribution}\n")
            else:
                md.append("\n")

            controls = obj.get("controls", [])
            for ctrl in controls:
                c_raw_id = ctrl.get("id", "").strip()
                c_id = clean_id(c_raw_id)
                level = ctrl.get("level", extract_level_from_id(c_raw_id))
                scope = ctrl.get("control_scope", ctrl.get("scope", "Service Provider"))
                service_type = ctrl.get("service_type", "All")
                desc = ctrl.get("desc", ctrl.get("description", ""))
                question = ctrl.get("question", "")

                q_id = ctrl.get("question_id", f"{c_id}.Q 1")
                if not q_id.startswith(c_id):
                    q_id = f"{c_id}.Q 1"

                md.append(f"### {c_id} ({level})\n")
                md.append(f"* **Scope:** {scope}")
                md.append(f"* **Service Type:** {service_type}")
                if desc:
                    md.append(f"* {desc}")
                if question:
                    md.append(f"* **{q_id}:** {question}\n")
                else:
                    md.append("\n")

                # Store for summary table
                reqs = ctrl.get("requirements", {})
                controls_for_table.append({
                    "id": c_id,
                    "initial": reqs.get("initial", False),
                    "managed": reqs.get("managed", False),
                    "advanced": reqs.get("advanced", False),
                    "future_proof": reqs.get("future_proof", False),
                })

            # Trennlinie nach jedem Control Objective Block
            md.append("---\n")

        # Summary Mapping Table at the end
        if controls_for_table:
            md.append("## Mapping of the Objectives to the corresponding Sovereignty Maturity Level\n")
            md.append("| ID | Initial | Managed | Advanced | Future-Proof |")
            md.append("|:---|:---:|:---:|:---:|:---:|")
            for c in controls_for_table:
                init_x = "x" if c["initial"] else ""
                man_x = "x" if c["managed"] else ""
                adv_x = "x" if c["advanced"] else ""
                fp_x = "x" if c["future_proof"] else ""
                md.append(f"| {c['id']} | {init_x} | {man_x} | {adv_x} | {fp_x} |")
            md.append("\n")

        content = "\n".join(md)

        if check_only:
            if not target_file.exists():
                print(f"❌ Out of sync: {target_file} does not exist.")
                all_synced = False
            elif target_file.read_text(encoding="utf-8") != content:
                print(f"❌ Out of sync: {target_file} differs from master JSON.")
                all_synced = False
            else:
                print(f"✅ In sync: {target_file}")
        else:
            target_file.write_text(content, encoding="utf-8")
            print(f"  ✓ Rendered: {target_file}")

        all_dimensions_data.append({
            "title": h1_title,
            "controls": controls_for_table
        })


    # Generate complete overview page: docs/overview.md
    if all_dimensions_data:
        target_overview = docs_dir / overview_file
        ov_md = [
            COPYRIGHT_HEADER,
            "",
            "# Mapping Overview of the Objectives to the corresponding Sovereignty Maturity Level (complete list)\n",
            "*Comprehensive overview mapping all controls across all nine dimensions of the ES³ Sovereignty Maturity Level (SML) Framework to their respective maturity levels (Initial, Managed, Advanced, Future-Proof).*\n",
            "---\n",
            "| ID | Initial | Managed | Advanced | Future-Proof |",
            "|:---|:---:|:---:|:---:|:---:|"
        ]
        for d in all_dimensions_data:
            ov_md.append(f"| **{d['title']}** | | | | |")
            for c in d["controls"]:
                init_x = "x" if c["initial"] else ""
                man_x = "x" if c["managed"] else ""
                adv_x = "x" if c["advanced"] else ""
                fp_x = "x" if c["future_proof"] else ""
                ov_md.append(f"| {c['id']} | {init_x} | {man_x} | {adv_x} | {fp_x} |")
        ov_md.append("\n")
        ov_content = "\n".join(ov_md)

        if check_only:
            if not target_overview.exists():
                print(f"❌ Out of sync: {target_overview} does not exist.")
                all_synced = False
            elif target_overview.read_text(encoding="utf-8") != ov_content:
                print(f"❌ Out of sync: {target_overview} differs from master JSON.")
                all_synced = False
            else:
                print(f"✅ In sync: {target_overview}")
        else:
            target_overview.write_text(ov_content, encoding="utf-8")
            print(f"  ✓ Rendered Complete Overview: {target_overview}")

    return all_synced

def main():
    parser = argparse.ArgumentParser(description="Generate MkDocs Markdown files with dividers and Mapping Table from master JSON.")
    parser.add_argument("--input", "-i", default="docs/sml_data.json", help="Path to master sml_data.json")
    parser.add_argument("--docs-dir", "-d", default="docs", help="Path to MkDocs docs directory")
    parser.add_argument("--overview-file", "-o", default="overview.md", help="Filename for the complete overview page (relative to docs-dir)")
    parser.add_argument("--check", action="store_true", help="Check synchronization without writing")
    args = parser.parse_args()

    json_path = Path(args.input)
    if not json_path.exists():
        if Path("sml_data.json").exists():
            json_path = Path("sml_data.json")
        else:
            print(f"❌ Error: Master JSON not found at '{args.input}'.")
            sys.exit(1)

    print(f"📖 Reading Master JSON from: {json_path}...")
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    success = generate_markdown(data, Path(args.docs_dir), overview_file=args.overview_file, check_only=args.check)
    if args.check:
        if success:
            print("🎉 Success: All MkDocs dimension pages match the master JSON!")
            sys.exit(0)
        else:
            print("❌ Failure: Documentation is out of sync with JSON.")
            sys.exit(1)
    else:
        print(f"\n✨ Generation Complete! All dimension pages synchronized from JSON in '{args.docs_dir}/dimensions'.")

if __name__ == "__main__":
    main()
