class InningStats:

    def __init__(self):
        self.runs = 0
        self.hits = 0
        self.errors = 0
        self.left_on_base = 0
        self.strikeouts = 0
        self.walks = 0
        self.pitches = 0
        self.strikes = 0

    def get_metapost_data(self):
        result = "    % inning stats\n"
        result += f"    set_inning_total_vars(xstart);\n"
        result += f"    label(btex {{\\bigsf {self.runs}}} etex, inn_run) withcolor clr;\n"
        result += f"    label(btex {{\\bigsf {self.hits}}} etex, inn_hit) withcolor clr;\n"
        result += f"    label(btex {{\\bigsf {self.errors}}} etex, inn_err) withcolor clr;\n"
        result += f"    label(btex {{\\bigsf {self.left_on_base}}} etex, inn_lob) withcolor clr;\n"
        result += f"    label(btex {{\\bigsf {self.walks}}} etex, inn_bb) withcolor clr;\n"
        result += f"    label(btex {{\\bigsf {self.strikeouts}}} etex, inn_so) withcolor clr;\n"
        result += f"    label(btex {{\\bigsf {self.pitches}}} etex, inn_pit) withcolor clr;\n"
        result += f"    label(btex {{\\bigsf {self.strikes}}} etex, inn_str) withcolor clr;\n"
        result += "\n"

        return result

    def __str__(self):
        result = "Inning totals:"

        if self.runs:
            result += f" {self.runs} R"

        if self.hits:
            result += f" {self.hits} H"

        if self.errors:
            result += f" {self.errors} E"

        if self.left_on_base:
            result += f" {self.left_on_base} LOB"

        if self.strikeouts:
            result += f" {self.strikeouts} K"

        if self.walks:
            result += f" {self.walks} BB"

        if self.pitches:
            result += f" {self.pitches} P"

        if self.strikes:
            result += f" {self.strikes} S"

        result += "\n"

        return result
