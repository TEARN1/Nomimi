class SimulationEngine:
    def run_simulation(self, spaceship):
        passed = all(
            val > 1.01 for key, val in spaceship.metrics.items() if "efficiency" in key
        )
        spaceship.metrics["simulated_performance"] = "pass" if passed else "fail"
        return passed