class SecurityManager:
    def __init__(self):
        self.ip_protected = []
        self.user_access = {}

    def protect_ip(self, item):
        self.ip_protected.append(item)

    def set_access(self, user, level):
        self.user_access[user] = level

    def check_access(self, user, item):
        if item in self.ip_protected:
            return self.user_access.get(user, "none") == "admin"
        return True