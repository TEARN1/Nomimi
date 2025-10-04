"""Demonstration pipeline wiring Phase 1 advanced modules."""
from orchestration_graph import OrchestrationGraph
from telemetry_bus import TelemetryBus
from plugin_registry import PluginRegistry
from semantic_knowledge_fabric import SemanticKnowledgeFabric
from pareto_optimizer import ParetoOptimizer
from constraint_formal_engine import ConstraintFormalEngine
from ecology_engine import EcologyEngine
from chaos_injector import ChaosInjector
from explainability_graph import ExplainabilityGraph
from provenance_chain import ProvenanceChain

telemetry = TelemetryBus()
plugins = PluginRegistry()
knowledge = SemanticKnowledgeFabric()
chaos = ChaosInjector(seed=42)
explain = ExplainabilityGraph()
provenance = ProvenanceChain()

ecology = EcologyEngine()
constraint_engine = ConstraintFormalEngine()
pareto = ParetoOptimizer(minimize=['energy'])

plugins.register('ecology.core', {'cycles': True})
plugins.register('optimizer.pareto', {'multi_objective': True})
plugins.register('constraints.formal', {'formal_check': True})

knowledge.ingest("fusion drive high isp low thrust sustainable core ignition")
knowledge.ingest("closed loop algae bioreactor oxygen regeneration nutrients recycling")
knowledge.ingest("spin gravity habitat psychology retention long term adaptation")

constraint_engine.assert_expr('energy < 1000')
constraint_engine.assert_expr('population >= 1000')

def orchestrate_advanced_system():
    graph = OrchestrationGraph()

    def node_ecology(ctx):
        snap = ecology.step(population=1500, dt=1.0)
        telemetry.inc('ecology_steps')
        explain.add('ecology_tick', snap, parents=[])
        provenance.record({'type': 'ecology', 'snapshot': snap})
        return snap

    def node_options(ctx):
        opts = [
            {'name': 'DesignA', 'energy': 800, 'reliability': 0.92, 'throughput': 120},
            {'name': 'DesignB', 'energy': 950, 'reliability': 0.95, 'throughput': 110},
            {'name': 'DesignC', 'energy': 700, 'reliability': 0.89, 'throughput': 115},
        ]
        explain.add('options_generated', opts, parents=['ecology_tick'])
        provenance.record({'type': 'options', 'count': len(opts)})
        return opts

    def node_pareto(ctx):
        opts = ctx['node_options']
        front = pareto.pareto_front(opts, objectives=['reliability', 'throughput', 'energy'])
        explain.add('pareto_front', front, parents=['options_generated'])
        provenance.record({'type': 'pareto', 'front_size': len(front)})
        return front

    def node_constraints(ctx):
        local_ctx = {
            'energy': min(o['energy'] for o in ctx['node_options']),
            'population': 1500
        }
        result = constraint_engine.check(local_ctx)
        explain.add('constraint_eval', result, parents=['pareto_front'])
        provenance.record({'type': 'constraints', 'status': result['all_ok']})
        return result

    graph.register('node_ecology', node_ecology)
    graph.register('node_options', node_options)
    graph.register('node_pareto', node_pareto)
    graph.register('node_constraints', node_constraints)

    graph.connect('node_ecology', 'node_options')
    graph.connect('node_options', 'node_pareto')
    graph.connect('node_pareto', 'node_constraints')

    chaos.maybe_fail(probability=0.0, label='ecology')

    context = graph.execute('node_ecology', {})

    return {
        'orchestration': context.get('__execution_order__'),
        'ecology_snapshot': context['node_ecology'],
        'pareto_front': context['node_pareto'],
        'constraints': context['node_constraints'],
        'telemetry': telemetry.snapshot(),
        'plugins': plugins.list(),
        'knowledge_sample': knowledge.search('fusion habitat'),
        'explainability': {'graph': explain.graph()},
        'provenance': provenance.all()
    }
