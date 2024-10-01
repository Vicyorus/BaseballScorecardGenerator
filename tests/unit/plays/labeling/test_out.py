import pytest
from baseball_scorecard.plays.labeling.out import Out

out_play = "U3"
strikeout_looking = "!K"


@pytest.mark.parametrize(
    "play, out_number, expected_metapost, expected_str",
    [
        (
            "U3",
            1,
            (
                "    label(btex {\\bigsf U3} etex, outlabel) withcolor outclr;\n"
                "    draw_out_one(xstart,ystart,clr);\n"
            ),
            "Out #1: U3",
        ),
        (
            "U3",
            2,
            (
                "    label(btex {\\bigsf U3} etex, outlabel) withcolor outclr;\n"
                "    draw_out_two(xstart,ystart,clr);\n"
            ),
            "Out #2: U3",
        ),
        (
            "U3",
            3,
            (
                "    label(btex {\\bigsf U3} etex, outlabel) withcolor outclr;\n"
                "    draw_out_three(xstart,ystart,clr);\n"
            ),
            "Out #3: U3",
        ),
        (
            "!K",
            1,
            (
                "    draw_strikeout_looking(outlabel, outclr);\n"
                "    draw_out_one(xstart,ystart,clr);\n"
            ),
            "Out #1: !K",
        ),
        (
            "!K",
            2,
            (
                "    draw_strikeout_looking(outlabel, outclr);\n"
                "    draw_out_two(xstart,ystart,clr);\n"
            ),
            "Out #2: !K",
        ),
        (
            "!K",
            3,
            (
                "    draw_strikeout_looking(outlabel, outclr);\n"
                "    draw_out_three(xstart,ystart,clr);\n"
            ),
            "Out #3: !K",
        ),
    ],
)
class TestOut:
    """Tests the Out class."""

    def test_get_metapost_data(self, play, out_number, expected_metapost, expected_str):
        """Test that the get_metapost_data method is correct."""
        out = Out(play, out_number)
        assert out.get_metapost_data() == expected_metapost

    def test_string_output(self, play, out_number, expected_metapost, expected_str):
        """Test that the string method is printing the expected format."""
        out = Out(play, out_number)
        assert str(out) == expected_str


# expected_label = "    draw_strikeout_looking(outlabel, outclr);\n"
