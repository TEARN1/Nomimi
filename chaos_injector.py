"""Chaos Injector (Phase 1)
Injects synthetic failures; future: schedule policies & blast radius controls.
"""
import random
from typing import Optional

class ChaosInjector:
    def __init__(self, seed: Optional[int] = None):
        self.random = random.Random(seed)
        self.events = []

    def inject(self, kind: str):
        event = {'type': kind, 'id': len(self.events) + 1}
        self.events.append(event)
        return event

    def maybe_fail(self, probability: float = 0.0, label: str = 'generic'):
        if self.random.random() < probability:
            return self.inject(f"failure:{label}")
        return None

    def history(self):
        return list(self.events)