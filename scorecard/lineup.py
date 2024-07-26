class Lineup:
    def __init__(self, data, roster):
        self.lineup = []
        self.current_batter = 1
        self.roster = roster # TODO: May want to remove this when the debugging stage is done

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
        self.current_batter %= 9

    def __str__(self):
        result = ""
        for order in self.lineup:
            for player_idx in range(len(order)):
                if player_idx != 0:
                    result += f'    {self.roster.get_player(order[player_idx]).get_lineup_str()}\n'
                else:
                    result += f'{self.roster.get_player(order[player_idx]).get_lineup_str()}\n'

        return result
