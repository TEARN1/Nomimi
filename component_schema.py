"""Core component and rule schema for Nomimi synthesis engine."""
from typing import List, Dict, Any, Optional
from dataclasses import dataclass, field
import hashlib, json

@dataclass
class Part:
    part_id: str
    family_id: str
    category: str
    geometry: Dict[str, Any]
    performance: Dict[str, Any]
    lifecycle: Dict[str, Any]
    materials: List[Dict[str, Any]]
    compat: Dict[str, Any] = field(default_factory=dict)
    constraints: List[str] = field(default_factory=list)
    provenance: Dict[str, Any] = field(default_factory=dict)

    def hash(self) -> str:
        raw = json.dumps({
            "part_id": self.part_id,
            "family_id": self.family_id,
            "geometry": self.geometry,
            "performance": self.performance
        }, sort_keys=True).encode()
        return hashlib.sha256(raw).hexdigest()

@dataclass
class Rule:
    rule_id: str
    domain: str
    inputs: List[str]
    outputs: List[str]
    formula: str  # Python expression evaluating to dict of new values
    constraints: List[str] = field(default_factory=list)
    priority: int = 100

@dataclass
class AssemblyResult:
    assembly_id: str
    parts: List[Part]
    derived: Dict[str, Any]
    variants: List[Dict[str, Any]]
    constraints_report: Dict[str, Any]
    explainability_nodes: Dict[str, Any]
    provenance: List[Dict[str, Any]]

