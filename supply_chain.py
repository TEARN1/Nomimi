class SupplyChainManager:
    def __init__(self):
        self.resources = {}
        self.paths = {}

    def add_resource(self, name, quantity):
        self.resources[name] = quantity

    def set_path(self, resource, path):
        self.paths[resource] = path

    def optimize_supply(self):
        total = sum(self.resources.values())
        return total, self.paths