"""
threat_modeling.py

Security threat modeling using STRIDE methodology for Nomimi.
Calculates risk scores and provides mitigation suggestions.
"""


class ThreatModel:
    """
    STRIDE-style threat modeling.
    
    STRIDE categories:
    - Spoofing: Impersonating something or someone else
    - Tampering: Modifying data or code
    - Repudiation: Claiming to have not performed an action
    - Information Disclosure: Exposing information to unauthorized parties
    - Denial of Service: Denying or degrading service to users
    - Elevation of Privilege: Gaining capabilities without proper authorization
    
    TODO: Add automatic threat identification based on architecture
    TODO: Implement attack tree generation
    TODO: Add integration with CVE databases
    """
    
    def __init__(self):
        self.threats = []
        self.mitigations = []
    
    def add_threat(self, threat_id, category, description, severity, likelihood):
        """
        Add a threat to the model.
        
        Args:
            threat_id: Unique threat identifier
            category: STRIDE category (S, T, R, I, D, or E)
            description: Threat description
            severity: Severity level (1-10)
            likelihood: Likelihood (0.0-1.0)
        """
        risk_score = self.calculate_risk_score(severity, likelihood)
        
        threat = {
            "id": threat_id,
            "category": category,
            "description": description,
            "severity": severity,
            "likelihood": likelihood,
            "risk_score": risk_score,
            "status": "open"
        }
        self.threats.append(threat)
        print(f"[ThreatModel] Added threat {threat_id} ({category}): risk score {risk_score:.2f}")
        
        # Suggest mitigation
        self._suggest_mitigation(threat)
    
    def calculate_risk_score(self, severity, likelihood):
        """
        Calculate risk score from severity and likelihood.
        
        Args:
            severity: Severity (1-10)
            likelihood: Likelihood (0.0-1.0)
            
        Returns:
            float: Risk score
        """
        return severity * likelihood
    
    def _suggest_mitigation(self, threat):
        """
        Suggest mitigations based on threat category.
        
        Args:
            threat: Threat dictionary
        """
        category = threat["category"].upper()
        
        mitigation_suggestions = {
            "S": ["Implement strong authentication", "Use multi-factor authentication", "Validate identity tokens"],
            "T": ["Implement integrity checks", "Use digital signatures", "Enable audit logging"],
            "R": ["Implement comprehensive logging", "Use non-repudiable signatures", "Enable audit trails"],
            "I": ["Encrypt sensitive data", "Implement access controls", "Use data loss prevention"],
            "D": ["Implement rate limiting", "Use redundancy and failover", "Deploy DDoS protection"],
            "E": ["Implement least privilege", "Use role-based access control", "Regular permission audits"]
        }
        
        suggestions = mitigation_suggestions.get(category, ["Review security best practices"])
        
        for suggestion in suggestions[:2]:  # Top 2 suggestions
            mitigation = {
                "threat_id": threat["id"],
                "suggestion": suggestion,
                "implemented": False
            }
            self.mitigations.append(mitigation)
    
    def get_threats_by_category(self, category):
        """
        Get all threats in a specific STRIDE category.
        
        Args:
            category: STRIDE category
            
        Returns:
            list: Threats in that category
        """
        return [t for t in self.threats if t["category"].upper() == category.upper()]
    
    def get_high_risk_threats(self, threshold=5.0):
        """
        Get threats with risk score above threshold.
        
        Args:
            threshold: Minimum risk score
            
        Returns:
            list: High-risk threats
        """
        return [t for t in self.threats if t["risk_score"] >= threshold]
    
    def get_summary(self):
        """
        Get threat model summary.
        
        Returns:
            dict: Summary of threats and mitigations
        """
        high_risk = self.get_high_risk_threats()
        
        # Count by category
        category_counts = {}
        for threat in self.threats:
            cat = threat["category"].upper()
            category_counts[cat] = category_counts.get(cat, 0) + 1
        
        return {
            "total_threats": len(self.threats),
            "high_risk_threats": len(high_risk),
            "mitigations_suggested": len(self.mitigations),
            "category_breakdown": category_counts,
            "average_risk_score": sum(t["risk_score"] for t in self.threats) / len(self.threats) if self.threats else 0
        }
    
    def integrate_with_risk_manager(self, risk_manager):
        """
        Integrate threat model with existing RiskManager.
        
        Args:
            risk_manager: RiskManager instance
            
        TODO: Implement two-way synchronization
        """
        # Add high-risk threats to risk manager
        for threat in self.get_high_risk_threats():
            risk_manager.assess_risk(
                subsystem=f"Security_{threat['category']}",
                probability=threat['likelihood'],
                impact=threat['severity']
            )
        
        print(f"[ThreatModel] Integrated {len(self.get_high_risk_threats())} high-risk threats with RiskManager")
