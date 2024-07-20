class Umpire:
    label_locations = {
        "HP": (2192, 228),
        "1B": (2224, 228),
        "2B": (2192, 578),
        "3B": (2224, 578),
        "LF": (2192, 928),
        "RF": (2224, 928),
    }

    def __init__(self, position, name):
        self.lineup_position = position
        self.name = name

    def __str__(self):
        return f'{self.lineup_position}: {self.name}\n'
