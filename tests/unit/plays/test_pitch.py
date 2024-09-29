from baseball_scorecard.plays.pitch import Pitch


class TestPitch:
    """Tests the Pitch class."""

    def test_info(self):
        """Test the information of a Pitch object."""
        pitch = Pitch("s")
        assert pitch.pitch_code == "s"
        assert pitch.inc_pitch_count == True
        assert pitch.is_strike == True

        pitch = Pitch("s", inc_pitch_count=False)
        assert pitch.pitch_code == "s"
        assert pitch.inc_pitch_count == False
        assert pitch.is_strike == True

        pitch = Pitch("s", is_strike=False)
        assert pitch.pitch_code == "s"
        assert pitch.inc_pitch_count == True
        assert pitch.is_strike == False

    def test_string_output(self):
        """Test that the string method is printing the expected format."""
        pitch = Pitch("s")
        assert str(pitch) == "s"
