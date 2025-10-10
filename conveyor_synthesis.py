"""Conveyor synthesis scaffold: derives belt width, speed, power, and selects basic parts."""
import math
from typing import Dict, Any, List
from component_schema import Part, AssemblyResult
from provenance_chain import ProvenanceChain
from explainability_graph import ExplainabilityGraph
from component_catalog.conveyor_parts import CONVEYOR_PARTS

def _pick_discrete(value: float, options: List[float]):
    return min(options, key=lambda x: abs(x - value))

def synthesize_conveyor(req: Dict[str, Any]) -> AssemblyResult:
    required_keys = ["throughput_tph", "bulk_density_kg_m3", "length_m", "incline_deg"]
    for k in required_keys:
        if k not in req:
            raise ValueError(f"Missing required key: {k}")

    provenance = ProvenanceChain()
    explain = ExplainabilityGraph()

    context = dict(req)
    parts: List[Part] = []

    g = 9.81
    throughput_tph = context["throughput_tph"]
    mass_flow_kg_s = (throughput_tph * 1000) / 3600
    context["mass_flow_kg_s"] = mass_flow_kg_s
    explain.add("mass_flow", {"mass_flow_kg_s": mass_flow_kg_s})
    provenance.record({"type": "calc", "key": "mass_flow_kg_s", "value": mass_flow_kg_s})

    candidate_speeds = [1.2, 1.5, 1.8, 2.0, 2.2]
    belt_speed = context.get("belt_speed_mps", 1.8)
    belt_speed = _pick_discrete(belt_speed, candidate_speeds)
    context["design_belt_speed_mps"] = belt_speed

    bulk_density = context["bulk_density_kg_m3"]
    fill_factor = 0.6
    cross_section_area_m2 = mass_flow_kg_s / (bulk_density * belt_speed)
    required_width_m = math.sqrt(cross_section_area_m2 / fill_factor)

    available_widths = [0.5, 0.6, 0.75, 0.9, 1.05, 1.2]
    chosen_width_m = _pick_discrete(required_width_m, available_widths)
    context["belt_width_m"] = chosen_width_m

    explain.add("belt_geometry", {
        "cross_section_area_m2": cross_section_area_m2,
        "required_width_m": required_width_m,
        "selected_width_m": chosen_width_m,
        "belt_speed_mps": belt_speed
    }, parents=["mass_flow"])
    provenance.record({"type": "decision", "stage": "belt_width", "value": chosen_width_m})

    material_mass_per_meter = bulk_density * cross_section_area_m2
    belt_mass_per_meter = 12.5 if chosen_width_m >= 1.0 else 9.0
    roller_mass_contrib = 3.0
    mass_per_meter = material_mass_per_meter + belt_mass_per_meter + roller_mass_contrib

    incline_deg = context["incline_deg"]
    elevation_component = math.sin(math.radians(incline_deg))
    rolling_resistance = 0.02
    resistive_force = mass_per_meter * g * (rolling_resistance + elevation_component)
    motor_power_kw = resistive_force * belt_speed / 1000 / 0.85
    context["motor_power_kw_est"] = motor_power_kw

    explain.add("power_estimation", {
        "mass_per_meter": mass_per_meter,
        "resistive_force_N": resistive_force,
        "motor_power_kw": motor_power_kw
    }, parents=["belt_geometry"])
    provenance.record({"type": "calc", "stage": "power", "motor_power_kw": motor_power_kw})

    selected_belt = selected_drive = selected_roller = None
    for p in CONVEYOR_PARTS:
        if p["category"] == "conveyor/belt" and abs(p["geometry"]["width_m"] - chosen_width_m) < 0.05:
            selected_belt = Part(**p)
        if p["category"] == "conveyor/drive" and p["performance"]["power_kw"] >= motor_power_kw * 1.15:
            if not selected_drive or p["performance"]["power_kw"] < selected_drive.performance["power_kw"]:
                selected_drive = Part(**p)
        if p["category"] == "conveyor/roller":
            if p["compat"]["belt_width_range_m"][0] <= chosen_width_m <= p["compat"]["belt_width_range_m"][1]:
                selected_roller = Part(**p)

    for comp, label in [(selected_belt, "belt"), (selected_drive, "drive"), (selected_roller, "roller")]:
        if comp:
            provenance.record({"type": "select", "component": label, "part_id": comp.part_id})
            explain.add(f"select_{label}", {"part_id": comp.part_id}, parents=["power_estimation"])

    constraints_report = {
        "belt_speed_ok": bool(selected_belt and belt_speed <= selected_belt.performance["max_speed_mps"]),
        "power_margin_ok": bool(selected_drive and selected_drive.performance["power_kw"] >= motor_power_kw * 1.15)
    }
    explain.add("constraints_conveyor", constraints_report, parents=["select_drive"])  # may be orphan if drive missing
    provenance.record({"type": "constraints", "report": constraints_report})

    parts = [p for p in [selected_belt, selected_drive, selected_roller] if p]

    derived = {
        "belt_speed_mps": belt_speed,
        "belt_width_m": chosen_width_m,
        "motor_power_kw_est": motor_power_kw
    }

    return AssemblyResult(
        assembly_id="conveyor_line_auto_1",
        parts=parts,
        derived=derived,
        variants=[],
        constraints_report=constraints_report,
        explainability_nodes=explain.graph(),
        provenance=provenance.all()
    )
