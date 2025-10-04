"""Multi-objective Pareto Optimizer (Phase 1)
Simplified: expects list of dict options with numeric objectives.
Future: evolutionary algorithms, constraint dominance, caching.
"""
from typing import List, Dict, Any

class ParetoOptimizer:
    def __init__(self, minimize: list[str] | None = None):
        self.minimize = set(minimize or [])

    def pareto_front(self, options: List[Dict[str, Any]], objectives: List[str]):
        front = []
        for i, opt in enumerate(options):
            dominated = False
            for j, other in enumerate(options):
                if i == j:
                    continue
                if self._dominates(other, opt, objectives):
                    dominated = True
                    break
            if not dominated:
                front.append(opt)
        return front

    def _dominates(self, a: Dict[str, Any], b: Dict[str, Any], objectives: List[str]):
        better_or_equal = True
        strictly_better = False
        for obj in objectives:
            av, bv = a.get(obj), b.get(obj)
            if obj in self.minimize:
                if av > bv:
                    better_or_equal = False
                    break
                if av < bv:
                    strictly_better = True
            else:
                if av < bv:
                    better_or_equal = False
                    break
                if av > bv:
                    strictly_better = True
        return better_or_equal and strictly_better