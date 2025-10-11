"""
Smoke tests for Nomimi system.

Tests basic functionality of new modules and pipeline integration.
"""

import pytest
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from data_integration import DataIngestor, DataPipeline
from human_factors import HumanFactorsModel, RegulatoryMonitor
from novelty_manager import PrototypeManager, NoveltyManager
from optimization_engine import OptimizationEngine
from dependency_graph import DependencyGraph
from ux_conversation import StatefulConversationalInterface
from validation_integration import TestPlanExporter, HardwareInLoopStub, FieldTrialTracker
from threat_modeling import ThreatModeler
from scalability_planner import ScalabilityPlanner
from main_pipeline import orchestrate_ultra_complex_system


class TestDataIntegration:
    """Test data integration module."""
    
    def test_data_ingestor_csv(self):
        ingestor = DataIngestor()
        data = ingestor.load_csv("nonexistent.csv")
        assert isinstance(data, list)
        assert len(data) > 0
        assert isinstance(data[0], dict)
    
    def test_data_ingestor_json(self):
        ingestor = DataIngestor()
        data = ingestor.load_json("nonexistent.json")
        assert isinstance(data, dict)
        assert "status" in data
    
    def test_data_ingestor_rest(self):
        ingestor = DataIngestor()
        data = ingestor.fetch_rest("http://example.com/api")
        assert isinstance(data, dict)
        assert "status" in data
    
    def test_data_ingestor_subscribe(self):
        ingestor = DataIngestor()
        sub_id = ingestor.subscribe_topic("test_topic")
        assert isinstance(sub_id, str)
        assert "subscription" in sub_id
    
    def test_data_pipeline_normalize(self):
        pipeline = DataPipeline()
        data = {"Name": "Test", "VALUE": 123}
        normalized = pipeline.normalize(data)
        assert "name" in normalized
        assert "value" in normalized
    
    def test_data_pipeline_validate(self):
        pipeline = DataPipeline()
        data = {"field1": "value1", "field2": "value2"}
        ok, issues = pipeline.validate(data, required_keys=["field1"])
        assert ok is True
        assert len(issues) == 0


class TestHumanFactors:
    """Test human factors module."""
    
    def test_fatigue_computation(self):
        model = HumanFactorsModel(task_load=0.8, shift_hours=12, experience_level=0.5)
        fatigue = model.compute_fatigue_index()
        assert 0.0 <= fatigue <= 1.0
    
    def test_error_rate_estimation(self):
        model = HumanFactorsModel(task_load=0.5, shift_hours=8, experience_level=1.0)
        error_rate = model.estimate_error_rate()
        assert 0.0 <= error_rate <= 1.0
    
    def test_regulatory_monitor(self):
        monitor = RegulatoryMonitor()
        monitor.track_standard("ISO 9001")
        changes = monitor.poll_changes()
        assert isinstance(changes, list)
        assert len(changes) > 0


class TestNoveltyManager:
    """Test novelty manager module."""
    
    def test_prototype_manager_hypotheses(self):
        mgr = PrototypeManager()
        hypotheses = mgr.propose_hypotheses("test problem")
        assert isinstance(hypotheses, list)
        assert len(hypotheses) > 0
        assert "hypothesis" in hypotheses[0]
    
    def test_prototype_manager_experiments(self):
        mgr = PrototypeManager()
        hypotheses = mgr.propose_hypotheses("test problem")
        experiments = mgr.design_experiments(hypotheses)
        assert isinstance(experiments, list)
    
    def test_novelty_cycle(self):
        nmgr = NoveltyManager()
        plan = nmgr.run_cycle("test requirements")
        assert "hypotheses_count" in plan
        assert "experiments_count" in plan
        assert "next_steps" in plan


class TestOptimizationEngine:
    """Test optimization engine."""
    
    def test_optimization(self):
        from spaceship_design import SpaceshipDesign
        design = SpaceshipDesign(population=1000)
        engine = OptimizationEngine()
        result = engine.optimize(design, objectives=["mass", "cost"])
        assert "pareto_set" in result
        assert len(result["pareto_set"]) > 0
        assert design.metrics["pareto_count"] > 0


