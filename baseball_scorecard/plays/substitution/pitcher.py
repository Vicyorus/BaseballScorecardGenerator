class PitchingSubstitution:
    def __init__(self, lineup_position: int, pitcher_info: str):
        self.lineup_position = lineup_position
        self.pitcher_info = pitcher_info

    def get_metapost_data(self, overflow: int = 0):
        y_start = 128 * (9 - self.lineup_position)

        result = (
            "    % pitching substitution\n"
            f"    ystart := {y_start};\n"
            "    set_vars(xstart,ystart);\n"
            "    draw(new_pitcher) withcolor pitcherclr;\n\n"
        )

        return result

    def __str__(self):
        return f"Pitching substitution: {self.pitcher_info}\n"
