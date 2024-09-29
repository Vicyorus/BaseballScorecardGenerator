class DefensiveSubstitution:
    def __init__(
        self, lineup_position: int, fielder_info: str, is_away_team: bool = False
    ):
        self.lineup_position = lineup_position
        self.fielder_info = fielder_info
        self.is_away_team = is_away_team

    def get_metapost_data(self, overflow: int = 0):
        y_start = 128 * (9 - self.lineup_position)

        result = "    % defensive substitution\n"
        result += f"    ystart := {y_start};\n"

        if self.is_away_team:
            result += "    xstart := xstart + 128;\n"

        result += (
            "    set_vars(xstart,ystart);\n"
            "    draw(new_hitter) withcolor batterclr;\n"
        )

        if self.is_away_team:
            result += "    xstart := xstart - 128;\n"
        result += "\n"

        return result

    def __str__(self):
        return f"Defensive substitution: {self.fielder_info}\n"
