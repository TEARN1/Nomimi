class MetaOptimizerLayer:
    def __init__(self, lower_layer, layer_id=1):
        self.lower_layer = lower_layer
        self.layer_id = layer_id

    def run(self, spaceship):
        print(f"[MetaOptimizerLayer {self.layer_id}] Optimizing...")
        self.lower_layer.run(spaceship)
        for section in spaceship.sections:
            spaceship.metrics[section + "_meta_quality"] = (
                spaceship.metrics.get(section + "_efficiency", 1.0) * 1.1
            )
        if len(spaceship.sections) >= 6 and all(
            v > 1.05 for v in spaceship.metrics.values() if isinstance(v, float)
        ):
            spaceship.completed = True