import pytest
from baseball_scorecard.plays.labeling.thrown_out import ThrownOut


class TestThrownOut:

    @pytest.mark.parametrize(
        "start_base, end_base, play, out_number, expected_metapost",
        [
            (
                1,
                1,
                "1 FC5",
                1,
                (
                    "    draw(cs_second) withcolor outclr;\n"
                    "    label.urt(btex {\\sf FC5} etex, waysecond) withcolor clr;\n"
                    "    label.urt(btex {\\sf 1} etex, waysecond+(0,10)) withcolor clr;\n"
                    "    draw_out_one(xstart,ystart,clr);\n"
                ),
            ),
            (
                1,
                2,
                "1 FC5",
                1,
                (
                    "    draw(cs_second) withcolor outclr;\n"
                    "    label.urt(btex {\\sf FC5} etex, waysecond) withcolor clr;\n"
                    "    label.urt(btex {\\sf 1} etex, waysecond+(0,10)) withcolor clr;\n"
                    "    draw_out_one(xstart,ystart,clr);\n"
                ),
            ),
            (
                1,
                3,
                "1 FC5",
                1,
                (
                    "    draw(cs_firstthird) withcolor outclr;\n"
                    "    label.ulft(btex {\\sf FC5} etex, waythird) withcolor clr;\n"
                    "    label.ulft(btex {\\sf 1} etex, waythird+(0,10)) withcolor clr;\n"
                    "    draw_out_one(xstart,ystart,clr);\n"
                ),
            ),
            (
                1,
                4,
                "1 FC5",
                1,
                (
                    "    draw(to_firsthome) withcolor outclr;\n"
                    "    label.lft(btex {\\sf 1} etex, wayhome+(-1,-2)) withcolor clr;\n"
                    "    label.llft(btex {\\sf FC5} etex, wayhome+(-1,-5)) withcolor clr;\n"
                    "    draw_out_one(xstart,ystart,clr);\n"
                ),
            ),
            (
                2,
                2,
                "1 FC5",
                1,
                (
                    "    draw(cs_third) withcolor outclr;\n"
                    "    label.ulft(btex {\\sf FC5} etex, waythird) withcolor clr;\n"
                    "    label.ulft(btex {\\sf 1} etex, waythird+(0,10)) withcolor clr;\n"
                    "    draw_out_one(xstart,ystart,clr);\n"
                ),
            ),
            (
                2,
                3,
                "1 FC5",
                1,
                (
                    "    draw(cs_third) withcolor outclr;\n"
                    "    label.ulft(btex {\\sf FC5} etex, waythird) withcolor clr;\n"
                    "    label.ulft(btex {\\sf 1} etex, waythird+(0,10)) withcolor clr;\n"
                    "    draw_out_one(xstart,ystart,clr);\n"
                ),
            ),
            (
                2,
                4,
                "1 FC5",
                1,
                (
                    "    draw(to_secondhome) withcolor outclr;\n"
                    "    label.lft(btex {\\sf 1} etex, wayhome+(-1,-2)) withcolor clr;\n"
                    "    label.llft(btex {\\sf FC5} etex, wayhome+(-1,-5)) withcolor clr;\n"
                    "    draw_out_one(xstart,ystart,clr);\n"
                ),
            ),
            (
                3,
                3,
                "1 FC5",
                1,
                (
                    "    draw(to_home) withcolor outclr;\n"
                    "    label.lft(btex {\\sf 1} etex, wayhome+(-1,-2)) withcolor clr;\n"
                    "    label.llft(btex {\\sf FC5} etex, wayhome+(-1,-5)) withcolor clr;\n"
                    "    draw_out_one(xstart,ystart,clr);\n"
                ),
            ),
            (
                3,
                4,
                "1 FC5",
                1,
                (
                    "    draw(to_home) withcolor outclr;\n"
                    "    label.lft(btex {\\sf 1} etex, wayhome+(-1,-2)) withcolor clr;\n"
                    "    label.llft(btex {\\sf FC5} etex, wayhome+(-1,-5)) withcolor clr;\n"
                    "    draw_out_one(xstart,ystart,clr);\n"
                ),
            ),
        ],
    )
    def test_get_metapost_data(
        self,
        start_base,
        end_base,
        play,
        out_number,
        expected_metapost,
    ):
        """Test that the get_metapost_data method is correct."""
        advance = ThrownOut(play, start_base, end_base, out_number)
        assert advance.get_metapost_data() == expected_metapost

    @pytest.mark.parametrize(
        "start_base, end_base, play, out_number, expected_metapost",
        [
            (
                1,
                2,
                "1 FC5",
                1,
                (
                    "    draw(cs_second) withcolor outclr;\n"
                    "    label.urt(btex {\\sf FC5} etex, waysecond) withcolor clr;\n"
                    "    label.urt(btex {\\sf 1} etex, waysecond+(0,10)) withcolor clr;\n"
                    "    draw_out_one(xstart,ystart,clr);\n"
                ),
            ),
            (
                1,
                2,
                "1 FC5",
                2,
                (
                    "    draw(cs_second) withcolor outclr;\n"
                    "    label.urt(btex {\\sf FC5} etex, waysecond) withcolor clr;\n"
                    "    label.urt(btex {\\sf 1} etex, waysecond+(0,10)) withcolor clr;\n"
                    "    draw_out_two(xstart,ystart,clr);\n"
                ),
            ),
            (
                1,
                2,
                "1 FC5",
                3,
                (
                    "    draw(cs_second) withcolor outclr;\n"
                    "    label.urt(btex {\\sf FC5} etex, waysecond) withcolor clr;\n"
                    "    label.urt(btex {\\sf 1} etex, waysecond+(0,10)) withcolor clr;\n"
                    "    draw_out_three(xstart,ystart,clr);\n"
                ),
            ),
        ],
    )
    def test_get_metapost_data_different_outs(
        self,
        start_base,
        end_base,
        play,
        out_number,
        expected_metapost,
    ):
        """Test that the get_metapost_data method is correct for a different out number."""
        advance = ThrownOut(play, start_base, end_base, out_number)
        assert advance.get_metapost_data() == expected_metapost

    def test_string_output(self):
        """Test that the string method is printing the expected format."""
        advance = ThrownOut("9-4", 0, 1, 1)
        expected_str = "Out #1: Thrown out (0 to 1), 9-4"
        assert str(advance) == expected_str
