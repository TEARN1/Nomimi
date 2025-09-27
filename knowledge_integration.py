class KnowledgeIntegrator:
    def __init__(self):
        self.knowledge_graph = {}

    def update_knowledge(self, new_data):
        for topic, info in new_data.items():
            self.knowledge_graph[topic] = info

    def get_latest(self, topic):
        return self.knowledge_graph.get(topic, None)