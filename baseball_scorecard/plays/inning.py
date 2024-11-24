from baseball_scorecard.plays.at_bat import AtBat
from baseball_scorecard.plays.substitution.pitcher import PitchingSubstitution
from baseball_scorecard.plays.substitution.batter import OffensiveSubstitution
from baseball_scorecard.stats.inning_stats import InningStats
from baseball_scorecard.team.team import Team


class Inning:
    """
    Represents a frame (or half-inning) of an inning.

    Attributes:
        top (bool): Whether the half-inning is the top or the bottom.
    """

    def __init__(self, number: int, top: bool, away_team: Team, home_team: Team):
        self.__number = number
        self.top = top
        self.__events = []
        self.__current_ab: AtBat = None
        self.__outs = {1: False, 2: False, 3: False}
        self.__stats = InningStats()

        if self.top:
            self.__fielding_team = home_team
            self.__batting_team = away_team
        else:
            self.__fielding_team = away_team
            self.__batting_team = home_team

    def new_ab(self, is_risp: bool = False):
        """Generates a new at-bat.

        Args:
            is_risp (bool, optional): Result of this at-bat counts for the
                team's batting average with runners in scoring position stat.
                Default is False."""
        ab = AtBat(
            self.__batting_team.lineup.current_batter,
            self.__batting_team.get_batter(),
            self.__fielding_team.get_current_pitcher(),
            self.__stats,
            is_risp,
        )
        self.__batting_team.next_batter()
        self.__events.append(ab)
        self.__current_ab = ab

    # Substitutions.
    def pitching_substitution(self, pitcher_id: int):
        """Registers a pitching substitution for the fielding team.

        Args:
            pitcher_id (int): Player ID for the entering pitcher.
        """
        self.__fielding_team.add_pitcher(pitcher_id, self.__number)
        self.__events.append(
            PitchingSubstitution(
                self.__batting_team.lineup.current_batter,
                str(self.__fielding_team.get_current_pitcher()),
            )
        )

    def offensive_substitution(self, order: int, player_id: int, position: str):
        """Registers an offensive substitution for the batting team.

        Args:
            order (int): Order in the lineup where the batter will bat (1-9).
            player_id (int): Player ID for the entering batter.
            position (str): Position for the new player, can be either `PH`
                for a pinch-hitter, or `PR` for a pinch-runner.
        """
        self.__batting_team.add_player(order, player_id, position, self.__number)
        self.__events.append(
            OffensiveSubstitution(
                order,
                str(self.__batting_team.roster.get_player(player_id)),
                True if position.upper() == "PR" else False,
            )
        )

    def defensive_substitution(self, order: int, player_id: int, position: str):
        """Registers a defensive substitution for the fielding team.

        Args:
            order (int): Order in the lineup where the fielder will bat (1-9).
            player_id (int): Player ID for the entering fielder.
            position (str): Position in the field for the new player.
        """
        self.__fielding_team.add_player(
            order, player_id, position, self.__number, is_defensive_sub=True
        )

    def defensive_switch(self, player_id: int, position: str):
        """Registers a defensive switch for the fielding team.

        Args:
            player_id (int): Player ID for the fielder.
            position (str): New defensive position for the fielder.
        """
        self.__fielding_team.defensive_switch(player_id, position)

    # Pitches.
    def pitch_list(self, pitches: str):
        """Register the pitches in a given at-bat.

        Args:
            pitches (str): List of pitches, each pitch separated by a space.
                The following codes are recognized:
                - `pso`: Pitcher step-off.
                - `1`, `2` or `3`: Pickoff attempts at 1B, 2B or 3B.
                - `vp`: Pitch clock violation on the pitcher,
                        counts as a ball.
                - `ab`: Pitch clock violation on the batter,
                        counts as a strike.
                - `s`: Swinging strike.
                - `c`: Called strike.
                - `f`: Foul.
                - `b`: Ball.
                - `d`: Ball in dirt.
                - `p`: Pitchout, counts as a ball.
                - `m`: Missed bunt attempt.
                - `t`: Foul tip.
                - `l`: Foul bunt.
        """
        self.__current_ab.pitch_list(pitches)

    # Batter results.
    def out(self, play: str, rbis: int = 0):
        """Register an out for the batter in the at-bat.

        Args:
            play (str): The play on which the out was made.
                Starting the play with the following codes will automatically
                tally certain statistics:
                - K: Swinging strikeout.
                - !K: Called strikeout.
                - SAC: Sacrifice bunt.
                - SF: Sacrifice fly.
                - DP: Double play.
                - TP: Triple play.
            rbis (int, optional): If the play resulted in runs batted in, set
                the number of RBIs. Default is 0.
        """
        # Sanity check, ensure the user isn't adding more than 3 outs.
        out_added = 0
        for i in range(1, 4):
            if not self.__outs[i]:
                self.__outs[i] = True
                out_added = i
                break
        if out_added == 0:
            raise Exception("More than 3 outs in inning")

        # Add team stats for the batting team.
        if "DP" in play.upper():
            self.__batting_team.get_stats().double_plays += 1
        if "TP" in play.upper():
            self.__batting_team.get_stats().triple_plays += 1
        if "SAC" in play.upper():
            self.__batting_team.get_stats().sac_bunts += 1
        if "SF" in play.upper():
            self.__batting_team.get_stats().sac_flys += 1

        # If this was an AB with RISP, add it to the team stats.
        if self.__current_ab.is_risp and self.__is_at_bat_out(play):
            self.__batting_team.get_stats().risp_at_bats += 1

        self.__current_ab.out(play, out_added, rbis=rbis)

    def hit(self, bases: str | int, rbis: int = 0):
        """Registers a hit for the batter in the at-bat.

        Args:
            bases (int/str): The amount of bases the hit allowed, from 1-4.
                In case the hit is classified as an unearned home run, use "U".
            rbis (int, optional): If the play resulted in runs batted in, set
                the number of RBIs. Default is 0.
        """
        # Add the corresponding type of hit for the batting team.
        hit_type = 4 if bases == "U" else bases
        self.__batting_team.stats.hits[hit_type] += 1

        # Unless the hit is not a home run, add a batter left on the basepaths.
        # If they get thrown out or advance to home, they will be removed.
        if hit_type != 4:
            self.__batting_team.stats.left_on_base += 1
            self.__stats.left_on_base += 1

        # If the hit is a home run, check if the user gave a number of RBIs and
        # use that, otherwise add one RBI by default.
        rbis_to_add = rbis
        if hit_type == 4 and rbis_to_add == 0:
            rbis_to_add = 1

        # If the hit is a home run, add a run to the batting team.
        if hit_type == 4:
            self.__batting_team.stats.runs += 1

        # If this was an AB with RISP, add it to the team stats.
        if self.__current_ab.is_risp:
            self.__batting_team.get_stats().risp_at_bats += 1
            self.__batting_team.get_stats().risp_hits += 1

        self.__current_ab.hit(bases, rbis=rbis_to_add)

    def reach(self, play: str, end_base: int = 1, rbis: int = 0):
        """Registers the batter reaching base in a non-hit play.

        Args:
            play (str): The play on which the batter reached base.
                Starting the play with the following codes will automatically
                tally certain statistics:
                - E: Fielding error.
                - BB: Base on Balls.
                - IBB: Intent walk.
                - HBP: Hit by pitch.
                - CI: Catcher's interference.
                - K: Strikeout.
                - SAC: Sacrifice bunt.
                - SF: Sacrifice fly.
                - DP: Double play.
            end_base (int, optional): If the batter-runner reached past 1B,
                use this argument. Default is 1 for 1B.
            rbis (int, optional): If the play resulted in runs batted in, set
                the number of RBIs. Default is 0.
        """
        # Since a batter reached base, mark them as left on base.
        # If they get thrown out or advance to home, they will be removed.
        self.__batting_team.stats.left_on_base += 1
        self.__stats.left_on_base += 1

        # If this was an AB with RISP, check if it needs to be counted.
        # Cases where this would not count include:
        # - Walks
        # - Hit by pitch
        # - Catcher's interference
        if self.__current_ab.is_risp and self.__is_at_bat_reach(play):
            self.__batting_team.get_stats().risp_at_bats += 1

        if "DP" in play.upper():
            self.__batting_team.get_stats().double_plays += 1
        if "SAC" in play.upper():
            self.__batting_team.get_stats().sac_bunts += 1
        if "SF" in play.upper():
            self.__batting_team.get_stats().sac_flys += 1

        self.__current_ab.reach(play, end_base=end_base, rbis=rbis)

    def __is_at_bat_out(self, play: str):
        if "SF" in play.upper() or "SAC" in play.upper():
            return False

        return True

    def __is_at_bat_reach(self, play: str):
        if play.upper() in ["BB", "IBB", "HBP", "HP", "CI"]:
            return False

        if "SAC" in play.upper() or "SF" in play.upper():
            return False

        return True

    # Runner results.
    def advance(self, end_base: str | int, play: str):
        """Registers a runner advancing bases.

        Args:
            end_base (int/str): The final base reached by the batter on a play.
                This can be:
                - 2: Second base.
                - 3: Third base.
                - 4: Home, for an earned run.
                - U: Home, for an unearned run.
            play (str): The play on which the runner advanced. If `SB` is used
                in the play, a stolen base is credited to the runner.
        """
        # Check if the runner reached home plate, add the corresponding
        # statistics to the team.
        if end_base == 4 or end_base == "U":
            self.__batting_team.stats.runs += 1
            self.__batting_team.stats.left_on_base -= 1
            self.__stats.left_on_base -= 1

        # Check if the batter stole a base, and if so, add a stolen base for
        # the batting team.
        if "SB" in play.upper():
            self.__batting_team.stats.stolen_bases += 1

        self.__current_ab.advance(end_base, play)

    def thrown_out(
        self,
        out_base: str | int,
        play: str,
        out_number: int = None,
        pitcher_id: int = None,
    ):
        """Registers a runner getting thrown out in the basepaths.

        Args:
            out_base (int): The final base reached by the batter on a play.
                - 2: Second base.
                - 3: Third base.
                - 4: Home, for an earned run.
                - U: Home, for an unearned run.
            play (str): The play on which the runner advanced.
                If `CS` is used in the play, a caught stealing is credited
                to the runner.
                IF `PO` is used in the play, a pickoff is credited
                to the runner.
            out_number (int, optional): Specific out number to use,
                otherwise the scorecard will assign the next available out.
            pitcher_id (int, optional): Player ID of the pitcher that made
                the out. Useful for when pitching changes occur mid-inning and
                the new pitcher makes an out on an inherited runner.
        """
        # Runner is no longer in the basepaths, remove them from the LOB count.
        self.__batting_team.stats.left_on_base -= 1
        self.__stats.left_on_base -= 1

        # Add stats to the team if the batter was thrown out caught
        # stealing or picked off.
        if "PO" in play.upper():
            self.__batting_team.stats.picked_off += 1

        if "CS" in play.upper():
            self.__batting_team.stats.caught_stealing += 1

        # Record the out in either the first available out, or in
        # the indicated out number.
        if out_number:
            if self.__outs[out_number]:
                raise Exception(
                    "Indicated out for thrown_out call has already been used."
                )

            self.__outs[out_number] = True
            out_added = out_number
        else:
            out_added = 0
            for i in range(1, 4):
                if not self.__outs[i]:
                    self.__outs[i] = True
                    out_added = i
                    break
            if out_added == 0:
                raise Exception("More than 3 outs in inning")

        # If the pitcher_id is passed, pass the pitcher to the at-bat object.
        responsible_pitcher = None
        if pitcher_id:
            responsible_pitcher = self.__fielding_team.roster.get_player(pitcher_id)

        self.__current_ab.thrown_out(out_base, play, out_added, responsible_pitcher)

    def place_runner(self, player_id: int = None, base: int = 2, label: str = None):
        """
        Registers a runner placed on base. Mostly to be used for extra-inning "ghost runners".

        Args:
            player_id (int, optional): The ID for the runner to be placed on base.
                If not provided, defaults to the last batter.
            base (int, optional): The base in which to place the runner.
                Defaults to 2 for 2B.
            label (str, optional): The label to put on the runner's base.
                Defaults to "RP" for "runner placed".
        """
        # Since the ghost runner counts for LOB, add a runner to the statistics.
        self.__batting_team.stats.left_on_base += 1
        self.__stats.left_on_base += 1

        # If the player ID is passed, get the player, otherwise obtain the previous batter.
        if player_id:
            lineup_pos, runner = self.__batting_team.get_player_in_lineup(player_id)
        else:
            lineup_pos, runner = self.__batting_team.get_previous_batter()

        # Create a new at-bat.
        ab = AtBat(
            lineup_pos,
            runner,
            self.__fielding_team.get_current_pitcher(),
            self.__stats,
        )
        self.__events.append(ab)
        self.__current_ab = ab

        # Place the runner on the base.
        self.__current_ab.reach(label if label else "RP", end_base=base)
        self.__current_ab.atbase(label if label else "RP", base)

    # Miscelaneous functions to detail additional events for the at-bat.
    def error(self, fielder: int):
        """Registers a fielding error.

        Args:
            fielder (int): Position of the fielder who made the error (1-9).
        """
        self.__fielding_team.stats.errors += 1
        self.__stats.errors += 1

    def balk(self):
        """Registers a balk to the current pitcher."""
        # Add a balk to the current pitcher. Advancements are to be handled
        # by calls to the advance method.
        self.__fielding_team.get_current_pitcher().pitcher_stats.balks += 1

    def wp(self, quantity: int = 1):
        """Registers a wild pitch to the current pitcher.

        Args:
            quantity (int, optional): The number of wild pitches in the at-bat.
              Defaults to 1.
        """
        self.__fielding_team.get_current_pitcher().pitcher_stats.wild_pitches += (
            quantity
        )

    def pb(self, quantity: int = 1):
        """Registers a passed ball to the fielding team.

        Args:
            quantity (int, optional): The number of passed balls in the at-bat.
                Defaults to 1.
        """
        self.__batting_team.stats.passed_balls += quantity

    def atbase(self, label: str, base: int = None):
        """Adds a label at a specific base.

        Args:
            label (str): The label to put at a given base.
            base (int, optional): The base to put the label at.
                By default, it will be placed at 1B.
        """
        self.__current_ab.atbase(label, base)

    def no_ab(self, label: str):
        """Registers that the at-bat was not completed and needs to continue.

        Args:
            label (str): Label to put in the center of the diamond.
        """
        # Since no at-bat occurred, when a new at-bat for the current batting
        # team is created, it should use the current batter.
        self.__batting_team.no_ab()
        self.__current_ab.no_ab(label)

    def get_at_bat_amount(self):
        return len([at_bat for at_bat in self.__events if isinstance(at_bat, AtBat)])

    def get_metapost_data(self, overflow: int):
        result = f"    % inning #{self.__number}\n"

        x_start = 128 * (self.__number + overflow - 1)
        result += f"    xstart := {x_start};\n"
        result += "    set_inning_num_label_vars(xstart);\n"
        result += f"    label(btex {{\\bigsf {self.__number}}} etex, top_inn_label) withcolor clr;\n"
        result += "\n"

        # In defensive substitutions, the expectation is that these are
        # registered while the team is fielding, but they will be printed
        # when they are batting.
        if self.__number in self.__batting_team.defensive_subs.keys():
            self.__events = (
                self.__batting_team.defensive_subs[self.__number] + self.__events
            )

        at_bats_printed = 1
        for event in self.__events:
            # Check for overflow only in at-bats, substitutions don't need
            # to do this check.
            if type(event) is AtBat:
                # Move the X start if the lineup has rolled over.
                if at_bats_printed > 9:
                    at_bats_printed = 1
                    overflow += 1
                    x_start += 128
                    result += f"    xstart := {x_start};\n"
                    result += "    set_inning_num_label_vars(xstart);\n"
                    result += "\n"

                at_bats_printed += 1

            result += event.get_metapost_data(self.__number)

        result += f"    label(btex {{\\bigsf {self.__number}}} etex, bot_inn_label) withcolor clr;\n"

        result += self.__stats.get_metapost_data()

        result += "    draw_inning_end(xstart,ystart,innendclr);\n"
        return (result, overflow)

    def __str__(self):
        inn = "Top" if self.top else "Bottom"
        result = f"{inn} of the {self.__ordinal(self.__number)}\n"

        if self.__number in self.__fielding_team.defensive_subs.keys():
            self.__events = (
                self.__fielding_team.defensive_subs[self.__number] + self.__events
            )

        for event in self.__events:
            result += f"{event}"

        result += f"{self.__stats}"
        result += "\n"
        return result

    def __ordinal(self, n: int):
        if 11 <= (n % 100) <= 13:
            suffix = "th"
        else:
            suffix = ["th", "st", "nd", "rd", "th"][min(n % 10, 4)]
        return str(n) + suffix
