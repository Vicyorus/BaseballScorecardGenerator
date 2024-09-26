from baseball_scorecard.misc.game_info import GameInfo

test_data = {
    "date": "1970-04-01 12:00-15:00",
    "temp": "78F, Sunny",
    "at": "Testname Park, Cityville",
    "att": "45,000",
    "scorer": "John Doe",
    "wind": "10mph, Out To RF",
}


def test_game_info_get_metapost_data():
    """Test that the generated metapost data for the GameInfo class is correct."""
    expected_output = "    % game data\n"
    expected_output += "    set_game_info_vars(innings);\n"
    expected_output += f"    label.top(btex {{\\bigsf {test_data['date']}}} etex rotated 90, game_date) withcolor clr;\n"
    expected_output += f"    label.top(btex {{\\bigsf {test_data['temp']}}} etex rotated 90, game_temp) withcolor clr;\n"
    expected_output += f"    label.top(btex {{\\bigsf {test_data['at']}}} etex rotated 90, game_location) withcolor clr;\n"
    expected_output += f"    label.top(btex {{\\bigsf {test_data['att']}}} etex rotated 90, game_attendance) withcolor clr;\n"
    expected_output += f"    label.top(btex {{\\bigsf {test_data['scorer']}}} etex rotated 90, game_scorer) withcolor clr;\n"
    expected_output += f"    label.top(btex {{\\bigsf {test_data['wind']}}} etex rotated 90, game_wind) withcolor clr;\n"
    expected_output += "\n"

    game_info = GameInfo(test_data)
    assert game_info.get_metapost_data() == expected_output


def test_game_info_string_output():
    """Test that the string method for the GameInfo class is printing the expected format."""

    expected_output = "Game info\n"
    expected_output += f"Date: {test_data['date']}\n"
    expected_output += f"At: {test_data['at']}\n"
    expected_output += f"Attendance: {test_data['att']}\n"
    expected_output += f"Weather: {test_data['temp']}, {test_data['wind']}\n"
    expected_output += f"Scorer: {test_data['scorer']}\n"
    expected_output += "\n"

    game_info = GameInfo(test_data)
    assert str(game_info) == expected_output
