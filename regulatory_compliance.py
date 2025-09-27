class ComplianceAuditor:
    def __init__(self):
        self.standards = []
        self.violations = []

    def load_standards(self, standards_list):
        self.standards = standards_list

    def audit(self, design):
        for standard in self.standards:
            if standard in design.metrics and not design.metrics[standard]:
                self.violations.append(f"Violation of {standard}")
        return self.violations