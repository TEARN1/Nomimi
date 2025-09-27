class RiskManager:
    def __init__(self):
        self.risks = {}

    def assess_risk(self, subsystem, probability, impact):
        self.risks[subsystem] = probability * impact

    def total_risk(self):
        return sum(self.risks.values())

    def mitigate(self, subsystem, strategy):
        if subsystem in self.risks:
            self.risks[subsystem] *= 0.5