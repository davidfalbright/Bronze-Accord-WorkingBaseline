class BraveEngine:
    def __init__(self, scanner, extractor, ranker, formatter, binder):
        self.scanner = scanner
        self.extractor = extractor
        self.ranker = ranker
        self.formatter = formatter
        self.binder = binder

    def process_input(self, text):
        tagged = self.scanner.tag(text)
        extracted = self.extractor.extract(tagged)
        ranked = self.ranker.rank(extracted)
        formatted = self.formatter.format(ranked)
        bound = self.binder.bind(formatted)
        return bound