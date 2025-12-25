class EthicalCompressionLoop:
    def __init__(self, stabilizer, rules):
        self.stabilizer = stabilizer
        self.rules = rules

    def compress(self, ethical_text):
        previous = ethical_text
        for _ in range(10):
            hardened = self.stabilizer.stabilize(previous)
            if self.rules.is_converged(previous, hardened):
                break
            previous = hardened
        return hardened