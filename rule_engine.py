"""Rule engine for iterative evaluation of design rules."""
import math
from typing import Dict, Any, List
from component_schema import Rule

class RuleEngine:
    def __init__(self, rules: List[Rule]):
        self.rules = sorted(rules, key=lambda r: r.priority)

    def evaluate(self, context: Dict[str, Any]) -> Dict[str, Any]:
        changed = True
        derived = {}
        while changed:
            changed = False
            for rule in self.rules:
                if all(k in context for k in rule.inputs):
                    local_env = dict(context)
                    try:
                        result = eval(rule.formula, {"math": math}, local_env)
                        if isinstance(result, dict):
                            for k, v in result.items():
                                if k not in context:
                                    context[k] = v
                                    derived[k] = v
                                    changed = True
                    except Exception:
                        pass
        return derived
