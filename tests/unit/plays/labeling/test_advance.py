import pytest
from baseball_scorecard.plays.labeling.advance import Advance


class TestAdvance:
    @pytest.mark.parametrize(
        "advance_code, play, end_base, expected_play, expected_basepath, expected_color",
        [
            ("Hit", 1, 1, "1B", "single", "hit"),
            ("Hit", 2, 2, "2B", "double", "hit"),
            ("Hit", 3, 3, "3B", "triple", "hit"),
            ("Hit", 4, 4, "HR", "homerun", "homer"),
            ("Hit", "U", "U", "HR", "homerun", "homer"),
            ("Walk", "BB", 1, "BB", "single", "walk"),
            ("Intent Walk", "IBB", 1, "IBB", "single", "walk"),
            ("Hit By Pitch", "HBP", 1, "HBP", "single", "clr"),
            ("Hit By Pitch", "HP", 1, "HBP", "single", "clr"),
        ],
    )
    def test_get_metapost_data_play_box(
        self,
        advance_code,
        play,
        end_base,
        expected_play,
        expected_basepath,
        expected_color,
    ):
        """Test that the get_metapost_data method is correct for advances that use the play box."""
        advance = Advance(advance_code, play, 0, end_base)

        expected_metapost = (
            f"    label(btex {{\\midsf {expected_play}}} etex, playloc) withcolor {expected_color};\n"
            f"    draw({expected_basepath}) withcolor {expected_color};\n"
        )

        assert advance.get_metapost_data() == expected_metapost

    @pytest.mark.parametrize(
        "advance_code, play, start_base, end_base, expected_play_metapost, expected_basepath, expected_color",
        [
            (
                "Error",
                "E1",
                0,
                1,
                "    label.lrt(btex {\\sf E1} etex, wayfirst) withcolor clr;\n",
                "single",
                "error",
            ),
            (
                "Reach",
                "FC5",
                0,
                1,
                "    label.lrt(btex {\\sf FC5} etex, wayfirst) withcolor clr;\n",
                "single",
                "clr",
            ),
            (
                "Advance",
                "FC5",
                0,
                1,
                "    label.lrt(btex {\\sf FC5} etex, wayfirst) withcolor clr;\n",
                "single",
                "clr",
            ),
            (
                "Advance",
                "FC5",
                1,
                2,
                "    label.urt(btex {\\sf FC5} etex, waysecond) withcolor clr;\n",
                "firstsecond",
                "clr",
            ),
            (
                "Advance",
                "FC5",
                1,
                3,
                "    label.ulft(btex {\\sf FC5} etex, waythird) withcolor clr;\n",
                "firstthird",
                "clr",
            ),
            (
                "Advance",
                "FC5",
                1,
                4,
                "    label.llft(btex {\\sf FC5} etex, wayhome+(-1,-2)) withcolor clr;\n",
                "firsthome",
                "clr",
            ),
            (
                "Advance",
                "FC5",
                2,
                3,
                "    label.ulft(btex {\\sf FC5} etex, waythird) withcolor clr;\n",
                "secondthird",
                "clr",
            ),
            (
                "Advance",
                "FC5",
                2,
                4,
                "    label.llft(btex {\\sf FC5} etex, wayhome+(-1,-2)) withcolor clr;\n",
                "secondhome",
                "clr",
            ),
            (
                "Advance",
                "FC5",
                3,
                4,
                "    label.llft(btex {\\sf FC5} etex, wayhome+(-1,-2)) withcolor clr;\n",
                "thirdhome",
                "clr",
            ),
            (
                "Advance",
                "FC5",
                1,
                "U",
                "    label.llft(btex {\\sf FC5} etex, wayhome+(-1,-2)) withcolor clr;\n",
                "firsthome",
                "clr",
            ),
            (
                "Advance",
                "FC5",
                2,
                "U",
                "    label.llft(btex {\\sf FC5} etex, wayhome+(-1,-2)) withcolor clr;\n",
                "secondhome",
                "clr",
            ),
            (
                "Advance",
                "FC5",
                3,
                "U",
                "    label.llft(btex {\\sf FC5} etex, wayhome+(-1,-2)) withcolor clr;\n",
                "thirdhome",
                "clr",
            ),
        ],
    )
    def test_get_metapost_data_wayside(
        self,
        advance_code,
        play,
        start_base,
        end_base,
        expected_play_metapost,
        expected_basepath,
        expected_color,
    ):
        """Test that the get_metapost_data method is correct for advances that label the side of the basepath."""
        advance = Advance(advance_code, play, start_base, end_base)

        expected_metapost = (
            f"{expected_play_metapost}"
            f"    draw({expected_basepath}) withcolor {expected_color};\n"
        )

        assert advance.get_metapost_data() == expected_metapost

    def test_string_output(self):
        """Test that the string method is printing the expected format."""
        advance = Advance("Hit", 1, 0, 1)

        expected_str = "Advance (0 to 1): Hit on 1"

        assert str(advance) == expected_str
