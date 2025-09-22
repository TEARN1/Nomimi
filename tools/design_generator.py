#!/usr/bin/env python3
"""
tools/design_generator.py

Simple Prompt -> Design Markdown generator for Nomimi.
Usage:
    python tools/design_generator.py "Design a modular rocket factory in South Africa"
Produces:
    designs/<slug>_design.md
"""
import os
import sys
import datetime
import re

TEMPLATE = """# {title}

Generated: {date}

## 1. Objectives
{objectives}

## 2. System Architecture
{architecture}

## 3. 3D Visualization Plan
{visualization}

## 4. Engineering Breakdown
{engineering}

## 5. Standards & Compliance
{standards}

## 6. Feasibility Analysis
{feasibility}

## 7. Action Items & GitHub Issues
{actions}

## 8. References
{references}
"""

def slugify(s):
    s = s.lower()
    s = re.sub(r'[^a-z0-9]+', '-', s).strip('-')
    return s[:80]

def simple_expand(prompt):
    # Very small heuristic expansions — replace later with AI or templates
    title = prompt.strip().capitalize()
    objectives = "- High-level: " + prompt + "\n- Deliverables: modular 3D model, engineering plan, feasibility report"
    architecture = "- Major subsystems: power, structure, control, safety, production (if factory)\n- Interfaces: mechanical, electrical, data"
    visualization = "- Assets: GLB/GLTF for each module\n- Thumbnails and manifest for quick loading\n- Annotation overlays for critical systems"
    engineering = "- Materials, actuators, sensors, power estimates\n- Initial assumptions: pilot mass 80kg, system mass TBD"
    standards = "- Identify domain-specific standards (TBD)"
    feasibility = "- Quick checks: estimated mass, rough thrust/power numbers, major risks"
    actions = "- Model each subsystem\n- Create simulation stubs\n- Create GitHub issues for each task"
    references = "- Add relevant real-world references and links"
    return {
        "title": title,
        "objectives": objectives,
        "architecture": architecture,
        "visualization": visualization,
        "engineering": engineering,
        "standards": standards,
        "feasibility": feasibility,
        "actions": actions,
        "references": references
    }

def main():
    if len(sys.argv) < 2:
        print("Usage: python tools/design_generator.py \"<prompt>\"")
        sys.exit(1)
    prompt = " ".join(sys.argv[1:])
    content = simple_expand(prompt)
    date = datetime.datetime.utcnow().isoformat() + "Z"
    md = TEMPLATE.format(date=date, **content)
    slug = slugify(content["title"])
    out_dir = os.path.join("designs")
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, f"{slug}_design.md")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(md)
    print(f"Generated: {out_file}")

if __name__ == "__main__":
    main()