class TradeStudy:
    def __init__(self, options):
        self.options = options
        self.scores = {}

    def evaluate(self, criteria):
        for option, params in self.options.items():
            score = sum(params.get(c, 0) for c in criteria)
            self.scores[option] = score

    def best_option(self):
        return max(self.scores, key=self.scores.get)