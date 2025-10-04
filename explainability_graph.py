"""Explainability Graph (Phase 1)
Tracks decision nodes and their parent dependencies.
Future: causal analysis, counterfactual generation, narrative synthesis.
"""
from typing import Dict, List, Any

class ExplainabilityGraph:
    def __init__(self):
        self.nodes: Dict[str, Dict[str, Any]] = {}

    def add(self, node_id: str, value: Any, parents: List[str] | None = None, meta=None):
        self.nodes[node_id] = {
            'value': value,
            'parents': parents or [],
            'meta': meta or {}
        }

    def trace(self, node_id: str, depth: int = 10):
        chain = []
        def _recurse(n, d):
            if d < 0 or n not in self.nodes:
                return
            chain.append((n, self.nodes[n]['value']))
            for p in self.nodes[n]['parents']:
                _recurse(p, d-1)
        _recurse(node_id, depth)
        return chain

    def graph(self):
        return self.nodes