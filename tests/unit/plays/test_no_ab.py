from baseball_scorecard.plays.no_ab import NoAtBat


class TestNoAtBat:
    """Tests the NoAtBat class."""

    def test_get_metapost_data(self):
        """Test that the get_metapost_data method is correct."""
        no_ab = NoAtBat("CS")
        assert (
            no_ab.get_metapost_data()
            == f"    label(btex {{\\bigsf CS}} etex, outlabel) withcolor clr;\n"
        )

    def test_string_output(self):
        """Test that the string method is printing the expected format."""
        no_ab = NoAtBat("CS")
        assert str(no_ab) == "No AB: CS"
