"""Mechanical ontology for engine components (Phase 1).
Future: add hierarchical relationships, materials, failure modes, and lifecycle states."""

ENGINE_ONTOLOGY = {
    "block": {"category": "structure", "children": ["cylinder", "coolant_jacket", "oil_gallery"]},
    "cylinder": {"category": "combustion_chamber", "attributes": ["bore", "stroke", "count"]},
    "piston": {"category": "reciprocating", "attributes": ["diameter", "compression_height", "pin_diameter"]},
    "connecting_rod": {"category": "reciprocating", "attributes": ["c_to_c_length", "big_end_bore", "small_end_bore"]},
    "crankshaft": {"category": "rotating", "attributes": ["main_journal_dia", "rod_journal_dia", "overall_length"]},
    "valve_intake": {"category": "valvetrain", "attributes": ["head_dia", "stem_dia", "length"]},
    "valve_exhaust": {"category": "valvetrain", "attributes": ["head_dia", "stem_dia", "length"]},
    "camshaft": {"category": "valvetrain", "attributes": ["journal_dia", "lobe_lift", "length"]},
    "intake_runner": {"category": "induction", "attributes": ["inner_dia", "length"]},
    "exhaust_primary": {"category": "exhaust", "attributes": ["inner_dia", "length"]},
    "injector": {"category": "fuel_system", "attributes": ["flow_cc_min", "body_length"]},
    "spark_plug": {"category": "ignition", "attributes": ["thread", "reach"]},
    "oil_pump": {"category": "lubrication", "attributes": ["impeller_od"]},
    "water_pump": {"category": "cooling", "attributes": ["impeller_od"]},
    "turbo_compressor": {"category": "forced_induction", "attributes": ["inducer_dia"]},
    "turbo_turbine": {"category": "forced_induction", "attributes": ["exducer_dia"]},
    "radiator": {"category": "cooling", "attributes": ["core_width", "core_height", "core_thickness"]}
}