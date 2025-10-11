"""
Dependency Graph Module

Manages component dependencies and performs topological sorting and critical path analysis.

TODO: Add visualization export and more sophisticated path algorithms.
"""


class DependencyGraph:
    """Manage component dependencies as a directed acyclic graph (DAG)."""
    
    def __init__(self):
        self.components = {}  # id -> metadata
        self.edges = {}  # src -> [dst1, dst2, ...]
        self.reverse_edges = {}  # dst -> [src1, src2, ...]
    
    def add_component(self, component_id, metadata=None):
        """
        Add a component to the graph.
        
        Args:
            component_id: Unique component identifier
            metadata: Optional dict with component metadata
        """
        self.components[component_id] = metadata or {}
        if component_id not in self.edges:
            self.edges[component_id] = []
        if component_id not in self.reverse_edges:
            self.reverse_edges[component_id] = []
    
    def add_dependency(self, src, dst):
        """
        Add a dependency edge from src to dst (src depends on dst).
        
        Args:
            src: Source component ID
            dst: Destination component ID (dependency)
        """
        if src not in self.edges:
            self.edges[src] = []
        if dst not in self.reverse_edges:
            self.reverse_edges[dst] = []
        
        if dst not in self.edges[src]:
            self.edges[src].append(dst)
        if src not in self.reverse_edges[dst]:
            self.reverse_edges[dst].append(src)
    
    def has_cycle(self):
        """
        Detect if graph has cycles using DFS.
        
        Returns:
            bool: True if cycle detected
        """
        visited = set()
        rec_stack = set()
        
        def dfs(node):
            visited.add(node)
            rec_stack.add(node)
            
            for neighbor in self.edges.get(node, []):
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True
                elif neighbor in rec_stack:
                    return True
            
            rec_stack.remove(node)
            return False
        
        for node in self.components:
            if node not in visited:
                if dfs(node):
                    return True
        
        return False
    
    def topo_order(self):
        """
        Compute topological ordering using Kahn's algorithm.
        
        Returns:
            list: Topologically sorted component IDs, or None if cycle exists
        """
        if self.has_cycle():
            return None
        
        # Calculate in-degrees
        in_degree = {node: 0 for node in self.components}
        for node in self.edges:
            for neighbor in self.edges[node]:
                in_degree[neighbor] = in_degree.get(neighbor, 0) + 1
        
        # Queue nodes with no incoming edges
        queue = [node for node in self.components if in_degree[node] == 0]
        result = []
        
        while queue:
            node = queue.pop(0)
            result.append(node)
            
            for neighbor in self.edges.get(node, []):
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        return result if len(result) == len(self.components) else None
    
    def critical_path(self):
        """
        Find critical path using longest path in DAG (unit weights).
        
        Returns:
            list: Critical path as list of component IDs
        """
        topo = self.topo_order()
        if not topo:
            return []
        
        # Initialize distances
        dist = {node: 0 for node in self.components}
        parent = {node: None for node in self.components}
        
        # Process nodes in topological order
        for node in topo:
            for neighbor in self.edges.get(node, []):
                # Unit weight = 1 for each edge
                if dist[node] + 1 > dist[neighbor]:
                    dist[neighbor] = dist[node] + 1
                    parent[neighbor] = node
        
        # Find node with maximum distance
        max_node = max(dist, key=dist.get)
        
        # Reconstruct path
        path = []
        current = max_node
        while current is not None:
            path.append(current)
            current = parent[current]
        
        path.reverse()
        return path
