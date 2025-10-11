"""
Test suite for new Nomimi capability modules.
Run with: pytest -q
"""

import pytest
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from data_integration import DataIngestor, DataPipeline
from human_factors import HumanFactorsModel, RegulatoryMonitor
from novelty_manager import PrototypeManager
from optimization_engine import OptimizationEngine
from dependency_graph import DependencyGraph
from ux_conversation import EnhancedConversationalInterface
from validation_integration import TestPlanExporter, HardwareInLoopStub, FieldTrialTracker
from threat_modeling import ThreatModel
from scalability_planner import ScalabilityPlanner


def test_data_integration():
    """Test data integration module."""
    ingestor = DataIngestor()
    
    # Test REST stub
    result = ingestor.fetch_rest("http://example.com/api", "GET")
    assert "status" in result
    assert result["status"] == "stub"
    
    # Test pipeline
    pipeline = DataPipeline()
    records = [{"Name": "Test", "Value": 123}]
    normalized = pipeline.normalize(records)
    assert len(normalized) == 1
    assert "name" in normalized[0]
    
    # Test validation
    valid, invalid = pipeline.validate(normalized, required_fields=["name"])
    assert len(valid) == 1
    assert len(invalid) == 0


def test_human_factors():
    """Test human factors module."""
    hf = HumanFactorsModel()
    
    hf.set_task_load(0.7)
    assert hf.task_load == 0.7
    assert hf.error_rate > 0.01
    
    hf.add_crew_member("Alice", "Engineer", 0.9)
    assert len(hf.crew_members) == 1
    
    perf = hf.calculate_performance_factor()
    assert 0.0 <= perf <= 1.0
    
    summary = hf.get_summary()
    assert "task_load" in summary
    assert summary["crew_count"] == 1


def test_novelty_manager():
    """Test novelty manager module."""
    pm = PrototypeManager()
    
    hypotheses = pm.propose_hypotheses("Test problem", 3)
    assert len(hypotheses) == 3
    assert "id" in hypotheses[0]
    
    exp = pm.design_experiments(hypotheses[0]["id"])
    assert "test_cases" in exp
    assert len(exp["test_cases"]) > 0
    
    result = pm.record_results(exp["id"], 1, {"metric": 0.9})
    assert "experiment_id" in result
    
    summary = pm.get_summary()
    assert summary["hypotheses_count"] == 3


def test_optimization_engine():
    """Test optimization engine module."""
    from spaceship_design import SpaceshipDesign
    
    optimizer = OptimizationEngine()
    design = SpaceshipDesign(population=1000)
    
    results = optimizer.optimize(design, objectives=["cost", "risk"], max_generations=5)
    assert "pareto_front_size" in results
    assert results["pareto_front_size"] > 0
    
    summary = optimizer.get_summary()
    assert "pareto_front_size" in summary


def test_dependency_graph():
    """Test dependency graph module."""
    graph = DependencyGraph()
    
    graph.add_component("A", "mechanical")
    graph.add_component("B", "electrical")
    graph.add_dependency("A", "B")
    
    assert len(graph.nodes) == 2
    assert len(graph.edges) == 1
    
    topo_order = graph.topological_sort()
    assert len(topo_order) == 2
    
    summary = graph.get_summary()
    assert summary["nodes"] == 2
    assert summary["edges"] == 1


def test_ux_conversation():
    """Test enhanced UX conversation module."""
    ux = EnhancedConversationalInterface()
    
    response = ux.interact("What are the risks?")
    assert isinstance(response, str)
    assert len(response) > 0
    
    suggestions = ux.get_suggestions()
    assert isinstance(suggestions, list)
    assert len(suggestions) > 0
    
    summary = ux.get_summary()
    assert "turns" in summary
    assert summary["turns"] == 1


def test_validation_integration():
    """Test validation integration module."""
    # Test plan exporter
    exporter = TestPlanExporter()
    exporter.add_test_case("TC001", "Test description", "Procedure", "Expected")
    
    json_plan = exporter.export_json()
    assert "test_cases" in json_plan
    
    md_plan = exporter.export_markdown()
    assert "TC001" in md_plan
    
    # HIL stub
    hil = HardwareInLoopStub()
    assert hil.connect("device1") == True
    
    result = hil.run_test("test1", {})
    assert result["status"] == "pass"
    
    # Field tracker
    tracker = FieldTrialTracker()
    tracker.register_trial("FT001", "Location A", "Description")
    tracker.record_outcome("FT001", "success", {"metric": 0.95})
    
    summary = tracker.get_summary()
    assert summary["trials_registered"] == 1


def test_threat_modeling():
    """Test threat modeling module."""
    tm = ThreatModel()
    
    tm.add_threat("T001", "S", "Spoofing attack", 8, 0.5)
    assert len(tm.threats) == 1
    
    risk_score = tm.calculate_risk_score(8, 0.5)
    assert risk_score == 4.0
    
    high_risk = tm.get_high_risk_threats(threshold=3.0)
    assert len(high_risk) == 1
    
    summary = tm.get_summary()
    assert summary["total_threats"] == 1


def test_scalability_planner():
    """Test scalability planner module."""
    planner = ScalabilityPlanner()
    
    planner.set_workload(users=10000, requests_per_second=200, data_size_gb=500)
    assert planner.workload_assumptions["concurrent_users"] == 10000
    
    arch = planner.plan_architecture()
    assert "application_tier" in arch
    assert arch["application_tier"]["replicas"] >= 2
    
    costs = planner.estimate_costs()
    assert "total" in costs
    assert costs["total"] > 0
    
    recommendations = planner.get_ha_recommendations()
    assert isinstance(recommendations, list)
    assert len(recommendations) > 0


def test_main_pipeline():
    """Test that main pipeline runs without errors."""
    from main_pipeline import orchestrate_ultra_complex_system
    
    results = orchestrate_ultra_complex_system()
    
    # Check existing keys still present
    assert "spaceship_desc" in results
    assert "knowledge" in results
    assert "risks" in results
    
    # Check new capability keys
    assert "data_summary" in results
    assert "human_factors" in results
    assert "novelty_plan" in results
    assert "optimization_summary" in results
    assert "dependencies" in results
    assert "ux_guidance" in results
    assert "validation_plan" in results
    assert "threat_model" in results
    assert "scalability_plan" in results


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
