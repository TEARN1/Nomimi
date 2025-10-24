# Nomimi — Repository Blueprint
This document defines a comprehensive structure and artifact list to make Nomimi a multidisciplinary engineering & science platform for projects (smart‑glasses, i20 computer, Pluto habitat, etc.). The structure covers research, design, simulation, verification, supply chain, governance, long‑term preservation — and power & energy systems essential to every project.

Goals
- Capture research and standards (papers, datasets, patents).
- Store deterministic engineering artifacts (PRDs, block diagrams, BOMs, schematics, CAD).
- Host simulation & analysis code (notebooks, FEA, thermal, radiation, orbital).
- Contain firmware, OS build scripts, test suites, and CI.
- Provide templates for compliance, risk, and long‑term archives.
- Enable reproducible builds and automated validation pipelines.

Top-level directories (what to add)
- /docs
  - Purpose: high-level docs, PRDs, roadmap, meeting notes, governance.
  - Example files:
    - PRD-TEMPLATE.md
    - ROADMAP.md
    - GOVERNANCE.md (roles, access, review process)
    - STANDARDS-AND-LICENSES.md (applicable standards, licenses)

- /research
  - Purpose: curated literature, data sources, IP/patent review, standards mapping.
  - Example files:
    - literature-bibliography.bib
    - STANDARDS-MAPPING.md (IEC, FCC, ISO, ASTM, medical regs)
    - DATASETS.md (links + ingestion scripts)
    - PATENT-SCAN.md

- /projects
  - Purpose: per-project engineering workspaces.
  - Structure: /projects/<project-name>/{requirements,architecture,hw,sw,sims,tests,manufacturing,compliance}
  - Example: /projects/nomimi-smart-glasses/
    - requirements.md
    - system-architecture.svg / .drawio
    - BOM.csv and BOM-choices.md
    - pcb/ (schematics, KiCad)
    - cad/ (STLs, STEP, CAD-README)
    - firmware/ (bootloader, OS, drivers)
    - mobile/ (companion app)
    - sims/ (optical simulation scripts, trs)
    - test-plans.md
    - suppliers.md

- /hw
  - Purpose: electronics parts, reference schematics, footprints, hardware test benches.
  - Example files:
    - PARTS-LIBRARY.md
    - reference-schematics/ (KiCad/Altium projects)
    - footprints/
    - hw-test-jigs/ (assembly & ATE specs)

- /sw
  - Purpose: OS images, build systems, CI config, drivers, apps, SDKs.
  - Example files:
    - yocto/ or buildroot/
    - docker/ (containers for builds)
    - ci/ (GitHub Actions workflows)
    - sw-architecture.md

- /sims
  - Purpose: simulation, modelling, notebooks, parameter sweeps, saved results.
  - Subfolders: thermal/, structural/, optics/, rf/, orbital/, systems/
  - Artifact types: Jupyter notebooks, Python modules, SPICE netlists, COMSOL export notes, OpenMC/MCNP config, FEA Meshing.

- /data
  - Purpose: validated datasets and processed test logs (kept small, or hosted externally with links).
  - Includes: material properties, component spec spreadsheets, New Horizons data references for Pluto, telemetry logs.

- /manufacturing
  - Purpose: DFM/DFX guidelines, supplier lists, quotes, tooling, assembly instructions.
  - Example: DFM-CHECKLIST.md, CM-ONBOARDING.md, supplier-catalog.csv

- /safety-compliance
  - Purpose: safety cases, risk registers, certification checklists (FCC/CE/IEC/etc.), eye‑safety, battery regs.
  - Example: RISK-REGISTER.md, COMPLIANCE‑MATRIX.csv

- /knowledge-preservation
  - Purpose: long‑term archiving, metadata, reproducible snapshots, DOI/archival notes.
  - Example: ARCHIVAL.md, data-package.json, release-manifests/

- /tools
  - Purpose: automation scripts, part lookup, BOM tools, cost calculators.
  - Example: scripts/bom-normalize.py, scripts/cost-estimate.py

- /community
  - Purpose: contribution guidelines, code of conduct, maintainers, communication channels.
  - Files: CONTRIBUTING.md, CODE_OF_CONDUCT.md, TEAM.md

- /legal
  - Purpose: licenses, IP policy, export control notes.
  - Files: LICENSE, IP-POLICY.md, EXPORT-CONTROL.md

- /archive
  - Purpose: retired designs, DO‑NOT‑USE warnings, historical baselines.

- /power
  - Purpose: centralized place for power & energy systems artifacts, templates, and safety guidance used across projects.
  - Example files:
    - POWER-SOURCES.md (catalog of energy sources: batteries, RTGs, fission, solar, ISRU)
    - POWER-BUDGET-TEMPLATE.ipynb (notebook for system power budgeting)
    - BATTERY-REQUIREMENTS.md (battery selection, safety, transport, lifecycle)
    - RTG-FISSION-GUIDE.md (nuclear power considerations and servicing)
    - GRID-ARCHITECTURES.md (microgrid, redundancy, distribution)

