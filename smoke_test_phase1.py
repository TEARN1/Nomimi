from main_pipeline_advanced import orchestrate_advanced_system

if __name__ == "__main__":
    res = orchestrate_advanced_system()
    assert res['constraints']['all_ok'], "Constraints failed"
    assert len(res['pareto_front']) >= 1, "Pareto front empty"
    print("Phase 1 smoke test passed.")