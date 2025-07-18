class SymbolTable:
    def __init__(self):
        self.table = {}

    def __setitem__(self, key, value):
        self.table[key] = value

    def __getitem__(self, key):
        return self.table.get(key, None)

    def __contains__(self, key):
        return key in self.table
