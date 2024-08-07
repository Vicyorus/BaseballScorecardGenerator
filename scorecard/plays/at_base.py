class AtBase:

    atbase_labels = {
        1: {"suffix": "rt", "location": "first"},
        2: {"suffix": "top", "location": "second"},
        3: {"suffix": "lft", "location": "third"},
        4: {"suffix": "bot", "location": "home"},
    }

    def __init__(self, label, base):
        self.label = label
        self.base = base

    def get_metapost_data(self):
        labels = AtBase.atbase_labels[self.base]
        return f"label.{labels['suffix']}(btex {{\\sf {self.label}}} etex, {labels['location']}) withcolor clr;"

    def __str__(self):
        return f'Label at base {self.base}: {self.label}'
