from scorecard.stats.batter_stats import BatterStats
from scorecard.stats.pitcher_stats import PitcherStats

class Player:
    # TODO: Currently this model only allows for one inning to be specified per player, should we expand to support switches?
    def __init__(self, id, number, name):
        self.id = id
        self.number = number
        self.name = name
        self.lineup_position = ""
        self.primary_position = ""
        self.is_bullpen = False
        self.in_lineup = False
        self.inning_entered = 0

        self.batter_stats = BatterStats()
        self.pitcher_stats = PitcherStats()

    def set_lineup_position(self, position, inning):
        self.in_lineup = True
        self.lineup_position = position
        self.inning_entered = inning

    def set_primary_position(self, position):
        self.primary_position = position

    def set_as_bullpen(self):
        self.set_primary_position("P")
        self.is_bullpen = True

    def is_in_lineup(self):
        return self.in_lineup

    def get_reserves_str(self):
        return f'#{self.number} {self.name} ({self.primary_position})'

    def get_lineup_str(self):
        return f'{self.__code_to_position(self.lineup_position)} {str(self)} ({self.inning_entered}) {str(self.batter_stats)}'

    def __code_to_position(self, code):
        codes = {
            "1": "P",
            "2": "C",
            "3": "1B",
            "4": "2B",
            "5": "3B",
            "6": "SS",
            "7": "LF",
            "8": "CF",
            "9": "RF",
            "0": "DH",
            "10": "DH",
            "PH": "PH",
            "PR": "PR",
        }

        return codes[code]

    def get_pitcher_str(self):
        return f'{str(self)} ({self.inning_entered}) {str(self.pitcher_stats)}'

    def __str__(self):
        return f'#{self.number} {self.name}'
