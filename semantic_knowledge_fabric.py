"""Semantic Knowledge Fabric (Phase 1)
Placeholder: simple keyword + naive embedding simulation.
Future: real vector store (FAISS / pgvector), temporal graph, provenance links.
"""
from typing import List, Dict, Any
import math

class SemanticKnowledgeFabric:
    def __init__(self):
        self.docs: List[Dict[str, Any]] = []

    def ingest(self, text: str, source: str = "manual", tags=None):
        tokens = text.lower().split()
        vec = self._fake_embed(tokens)
        record = {'text': text, 'source': source, 'tags': tags or [], 'vector': vec}
        self.docs.append(record)
        return record

    def search(self, query: str, top_k: int = 3):
        q_tokens = query.lower().split()
        q_vec = self._fake_embed(q_tokens)
        scored = []
        for d in self.docs:
            score = self._cosine(q_vec, d['vector'])
            scored.append((score, d))
        scored.sort(key=lambda x: x[0], reverse=True)
        return [d for _, d in scored[:top_k]]

    def _fake_embed(self, tokens: List[str]):
        dim = 32
        vec = [0.0]*dim
        for t in tokens:
            h = sum(ord(c) for c in t) % dim
            vec[h] += 1.0
        norm = math.sqrt(sum(v*v for v in vec)) or 1.0
        return [v/norm for v in vec]

    def _cosine(self, a, b):
        return sum(x*y for x, y in zip(a, b))