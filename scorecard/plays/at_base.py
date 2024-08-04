class AtBase:
    def __init__(self, label, base):
        self.label = label
        self.base = base

    def __str__(self):
        return f'Label at base {self.base}: {self.label}'
