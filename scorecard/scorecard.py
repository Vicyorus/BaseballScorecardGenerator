from scorecard.inning import Inning
from scorecard.umpire import Umpire
from scorecard.team import Team

class Scorecard:
    def __init__(self, data):

        # Sanity check, ensure there is an "extended_roster" key in the data.
        if "extended_roster" not in data.keys():
            data["extended_roster"] = False

        self.scorer = data["scorer"]
        self.date = data["date"]
        self.at = data["at"]
        self.att = data["att"]
        self.temp = data["temp"]
        self.wind = data["wind"]

        self.away = self.__create_team(data["away"], data["extended_roster"])
        self.home = self.__create_team(data["home"], data["extended_roster"])

        self.innings = []
        self.current_inning = 1
        self.is_top_inning = True

        if "umpires" in data.keys():
            self.umpires = self.__create_umpires(data["umpires"])
        else:
            self.umpires = []

    def __create_team(self, team_data, use_extended_roster):
        return Team(team_data, use_extended_roster)

    def __create_umpires(self, umpires):
        umpire_list = []

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

    def __str__(self):
        result = ""

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
