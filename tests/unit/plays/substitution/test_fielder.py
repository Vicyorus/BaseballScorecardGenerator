import pytest
from baseball_scorecard.plays.substitution.fielder import DefensiveSubstitution


@pytest.mark.parametrize(
    "position, fielder, is_away_team, expected_metapost, expected_str",
    [
        (
            1,
            "#1 John Doe",
            False,
            (
                "    % defensive substitution\n"
                "    ystart := 1024;\n"
                "    set_vars(xstart,ystart);\n"
                "    draw(new_hitter) withcolor batterclr;\n\n"
            ),
            "Defensive substitution: #1 John Doe\n",
        ),
        (
            1,
            "#1 John Doe",
            True,
            (
                "    % defensive substitution\n"
                "    ystart := 1024;\n"
                "    xstart := xstart + 128;\n"
                "    set_vars(xstart,ystart);\n"
                "    draw(new_hitter) withcolor batterclr;\n"
                "    xstart := xstart - 128;\n\n"
            ),
            "Defensive substitution: #1 John Doe\n",
        ),
        (
            9,
            "#1 John Doe",
            False,
            (
                "    % defensive substitution\n"
                "    ystart := 0;\n"
                "    set_vars(xstart,ystart);\n"
                "    draw(new_hitter) withcolor batterclr;\n\n"
            ),
            "Defensive substitution: #1 John Doe\n",
        ),
        (
            9,
            "#1 John Doe",
            True,
            (
                "    % defensive substitution\n"
                "    ystart := 0;\n"
                "    xstart := xstart + 128;\n"
                "    set_vars(xstart,ystart);\n"
                "    draw(new_hitter) withcolor batterclr;\n"
                "    xstart := xstart - 128;\n\n"
            ),
            "Defensive substitution: #1 John Doe\n",
        ),
    ],
)
class TestDefensiveSubstitution:
    """Tests the DefensiveSubstitution class."""

    def test_get_metapost_data(
        self, position, fielder, is_away_team, expected_metapost, expected_str
    ):
        """Test that the get_metapost_data method is correct."""
        defensive_sub = DefensiveSubstitution(
            position, fielder, is_away_team=is_away_team
        )
        assert defensive_sub.get_metapost_data() == expected_metapost

    def test_string_output(
        self, position, fielder, is_away_team, expected_metapost, expected_str
    ):
        """Test that the string method is printing the expected format."""
        defensive_sub = DefensiveSubstitution(
            position, fielder, is_away_team=is_away_team
        )
        assert str(defensive_sub) == expected_str
