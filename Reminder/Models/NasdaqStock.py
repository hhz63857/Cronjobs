import BaseObject

class NasdaqStock(BaseObject):
    id = None
    symbol = None
    pattern = None
    min = 0
    max = 10000

    def __init__(self, id, symbol, pattern, min, max):
        self.id = id
        self.symbol = symbol
        self.pattern = pattern
        self.min = min
        self.max = max
        BaseObject.BaseObject.__init__()

    def generate_id(self):
        id = 0
        for c in self.symbol:
            id += (ord(c) - 97)
            id *= 26
        return id