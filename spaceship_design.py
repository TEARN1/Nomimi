class SpaceshipDesign:
    def __init__(self, population: int):
        self.population = population
        self.sections = []
        self.metrics = {}
        self.completed = False

    def describe(self):
        return f"Spaceship for {self.population} people\nSections: {self.sections}\nMetrics: {self.metrics}"