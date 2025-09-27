class RequirementsManager:
    def __init__(self):
        self.requirements = []
        self.conflicts = []

    def add_requirement(self, req):
        self.requirements.append(req)
        self.check_conflicts()

    def check_conflicts(self):
        for req in self.requirements:
            if "mass <" in req and "shielding >" in req:
                self.conflicts.append((req, "Potential conflict: mass vs. shielding"))

    def get_requirements(self):
        return self.requirements

    def get_conflicts(self):
        return self.conflicts