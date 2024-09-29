import pytest
from baseball_scorecard.plays.substitution.pitcher import PitchingSubstitution


@pytest.mark.parametrize(
    "position, pitcher, expected_metapost, expected_str",
    [
        (
            1,
            "#1 John Doe",
            (
                "    % pitching substitution\n"
                "    ystart := 1024;\n"
                "    set_vars(xstart,ystart);\n"
                "    draw(new_pitcher) withcolor pitcherclr;\n\n"
            ),
            "Pitching substitution: #1 John Doe\n",
        ),
        (
            9,
            "#1 John Doe",
            (
                "    % pitching substitution\n"
                "    ystart := 0;\n"
                "    set_vars(xstart,ystart);\n"
                "    draw(new_pitcher) withcolor pitcherclr;\n\n"
            ),
            "Pitching substitution: #1 John Doe\n",
        ),
    ],
)
class TestPitchingSubstitution:
    """Tests the PitchingSubstitution class."""

    def test_get_metapost_data(
        self, position, pitcher, expected_metapost, expected_str
    ):
        """Test that the get_metapost_data method is correct."""
        pitching_sub = PitchingSubstitution(position, pitcher)
        assert pitching_sub.get_metapost_data() == expected_metapost

    def test_string_output(self, position, pitcher, expected_metapost, expected_str):
        """Test that the string method is printing the expected format."""
        pitching_sub = PitchingSubstitution(position, pitcher)
        assert str(pitching_sub) == expected_str