Essential files / templates to create first
- PRD-TEMPLATE.md — product requirements doc template with acceptance criteria.
- BOM-CSV-TEMPLATE.csv — standardized BOM columns (ref, qty, MPN, footprint, cost, supplier, lead time, alt parts).
- SCHEMATIC-README.md — how to add schematics with preferred toolchain rules.
- CAD-README.md — how to submit STEP/STL and coordinate frames.
- SIMULATION-TEMPLATE.ipynb — sample notebook for thermal or power budget simulation.
- TEST-PLAN-TEMPLATE.md — unit/system/integration acceptance tests.
- RISK-REGISTER.md — risk, likelihood, impact, mitigation, owner.
- COMPLIANCE-MATRIX.csv — map features to required standards and test labs.
- RELEASE-SNAPSHOT.md — format for releases with manifest of artifacts and checksums.
- POWER-SOURCES.md — energy source catalog and recommended templates (also added under /power).

CI and automation (recommend)
- GitHub Actions workflows:
  - docs-build: build & publish docs site (MkDocs or Sphinx).
  - linting and static checks (python, shellcheck).
  - sim-tests: run small deterministic sims (unit tests) in containers.
  - bom-check: validate BOM format & prices.
  - cad-check: validate new CAD assets added follow naming rules (via CI scripts).
- Containerized reproducible environments: Docker images for build toolchains (Yocto, KiCad headless, simulation libs).

Research & standards capture
- Create a Standards Matrix per project mapping:
  - Feature → Standard (IEC / ISO / IEEE / FCC / FDA) → Test needed → Estimated cost → Lab contacts
- Curate canonical references:
  - Keep bibliographic entries (.bib) and a short summary for each important paper or dataset.

Simulations & validation
- Start with simple deterministic models:
  - Mass & energy budgets (spreadsheet + notebook).
  - Thermal steady‑state & transient approximations.
  - Structural FEA for enclosures (open formats for interchange).
  - Optical raytrace for displays (Zemax/OpticStudio notes or open alternatives).
  - Radiation & micrometeoroid flux estimation for Pluto habitat (use available tools).
- Document assumptions and provenance for each sim run.

Hardware & supply chain
- Maintain a living supplier registry with:
  - supplier name, part categories, reliability score, lead times, contact info, alternate suppliers.
- Track end‑of‑life (EOL) warnings and pin MPNs with alternatives.

Security, firmware & trust
- Secure boot & update design doc.
- Firmware signing & chain of custody processes.
- Threat model per project (e.g., privacy for smart glasses, safety for habitat reactors).

Long‑term operation & governance (important for 10k year thinking)
- Knowledge preservation policies: multiple redundant archival formats, geo‑distributed archives, periodic integrity checks.
- Maintenance & generational training plan: competency matrix, apprenticeship, automated training curricula (simulators & labs).
- Governance artifacts: decision logs, architecture review board, emergency playbooks.

Suggested onboarding tasks (first 12 weeks)
1. Add PRD template and create the first PRD for Nomimi‑Smart‑Glasses.
2. Seed /projects/nomimi-smart-glasses with system architecture and BOM-CSV-TEMPLATE.
3. Add SIMULATION-TEMPLATE.ipynb with a basic power & mass budget.
4. Add CONTRIBUTING.md, CODE_OF_CONDUCT.md, and TEAM.md.
5. Add initial CI workflows (docs-build + bom-check + lint).
6. Curate a /research/literature-bibliography.bib with 10 canonical references per domain (optics, CPU/SoC selection, life support basics).

Prioritization guidance
- Week 0–2: governance, templates, PRD, CONTRIBUTING (low friction, big impact).
- Week 2–6: seed one project workspace end‑to‑end (PRD -> architecture -> BOM -> sim).
- Week 6–12: CI for deterministic checks and simulation regression tests, add CAD and schematic submission rules.

Where I can help next (pick one)
- I can generate the PRD-TEMPLATE.md and commit it to TEARN1/Nomimi.
- I can seed /projects/nomimi-smart-glasses with requirements, BOM.csv and a simple power/mass simulation notebook.
- I can create GitHub Actions workflow files for docs‑build and bom‑check.
- I can produce a `STANDARDS-MAPPING.md` for smart glasses and the Pluto habitat (mapping features to required tests/standards).

Which of those should I create first and push to the repo? (If you want, I’ll start by creating PRD-TEMPLATE.md and CONTRIBUTING.md and push them to TEARN1/Nomimi.