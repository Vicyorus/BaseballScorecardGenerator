import pytest
from baseball_scorecard.team.team import Team
from baseball_scorecard.stats.pitcher_stats import PitcherStats


class TestTeam:
    """Tests the Team class."""

    @pytest.fixture(autouse=True)
    def setup_roster_data(self):
        # Set up the roster
        self._team_data = {
            "team": "Foo Bars",
            "roster": {
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
            "starter": 1,
            "lefties": [1, 10, 11],
            "lineup": [
                [1, "1"],
                [2, "2"],
                [3, "3"],
                [4, "4"],
                [5, "5"],
                [6, "6"],
                [7, "7"],
                [8, "8"],
                [9, "9"],
            ],
            "bench": [
                [10, "C"],
                [11, "1B"],
                [12, "RF"],
            ],
            "bullpen": [13, 14, 15, 16, 17, 18, 19, 20],
        }

    def test_add_pitcher(self):
        """Test that the add_pitcher method is correct."""
        new_pitcher_id = 13
        team = Team(self._team_data)
        team.add_pitcher(new_pitcher_id, 2)
        assert team.pitcher_lineup.get_current_pitcher().id == new_pitcher_id

    def test_add_player(self):
        """Test that the add_player method is correct."""

        team = Team(self._team_data)
        team.add_player(2, 10, "PH", 2)

        assert team.lineup.lineup[1][1].id == 10

    def test_add_player_defensive_substitution(self):
        """Test that the add_player method is correct."""

        team = Team(self._team_data)
        team.add_player(2, 10, "C", 2, is_defensive_sub=True)

        assert team.lineup.lineup[1][1].id == 10
        assert team.defensive_subs[2][0].fielder_info == "#10 John Doe"

        team.add_player(2, 11, "C", 2, is_defensive_sub=True)

        assert team.lineup.lineup[1][2].id == 11
        assert team.defensive_subs[2][1].fielder_info == "#11 John Doe"

    def test_defensive_switch(self):
        """Test that the defensive_switch method is correct."""
        team = Team(self._team_data)
        team.defensive_switch(1, "2")
        assert team.roster.get_player(1).defensive_position == ["1", "2"]

    def test_next_batter(self):
        """Test that the next_batter method is correct."""
        team = Team(self._team_data)

        assert team.lineup.current_batter == 1
        for i in range(2, 11):
            team.next_batter()
            if i == 10:
                assert team.lineup.current_batter == 1
            else:
                assert team.lineup.current_batter == i

    def test_no_ab(self):
        """Test that the no_ab method is correct."""
        team = Team(self._team_data)
        assert team.lineup.current_batter == 1
        for i in range(9, -1, -1):
            team.no_ab()
            if i == 0:
                assert team.lineup.current_batter == 9
            else:
                assert team.lineup.current_batter == i

    def test_winning_pitcher(self):
        """Test that the winning_pitcher method is correct."""
        team = Team(self._team_data)
        team.winning_pitcher(1)

        assert team.roster.get_player(1).pitcher_stats.decision == ["W"]

    def test_losing_pitcher(self):
        """Test that the losing_pitcher method is correct."""
        team = Team(self._team_data)
        team.losing_pitcher(1)

        assert team.roster.get_player(1).pitcher_stats.decision == ["L"]

    def test_save_pitcher(self):
        """Test that the save_pitcher method is correct."""
        team = Team(self._team_data)
        team.save_pitcher(1)

        assert team.roster.get_player(1).pitcher_stats.decision == ["S"]

    def test_get_player_in_lineup(self):
        """Test that the get_player_in_lineup method is correct."""

        team = Team(self._team_data)
        assert team.get_player_in_lineup(1) == (1, team.roster.get_player(1))

    def test_get_player_in_lineup_no_player_in_roster(self):
        """Test that the get_player_in_lineup method raises an exception when no player is found."""

        team = Team(self._team_data)
        with pytest.raises(Exception) as e_info:
            team.get_player_in_lineup(21)

    def test_get_batter(self):
        """Test that the get_batter method is correct."""
        team = Team(self._team_data)
        assert team.get_batter() == team.roster.get_player(1)

    def test_get_previous_batter(self):
        """Test that the get_previous_batter method is correct."""
        team = Team(self._team_data)
        assert team.get_previous_batter() == (9, team.roster.get_player(9))

    def test_get_current_pitcher(self):
        """Test that the get_current_pitcher method is correct."""
        team = Team(self._team_data)
        assert team.get_current_pitcher() == team.roster.get_player(1)

    def test_get_stats(self):
        """Test that the get_stats method is correct."""
        team = Team(self._team_data)
        assert team.get_stats() == team.stats

    def test_get_pitching_totals(self):
        """Test that the get_pitching_totals method is correct."""
        team = Team(self._team_data)
        pitching_stats = team.get_pitching_totals()
        assert pitching_stats.decision == []
        assert pitching_stats.outs == 0
        assert pitching_stats.batters_faced == 0
        assert pitching_stats.hits == 0
        assert pitching_stats.runs == 0
        assert pitching_stats.earned_runs == 0
        assert pitching_stats.walks == 0
        assert pitching_stats.intent_walks == 0
        assert pitching_stats.strikeouts == 0
        assert pitching_stats.hits_by_pitch == 0
        assert pitching_stats.balks == 0
        assert pitching_stats.wild_pitches == 0
        assert pitching_stats.home_runs == 0
        assert pitching_stats.pitches == 0
        assert pitching_stats.strikes == 0

    def test_get_total_at_bats(self):
        """Test that the get_total_at_bats method is correct."""
        team = Team(self._team_data)
        for i in range(1, 21):
            team.roster.get_player(i).batter_stats.at_bats = 3

        assert team.get_total_at_bats() == 27

    def test_get_team_metapost_data(self):
        """Test that the get_team_metapost_data method is correct."""
        team = Team(self._team_data)
        expected_metapost = (
            "    % team info\n"
            "    label.top(btex {\\bigsf Foo Bars} etex rotated 90, game_team) withcolor clr;\n"
            "\n"
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
            "\n"
            "    % bench info\n"
            "    %% bench #1\n"
            "    set_bench_name_vars(1);\n"
            "    label(btex {\\bigsf 10} etex, bench_no) withcolor clr;\n"
            "    label(btex {\\bigsf John Doe} etex, bench_name) withcolor clr;\n"
            "    label(btex {\\bigsf C} etex, bench_extra) withcolor clr;\n"
            "\n"
            "    %% bench #2\n"
            "    set_bench_name_vars(2);\n"
            "    label(btex {\\bigsf 11} etex, bench_no) withcolor clr;\n"
            "    label(btex {\\bigsf John Doe} etex, bench_name) withcolor clr;\n"
            "    label(btex {\\bigsf 1B} etex, bench_extra) withcolor clr;\n"
            "\n"
            "    %% bench #3\n"
            "    set_bench_name_vars(3);\n"
            "    label(btex {\\bigsf 12} etex, bench_no) withcolor clr;\n"
            "    label(btex {\\bigsf John Doe} etex, bench_name) withcolor clr;\n"
            "    label(btex {\\bigsf RF} etex, bench_extra) withcolor clr;\n"
            "\n"
        )
        assert team.get_team_metapost_data() == expected_metapost

    def test_get_pitcher_metapost_data(self):
        """Test that the get_pitcher_metapost_data method is correct."""
        team = Team(self._team_data)
        team.add_pitcher(13, 2)
        expected_metapost = (
            "    % pitcher info\n"
            "    %% pitcher #1\n"
            "    set_pitcher_name_vars(1);\n"
            "    label.urt(btex {\\bigsf 1} etex, pitcher_no) withcolor clr;\n"
            "    label.urt(btex {\\bigsf John Doe} etex, pitcher_name) withcolor clr;\n"
            "    label.urt(btex {\\bigsf L} etex, pitcher_handedness) withcolor clr;\n"
            "    label.urt(btex {\\bigsf 1} etex, pitcher_inn) withcolor clr;\n"
            "\n"
            "    %% pitcher #2\n"
            "    set_pitcher_name_vars(2);\n"
            "    label.urt(btex {\\bigsf 13} etex, pitcher_no) withcolor clr;\n"
            "    label.urt(btex {\\bigsf John Doe} etex, pitcher_name) withcolor clr;\n"
            "    label.urt(btex {\\bigsf R} etex, pitcher_handedness) withcolor clr;\n"
            "    label.urt(btex {\\bigsf 2} etex, pitcher_inn) withcolor clr;\n"
            "\n\n"
            "    % bullpen info\n"
            "    %% bullpen #1\n"
            "    set_bullpen_name_vars(1);\n"
            "    label(btex {\\bigsf 13} etex, bullpen_no) withcolor clr;\n"
            "    label(btex {\\bigsf John Doe} etex, bullpen_name) withcolor clr;\n"
            "    label(btex {\\bigsf R} etex, bullpen_extra) withcolor clr;\n"
            "    strikethrough_bullpen_name(1, clr);\n"
            "\n"
            "    %% bullpen #2\n"
            "    set_bullpen_name_vars(2);\n"
            "    label(btex {\\bigsf 14} etex, bullpen_no) withcolor clr;\n"
            "    label(btex {\\bigsf John Doe} etex, bullpen_name) withcolor clr;\n"
            "    label(btex {\\bigsf R} etex, bullpen_extra) withcolor clr;\n"
            "\n"
            "    %% bullpen #3\n"
            "    set_bullpen_name_vars(3);\n"
            "    label(btex {\\bigsf 15} etex, bullpen_no) withcolor clr;\n"
            "    label(btex {\\bigsf John Doe} etex, bullpen_name) withcolor clr;\n"
            "    label(btex {\\bigsf R} etex, bullpen_extra) withcolor clr;\n"
            "\n"
            "    %% bullpen #4\n"
            "    set_bullpen_name_vars(4);\n"
            "    label(btex {\\bigsf 16} etex, bullpen_no) withcolor clr;\n"
            "    label(btex {\\bigsf John Doe} etex, bullpen_name) withcolor clr;\n"
            "    label(btex {\\bigsf R} etex, bullpen_extra) withcolor clr;\n"
            "\n"
            "    %% bullpen #5\n"
            "    set_bullpen_name_vars(5);\n"
            "    label(btex {\\bigsf 17} etex, bullpen_no) withcolor clr;\n"
            "    label(btex {\\bigsf John Doe} etex, bullpen_name) withcolor clr;\n"
            "    label(btex {\\bigsf R} etex, bullpen_extra) withcolor clr;\n"
            "\n"
            "    %% bullpen #6\n"
            "    set_bullpen_name_vars(6);\n"
            "    label(btex {\\bigsf 18} etex, bullpen_no) withcolor clr;\n"
            "    label(btex {\\bigsf John Doe} etex, bullpen_name) withcolor clr;\n"
            "    label(btex {\\bigsf R} etex, bullpen_extra) withcolor clr;\n"
            "\n"
            "    %% bullpen #7\n"
            "    set_bullpen_name_vars(7);\n"
            "    label(btex {\\bigsf 19} etex, bullpen_no) withcolor clr;\n"
            "    label(btex {\\bigsf John Doe} etex, bullpen_name) withcolor clr;\n"
            "    label(btex {\\bigsf R} etex, bullpen_extra) withcolor clr;\n"
            "\n"
            "    %% bullpen #8\n"
            "    set_bullpen_name_vars(8);\n"
            "    label(btex {\\bigsf 20} etex, bullpen_no) withcolor clr;\n"
            "    label(btex {\\bigsf John Doe} etex, bullpen_name) withcolor clr;\n"
            "    label(btex {\\bigsf R} etex, bullpen_extra) withcolor clr;\n"
            "\n"
        )
        assert team.get_pitcher_metapost_data() == expected_metapost

    def test_get_batter_stats_metapost_data(self):
        """Test that the get_batter_stats_metapost_data method is correct."""
        team = Team(self._team_data)
        expected_metapost = (
            "    % batter stats\n"
            "    %% batter 1-1\n"
            "    set_batter_total_vars(1, 1, innings);\n"
            "    label(btex {\\bigsf 0} etex, batter_ab) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_r) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_h) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_rbi) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_bb) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_so) withcolor clr;\n"
            "\n"
            "    %% batter 2-1\n"
            "    set_batter_total_vars(2, 1, innings);\n"
            "    label(btex {\\bigsf 0} etex, batter_ab) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_r) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_h) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_rbi) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_bb) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_so) withcolor clr;\n"
            "\n"
            "    %% batter 3-1\n"
            "    set_batter_total_vars(3, 1, innings);\n"
            "    label(btex {\\bigsf 0} etex, batter_ab) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_r) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_h) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_rbi) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_bb) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_so) withcolor clr;\n"
            "\n"
            "    %% batter 4-1\n"
            "    set_batter_total_vars(4, 1, innings);\n"
            "    label(btex {\\bigsf 0} etex, batter_ab) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_r) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_h) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_rbi) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_bb) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_so) withcolor clr;\n"
            "\n"
            "    %% batter 5-1\n"
            "    set_batter_total_vars(5, 1, innings);\n"
            "    label(btex {\\bigsf 0} etex, batter_ab) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_r) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_h) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_rbi) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_bb) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_so) withcolor clr;\n"
            "\n"
            "    %% batter 6-1\n"
            "    set_batter_total_vars(6, 1, innings);\n"
            "    label(btex {\\bigsf 0} etex, batter_ab) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_r) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_h) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_rbi) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_bb) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_so) withcolor clr;\n"
            "\n"
            "    %% batter 7-1\n"
            "    set_batter_total_vars(7, 1, innings);\n"
            "    label(btex {\\bigsf 0} etex, batter_ab) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_r) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_h) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_rbi) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_bb) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_so) withcolor clr;\n"
            "\n"
            "    %% batter 8-1\n"
            "    set_batter_total_vars(8, 1, innings);\n"
            "    label(btex {\\bigsf 0} etex, batter_ab) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_r) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_h) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_rbi) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_bb) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_so) withcolor clr;\n"
            "\n"
            "    %% batter 9-1\n"
            "    set_batter_total_vars(9, 1, innings);\n"
            "    label(btex {\\bigsf 0} etex, batter_ab) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_r) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_h) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_rbi) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_bb) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_so) withcolor clr;\n"
            "\n"
            "    %% batter 10-1\n"
            "    set_batter_total_vars(10, 1, innings);\n"
            "    label(btex {\\bigsf 0} etex, batter_ab) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_r) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_h) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_rbi) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_bb) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, batter_so) withcolor clr;\n"
            "\n"
        )
        assert team.get_batter_stats_metapost_data() == expected_metapost

    def test_get_pitcher_stats_metapost_data(self):
        """Test that the get_pitcher_stats_metapost_data method is correct."""
        team = Team(self._team_data)
        expected_metapost = (
            "    % pitcher stats\n"
            "    set_pitcher_total_vars(1);\n"
            "    label(btex {\\bigsf 0} etex, pitcher_bf) withcolor clr;\n"
            "    label(btex {\\bigsf 0.0} etex, pitcher_ip) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, pitcher_h) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, pitcher_r) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, pitcher_er) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, pitcher_bb) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, pitcher_so) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, pitcher_ibb) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, pitcher_hbp) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, pitcher_blk) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, pitcher_wp) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, pitcher_hr) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, pitcher_pit) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, pitcher_str) withcolor clr;\n"
            "\n"
            "    set_pitcher_total_vars(13);\n"
            "    label(btex {\\bigsf 0} etex, pitcher_bf) withcolor clr;\n"
            "    label(btex {\\bigsf 0.0} etex, pitcher_ip) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, pitcher_h) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, pitcher_r) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, pitcher_er) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, pitcher_bb) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, pitcher_so) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, pitcher_ibb) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, pitcher_hbp) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, pitcher_blk) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, pitcher_wp) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, pitcher_hr) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, pitcher_pit) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, pitcher_str) withcolor clr;\n"
            "\n\n"
        )
        assert team.get_pitcher_stats_metapost_data() == expected_metapost

    def test_get_stats_metapost_data(self):
        """Test that the get_stats_metapost_data method is correct."""
        team = Team(self._team_data)
        expected_metapost = (
            "    %% game totals\n"
            "    set_game_total_vars(innings);\n"
            "    label(btex {\\bigsf 0} etex, inn_run) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, inn_hit) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, inn_err) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, inn_lob) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, inn_bb) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, inn_so) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, inn_pit) withcolor clr;\n"
            "    label(btex {\\bigsf 0} etex, inn_str) withcolor clr;\n"
            "\n"
            "    %% basepaths totals\n"
            "    set_basepath_total_vars(innings);\n"
            "    label.urt(btex {\\sf 0} etex, basepath_first_label) withcolor clr;\n"
            "    label.urt(btex {\\sf 0} etex, basepath_second_label) withcolor clr;\n"
            "    label.urt(btex {\\sf 0} etex, basepath_third_label) withcolor clr;\n"
            "    label.urt(btex {\\sf 0} etex, basepath_hr_label) withcolor clr;\n"
            "    label.urt(btex {\\sf 0} etex, basepath_sf_label) withcolor clr;\n"
            "    label.urt(btex {\\sf 0} etex, basepath_sac_label) withcolor clr;\n"
            "\n"
            "    label.urt(btex {\\sf 0} etex, basepath_tb_label) withcolor clr;\n"
            "    label.urt(btex {\\sf 0} etex, basepath_hbp_label) withcolor clr;\n"
            "    label.urt(btex {\\sf 0} etex, basepath_ibb_label) withcolor clr;\n"
            "    label.urt(btex {\\sf 0} etex, basepath_blk_label) withcolor clr;\n"
            "    label.urt(btex {\\sf 0} etex, basepath_wp_label) withcolor clr;\n"
            "    label.urt(btex {\\sf 0} etex, basepath_pb_label) withcolor clr;\n"
            "\n"
            "    label.urt(btex {\\sf 0} etex, basepath_sb_label) withcolor clr;\n"
            "    label.urt(btex {\\sf 0} etex, basepath_cs_label) withcolor clr;\n"
            "    label.urt(btex {\\sf 0} etex, basepath_po_label) withcolor clr;\n"
            "    label.urt(btex {\\sf 0} etex, basepath_dp_label) withcolor clr;\n"
            "    label.urt(btex {\\sf 0} etex, basepath_tp_label) withcolor clr;\n"
            "    label(btex {\\sf 0-0} etex, basepath_risp_label) withcolor clr;\n"
            "\n"
            "    label.urt(btex {\\sf 27+0+0+0+0~~=~~27} etex, basepath_totals_label) withcolor clr;\n"
            "    label.urt(btex {\\sf 0+0+0~~=~~0} etex, basepath_run_lob_opo_label) withcolor clr;\n"
        )
        assert team.get_stats_metapost_data(27, PitcherStats()) == expected_metapost

    def test_string_output(self):
        """Test that the string method is printing the expected format."""
        team = Team(self._team_data)
        expected_str = (
            "Foo Bars\n"
            "\n"
            "P #1 John Doe (1) \n"
            "C #2 John Doe (1) \n"
            "1B #3 John Doe (1) \n"
            "2B #4 John Doe (1) \n"
            "3B #5 John Doe (1) \n"
            "SS #6 John Doe (1) \n"
            "LF #7 John Doe (1) \n"
            "CF #8 John Doe (1) \n"
            "RF #9 John Doe (1) \n"
            "\n"
            "#1 John Doe (1) 0.0 IP\n"
            "\n"
            "#10 John Doe (C)\n"
            "#11 John Doe (1B)\n"
            "#12 John Doe (RF)\n"
            "\n"
            "#13 John Doe (P)\n"
            "#14 John Doe (P)\n"
            "#15 John Doe (P)\n"
            "#16 John Doe (P)\n"
            "#17 John Doe (P)\n"
            "#18 John Doe (P)\n"
            "#19 John Doe (P)\n"
            "#20 John Doe (P)\n"
            "\n"
            "R: 0\n"
            "1B: 0\n"
            "2B: 0\n"
            "3B: 0\n"
            "HR: 0\n"
            "SAC: 0\n"
            "SF: 0\n"
            "DP: 0\n"
            "TP: 0\n"
            "SB: 0\n"
            "CS: 0\n"
            "PO: 0\n"
            "PB: 0\n"
            "E: 0\n"
            "LOB: 0\n"
            "RISP: 0-0\n"
            "\n\n"
        )
        assert str(team) == expected_str
