# POWER-SOURCES — Catalog and Guidance

Purpose
- Provide a centralized reference for energy sources that projects in Nomimi may use.
- Describe trade-offs, key selection criteria, safety/regulatory notes, and recommended artifacts to include in each project.

Scope
- Short list of commercially available and conceptual power sources: batteries (Li-ion, LiFePO4, solid-state), fuel cells, solar (photovoltaic), thermal (RTG), fission reactors, (conceptual) fusion, chemical fuels, ISRU-derived fuels, and microgrid architectures.
- Guidance for selection, integration, safety, lifecycle, and long-term sustainment (including multi-decade/century scenarios).

1. Overview of Energy Sources
- Batteries
  - Types: Li-ion (NMC, NCA), LiFePO4, Li-poly, NiMH, solid-state (emerging).
  - Use cases: portable devices, short‑term buffering, UPS, hybrid systems.
  - Pros: high energy density, mature supply chain.
  - Cons: degradation, thermal runaway risk, transport restrictions, finite cycle life.
  - Key metrics: energy density (Wh/kg, Wh/L), cycle life, C-rate, operating temperature range, self-discharge, calendar life, cost ($/kWh), safety certifications (IEC 62133, UN38.3).

- Fuel Cells
  - Types: PEMFC, SOFC, direct methanol.
  - Use cases: longer-duration mobile power, backup with fuel logistics.
  - Pros: good energy/power ratio, quiet.
  - Cons: fuel supply, catalysts, humidity/temperature sensitivity.

- Solar Photovoltaic (PV)
  - Use cases: terrestrial and near-Sun environments; limited utility in low-insolation contexts (outer solar system).
  - Pros: renewable, low maintenance.
  - Cons: low output in low-light environments; need for large area; degradation (radiation and micrometeoroids in space).

- Radioisotope Thermoelectric Generators (RTGs) and Radioisotope Heater Units (RHUs)
  - Use cases: deep-space probes, remote unmanned sites.
  - Pros: reliable multi-decade baseline power.
  - Cons: low power density, radioactive material handling/regulatory burden, eventual decay.

- Fission Reactors
  - Use cases: high continuous power for habitats, industrial sites (terrestrial or off-Earth).
  - Pros: high power, refuelable (depending on design).
  - Cons: complexity, shielding, refueling & reprocessing logistics, regulatory & political constraints.

- (Conceptual) Fusion
  - Use cases: theoretical multi-megawatt to gigawatt power with abundant fuel.
  - Status: research-stage; do not assume availability for baseline designs.

- Chemical Fuels / Combustion Generators
  - Use cases: backup power or mobile power where fuels are available.
  - Pros: mature technology.
  - Cons: emissions, supply chain, maintenance.

- In-Situ Resource Utilization (ISRU)
  - Use cases: extraction of volatiles/ice to produce fuels (H2, CH4), processing for power systems.
  - Cons: requires complex processing plants and initial equipment delivery.

2. Selection Criteria & Decision Matrix
- Functional requirements: power peak, continuous power, energy storage, mission duration.
- Environmental constraints: temperature range, radiation, gravity, atmospheric composition.
- Mass & volume budget: Wh/kg and Wh/L targets.
- Reliability & maintenance: MTBF, serviceability, spare parts.
- Safety & certification: transport (UN), installation (local/national), radiation handling.
- Supply & lifecycle: fuel availability, recycling, end-of-life handling.
- Cost & scalability: $/kWh energy delivered over lifecycle, initial CapEx vs OpEx.
- Long-term sustainment: repairability, raw material availability, recyclability, ability to manufacture replacement parts in-situ.

3. Architectures & Integration Patterns
- Hybrid systems: batteries + primary generator (fission/RTG) + renewables for redundancy and load smoothing.
- Microgrid topologies: centralized generation vs distributed nodes, protective relays, islanding capability, energy management systems (EMS).
- Energy buffering & UPS design: sizing batteries for critical loads and safe shutdown.
- Thermal integration: use waste heat from reactors/engines for habitat heating or industrial processes.

4. Safety, Standards & Regulations
- Batteries: IEC 62133 (portable cells), UN Manual of Tests and Criteria (UN38.3), IEC 62619 (industrial cells), IEC 62281 (transportation & packaging), IEC 62133 for cell/battery safety testing.
- Nuclear: national nuclear regulatory frameworks, IAEA guidance, waste handling, licensing for reactors/RTGs.
- Electrical safety: local electrical codes, grounding/bonding, overcurrent protection, EMC/EMI for power electronics.
- Environmental & transport: RoHS, REACH, hazardous materials regs.

5. Long-term & Multi-decade Considerations
- Lifecycle provisioning: spare-part mass and replacement strategy, component commonality to simplify logistics.
- Degradation & aging: accelerated testing, refurbishment schedules, end-of-life recycling.
- Autonomous operation & fault recovery: diagnostic telemetry, prognostics, autonomous repair/robotics integration.
- Knowledge preservation: maintenance manuals, training curricula, parts fabrication recipes (including 3D-printable feeds).

6. Recommended Artifacts (per project)
- POWER-BUDGET-TEMPLATE.ipynb — base notebook for steady-state and transient power budgeting.
- BATTERY-REQUIREMENTS.md — battery selection checklist and acceptance criteria.
- RTG-FISSION-GUIDE.md — summary of nuclear power options, servicing, and high-level safety constraints.
- GRID-ARCHITECTURES.md — templates for microgrid design and protective device selection.
- POWER-SAFETY-CASE.md — project-specific safety case, hazard analysis (FMEA/FMECA), and mitigation plan.

7. Suggested Next Steps for Nomimi
- Create BATTERY-REQUIREMENTS.md and populate with templated acceptance tests and safety checks.
- Add a POWER-BUDGET-TEMPLATE.ipynb in /power/sims and seed with a sample load profile (mobile device, habitat, and remote probe).
- For each active project, require a filled power-budget and a recommended power architecture as part of the PRD review checklist.

References & further reading
- IEC 62133, UN Manual of Tests and Criteria (UN38.3), IAEA technical documents on RTGs and small reactors.
- Battery consortium whitepapers (e.g., NREL, DOE reports), IEEE power electronics references.