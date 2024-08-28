class Umpire:
    label_locations = {
        "HP": (2192, 228),
        "1B": (2224, 228),
        "2B": (2192, 578),
        "3B": (2224, 578),
        "LF": (2192, 928),
        "RF": (2224, 928),
    }

    umpire_template = "    label.top(btex {{\\bigsf {}}} etex rotated 90, {}) withcolor clr;\n"

    def __init__(self, position, name):
        self.ump_position = position
        self.name = name

    def get_metapost_data(self):
        return Umpire.umpire_template.format(self.name, Umpire.label_locations[self.ump_position])

    def __str__(self):
        return f'{self.ump_position}: {self.name}\n'
