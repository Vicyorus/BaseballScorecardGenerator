import pytest
from baseball_scorecard.team.lineup import Lineup
from baseball_scorecard.team.roster import Roster


class TestLineup:
    """Tests the Lineup class."""

    @pytest.fixture(autouse=True)
    def setup_roster_data(self):
        # Set up the roster
        self._roster: Roster = Roster(
            {
                1: "John Doe",
                2: "John Doe",
                3: "John Doe",
                4: "John Doe",
                5: "John Doe",
                6: "John Doe",
                7: "John Doe",
                8: "John Doe",
                9: "John Doe",
                10: "John Doe",
                11: "John Doe",
                12: "John Doe",
                13: "John Doe",
                14: "John Doe",
                15: "John Doe",
                16: "John Doe",
                17: "John Doe",
                18: "John Doe",
                19: "John Doe",
                20: "John Doe",
            },
            [1],
            False,
        )

        # Set leadoff and 9th batter variables for comparing.
        self._leadoff_batter = self._roster.get_player(1)
        self._ninth_batter = self._roster.get_player(9)
        self._tenth_batter = self._roster.get_player(10)

        # Set at bats for the batters.
        for i in range(1, 10):
            self._roster.get_player(i).batter_stats.at_bats = 3

        self._lineup_data = [
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"],
            [5, "5"],
            [6, "6"],
            [7, "7"],
            [8, "8"],
            [9, "9"],
        ]

    def test_add_player(self):
        """Test that the add_player method is correct."""

        lineup = Lineup(self._lineup_data, self._roster)
        lineup.add_player(1, self._roster.get_player(10), "1", 2)

        assert lineup.lineup[0][1] == self._tenth_batter

    def test_get_batter(self):
        """Test that the get_batter method is correct."""
        lineup = Lineup(self._lineup_data, self._roster)

        assert lineup.get_batter() == self._leadoff_batter

    def test_next_batter(self):
        """Test that the next_batter method is correct."""
        lineup = Lineup(self._lineup_data, self._roster)

        assert lineup.current_batter == 1
        for i in range(2, 11):
            lineup.next_batter()
            if i == 10:
                assert lineup.current_batter == 1
            else:
                assert lineup.current_batter == i

    def test_get_previous_batter(self):
        """Test that the get_previous_batter method is correct."""
        lineup = Lineup(self._lineup_data, self._roster)
        assert lineup.get_previous_batter() == (9, self._ninth_batter)

    def test_get_player_in_lineup(self):
        """Test that the get_player_in_lineup method is correct."""
        lineup = Lineup(self._lineup_data, self._roster)
        assert lineup.get_player_in_lineup(1) == (1, self._leadoff_batter)
        assert lineup.get_player_in_lineup(9) == (9, self._ninth_batter)

    def test_get_player_in_lineup_player_not_in_lineup(self):
        """Test that the get_player_in_lineup method is correct, when a player is not in the lineup."""
        lineup = Lineup(self._lineup_data, self._roster)
        assert lineup.get_player_in_lineup(21) == (-1, None)

    def test_no_ab(self):
        """Test that the no_ab method is correct."""
        lineup = Lineup(self._lineup_data, self._roster)
        assert lineup.current_batter == 1
        for i in range(9, -1, -1):
            lineup.no_ab()
            if i == 0:
                assert lineup.current_batter == 9
            else:
                assert lineup.current_batter == i

    def test_get_total_at_bats(self):
        """Test that the get_total_at_bats method is correct."""
        lineup = Lineup(self._lineup_data, self._roster)
        assert lineup.get_total_at_bats() == 27

    def test_get_batter_info_metapost_data(self):
        """Test that the get_batter_info_metapost_data method is correct."""
        lineup = Lineup(self._lineup_data, self._roster)

        expected_metapost = (
            "    % lineup info\n"
            "    %% lineup 1-1\n"
            "    set_batter_name_vars(1, 1);\n"
            "    label.urt(btex {\\bigsf 1} etex, (number_x,player_y)) withcolor clr;\n"
            "    label.urt(btex {\\bigsf John Doe} etex, (name_x,player_y)) withcolor clr;\n"
            "    label.urt(btex {\\bigsf 1} etex, (inn_x,player_y)) withcolor clr;\n"
            "    label.urt(btex {\\bigsf 1} etex, (pos_x,player_y)) withcolor clr;\n"
            "\n"
            "    %% lineup 2-1\n"
            "    set_batter_name_vars(2, 1);\n"
            "    label.urt(btex {\\bigsf 2} etex, (number_x,player_y)) withcolor clr;\n"
            "    label.urt(btex {\\bigsf John Doe} etex, (name_x,player_y)) withcolor clr;\n"
            "    label.urt(btex {\\bigsf 1} etex, (inn_x,player_y)) withcolor clr;\n"
            "    label.urt(btex {\\bigsf 2} etex, (pos_x,player_y)) withcolor clr;\n"
            "\n"
            "    %% lineup 3-1\n"
            "    set_batter_name_vars(3, 1);\n"
            "    label.urt(btex {\\bigsf 3} etex, (number_x,player_y)) withcolor clr;\n"
            "    label.urt(btex {\\bigsf John Doe} etex, (name_x,player_y)) withcolor clr;\n"
            "    label.urt(btex {\\bigsf 1} etex, (inn_x,player_y)) withcolor clr;\n"
            "    label.urt(btex {\\bigsf 3} etex, (pos_x,player_y)) withcolor clr;\n"
            "\n"
            "    %% lineup 4-1\n"
            "    set_batter_name_vars(4, 1);\n"
            "    label.urt(btex {\\bigsf 4} etex, (number_x,player_y)) withcolor clr;\n"
            "    label.urt(btex {\\bigsf John Doe} etex, (name_x,player_y)) withcolor clr;\n"
            "    label.urt(btex {\\bigsf 1} etex, (inn_x,player_y)) withcolor clr;\n"
            "    label.urt(btex {\\bigsf 4} etex, (pos_x,player_y)) withcolor clr;\n"
            "\n"
            "    %% lineup 5-1\n"
            "    set_batter_name_vars(5, 1);\n"
            "    label.urt(btex {\\bigsf 5} etex, (number_x,player_y)) withcolor clr;\n"
            "    label.urt(btex {\\bigsf John Doe} etex, (name_x,player_y)) withcolor clr;\n"
            "    label.urt(btex {\\bigsf 1} etex, (inn_x,player_y)) withcolor clr;\n"
            "    label.urt(btex {\\bigsf 5} etex, (pos_x,player_y)) withcolor clr;\n"
            "\n"
            "    %% lineup 6-1\n"
            "    set_batter_name_vars(6, 1);\n"
            "    label.urt(btex {\\bigsf 6} etex, (number_x,player_y)) withcolor clr;\n"
            "    label.urt(btex {\\bigsf John Doe} etex, (name_x,player_y)) withcolor clr;\n"
            "    label.urt(btex {\\bigsf 1} etex, (inn_x,player_y)) withcolor clr;\n"
            "    label.urt(btex {\\bigsf 6} etex, (pos_x,player_y)) withcolor clr;\n"
            "\n"
            "    %% lineup 7-1\n"
            "    set_batter_name_vars(7, 1);\n"
            "    label.urt(btex {\\bigsf 7} etex, (number_x,player_y)) withcolor clr;\n"
            "    label.urt(btex {\\bigsf John Doe} etex, (name_x,player_y)) withcolor clr;\n"
            "    label.urt(btex {\\bigsf 1} etex, (inn_x,player_y)) withcolor clr;\n"
            "    label.urt(btex {\\bigsf 7} etex, (pos_x,player_y)) withcolor clr;\n"
            "\n"
            "    %% lineup 8-1\n"
            "    set_batter_name_vars(8, 1);\n"
            "    label.urt(btex {\\bigsf 8} etex, (number_x,player_y)) withcolor clr;\n"
            "    label.urt(btex {\\bigsf John Doe} etex, (name_x,player_y)) withcolor clr;\n"
            "    label.urt(btex {\\bigsf 1} etex, (inn_x,player_y)) withcolor clr;\n"
            "    label.urt(btex {\\bigsf 8} etex, (pos_x,player_y)) withcolor clr;\n"
            "\n"
            "    %% lineup 9-1\n"
            "    set_batter_name_vars(9, 1);\n"
            "    label.urt(btex {\\bigsf 9} etex, (number_x,player_y)) withcolor clr;\n"
            "    label.urt(btex {\\bigsf John Doe} etex, (name_x,player_y)) withcolor clr;\n"
            "    label.urt(btex {\\bigsf 1} etex, (inn_x,player_y)) withcolor clr;\n"
            "    label.urt(btex {\\bigsf 9} etex, (pos_x,player_y)) withcolor clr;\n"
            "\n"
        )
        assert lineup.get_batter_info_metapost_data() == expected_metapost

    def test_get_batter_info_metapost_data_extra_batters(self):
        """Test that the get_batter_info_metapost_data method is correct, with extra batters."""
        lineup = Lineup(self._lineup_data, self._roster)
        lineup.add_player(1, self._roster.get_player(10), "1", 2)
        lineup.add_player(1, self._roster.get_player(11), "1", 3)
        lineup.add_player(1, self._roster.get_player(12), "1", 4)
        lineup.add_player(1, self._roster.get_player(13), "1", 5)
        lineup.add_player(1, self._roster.get_player(14), "1", 6)
        lineup.add_player(1, self._roster.get_player(15), "1", 7)
        lineup.add_player(1, self._roster.get_player(16), "1", 8)
        lineup.add_player(1, self._roster.get_player(17), "1", 9)
        lineup.add_player(1, self._roster.get_player(18), "1", 10)
        lineup.add_player(1, self._roster.get_player(19), "1", 11)
        lineup.add_player(1, self._roster.get_player(20), "1", 12)

        expected_metapost = (
            "    % lineup info\n"
            "    %% lineup 1-1\n"
            "    set_batter_name_vars(1, 1);\n"
            "    label.urt(btex {\\bigsf 1} etex, (number_x,player_y)) withcolor clr;\n"
            "    label.urt(btex {\\bigsf John Doe} etex, (name_x,player_y)) withcolor clr;\n"
            "    label.urt(btex {\\bigsf 1} etex, (inn_x,player_y)) withcolor clr;\n"
            "    label.urt(btex {\\bigsf 1} etex, (pos_x,player_y)) withcolor clr;\n"
            "\n"
            "    %% lineup 1-2\n"
            "    set_batter_name_vars(1, 2);\n"
            "    label.urt(btex {\\bigsf 10} etex, (number_x,player_y)) withcolor clr;\n"
            "    label.urt(btex {\\bigsf John Doe} etex, (name_x,player_y)) withcolor clr;\n"
            "    label.urt(btex {\\bigsf 2} etex, (inn_x,player_y)) withcolor clr;\n"
            "    label.urt(btex {\\bigsf 1} etex, (pos_x,player_y)) withcolor clr;\n"
            "\n"
            "    %% lineup 1-3\n"
            "    set_batter_name_vars(1, 3);\n"
            "    label.urt(btex {\\bigsf 11} etex, (number_x,player_y)) withcolor clr;\n"
            "    label.urt(btex {\\bigsf John Doe} etex, (name_x,player_y)) withcolor clr;\n"
            "    label.urt(btex {\\bigsf 3} etex, (inn_x,player_y)) withcolor clr;\n"
            "    label.urt(btex {\\bigsf 1} etex, (pos_x,player_y)) withcolor clr;\n"
            "\n"
            "    %% lineup 1-4\n"
            "    set_batter_name_vars(1, 4);\n"
            "    label.urt(btex {\\bigsf 12} etex, (number_x,player_y)) withcolor clr;\n"
            "    label.urt(btex {\\bigsf John Doe} etex, (name_x,player_y)) withcolor clr;\n"
            "    label.urt(btex {\\bigsf 4} etex, (inn_x,player_y)) withcolor clr;\n"
            "    label.urt(btex {\\bigsf 1} etex, (pos_x,player_y)) withcolor clr;\n"
            "\n"
            "    %% lineup 10-1\n"
            "    set_batter_name_vars(10, 1);\n"
            "    label(btex {\\sf 1} etex, (-324,player_y+32-6)) withcolor clr;\n"
            "    label.urt(btex {\\bigsf 13} etex, (number_x,player_y)) withcolor clr;\n"
            "    label.urt(btex {\\bigsf John Doe (5)} etex, (name_x,player_y)) withcolor clr;\n"
            "    label.urt(btex {\\bigsf 1} etex, (pos_x,player_y)) withcolor clr;\n"
            "\n"
            "    %% lineup 10-2\n"
            "    set_batter_name_vars(10, 2);\n"
            "    label(btex {\\sf 1} etex, (-324,player_y+32-6)) withcolor clr;\n"
            "    label.urt(btex {\\bigsf 14} etex, (number_x,player_y)) withcolor clr;\n"
            "    label.urt(btex {\\bigsf John Doe (6)} etex, (name_x,player_y)) withcolor clr;\n"
            "    label.urt(btex {\\bigsf 1} etex, (pos_x,player_y)) withcolor clr;\n"
            "\n"
            "    %% lineup 10-3\n"
            "    set_batter_name_vars(10, 3);\n"
            "    label(btex {\\sf 1} etex, (-324,player_y+32-6)) withcolor clr;\n"
            "    label.urt(btex {\\bigsf 15} etex, (number_x,player_y)) withcolor clr;\n"
            "    label.urt(btex {\\bigsf John Doe (7)} etex, (name_x,player_y)) withcolor clr;\n"
            "    label.urt(btex {\\bigsf 1} etex, (pos_x,player_y)) withcolor clr;\n"
            "\n"
            "    %% lineup 10-4\n"
            "    set_batter_name_vars(10, 4);\n"
            "    label(btex {\\sf 1} etex, (-324,player_y+32-6)) withcolor clr;\n"
            "    label.urt(btex {\\bigsf 16} etex, (number_x,player_y)) withcolor clr;\n"
            "    label.urt(btex {\\bigsf John Doe (8)} etex, (name_x,player_y)) withcolor clr;\n"
            "    label.urt(btex {\\bigsf 1} etex, (pos_x,player_y)) withcolor clr;\n"
            "\n"
            "    %% lineup 10-5\n"
            "    set_batter_name_vars(10, 5);\n"
            "    label(btex {\\sf 1} etex, (-324,player_y+32-6)) withcolor clr;\n"
            "    label.urt(btex {\\bigsf 17} etex, (number_x,player_y)) withcolor clr;\n"
            "    label.urt(btex {\\bigsf John Doe (9)} etex, (name_x,player_y)) withcolor clr;\n"
            "    label.urt(btex {\\bigsf 1} etex, (pos_x,player_y)) withcolor clr;\n"
            "\n"
            "    %% lineup 10-6\n"
            "    set_batter_name_vars(10, 6);\n"
            "    label(btex {\\sf 1} etex, (-324,player_y+32-6)) withcolor clr;\n"
            "    label.urt(btex {\\bigsf 18} etex, (number_x,player_y)) withcolor clr;\n"
            "    label.urt(btex {\\bigsf John Doe (10)} etex, (name_x,player_y)) withcolor clr;\n"
            "    label.urt(btex {\\bigsf 1} etex, (pos_x,player_y)) withcolor clr;\n"
            "\n"
            "    %% lineup 10-7\n"
            "    set_batter_name_vars(10, 7);\n"
            "    label(btex {\\sf 1} etex, (-324,player_y+32-6)) withcolor clr;\n"
            "    label.urt(btex {\\bigsf 19} etex, (number_x,player_y)) withcolor clr;\n"
            "    label.urt(btex {\\bigsf John Doe (11)} etex, (name_x,player_y)) withcolor clr;\n"
            "    label.urt(btex {\\bigsf 1} etex, (pos_x,player_y)) withcolor clr;\n"
            "\n"
            "    %% lineup 2-1\n"
            "    set_batter_name_vars(2, 1);\n"
            "    label.urt(btex {\\bigsf 2} etex, (number_x,player_y)) withcolor clr;\n"
            "    label.urt(btex {\\bigsf John Doe} etex, (name_x,player_y)) withcolor clr;\n"
            "    label.urt(btex {\\bigsf 1} etex, (inn_x,player_y)) withcolor clr;\n"
            "    label.urt(btex {\\bigsf 2} etex, (pos_x,player_y)) withcolor clr;\n"
            "\n"
            "    %% lineup 3-1\n"
            "    set_batter_name_vars(3, 1);\n"
            "    label.urt(btex {\\bigsf 3} etex, (number_x,player_y)) withcolor clr;\n"
            "    label.urt(btex {\\bigsf John Doe} etex, (name_x,player_y)) withcolor clr;\n"
            "    label.urt(btex {\\bigsf 1} etex, (inn_x,player_y)) withcolor clr;\n"
            "    label.urt(btex {\\bigsf 3} etex, (pos_x,player_y)) withcolor clr;\n"
            "\n"
            "    %% lineup 4-1\n"
            "    set_batter_name_vars(4, 1);\n"
            "    label.urt(btex {\\bigsf 4} etex, (number_x,player_y)) withcolor clr;\n"
            "    label.urt(btex {\\bigsf John Doe} etex, (name_x,player_y)) withcolor clr;\n"
            "    label.urt(btex {\\bigsf 1} etex, (inn_x,player_y)) withcolor clr;\n"
            "    label.urt(btex {\\bigsf 4} etex, (pos_x,player_y)) withcolor clr;\n"
            "\n"
            "    %% lineup 5-1\n"
            "    set_batter_name_vars(5, 1);\n"
            "    label.urt(btex {\\bigsf 5} etex, (number_x,player_y)) withcolor clr;\n"
            "    label.urt(btex {\\bigsf John Doe} etex, (name_x,player_y)) withcolor clr;\n"
            "    label.urt(btex {\\bigsf 1} etex, (inn_x,player_y)) withcolor clr;\n"
            "    label.urt(btex {\\bigsf 5} etex, (pos_x,player_y)) withcolor clr;\n"
            "\n"
            "    %% lineup 6-1\n"
            "    set_batter_name_vars(6, 1);\n"
            "    label.urt(btex {\\bigsf 6} etex, (number_x,player_y)) withcolor clr;\n"
            "    label.urt(btex {\\bigsf John Doe} etex, (name_x,player_y)) withcolor clr;\n"
            "    label.urt(btex {\\bigsf 1} etex, (inn_x,player_y)) withcolor clr;\n"
            "    label.urt(btex {\\bigsf 6} etex, (pos_x,player_y)) withcolor clr;\n"
            "\n"
            "    %% lineup 7-1\n"
            "    set_batter_name_vars(7, 1);\n"
            "    label.urt(btex {\\bigsf 7} etex, (number_x,player_y)) withcolor clr;\n"
            "    label.urt(btex {\\bigsf John Doe} etex, (name_x,player_y)) withcolor clr;\n"
            "    label.urt(btex {\\bigsf 1} etex, (inn_x,player_y)) withcolor clr;\n"
            "    label.urt(btex {\\bigsf 7} etex, (pos_x,player_y)) withcolor clr;\n"
            "\n"
            "    %% lineup 8-1\n"
            "    set_batter_name_vars(8, 1);\n"
            "    label.urt(btex {\\bigsf 8} etex, (number_x,player_y)) withcolor clr;\n"
            "    label.urt(btex {\\bigsf John Doe} etex, (name_x,player_y)) withcolor clr;\n"
            "    label.urt(btex {\\bigsf 1} etex, (inn_x,player_y)) withcolor clr;\n"
            "    label.urt(btex {\\bigsf 8} etex, (pos_x,player_y)) withcolor clr;\n"
            "\n"
            "    %% lineup 9-1\n"
            "    set_batter_name_vars(9, 1);\n"
            "    label.urt(btex {\\bigsf 9} etex, (number_x,player_y)) withcolor clr;\n"
            "    label.urt(btex {\\bigsf John Doe} etex, (name_x,player_y)) withcolor clr;\n"
            "    label.urt(btex {\\bigsf 1} etex, (inn_x,player_y)) withcolor clr;\n"
            "    label.urt(btex {\\bigsf 9} etex, (pos_x,player_y)) withcolor clr;\n"
            "\n"
        )
        assert lineup.get_batter_info_metapost_data() == expected_metapost

    def test_get_batter_stats_metapost_data(self):
        """Test that the get_batter_stats_metapost_data method is correct."""
        lineup = Lineup(self._lineup_data, self._roster)

        expected_metapost = (
            "    %% batter 1-1\n"
            "    set_batter_total_vars(1, 1, innings);\n"
            "    label(btex {\\bigsf 3} etex, batter_ab) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_r) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_h) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_rbi) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_bb) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_so) withcolor clr;\n"
            "\n"
            "    %% batter 2-1\n"
            "    set_batter_total_vars(2, 1, innings);\n"
            "    label(btex {\\bigsf 3} etex, batter_ab) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_r) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_h) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_rbi) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_bb) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_so) withcolor clr;\n"
            "\n"
            "    %% batter 3-1\n"
            "    set_batter_total_vars(3, 1, innings);\n"
            "    label(btex {\\bigsf 3} etex, batter_ab) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_r) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_h) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_rbi) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_bb) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_so) withcolor clr;\n"
            "\n"
            "    %% batter 4-1\n"
            "    set_batter_total_vars(4, 1, innings);\n"
            "    label(btex {\\bigsf 3} etex, batter_ab) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_r) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_h) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_rbi) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_bb) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_so) withcolor clr;\n"
            "\n"
            "    %% batter 5-1\n"
            "    set_batter_total_vars(5, 1, innings);\n"
            "    label(btex {\\bigsf 3} etex, batter_ab) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_r) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_h) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_rbi) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_bb) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_so) withcolor clr;\n"
            "\n"
            "    %% batter 6-1\n"
            "    set_batter_total_vars(6, 1, innings);\n"
            "    label(btex {\\bigsf 3} etex, batter_ab) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_r) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_h) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_rbi) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_bb) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_so) withcolor clr;\n"
            "\n"
            "    %% batter 7-1\n"
            "    set_batter_total_vars(7, 1, innings);\n"
            "    label(btex {\\bigsf 3} etex, batter_ab) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_r) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_h) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_rbi) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_bb) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_so) withcolor clr;\n"
            "\n"
            "    %% batter 8-1\n"
            "    set_batter_total_vars(8, 1, innings);\n"
            "    label(btex {\\bigsf 3} etex, batter_ab) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_r) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_h) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_rbi) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_bb) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_so) withcolor clr;\n"
            "\n"
            "    %% batter 9-1\n"
            "    set_batter_total_vars(9, 1, innings);\n"
            "    label(btex {\\bigsf 3} etex, batter_ab) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_r) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_h) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_rbi) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_bb) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_so) withcolor clr;\n"
            "\n"
            "    %% batter 10-1\n"
            "    set_batter_total_vars(10, 1, innings);\n"
            "    label(btex {\\bigsf 27} etex, batter_ab) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_r) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_h) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_rbi) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_bb) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_so) withcolor clr;\n"
        )
        assert lineup.get_batter_stats_metapost_data() == expected_metapost

    def test_get_batter_stats_metapost_data_extra_batters(self):
        """Test that the get_batter_stats_metapost_data method is correct, with extra batters."""
        lineup = Lineup(self._lineup_data, self._roster)
        lineup.add_player(1, self._roster.get_player(10), "1", 2)
        lineup.add_player(1, self._roster.get_player(11), "1", 3)
        lineup.add_player(1, self._roster.get_player(12), "1", 4)
        lineup.add_player(1, self._roster.get_player(13), "1", 5)
        lineup.add_player(1, self._roster.get_player(14), "1", 6)
        lineup.add_player(1, self._roster.get_player(15), "1", 7)
        lineup.add_player(1, self._roster.get_player(16), "1", 8)
        lineup.add_player(1, self._roster.get_player(17), "1", 9)
        lineup.add_player(1, self._roster.get_player(18), "1", 10)
        lineup.add_player(1, self._roster.get_player(19), "1", 11)

        expected_metapost = (
            "    %% batter 1-1\n"
            "    set_batter_total_vars(1, 1, innings);\n"
            "    label(btex {\\bigsf 3} etex, batter_ab) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_r) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_h) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_rbi) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_bb) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_so) withcolor clr;\n"
            "\n"
            "    %% batter 1-2\n"
            "    set_batter_total_vars(1, 2, innings);\n"
            "    label(btex {\\bigsf 0} etex, batter_ab) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_r) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_h) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_rbi) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_bb) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_so) withcolor clr;\n"
            "\n"
            "    %% batter 1-3\n"
            "    set_batter_total_vars(1, 3, innings);\n"
            "    label(btex {\\bigsf 0} etex, batter_ab) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_r) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_h) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_rbi) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_bb) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_so) withcolor clr;\n"
            "\n"
            "    %% batter 1-4\n"
            "    set_batter_total_vars(1, 4, innings);\n"
            "    label(btex {\\bigsf 0} etex, batter_ab) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_r) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_h) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_rbi) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_bb) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_so) withcolor clr;\n"
            "\n"
            "    %% batter 2-1\n"
            "    set_batter_total_vars(2, 1, innings);\n"
            "    label(btex {\\bigsf 3} etex, batter_ab) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_r) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_h) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_rbi) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_bb) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_so) withcolor clr;\n"
            "\n"
            "    %% batter 3-1\n"
            "    set_batter_total_vars(3, 1, innings);\n"
            "    label(btex {\\bigsf 3} etex, batter_ab) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_r) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_h) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_rbi) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_bb) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_so) withcolor clr;\n"
            "\n"
            "    %% batter 4-1\n"
            "    set_batter_total_vars(4, 1, innings);\n"
            "    label(btex {\\bigsf 3} etex, batter_ab) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_r) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_h) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_rbi) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_bb) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_so) withcolor clr;\n"
            "\n"
            "    %% batter 5-1\n"
            "    set_batter_total_vars(5, 1, innings);\n"
            "    label(btex {\\bigsf 3} etex, batter_ab) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_r) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_h) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_rbi) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_bb) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_so) withcolor clr;\n"
            "\n"
            "    %% batter 6-1\n"
            "    set_batter_total_vars(6, 1, innings);\n"
            "    label(btex {\\bigsf 3} etex, batter_ab) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_r) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_h) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_rbi) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_bb) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_so) withcolor clr;\n"
            "\n"
            "    %% batter 7-1\n"
            "    set_batter_total_vars(7, 1, innings);\n"
            "    label(btex {\\bigsf 3} etex, batter_ab) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_r) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_h) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_rbi) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_bb) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_so) withcolor clr;\n"
            "\n"
            "    %% batter 8-1\n"
            "    set_batter_total_vars(8, 1, innings);\n"
            "    label(btex {\\bigsf 3} etex, batter_ab) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_r) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_h) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_rbi) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_bb) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_so) withcolor clr;\n"
            "\n"
            "    %% batter 9-1\n"
            "    set_batter_total_vars(9, 1, innings);\n"
            "    label(btex {\\bigsf 3} etex, batter_ab) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_r) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_h) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_rbi) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_bb) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_so) withcolor clr;\n"
            "\n"
            "    %% batter 10-1\n"
            "    set_batter_total_vars(10, 1, innings);\n"
            "    label(btex {\\bigsf 27} etex, batter_ab) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_r) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_h) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_rbi) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_bb) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_so) withcolor clr;\n"
        )
        assert lineup.get_batter_stats_metapost_data() == expected_metapost

    def test_string_output(self):
        """Test that the string method is printing the expected format."""
        lineup = Lineup(self._lineup_data, self._roster)
        lineup.add_player(1, self._roster.get_player(10), "1", 2)
        lineup.add_player(1, self._roster.get_player(11), "1", 3)
        lineup.add_player(1, self._roster.get_player(12), "1", 4)
        lineup.add_player(1, self._roster.get_player(13), "1", 5)
        lineup.add_player(1, self._roster.get_player(14), "1", 6)
        lineup.add_player(1, self._roster.get_player(15), "1", 7)
        lineup.add_player(1, self._roster.get_player(16), "1", 8)
        lineup.add_player(1, self._roster.get_player(17), "1", 9)
        lineup.add_player(1, self._roster.get_player(18), "1", 10)
        lineup.add_player(1, self._roster.get_player(19), "1", 11)

        expected_str = (
            "P #1 John Doe (1) 3 AB\n"
            "    P #10 John Doe (2) \n"
            "    P #11 John Doe (3) \n"
            "    P #12 John Doe (4) \n"
            "    P #13 John Doe (5) \n"
            "    P #14 John Doe (6) \n"
            "    P #15 John Doe (7) \n"
            "    P #16 John Doe (8) \n"
            "    P #17 John Doe (9) \n"
            "    P #18 John Doe (10) \n"
            "    P #19 John Doe (11) \n"
            "C #2 John Doe (1) 3 AB\n"
            "1B #3 John Doe (1) 3 AB\n"
            "2B #4 John Doe (1) 3 AB\n"
            "3B #5 John Doe (1) 3 AB\n"
            "SS #6 John Doe (1) 3 AB\n"
            "LF #7 John Doe (1) 3 AB\n"
            "CF #8 John Doe (1) 3 AB\n"
            "RF #9 John Doe (1) 3 AB\n"
        )
        assert str(lineup) == expected_str
