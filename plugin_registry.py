"""Plugin Registry (Phase 1)
Future: signed manifests, hot reload, capability graph merge.
"""
from typing import Dict, Any
import uuid, time

class PluginRegistry:
    def __init__(self):
        self.plugins: Dict[str, Dict[str, Any]] = {}

    def register(self, name: str, capabilities: dict, version: str = "0.1.0"):
        pid = str(uuid.uuid4())
        self.plugins[name] = {
            'id': pid,
            'version': version,
            'capabilities': capabilities,
            'registered_at': time.time()
        }
        return pid

    def list(self):
        return self.plugins