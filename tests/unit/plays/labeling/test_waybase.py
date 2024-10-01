import pytest
from baseball_scorecard.plays.labeling.waybase import WayBase


@pytest.mark.parametrize(
    "label, start, end, expected",
    [
        # Labels starting from home plate.
        (
            "FC1",
            0,
            1,
            "    label.lrt(btex {\\sf FC1} etex, wayfirst) withcolor clr;\n",
        ),
        (
            "FC1",
            0,
            2,
            "    label.urt(btex {\\sf FC1} etex, waysecond) withcolor clr;\n",
        ),
        (
            "FC1",
            0,
            3,
            "    label.ulft(btex {\\sf FC1} etex, waythird) withcolor clr;\n",
        ),
        (
            "FC1",
            0,
            4,
            "    label.llft(btex {\\sf FC1} etex, wayhome+(-1,-2)) withcolor clr;\n",
        ),
        (
            "FC1",
            0,
            "U",
            "    label.llft(btex {\\sf FC1} etex, wayhome+(-1,-2)) withcolor clr;\n",
        ),
        # Labels starting at 1B, no jersey number.
        (
            "1-3",
            1,
            1,
            "    label.urt(btex {\\sf 1-3} etex, waysecond) withcolor clr;\n",
        ),
        (
            "9-4",
            1,
            2,
            "    label.urt(btex {\\sf 9-4} etex, waysecond) withcolor clr;\n",
        ),
        (
            "7-5",
            1,
            3,
            "    label.ulft(btex {\\sf 7-5} etex, waythird) withcolor clr;\n",
        ),
        (
            "7-2",
            1,
            4,
            "    label.llft(btex {\\sf 7-2} etex, wayhome+(-1,-2)) withcolor clr;\n",
        ),
        (
            "7-2",
            1,
            "U",
            "    label.llft(btex {\\sf 7-2} etex, wayhome+(-1,-2)) withcolor clr;\n",
        ),
        # Labels starting at 1B, with jersey number.
        (
            "1 PO",
            1,
            1,
            (
                "    label.urt(btex {\\sf PO} etex, waysecond) withcolor clr;\n"
                "    label.urt(btex {\\sf 1} etex, waysecond+(0,10)) withcolor clr;\n"
            ),
        ),
        (
            "1 1B",
            1,
            2,
            (
                "    label.urt(btex {\\sf 1B} etex, waysecond) withcolor clr;\n"
                "    label.urt(btex {\\sf 1} etex, waysecond+(0,10)) withcolor clr;\n"
            ),
        ),
        (
            "1 2B",
            1,
            3,
            (
                "    label.ulft(btex {\\sf 2B} etex, waythird) withcolor clr;\n"
                "    label.ulft(btex {\\sf 1} etex, waythird+(0,10)) withcolor clr;\n"
            ),
        ),
        (
            "1 3B",
            1,
            4,
            (
                "    label.lft(btex {\\sf 1} etex, wayhome+(-1,-2)) withcolor clr;\n"
                "    label.llft(btex {\\sf 3B} etex, wayhome+(-1,-5)) withcolor clr;\n"
            ),
        ),
        (
            "1 HR",
            1,
            "U",
            (
                "    label.lft(btex {\\sf 1} etex, wayhome+(-1,-2)) withcolor clr;\n"
                "    label.llft(btex {\\sf HR} etex, wayhome+(-1,-5)) withcolor clr;\n"
            ),
        ),
        # Labels starting at 2B, no jersey number.
        (
            "9-4",
            2,
            2,
            "    label.ulft(btex {\\sf 9-4} etex, waythird) withcolor clr;\n",
        ),
        (
            "7-5",
            2,
            3,
            "    label.ulft(btex {\\sf 7-5} etex, waythird) withcolor clr;\n",
        ),
        (
            "7-2",
            2,
            4,
            "    label.llft(btex {\\sf 7-2} etex, wayhome+(-1,-2)) withcolor clr;\n",
        ),
        (
            "7-2",
            2,
            "U",
            "    label.llft(btex {\\sf 7-2} etex, wayhome+(-1,-2)) withcolor clr;\n",
        ),
        # Labels starting at 2B, with jersey number.
        (
            "2 PO",
            2,
            2,
            (
                "    label.ulft(btex {\\sf PO} etex, waythird) withcolor clr;\n"
                "    label.ulft(btex {\\sf 2} etex, waythird+(0,10)) withcolor clr;\n"
            ),
        ),
        (
            "2 2B",
            2,
            3,
            (
                "    label.ulft(btex {\\sf 2B} etex, waythird) withcolor clr;\n"
                "    label.ulft(btex {\\sf 2} etex, waythird+(0,10)) withcolor clr;\n"
            ),
        ),
        (
            "2 3B",
            2,
            4,
            (
                "    label.lft(btex {\\sf 2} etex, wayhome+(-1,-2)) withcolor clr;\n"
                "    label.llft(btex {\\sf 3B} etex, wayhome+(-1,-5)) withcolor clr;\n"
            ),
        ),
        (
            "2 HR",
            2,
            "U",
            (
                "    label.lft(btex {\\sf 2} etex, wayhome+(-1,-2)) withcolor clr;\n"
                "    label.llft(btex {\\sf HR} etex, wayhome+(-1,-5)) withcolor clr;\n"
            ),
        ),
        # Labels starting at 3B, no jersey number.
        (
            "7-5",
            3,
            3,
            "    label.llft(btex {\\sf 7-5} etex, wayhome+(-1,-2)) withcolor clr;\n",
        ),
        (
            "7-2",
            3,
            4,
            "    label.llft(btex {\\sf 7-2} etex, wayhome+(-1,-2)) withcolor clr;\n",
        ),
        (
            "7-2",
            3,
            "U",
            "    label.llft(btex {\\sf 7-2} etex, wayhome+(-1,-2)) withcolor clr;\n",
        ),
        # Labels starting at 3B, with jersey number.
        (
            "3 PO",
            3,
            3,
            (
                "    label.lft(btex {\\sf 3} etex, wayhome+(-1,-2)) withcolor clr;\n"
                "    label.llft(btex {\\sf PO} etex, wayhome+(-1,-5)) withcolor clr;\n"
            ),
        ),
        (
            "3 3B",
            3,
            4,
            (
                "    label.lft(btex {\\sf 3} etex, wayhome+(-1,-2)) withcolor clr;\n"
                "    label.llft(btex {\\sf 3B} etex, wayhome+(-1,-5)) withcolor clr;\n"
            ),
        ),
        (
            "3 HR",
            3,
            "U",
            (
                "    label.lft(btex {\\sf 3} etex, wayhome+(-1,-2)) withcolor clr;\n"
                "    label.llft(btex {\\sf HR} etex, wayhome+(-1,-5)) withcolor clr;\n"
            ),
        ),
    ],
)
class TestWaybase:
    """Test the Waybase class."""

    def test_get_metapost_data(self, label, start, end, expected):
        """Test the get_metapost_data method."""
        waybase = WayBase(label, start, end)
        assert waybase.get_metapost_data() == expected
