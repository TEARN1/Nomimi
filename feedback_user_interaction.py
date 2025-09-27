class FeedbackManager:
    def __init__(self):
        self.feedback_log = []

    def record_feedback(self, user, msg):
        self.feedback_log.append((user, msg))

    def get_feedback(self):
        return self.feedback_log

class ConversationalInterface:
    def interact(self, prompt):
        response = f"Nomimi received: {prompt}"
        print(response)
        return response