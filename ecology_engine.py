"""Ecology Engine (Phase 1)
Very simplified closed-loop resource cycle model.
Variables: O2, CO2, biomass, nutrients.
Future: multi-species dynamics, stochastic perturbations, resilience metrics.
"""
class EcologyEngine:
    def __init__(self):
        self.state = {
            'o2': 1_000_000.0,
            'co2': 500_000.0,
            'biomass': 200_000.0,
            'nutrients': 100_000.0
        }

    def step(self, population: int = 1000, dt: float = 1.0):
        o2_use = population * 0.8 * dt
        co2_prod = population * 0.85 * dt
        self.state['o2'] -= o2_use
        self.state['co2'] += co2_prod
        fix_rate = min(self.state['co2'], self.state['nutrients']) * 0.001 * dt
        self.state['co2'] -= fix_rate
        self.state['o2'] += fix_rate
        self.state['biomass'] += fix_rate * 0.5
        self.state['nutrients'] -= fix_rate * 0.1
        self.state['nutrients'] += 50 * dt
        return dict(self.state)

    def snapshot(self):
        return dict(self.state)