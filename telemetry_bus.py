"""Lightweight telemetry/event bus (Phase 1).
Future: Export to OpenTelemetry / Prometheus.
"""
from typing import Callable, Dict, List, Any
import time

class TelemetryBus:
    def __init__(self):
        self.subscribers: Dict[str, List[Callable[[Dict[str, Any]], None]]] = {}
        self.counters: Dict[str, int] = {}
        self.timings: Dict[str, List[float]] = {}

    def emit(self, topic: str, payload: Dict[str, Any]):
        payload = dict(payload)
        payload['timestamp'] = time.time()
        for fn in self.subscribers.get(topic, []):
            try:
                fn(payload)
            except Exception:
                # Swallow for now; advanced version will log
                pass

    def on(self, topic: str, handler: Callable[[Dict[str, Any]], None]):
        self.subscribers.setdefault(topic, []).append(handler)

    def inc(self, name: str, value: int = 1):
        self.counters[name] = self.counters.get(name, 0) + value

    def time(self, name: str, duration: float):
        self.timings.setdefault(name, []).append(duration)

    def snapshot(self):
        return {
            'counters': dict(self.counters),
            'timings': {k: {'n': len(v), 'avg': sum(v)/len(v) if v else 0.0} for k, v in self.timings.items()}
        }