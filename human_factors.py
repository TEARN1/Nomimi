"""
Human Factors Module

Models human factors such as task load, fatigue, and error rates.
Tracks regulatory standards and changes.

TODO: Implement more sophisticated fatigue models and real regulatory feeds.
"""


class HumanFactorsModel:
    """Model human performance factors."""
    
    def __init__(self, task_load=0.5, shift_hours=8, experience_level=1.0):
        """
        Initialize human factors model.
        
        Args:
            task_load: Task load factor (0.0 to 1.0)
            shift_hours: Working hours per shift
            experience_level: Experience factor (0.0 to 1.0+)
        """
        self.task_load = task_load
        self.shift_hours = shift_hours
        self.experience_level = experience_level
    
    def compute_fatigue_index(self):
        """
        Compute fatigue index based on task load and shift hours.
        
        Returns:
            float: Fatigue index (higher = more fatigued)
        """
        # Simple heuristic: fatigue increases with task load and hours
        base_fatigue = self.task_load * 0.5
        hour_fatigue = (self.shift_hours / 24.0) * 0.5
        return min(1.0, base_fatigue + hour_fatigue)
    
    def estimate_error_rate(self):
        """
        Estimate human error rate.
        
        Returns:
            float: Error rate (0.0 to 1.0)
        """
        fatigue = self.compute_fatigue_index()
        # Error rate increases with fatigue and decreases with experience
        error_rate = fatigue * 0.1 / max(0.1, self.experience_level)
        return min(1.0, error_rate)


class RegulatoryMonitor:
    """Monitor regulatory standards and changes."""
    
    def __init__(self):
        self.standards = []
    
    def track_standard(self, name):
        """
        Track a regulatory standard.
        
        Args:
            name: Standard name (e.g., "ISO 9001")
        """
        if name not in self.standards:
            self.standards.append(name)
    
    def poll_changes(self):
        """
        Poll for regulatory changes (stub).
        
        Returns:
            list[dict]: Example change notices
            
        TODO: Implement real regulatory feed polling
        """
        return [
            {
                "standard": "ISO 9001",
                "change": "Minor update to section 8.5.1",
                "effective_date": "2025-12-01",
                "severity": "low"
            },
            {
                "standard": "FAA Part 107",
                "change": "New requirements for beyond visual line of sight",
                "effective_date": "2026-01-15",
                "severity": "medium"
            }
        ]
