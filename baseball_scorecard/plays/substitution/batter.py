class OffensiveSubstitution:
    def __init__(self, lineup_position, batter, is_runner):
        self.lineup_position = lineup_position
        self.batter = batter
        self.is_runner = is_runner

    def get_metapost_data(self, overflow):
        pinch_position = "pinch-runner" if self.is_runner else "pinch-hitter"
        result = f"    % offensive substitution: {pinch_position}\n"
        y_start = 128 * (9 - self.lineup_position)
        result += f"    ystart := {y_start};\n"
        if self.is_runner:
            result += "    xstart := xstart + 128;\n"
        result += "    set_vars(xstart,ystart);\n"
        result += "    draw(new_hitter) withcolor batterclr;\n"
        if self.is_runner:
            result += "    xstart := xstart - 128;\n"
        result += "\n"

        return result

    def __str__(self):
        pinch_position = "Pinch-runner" if self.is_runner else "Pinch-hitter"
        return f"Offensive substitution ({pinch_position}): {self.batter}\n"
