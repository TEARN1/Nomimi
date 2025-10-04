"""Provenance Chain (Phase 1)
Creates a simple hash chain of artifacts for tamper-evidence.
Future: digital signatures, Merkle trees, remote attestation.
"""
import hashlib, json, time
from typing import List, Dict, Any

class ProvenanceChain:
    def __init__(self):
        self.chain: List[Dict[str, Any]] = []

    def record(self, artifact: Dict[str, Any]):
        prev_hash = self.chain[-1]['hash'] if self.chain else 'GENESIS'
        payload = {
            'timestamp': time.time(),
            'artifact': artifact,
            'prev_hash': prev_hash
        }
        raw = json.dumps(payload, sort_keys=True).encode('utf-8')
        h = hashlib.sha256(raw).hexdigest()
        payload['hash'] = h
        self.chain.append(payload)
        return payload

    def verify(self):
        for i, block in enumerate(self.chain):
            raw = json.dumps({k: block[k] for k in ['timestamp','artifact','prev_hash']}, sort_keys=True).encode('utf-8')
            h = hashlib.sha256(raw).hexdigest()
            if h != block['hash']:
                return False, i
            if i > 0 and block['prev_hash'] != self.chain[i-1]['hash']:
                return False, i
        return True, None

    def head(self):
        return self.chain[-1] if self.chain else None

    def all(self):
        return list(self.chain)