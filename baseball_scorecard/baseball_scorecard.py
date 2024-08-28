# -*- coding: utf-8 -*-
"""Baseball scorecard generator for Python

This module provides an API to record a baseball game, and generate a series
of Metapost files that can be compiled into a PDF baseball_scorecard.
"""

from baseball_scorecard.plays.inning import Inning
from baseball_scorecard.misc.umpire import Umpire
from baseball_scorecard.misc.game_info import GameInfo
from baseball_scorecard.team.team import Team
from baseball_scorecard.metapost.metapost_builder import MetapostBuilder


class Scorecard:
    """Represents a scorecard to record a baseball game.

    Args:
        output_dir (str): Full path to which to output the Metapost files.
        data (dict): Data of the baseball game. Format of this argument can be
            found in the README for the project.
    """
    def __init__(self, output_dir: str, data: dict):
        self.__output_dir = output_dir

        # Sanity check, ensure there is an "extended_roster" key in the data.
        if "extended_roster" not in data.keys():
            data["extended_roster"] = False

        self.__game_info = GameInfo(data)

        self.__away = self.__create_team(data["away"], data["extended_roster"])
        self.__home = self.__create_team(data["home"], data["extended_roster"])

        self.__innings = []
        self.__current_inning = 1
        self.__is_top_inning = True

        self.__umpires = self.__create_umpires(data)

    def __create_team(self, team_data: dict,
                      use_extended_roster: bool) -> Team:
        return Team(team_data, use_extended_roster)

    def __create_umpires(self, data: dict) -> list:
        umpire_list = []

        # If there are umpires in the game data, use them.
        # Otherwise, use a blank dict.
        if "umpires" in data.keys():
            umpires = data["umpires"]
        else:
            umpires = {}

        # Fill any blanks in the umpire data.
        for position in ["HP", "1B", "2B", "3B", "LF", "RF"]:
            if position not in umpires.keys():
                umpires[position] = "N/A"

        for position in umpires.keys():
            umpire = Umpire(position, umpires[position])
            umpire_list.append(umpire)

        return umpire_list

    def new_inning(self) -> Inning:
        """Creates a new Inning object and adds it to the baseball_scorecard.

        Returns:
            Inning: A new Inning object.
        """

        # Create the new inning and add it to the list of innings.
        inning = Inning(
            self.__current_inning, self.__is_top_inning,
            self.__away, self.__home)
        self.__innings.append(inning)

        # Move the inning counters.
        self.__is_top_inning = not self.__is_top_inning
        if self.__is_top_inning:
            self.__current_inning += 1

        return inning

    def winning_pitcher(self, pitcher_id: int, is_away_team: bool = False):
        """Notes down the winning pitcher for the game.

        Args:
            pitcher_id (int): Player ID for the pitcher.
            is_away_team (bool): Set this to true is pitcher is from
                the away team.
                By default set to False, pitcher is assumed to be from
                the home team.
        """

        if is_away_team:
            self.__away.winning_pitcher(pitcher_id)
        else:
            self.__home.winning_pitcher(pitcher_id)

    def losing_pitcher(self, pitcher_id, is_away_team=False):
        """Notes down the losing pitcher for the game.

        Args:
            pitcher_id (int): Player ID for the pitcher.
            is_away_team (bool): Set this to true is pitcher is from
                the away team.
                By default set to False, pitcher is assumed to be from
                the home team.
        """

        if is_away_team:
            self.__away.losing_pitcher(pitcher_id)
        else:
            self.__home.losing_pitcher(pitcher_id)

    def save_pitcher(self, pitcher_id, is_away_team=False):
        """Notes down the save pitcher for the game.

        Args:
            pitcher_id (int): Player ID for the pitcher.
            is_away_team (bool): Set this to true is pitcher is from
                the away team.
                By default set to False, pitcher is assumed to be from
                the home team.
        """

        if is_away_team:
            self.__away.save_pitcher(pitcher_id)
        else:
            self.__home.save_pitcher(pitcher_id)

    def generate_scorecard(self):
        """Generates the Metapost files with the completed baseball_scorecard."""

        builder = MetapostBuilder(
            self.__output_dir, self.__game_info, self.__away,
            self.__home, self.__umpires, self.__innings)
        builder.generate_away_scorecard()
        builder.generate_home_scorecard()
        builder.generate_scorecard()

    def __str__(self):
        result = f"{self.__game_info}"

        result += f"Away team: {self.__away}"
        result += f"Home team: {self.__home}"

        result += "Umpires:\n"
        for ump in self.__umpires:
            result += str(ump)

        result += "\n"
        result += "Play ball!\n"
        result += "\n"

        for inn in self.__innings:
            result += str(inn)

        return result
