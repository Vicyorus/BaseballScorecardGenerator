class Umpire:
    label_locations = {
        "HP": "game_hp_ump",
        "1B": "game_first_ump",
        "2B": "game_second_ump",
        "3B": "game_third_ump",
        "LF": "game_lf_ump",
        "RF": "game_rf_ump",
    }

    umpire_template = (
        "    label.top(btex {{\\bigsf {}}} etex rotated 90, {}) withcolor clr;\n"
    )

    def __init__(self, position, name):
        self.ump_position = position
        self.name = name

    def get_metapost_data(self):
        return Umpire.umpire_template.format(
            self.name, Umpire.label_locations[self.ump_position]
        )

    def __str__(self):
        return f"{self.ump_position}: {self.name}\n"
