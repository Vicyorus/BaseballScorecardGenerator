from baseball_scorecard.stats.batter_stats import BatterStats

class Lineup:

    max_replacements = 4
    max_extras = 7

    def __init__(self, data, roster):
        self.lineup = []
        self.current_batter = 1
        self.roster = roster

        for lineup_player in data:
            player = roster.get_player(lineup_player[0])
            player.set_lineup_position(lineup_player[1], 1)

            self.lineup.append([lineup_player[0]])

    def add_player(self, order, player_id):
        self.lineup[order - 1].append(player_id)

    def get_batter(self):
        player_id = self.lineup[self.current_batter - 1][-1]
        return self.roster.get_player(player_id)

    def next_batter(self):
        self.current_batter += 1
        self.current_batter %= 10
        if self.current_batter == 0:
            self.current_batter = 1

    def no_ab(self):
        if self.current_batter == 1:
            self.current_batter = 9
        else:
            self.current_batter -= 1

    def get_total_at_bats(self):
        total_abs = 0
        for position in self.lineup:
            for spot in position:
                # Get the player information.
                player = self.roster.get_player(spot)
                total_abs += player.batter_stats.at_bats
        return total_abs

    def get_batter_info_metapost_data(self):
        result = "    % lineup info\n"

        # Go through the positions in the lineup
        extras_position_idx = 1
        position_idx = 0
        for position in self.lineup:
            spot_idx = 0
            position_idx += 1
            # Go through the spots in each of the positions.
            for spot in position:
                spot_idx += 1

                # Get the player information.
                player = self.roster.get_player(spot)

                # In case the limit of max replacements in the scorecard has been reached,
                # print out the player in the extra slots.
                if spot_idx > Lineup.max_replacements:

                    # If all the extras are filled up, don't continue printing the player info
                    # for this position.
                    if extras_position_idx > Lineup.max_extras:
                        break

                    # Print the setup variables function, and the information for the player.
                    result += player.get_lineup_metapost_data(10, extras_position_idx, is_extra=True, original_postion_idx=position_idx)

                    # Increment the index for extras position.
                    extras_position_idx += 1
                    continue

                # Print out player information.
                result += player.get_lineup_metapost_data(position_idx, spot_idx)

        return result

    def get_batter_stats_metapost_data(self):
        result = ""
        total_batter_stats = BatterStats()

        # Go through the positions in the lineup
        position_idx = 0
        for position in self.lineup:
            spot_idx = 0
            position_idx += 1
            # Go through the spots in each of the positions.
            for spot in position:
                spot_idx += 1

                # Get the player information.
                player = self.roster.get_player(spot)

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
        for order in self.lineup:
            for player_idx in range(len(order)):
                if player_idx != 0:
                    result += f'    {self.roster.get_player(order[player_idx]).get_lineup_str()}\n'
                else:
                    result += f'{self.roster.get_player(order[player_idx]).get_lineup_str()}\n'

        return result
