"""
human_factors.py

Human factors and soft constraints modeling for Nomimi.
Handles task load, error rates, shift scheduling, and regulatory monitoring.
"""


class HumanFactorsModel:
    """
    Models human performance factors and constraints.
    
    TODO: Integrate fatigue models (e.g., Sleep/Wake Predictor)
    TODO: Add cognitive load assessment
    TODO: Implement crew scheduling optimization
    TODO: Add training and skill decay modeling
    """
    
    def __init__(self):
        self.task_load = 0.0
        self.error_rate = 0.01  # Default 1% error rate
        self.shift_schedule = []
        self.crew_members = []
    
    def set_task_load(self, load_factor):
        """
        Set the current task load factor.
        
        Args:
            load_factor: Float between 0.0 and 1.0 representing workload
        """
        self.task_load = max(0.0, min(1.0, load_factor))
        # Error rate increases with task load
        self.error_rate = 0.01 + (self.task_load * 0.05)
        print(f"[HumanFactors] Task load set to {self.task_load:.2f}, error rate: {self.error_rate:.3f}")
    
    def add_crew_member(self, name, role, skill_level=1.0):
        """
        Add a crew member to the model.
        
        Args:
            name: Crew member name
            role: Role/position
            skill_level: Skill level (0.0 to 1.0)
        """
        member = {
            "name": name,
            "role": role,
            "skill_level": skill_level,
            "fatigue": 0.0,
            "hours_worked": 0
        }
        self.crew_members.append(member)
        print(f"[HumanFactors] Added crew member: {name} ({role})")
    
    def schedule_shift(self, crew_member_name, start_hour, duration_hours):
        """
        Schedule a work shift for a crew member.
        
        Args:
            crew_member_name: Name of the crew member
            start_hour: Shift start hour (0-23)
            duration_hours: Length of shift in hours
            
        TODO: Add shift overlap detection and conflict resolution
        TODO: Implement circadian rhythm considerations
        """
        shift = {
            "crew_member": crew_member_name,
            "start_hour": start_hour,
            "duration": duration_hours,
            "end_hour": (start_hour + duration_hours) % 24
        }
        self.shift_schedule.append(shift)
        print(f"[HumanFactors] Scheduled shift for {crew_member_name}: {start_hour}-{shift['end_hour']} ({duration_hours}h)")
    
    def calculate_performance_factor(self):
        """
        Calculate overall human performance factor based on current state.
        
        Returns:
            float: Performance factor (0.0 to 1.0, higher is better)
        """
        if not self.crew_members:
            return 1.0
        
        # Simple model: average skill level minus task load impact
        avg_skill = sum(m["skill_level"] for m in self.crew_members) / len(self.crew_members)
        performance = avg_skill * (1.0 - self.task_load * 0.3)
        
        print(f"[HumanFactors] Performance factor: {performance:.3f}")
        return performance
    
    def get_summary(self):
        """
        Get a summary of human factors state.
        
        Returns:
            dict: Summary of current human factors
        """
        return {
            "task_load": self.task_load,
            "error_rate": self.error_rate,
            "crew_count": len(self.crew_members),
            "shifts_scheduled": len(self.shift_schedule),
            "performance_factor": self.calculate_performance_factor()
        }


class RegulatoryMonitor:
    """
    Monitors regulatory standards and policy changes.
    
    TODO: Implement feeds for regulatory updates (FAA, ISO, etc.)
    TODO: Add automatic compliance checking against standards
    TODO: Implement change impact assessment
    """
    
    def __init__(self):
        self.standards = {}
        self.policy_updates = []
    
    def load_standard(self, standard_id, description, requirements=None):
        """
        Load a regulatory standard into the system.
        
        Args:
            standard_id: Unique identifier for the standard
            description: Description of the standard
            requirements: Optional list of specific requirements
        """
        if requirements is None:
            requirements = []
        
        self.standards[standard_id] = {
            "description": description,
            "requirements": requirements,
            "loaded_date": "2025-10-11"  # Stub date
        }
        print(f"[RegulatoryMonitor] Loaded standard: {standard_id}")
    
    def check_policy_feed(self, feed_url):
        """
        Check a policy change feed for updates (stub implementation).
        
        Args:
            feed_url: URL of the policy feed
            
        Returns:
            list: List of policy updates (stub data)
            
        TODO: Implement RSS/Atom feed parsing
        TODO: Add email notifications for critical updates
        """
        print(f"[RegulatoryMonitor] Checking policy feed: {feed_url}")
        
        # Stub: return example policy updates
        stub_updates = [
            {
                "standard_id": "ISO-9001",
                "update_type": "revision",
                "description": "Minor clarification to section 8.5.1",
                "effective_date": "2026-01-01"
            }
        ]
        
        self.policy_updates.extend(stub_updates)
        return stub_updates
    
    def get_compliance_status(self, design):
        """
        Get compliance status for a design.
        
        Args:
            design: Design object to check
            
        Returns:
            dict: Compliance status
            
        TODO: Implement detailed requirement mapping
        """
        return {
            "standards_loaded": len(self.standards),
            "recent_updates": len(self.policy_updates),
            "status": "monitoring",
            "standards": list(self.standards.keys())
        }
