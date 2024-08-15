from scorecard.plays.inning import Inning
from scorecard.misc.umpire import Umpire
from scorecard.misc.game_info import GameInfo
from scorecard.team.team import Team
from scorecard.metapost.metapost_builder import MetapostBuilder

class Scorecard:
    def __init__(self, output_dir, data):
        self.output_dir = output_dir

        # Sanity check, ensure there is an "extended_roster" key in the data.
        if "extended_roster" not in data.keys():
            data["extended_roster"] = False

        self.game_info = GameInfo(data)

        self.away = self.__create_team(data["away"], data["extended_roster"])
        self.home = self.__create_team(data["home"], data["extended_roster"])

        self.innings = []
        self.current_inning = 1
        self.is_top_inning = True

        self.umpires = self.__create_umpires(data)

    def __create_team(self, team_data, use_extended_roster):
        return Team(team_data, use_extended_roster)

    def __create_umpires(self, data):
        umpire_list = []

        # If there are umpires in the game data, use them. Otherwise, use a blank dict.
        if "umpires" in data.keys():
            umpires = data["umpires"]
        else:
            umpires = {}

        # Fill any blanks in the umpire data.
        for position in ["HP", "1B", "2B", "3B", "LF", "RF"]:
            if not position in umpires.keys():
                umpires[position] = "N/A"

        for position in umpires.keys():
            umpire = Umpire(position, umpires[position])
            umpire_list.append(umpire)

        return umpire_list

    def new_inning(self):

        # Create the new inning and add it to the list of innings.
        inning = Inning(self.current_inning, self.is_top_inning, self.away, self.home)
        self.innings.append(inning)

        # Move the inning counters.
        self.is_top_inning = not self.is_top_inning
        if self.is_top_inning:
            self.current_inning += 1

        return inning

    # TODO: Add methods for recording WLS on pitchers.

    def generate_scorecard(self):
        builder = MetapostBuilder(self.output_dir, self.game_info, self.away, self.home, self.umpires, self.innings)
        builder.generate_away_scorecard()
        builder.generate_home_scorecard()
        builder.generate_scorecard()

    def __str__(self):
        result = f"{self.game_info}"

        result += f"Away team: {self.away}"
        result += f"Home team: {self.home}"

        result += "Umpires:\n"
        for ump in self.umpires:
            result += str(ump)

        result += "\n"
        result += "Play ball!\n"
        result += "\n"

        for inn in self.innings:
            result += str(inn)

        return result
