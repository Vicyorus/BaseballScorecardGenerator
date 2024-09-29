class OffensiveSubstitution:
    def __init__(self, lineup_position: int, batter_info: str, is_runner: bool = False):
        self.lineup_position = lineup_position
        self.batter_info = batter_info
        self.is_runner = is_runner

    def get_metapost_data(self, overflow: int = 0):
        pinch_position = "pinch-runner" if self.is_runner else "pinch-hitter"
        y_start = 128 * (9 - self.lineup_position)

        result = (
            f"    % offensive substitution: {pinch_position}\n"
            f"    ystart := {y_start};\n"
        )

        if self.is_runner:
            result += "    xstart := xstart + 128;\n"

        result += (
            "    set_vars(xstart,ystart);\n"
            "    draw(new_hitter) withcolor batterclr;\n"
        )

        if self.is_runner:
            result += "    xstart := xstart - 128;\n"
        result += "\n"

        return result

    def __str__(self):
        pinch_position = "Pinch-runner" if self.is_runner else "Pinch-hitter"
        return f"Offensive substitution ({pinch_position}): {self.batter_info}\n"
