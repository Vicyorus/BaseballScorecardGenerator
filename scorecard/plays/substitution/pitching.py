class PitchingSubstitution:
    def __init__(self, lineup_position, pitcher):
        self.lineup_position = lineup_position
        self.pitcher = pitcher

    def get_metapost_data(self, overflow):
        result = "    % pitching change\n"
        y_start = 128 * (9 - self.lineup_position)
        result += f"    ystart := {y_start};\n"
        result += "    set_vars(xstart,ystart);\n"
        result +=     "    draw(new_pitcher) withcolor pitcherclr;\n"
        return result

    def __str__(self):
        return f"Pitching substitution: {self.pitcher}\n"