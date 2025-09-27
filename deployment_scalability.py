class DeploymentManager:
    def __init__(self):
        self.environments = []
        self.status = {}

    def add_environment(self, env):
        self.environments.append(env)
        self.status[env] = "pending"

    def deploy(self, env):
        self.status[env] = "deployed"
        print(f"Deployed to {env}")

    def check_status(self, env):
        return self.status.get(env, "unknown")