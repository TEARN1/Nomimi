"""
dependency_graph.py

Interdisciplinary dependency modeling for complex systems.
Builds and analyzes dependency graphs between components.
"""


class DependencyGraph:
    """
    Models dependencies between system components.
    
    TODO: Add support for weighted dependencies
    TODO: Implement automatic dependency inference from design specs
    TODO: Add visualization export (GraphViz, etc.)
    TODO: Implement change impact analysis
    """
    
    def __init__(self):
        self.nodes = {}
        self.edges = []
    
    def add_component(self, component_id, component_type, properties=None):
        """
        Add a component node to the graph.
        
        Args:
            component_id: Unique identifier for the component
            component_type: Type of component (e.g., 'mechanical', 'electrical', 'software')
            properties: Optional dictionary of component properties
        """
        if properties is None:
            properties = {}
        
        self.nodes[component_id] = {
            "type": component_type,
            "properties": properties,
            "dependencies": []
        }
        print(f"[DependencyGraph] Added component: {component_id} ({component_type})")
    
    def add_dependency(self, from_component, to_component, dependency_type="requires"):
        """
        Add a dependency edge between components.
        
        Args:
            from_component: Source component ID
            to_component: Target component ID
            dependency_type: Type of dependency (e.g., 'requires', 'provides', 'uses')
        """
        if from_component not in self.nodes or to_component not in self.nodes:
            print(f"[DependencyGraph] Warning: Component not found for dependency")
            return
        
        edge = {
            "from": from_component,
            "to": to_component,
            "type": dependency_type
        }
        self.edges.append(edge)
        self.nodes[from_component]["dependencies"].append(to_component)
        print(f"[DependencyGraph] Added dependency: {from_component} -> {to_component} ({dependency_type})")
    
    def compute_critical_path(self):
        """
        Compute critical path through the dependency graph.
        
        Returns:
            list: Ordered list of component IDs on the critical path
            
        TODO: Implement proper critical path algorithm with timing data
        TODO: Add slack time calculations
        """
        # Stub: Simple topological sort as a proxy for critical path
        return self.topological_sort()
    
    def topological_sort(self):
        """
        Perform topological sort of the dependency graph.
        
        Returns:
            list: Topologically sorted component IDs
        """
        # Simple topological sort using DFS
        visited = set()
        result = []
        
        def visit(node_id):
            if node_id in visited:
                return
            visited.add(node_id)
            
            # Visit dependencies first
            for dep in self.nodes[node_id]["dependencies"]:
                if dep in self.nodes:
                    visit(dep)
            
            result.append(node_id)
        
        # Visit all nodes
        for node_id in self.nodes:
            visit(node_id)
        
        result.reverse()
        print(f"[DependencyGraph] Topological order: {' -> '.join(result[:5])}{'...' if len(result) > 5 else ''}")
        return result
    
    def find_cycles(self):
        """
        Detect circular dependencies in the graph.
        
        Returns:
            list: List of cycles found (each cycle is a list of component IDs)
            
        TODO: Implement cycle detection algorithm
        """
        # Stub: Return empty list (no cycles detected in stub)
        print(f"[DependencyGraph] Checking for cycles...")
        return []
    
    def get_component_dependencies(self, component_id):
        """
        Get all dependencies for a specific component.
        
        Args:
            component_id: Component to query
            
        Returns:
            list: List of component IDs this component depends on
        """
        if component_id not in self.nodes:
            return []
        
        return self.nodes[component_id]["dependencies"]
    
    def get_dependents(self, component_id):
        """
        Get all components that depend on the specified component.
        
        Args:
            component_id: Component to query
            
        Returns:
            list: List of component IDs that depend on this component
        """
        dependents = []
        for edge in self.edges:
            if edge["to"] == component_id:
                dependents.append(edge["from"])
        
        return dependents
    
    def get_summary(self):
        """
        Get a summary of the dependency graph.
        
        Returns:
            dict: Graph statistics and structure summary
        """
        critical_path = self.compute_critical_path()
        cycles = self.find_cycles()
        
        return {
            "nodes": len(self.nodes),
            "edges": len(self.edges),
            "critical_path_length": len(critical_path),
            "critical_path_preview": critical_path[:5],
            "cycles_found": len(cycles),
            "component_types": list(set(n["type"] for n in self.nodes.values()))
        }
