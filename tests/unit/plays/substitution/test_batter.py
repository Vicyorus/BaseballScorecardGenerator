import pytest
from baseball_scorecard.plays.substitution.batter import OffensiveSubstitution


@pytest.mark.parametrize(
    "position, batter, is_runner, expected_metapost, expected_str",
    [
        (
            1,
            "#1 John Doe",
            False,
            (
                "    % offensive substitution: pinch-hitter\n"
                "    ystart := 1024;\n"
                "    set_vars(xstart,ystart);\n"
                "    draw(new_hitter) withcolor batterclr;\n\n"
            ),
            "Offensive substitution (Pinch-hitter): #1 John Doe\n",
        ),
        (
            1,
            "#1 John Doe",
            True,
            (
                "    % offensive substitution: pinch-runner\n"
                "    ystart := 1024;\n"
                "    xstart := xstart + 128;\n"
                "    set_vars(xstart,ystart);\n"
                "    draw(new_hitter) withcolor batterclr;\n"
                "    xstart := xstart - 128;\n\n"
            ),
            "Offensive substitution (Pinch-runner): #1 John Doe\n",
        ),
        (
            9,
            "#1 John Doe",
            False,
            (
                "    % offensive substitution: pinch-hitter\n"
                "    ystart := 0;\n"
                "    set_vars(xstart,ystart);\n"
                "    draw(new_hitter) withcolor batterclr;\n\n"
            ),
            "Offensive substitution (Pinch-hitter): #1 John Doe\n",
        ),
        (
            9,
            "#1 John Doe",
            True,
            (
                "    % offensive substitution: pinch-runner\n"
                "    ystart := 0;\n"
                "    xstart := xstart + 128;\n"
                "    set_vars(xstart,ystart);\n"
                "    draw(new_hitter) withcolor batterclr;\n"
                "    xstart := xstart - 128;\n\n"
            ),
            "Offensive substitution (Pinch-runner): #1 John Doe\n",
        ),
    ],
)
class TestOffensiveSubstitution:
    """Tests the OffensiveSubstitution class."""

    def test_get_metapost_data(
        self, position, batter, is_runner, expected_metapost, expected_str
    ):
        """Test that the get_metapost_data method is correct."""
        offensive_sub = OffensiveSubstitution(position, batter, is_runner=is_runner)
        assert offensive_sub.get_metapost_data() == expected_metapost

    def test_string_output(
        self, position, batter, is_runner, expected_metapost, expected_str
    ):
        """Test that the string method is printing the expected format."""
        offensive_sub = OffensiveSubstitution(position, batter, is_runner=is_runner)
        assert str(offensive_sub) == expected_str
