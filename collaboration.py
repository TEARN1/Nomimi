class CollaborationManager:
    def __init__(self):
        self.versions = {}
        self.changes = []

    def commit(self, version, change):
        self.versions[version] = change
        self.changes.append((version, change))

    def get_history(self):
        return self.changes