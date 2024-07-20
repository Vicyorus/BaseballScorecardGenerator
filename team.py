from player import Player
from roster import Roster
from lineup import Lineup
from pitcher_lineup import PitcherLineup
from reserves import Reserves

class Team:
    def __init__(self, data, use_extended_roster):
        self.team = data["team"]
        self.lefties = data["lefties"]
        self.bench = data["bench"]
        self.bullpen = data["bullpen"]

        self.roster = Roster(data["roster"], use_extended_roster)
        self.lineup = Lineup(data["lineup"], self.roster)
        self.pitcher_lineup = PitcherLineup(data["starter"], self.roster)

        self.reserves = Reserves(data["bullpen"], data["bench"], self.roster)

        # TODO: Should these live inside the respective lineups?
        self.current_batter = 1
        self.current_pitcher = data["starter"]
    
    def add_pitcher(self, pitcher_id, inning):
        # Sanity check, ensure the pitcher is in the roster.
        pitcher = self.roster.get_player(pitcher_id)
        if not pitcher:
            raise Exception(f'No pitcher found with the ID {pitcher_id} for team {self.team}')

        # TODO: Mark the pitcher as out of the bullpen/bench.
        pitcher.set_lineup_position("1", inning)
        self.pitcher_lineup.add_pitcher(pitcher_id)

    def add_player(self, order, player_id, position, inning):
        # Sanity check, ensure the player is in the roster.
        player = self.roster.get_player(player_id)
        if not player:
            raise Exception(f'No player found with the ID {player_id} for team {self.team}')
        
        # TODO: Mark the player as out of the bench/bullpen.
        player.set_lineup_position(position, inning)

        self.lineup.add_player(order, player_id)

    def __str__(self):
        result = f"{self.team}\n\n"
        result += f"{str(self.lineup)}\n"
        result += f"{str(self.pitcher_lineup)}\n"
        result += f"{str(self.reserves)}\n"

        return result
