import os

from baseball_scorecard.misc.game_info import GameInfo
from baseball_scorecard.team.team import Team
from baseball_scorecard.plays.inning import Inning
from baseball_scorecard.misc.umpire import Umpire


class MetapostBuilder:

    min_innings = 15

    def __init__(
        self,
        output_dir: str,
        template_dir: str,
        game_info: GameInfo,
        away_team: Team,
        home_team: Team,
        umpires: list[Umpire],
        innings: list[Inning],
    ):
        self.output_dir = output_dir
        self.template_dir = template_dir
        self.game_info = game_info
        self.away_team = away_team
        self.home_team = home_team
        self.umpires = umpires
        self.top_innings = []
        self.bottom_innings = []

        for inning in innings:
            if inning.top:
                self.top_innings.append(inning)
            else:
                self.bottom_innings.append(inning)

        # Set the templates folder location.
        if not self.template_dir:
            self.template_dir = os.path.join(
                os.path.dirname(os.path.abspath(__file__)), "templates"
            )

    def generate_away_scorecard(self):
        self.__generate_team_scorecard(is_away_team=True)

    def generate_home_scorecard(self):
        self.__generate_team_scorecard(is_away_team=False)

    def __generate_team_scorecard(self, is_away_team: bool = False):
        if is_away_team:
            batting_team = self.away_team
            fielding_team = self.home_team
            innings = self.top_innings
            file_name_suffix = "away"
        else:
            batting_team = self.home_team
            fielding_team = self.away_team
            innings = self.bottom_innings
            file_name_suffix = "home"

        # Open the template file and read it.
        with open(os.path.join(self.template_dir, "team_scorecard_template.mp")) as fd:
            scorecard_template = fd.read()

        # Open the file for writing and write all the generated information.
        with open(
            os.path.join(self.output_dir, f"scorecard_{file_name_suffix}.mp"), "w"
        ) as scorecard_fd:
            # Write the template for the scorecard.
            scorecard_fd.write(scorecard_template)
            scorecard_fd.write("\n\n")

            # Obtain the number of innings required for the scorecard.
            # It is the maximum number between 15, or the amount of innings of the away team.
            inning_num = (
                len(self.top_innings)
                if len(self.top_innings) > MetapostBuilder.min_innings
                else MetapostBuilder.min_innings
            )

            # Open the figure where the scorecard is to be drawn.
            scorecard_fd.write("beginfig(0);\n")
            scorecard_fd.write(f"    innings := {inning_num};\n")
            scorecard_fd.write("    draw_full_scorecard(innings);\n\n")
            scorecard_fd.write("    clr:=scoring;\n\n")

            # Print the game data.
            scorecard_fd.write(self.game_info.get_metapost_data())

            # Print the umpires.
            for umpire in self.umpires:
                scorecard_fd.write(umpire.get_metapost_data())

            # Print the team data.
            scorecard_fd.write(batting_team.get_team_metapost_data())

            # Print the opposing pitchers.
            scorecard_fd.write(fielding_team.get_pitcher_metapost_data())

            # Print the innings.
            overflow = 0
            for inning in innings:
                inning_txt, overflow = inning.get_metapost_data(overflow)
                scorecard_fd.write(inning_txt)

            # Print the batter stats data.
            scorecard_fd.write(batting_team.get_batter_stats_metapost_data())

            # Print the pitcher stats data.
            scorecard_fd.write(fielding_team.get_pitcher_stats_metapost_data())

            # Print the game stats data.
            pitching_stats = fielding_team.get_pitching_totals()
            total_at_bats = batting_team.get_total_at_bats()
            scorecard_fd.write(
                batting_team.get_stats_metapost_data(total_at_bats, pitching_stats)
            )

            # Close the scorecard figure.
            scorecard_fd.write("endfig;\n")
            scorecard_fd.write("end\n")

    def generate_scorecard(self):
        with open(
            os.path.join(self.template_dir, "final_scorecard_template.tex")
        ) as template:
            with open(
                os.path.join(self.output_dir, "scorecard.tex"), "w"
            ) as scorecard_tex_fd:
                scorecard_tex_fd.write(template.read())
