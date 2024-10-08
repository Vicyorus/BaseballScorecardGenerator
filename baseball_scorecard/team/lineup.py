from baseball_scorecard.stats.batter_stats import BatterStats
from baseball_scorecard.team.roster import Roster
from baseball_scorecard.team.player import Player


class Lineup:

    max_replacements = 4
    max_extras = 7

    def __init__(self, lineup_data: list[list[int, str]], roster: Roster):
        self.lineup: list[list[Player]] = []
        self.current_batter: int = 1

        for lineup_player in lineup_data:
            player = roster.get_player(lineup_player[0])
            player.set_lineup_position(lineup_player[1], 1)

            self.lineup.append([player])

    def add_player(self, order: int, player: Player, position: str, inning: int):
        player.set_lineup_position(position, inning)
        self.lineup[order - 1].append(player)

    def get_batter(self) -> Player:
        return self.lineup[self.current_batter - 1][-1]

    def next_batter(self):
        self.current_batter += 1
        self.current_batter %= 10
        if self.current_batter == 0:
            self.current_batter = 1

    def get_previous_batter(self) -> tuple[int, Player]:
        self.no_ab()
        lineup_pos = self.current_batter
        batter = self.get_batter()
        self.next_batter()
        return lineup_pos, batter

    def get_player_in_lineup(self, player_id: int) -> tuple[int, Player]:
        for order, lineup_position in enumerate(self.lineup):
            if lineup_position[-1].id == player_id:
                return order + 1, lineup_position[-1]

        return -1, None

    def no_ab(self):
        if self.current_batter in [0, 1]:
            self.current_batter = 9
        else:
            self.current_batter -= 1

    def get_total_at_bats(self) -> int:
        total_abs = 0
        for position in self.lineup:
            for player in position:
                # Get the player information.
                total_abs += player.batter_stats.at_bats
        return total_abs

    def get_batter_info_metapost_data(self) -> str:
        result = "    % lineup info\n"

        # Go through the positions in the lineup
        extras_position_idx = 1
        position_idx = 0
        for position in self.lineup:
            spot_idx = 0
            position_idx += 1
            # Go through the spots in each of the positions.
            for player in position:
                spot_idx += 1

                # In case the limit of max replacements in the scorecard has been reached,
                # print out the player in the extra slots.
                if spot_idx > Lineup.max_replacements:

                    # If all the extras are filled up, don't continue printing the player info
                    # for this position.
                    if extras_position_idx > Lineup.max_extras:
                        break

                    # Print the setup variables function, and the information for the player.
                    result += player.get_lineup_metapost_data(
                        10,
                        extras_position_idx,
                        is_extra=True,
                        original_postion_idx=position_idx,
                    )

                    # Increment the index for extras position.
                    extras_position_idx += 1
                    continue

                # Print out player information.
                result += player.get_lineup_metapost_data(position_idx, spot_idx)

        return result

    def get_batter_stats_metapost_data(self) -> str:
        result = ""
        total_batter_stats = BatterStats()

        # Go through the positions in the lineup
        position_idx = 0
        for position in self.lineup:
            spot_idx = 0
            position_idx += 1
            # Go through the spots in each of the positions.
            for player in position:
                spot_idx += 1

                # Add the stats of this player to the total.
                total_batter_stats.add_stats(player.batter_stats)

                # In case the limit of max replacements in the scorecard has been
                # reached, don't print the info for any remaining batter on this position.
                if spot_idx > Lineup.max_replacements:
                    break

                # Print out the batter stats.
                result += player.batter_stats.get_metapost_data(position_idx, spot_idx)
                result += "\n"

        # Print out the totals for all the team.
        result += total_batter_stats.get_metapost_data(10, 1)

        return result

    def __str__(self):
        result = ""
        for position in self.lineup:
            for idx, player in enumerate(position):
                if idx != 0:
                    result += f"    {player.get_lineup_str()}"
                else:
                    result += f"{player.get_lineup_str()}"

        return result
