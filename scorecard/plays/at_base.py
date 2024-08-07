class AtBase:
    def __init__(self, label, base):
        self.label = label
        self.base = base

    def get_metapost_data(self):
        # TODO: Implement me!
        return ""

    def __str__(self):
        return f'Label at base {self.base}: {self.label}'
