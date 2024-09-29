import pytest
from baseball_scorecard.misc.game_info import GameInfo


@pytest.mark.parametrize(
    "data",
    [
        (
            {
                "date": "1970-04-01 12:00-15:00",
                "temp": "78F, Sunny",
                "at": "Testname Park, Cityville",
                "att": "45,000",
                "scorer": "John Doe",
                "wind": "10mph, Out To RF",
            }
        )
    ],
)
class TestGameInfo:
    """Tests the GameInfo class."""

    def test_get_metapost_data(self, data):
        """Test that the get_metapost_data method is correct."""
        expected_output = (
            "    % game data\n"
            "    set_game_info_vars(innings);\n"
            f"    label.top(btex {{\\bigsf {data['date']}}} etex rotated 90, game_date) withcolor clr;\n"
            f"    label.top(btex {{\\bigsf {data['temp']}}} etex rotated 90, game_temp) withcolor clr;\n"
            f"    label.top(btex {{\\bigsf {data['at']}}} etex rotated 90, game_location) withcolor clr;\n"
            f"    label.top(btex {{\\bigsf {data['att']}}} etex rotated 90, game_attendance) withcolor clr;\n"
            f"    label.top(btex {{\\bigsf {data['scorer']}}} etex rotated 90, game_scorer) withcolor clr;\n"
            f"    label.top(btex {{\\bigsf {data['wind']}}} etex rotated 90, game_wind) withcolor clr;\n\n"
        )

        game_info = GameInfo(data)
        assert game_info.get_metapost_data() == expected_output

    def test_string_output(self, data):
        """Test that the string method is printing the expected format."""
        expected_output = (
            "Game info\n"
            f"Date: {data['date']}\n"
            f"At: {data['at']}\n"
            f"Attendance: {data['att']}\n"
            f"Weather: {data['temp']}, {data['wind']}\n"
            f"Scorer: {data['scorer']}\n\n"
        )

        game_info = GameInfo(data)
        assert str(game_info) == expected_output
