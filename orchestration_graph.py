"""Dynamic orchestration graph for adaptive execution pipelines.
Phase 1: Minimal functionality (register + connect + simple DFS execution).
Future: metric-driven reordering, failure routing, dynamic replanning.
"""
from typing import Callable, Dict, List, Any

class OrchestrationGraph:
    def __init__(self):
        self.nodes: Dict[str, Dict[str, Any]] = {}
        self.edges: Dict[str, List[str]] = {}

    def register(self, name: str, handler: Callable[[Dict[str, Any]], Any], inputs=None, outputs=None, meta=None):
        self.nodes[name] = {
            'handler': handler,
            'inputs': inputs or [],
            'outputs': outputs or [],
            'meta': meta or {}
        }

    def connect(self, src: str, dst: str):
        self.edges.setdefault(src, []).append(dst)

    def execute(self, start: str, context: Dict[str, Any] | None = None):
        context = context or {}
        visited = set()
        stack = [start]
        order = []
        while stack:
            node = stack.pop()
            if node in visited:
                continue
            if node not in self.nodes:
                raise KeyError(f"Node '{node}' not registered")
            result = self.nodes[node]['handler'](context)
            context[node] = result
            order.append(node)
            for nxt in self.edges.get(node, []):
                stack.append(nxt)
            visited.add(node)
        context['__execution_order__'] = order
        return context
