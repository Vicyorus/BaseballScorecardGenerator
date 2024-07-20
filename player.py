class Player:
    # TODO: Add inning when the player entered the game.
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

    def __str__(self):
        return f'{self.lineup_position} #{self.number} {self.name} ({self.inning_entered})'
