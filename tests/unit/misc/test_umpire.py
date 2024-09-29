import pytest
from baseball_scorecard.misc.umpire import Umpire

label_template = (
    "    label.top(btex {{\\bigsf {}}} etex rotated 90, {}) withcolor clr;\n"
)


@pytest.mark.parametrize(
    "base, name, location",
    [
        ("HP", "HP Ump", "game_hp_ump"),
        ("1B", "1B Ump", "game_first_ump"),
        ("2B", "2B Ump", "game_second_ump"),
        ("3B", "3B Ump", "game_third_ump"),
        ("LF", "LF Ump", "game_lf_ump"),
        ("RF", "RF Ump", "game_rf_ump"),
    ],
)
class TestUmpire:
    """Tests the Umpire class."""

    def test_get_metapost_data(self, base, name, location):
        """Test that the get_metapost_data method is correct."""
        umpire = Umpire(base, name)
        assert umpire.get_metapost_data() == label_template.format(name, location)

    def test_string_output(self, base, name, location):
        """Test that the string method is printing the expected format."""
        umpire = Umpire(base, name)
        assert str(umpire) == f"{base}: {name}\n"