class TestDependencyGraph:
    """Test dependency graph module."""
    
    def test_add_components(self):
        graph = DependencyGraph()
        graph.add_component("A")
        graph.add_component("B")
        assert "A" in graph.components
        assert "B" in graph.components
    
    def test_topo_order(self):
        graph = DependencyGraph()
        graph.add_component("A")
        graph.add_component("B")
        graph.add_component("C")
        graph.add_dependency("A", "B")
        graph.add_dependency("B", "C")
        topo = graph.topo_order()
        assert topo is not None
        assert len(topo) == 3
    
    def test_critical_path(self):
        graph = DependencyGraph()
        graph.add_component("A")
        graph.add_component("B")
        graph.add_dependency("A", "B")
        path = graph.critical_path()
        assert isinstance(path, list)


class TestUXConversation:
    """Test UX conversation module."""
    
    def test_interact(self):
        convo = StatefulConversationalInterface()
        response = convo.interact("Hello")
        assert isinstance(response, str)
        assert len(convo.get_history()) > 0
    
    def test_guide_next_steps(self):
        convo = StatefulConversationalInterface()
        suggestions = convo.guide_next_steps({"risks": {}, "conflicts": []})
        assert isinstance(suggestions, list)


class TestValidationIntegration:
    """Test validation integration module."""
    
    def test_test_plan_export_json(self):
        exporter = TestPlanExporter()
        plan = {"name": "Test Plan", "tests": []}
        json_str = exporter.export_json(plan)
        assert isinstance(json_str, str)
        assert "Test Plan" in json_str
    
    def test_test_plan_export_markdown(self):
        exporter = TestPlanExporter()
        plan = {"name": "Test Plan", "tests": []}
        md_str = exporter.export_markdown(plan)
        assert isinstance(md_str, str)
        assert "Test Plan" in md_str
    
    def test_hil_stub(self):
        hil = HardwareInLoopStub()
        result = hil.run_test("test", {"param": "value"})
        assert "status" in result
        assert "name" in result
    
    def test_field_trial_tracker(self):
        tracker = FieldTrialTracker()
        tracker.record({"name": "Trial 1", "status": "completed"})
        summary = tracker.summary()
        assert summary["total_trials"] == 1


class TestThreatModeling:
    """Test threat modeling module."""
    
    def test_threat_analysis(self):
        modeler = ThreatModeler()
        analysis = modeler.analyze(["Asset1", "Asset2"])
        assert "stride" in analysis
        assert "total_threats" in analysis
        assert analysis["total_threats"] > 0
    
    def test_risk_calculation(self):
        modeler = ThreatModeler()
        risk = modeler.calculate_risk("admin_password")
        assert 0.0 <= risk <= 1.0


class TestScalabilityPlanner:
    """Test scalability planner module."""
    
    def test_scalability_plan(self):
        planner = ScalabilityPlanner()
        plan = planner.plan({
            "requests_per_second": 100,
            "data_size_gb": 10,
            "user_count": 1000,
            "availability_target": 0.99
        })
        assert "replicas" in plan
        assert "regions" in plan
        assert "failover_strategy" in plan
        assert "estimated_cost_usd_month" in plan


class TestPipeline:
    """Test main pipeline integration."""
    
    def test_orchestrate_has_all_keys(self):
        results = orchestrate_ultra_complex_system()
        
        # Original keys
        assert "knowledge" in results
        assert "requirements" in results
        assert "spaceship_metrics" in results
        
        # New keys
        assert "data_summary" in results
        assert "human_factors" in results
        assert "novelty_plan" in results
        assert "optimization_summary" in results
        assert "dependencies" in results
        assert "ux_guidance" in results
        assert "validation_plan" in results
        assert "threat_model" in results
        assert "scalability_plan" in results
    
    def test_data_summary_structure(self):
        results = orchestrate_ultra_complex_system()
        data_summary = results["data_summary"]
        assert "rows" in data_summary
        assert "fields" in data_summary
        assert "sample" in data_summary
    
    def test_human_factors_structure(self):
        results = orchestrate_ultra_complex_system()
        hf = results["human_factors"]
        assert "fatigue_index" in hf
        assert "error_rate" in hf
        assert "regulatory_notices" in hf
