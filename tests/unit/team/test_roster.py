import pytest
from baseball_scorecard.team.roster import Roster


class TestRoster:
    """Tests the Roster class."""

    @pytest.mark.parametrize(
        "roster_data, lefties, use_extended_roster, expected_str",
        [
            (
                {
                    1: "John Doe",
                    2: "Jack Doe",
                    3: "James Doe",
                },
                [1],
                False,
                ("#1 John Doe\n" "#2 Jack Doe\n" "#3 James Doe\n"),
            ),
            (
                {
                    1: {"jersey": 1, "name": "John Doe"},
                    2: {"jersey": 2, "name": "Jack Doe"},
                    3: {"jersey": 3, "name": "James Doe"},
                },
                [1],
                True,
                ("#1 John Doe\n" "#2 Jack Doe\n" "#3 James Doe\n"),
            ),
        ],
    )
    def test_get_player(self, roster_data, lefties, use_extended_roster, expected_str):
        """Test that the get_player method is correct."""

        roster = Roster(roster_data, lefties, use_extended_roster)

        for id, info in roster_data.items():
            if use_extended_roster:
                assert roster.get_player(id).name == info["name"]
            else:
                assert roster.get_player(id).name == info

    def test_get_player_no_player_in_roster(self):
        """Test that the get_player method raises an exception when no player is found."""
        roster = Roster({}, [], False)
        with pytest.raises(Exception) as e_info:
            roster.get_player(1)

    @pytest.mark.parametrize(
        "roster_data, lefties, use_extended_roster, expected_str",
        [
            (
                {
                    1: "John Doe",
                    2: "Jack Doe",
                    3: "James Doe",
                },
                [1],
                False,
                ("#1 John Doe\n" "#2 Jack Doe\n" "#3 James Doe\n"),
            ),
            (
                {
                    1: {"jersey": 1, "name": "John Doe"},
                    2: {"jersey": 2, "name": "Jack Doe"},
                    3: {"jersey": 3, "name": "James Doe"},
                },
                [1],
                True,
                ("#1 John Doe\n" "#2 Jack Doe\n" "#3 James Doe\n"),
            ),
        ],
    )
    def test_string_output(
        self, roster_data, lefties, use_extended_roster, expected_str
    ):
        """Test that the string method is printing the expected format."""
        roster = Roster(roster_data, lefties, use_extended_roster)
        assert str(roster) == expected_str
