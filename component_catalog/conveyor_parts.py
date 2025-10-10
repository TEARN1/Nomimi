"""Seed conveyor component catalog (minimal initial set)."""
CONVEYOR_PARTS = [
    {
        "part_id": "conv.belt.std.1200x",
        "family_id": "belt.standard",
        "category": "conveyor/belt",
        "geometry": {"width_m": 1.2, "thickness_mm": 10},
        "performance": {"max_speed_mps": 3.0, "max_load_kg_m": 450},
        "lifecycle": {"mtbf_hours": 20000},
        "materials": [{"name": "reinforced_polymer", "mass_per_meter_kg": 12.5}],
        "compat": {"roller_diameters_mm": [50, 63, 89]},
        "constraints": ["design_belt_speed_mps <= performance.max_speed_mps"],
        "provenance": {"source": "seed_catalog_v1"}
    },
    {
        "part_id": "conv.roller.std.d63",
        "family_id": "roller.standard",
        "category": "conveyor/roller",
        "geometry": {"diameter_mm": 63, "face_length_mm": 1250},
        "performance": {"rpm_limit": 600, "load_rating_N": 3500},
        "lifecycle": {"mtbf_hours": 40000},
        "materials": [{"name": "galvanized_steel", "mass_kg": 4.2}],
        "compat": {"belt_width_range_m": [0.6, 1.2]},
        "constraints": [],
        "provenance": {"source": "seed_catalog_v1"}
    },
    {
        "part_id": "conv.drive.motor.45kw",
        "family_id": "drive.motor",
        "category": "conveyor/drive",
        "geometry": {"frame_size": "180M"},
        "performance": {"power_kw": 45, "efficiency": 0.94},
        "lifecycle": {"mtbf_hours": 60000},
        "materials": [{"name": "steel_housing", "mass_kg": 320}],
        "compat": {"voltage": "400VAC"},
        "constraints": [],
        "provenance": {"source": "seed_catalog_v1"}
    }
]
