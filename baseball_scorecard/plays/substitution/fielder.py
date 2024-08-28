class DefensiveSubstitution:
    def __init__(self, lineup_position, fielder):
        self.lineup_position = lineup_position
        self.fielder = fielder

    def get_metapost_data(self, overflow):
        result = "    % defensive substitution\n"
        y_start = 128 * (9 - self.lineup_position)
        result += f"    ystart := {y_start};\n"
        result += "    set_vars(xstart,ystart);\n"
        result += "    draw(new_hitter) withcolor batterclr;\n"
        result += "\n"

        return result

    def __str__(self):
        return f"Defensive substitution: {self.fielder}\n"
