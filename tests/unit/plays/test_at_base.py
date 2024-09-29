import pytest
from baseball_scorecard.plays.at_base import AtBase


@pytest.mark.parametrize(
    "base, label, expected_metapost, expected_str",
    [
        (
            1,
            "1B",
            "    label.rt(btex {\\sf 1B} etex, first) withcolor clr;\n",
            "Label at base 1: 1B",
        ),
        (
            2,
            "2B",
            "    label.top(btex {\\sf 2B} etex, second) withcolor clr;\n",
            "Label at base 2: 2B",
        ),
        (
            3,
            "3B",
            "    label.lft(btex {\\sf 3B} etex, third) withcolor clr;\n",
            "Label at base 3: 3B",
        ),
        (
            4,
            "HOME",
            "    label.bot(btex {\\sf HOME} etex, home) withcolor clr;\n",
            "Label at base 4: HOME",
        ),
    ],
)
class TestAtBase:
    """Tests the AtBase class."""

    def test_get_metapost_data(self, base, label, expected_metapost, expected_str):
        """Test that the get_metapost_data method is correct."""
        at_base = AtBase(label, base)
        assert at_base.get_metapost_data() == expected_metapost

    def test_string_output(self, base, label, expected_metapost, expected_str):
        """Test that the string method is printing the expected format."""
        at_base = AtBase(label, base)
        assert str(at_base) == expected_str
