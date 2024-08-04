class GameInfo:

    game_info_coords = {
        "date": (2128,576),
        "temp": (2128,960),
        "at": (2160,96),
        "att": (2160,576),
        "scorer": (2160,720),
        "wind": (2160,960),
    }

    info_template = "    label.top(btex {{\\bigsf {}}} etex rotated 90, {}) withcolor clr;\n"

    def __init__(self, data):
        self.date = data["date"]
        self.temp = data["temp"]
        self.at = data["at"]
        self.att = data["att"]
        self.scorer = data["scorer"]
        self.wind = data["wind"]

    def get_metapost_data(self):
        result = "    % game data\n"

        result += GameInfo.info_template.format(self.date, GameInfo.game_info_coords["date"])
        result += GameInfo.info_template.format(self.temp, GameInfo.game_info_coords["temp"])
        result += GameInfo.info_template.format(self.at, GameInfo.game_info_coords["at"])
        result += GameInfo.info_template.format(self.att, GameInfo.game_info_coords["att"])
        result += GameInfo.info_template.format(self.scorer, GameInfo.game_info_coords["scorer"])
        result += GameInfo.info_template.format(self.wind, GameInfo.game_info_coords["wind"])

        result += "\n"
        return result

    def __str__(self):
        result = "Game info\n"
        result += f"Scorer: {self.scorer}\n"
        result += f"Date: {self.date}\n"
        result += f"At: {self.at}\n"
        result += f"Attendance: {self.att}\n"
        result += f"Weather: {self.temp}, {self.wind}\n"
        result += "\n"

        return result
