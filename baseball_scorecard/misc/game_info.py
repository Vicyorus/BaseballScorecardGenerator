class GameInfo:

    info_template = (
        "    label.top(btex {{\\bigsf {}}} etex rotated 90, {}) withcolor clr;\n"
    )

    def __init__(self, data):
        self.date = data["date"]
        self.temp = data["temp"]
        self.at = data["at"]
        self.att = data["att"]
        self.scorer = data["scorer"]
        self.wind = data["wind"]

    def get_metapost_data(self):
        result = "    % game data\n"
        result += "    set_game_info_vars(innings);\n"

        result += GameInfo.info_template.format(self.date, "game_date")
        result += GameInfo.info_template.format(self.temp, "game_temp")
        result += GameInfo.info_template.format(self.at, "game_location")
        result += GameInfo.info_template.format(self.att, "game_attendance")
        result += GameInfo.info_template.format(self.scorer, "game_scorer")
        result += GameInfo.info_template.format(self.wind, "game_wind")

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
