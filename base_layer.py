from spaceship_design import SpaceshipDesign

class BaseLayer:
    def run(self, spaceship: SpaceshipDesign):
        print("[BaseLayer] Initial design...")
        for name in ["Habitat", "LifeSupport", "Propulsion", "Storage", "Recreation", "Control"]:
            spaceship.sections.append(name)
            spaceship.metrics[name + "_efficiency"] = 1.0