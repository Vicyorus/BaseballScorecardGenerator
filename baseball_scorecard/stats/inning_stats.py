class InningStats:

    def __init__(self):
        self.runs: int = 0
        self.hits: int = 0
        self.errors: int = 0
        self.left_on_base: int = 0
        self.walks: int = 0
        self.strikeouts: int = 0
        self.pitches: int = 0
        self.strikes: int = 0

    def get_metapost_data(self):
        result = (
            "    % inning stats\n"
            f"    set_inning_total_vars(xstart);\n"
            f"    label(btex {{\\bigsf {self.runs}}} etex, inn_run) withcolor clr;\n"
            f"    label(btex {{\\bigsf {self.hits}}} etex, inn_hit) withcolor clr;\n"
            f"    label(btex {{\\bigsf {self.errors}}} etex, inn_err) withcolor clr;\n"
            f"    label(btex {{\\bigsf {self.left_on_base}}} etex, inn_lob) withcolor clr;\n"
            f"    label(btex {{\\bigsf {self.walks}}} etex, inn_bb) withcolor clr;\n"
            f"    label(btex {{\\bigsf {self.strikeouts}}} etex, inn_so) withcolor clr;\n"
            f"    label(btex {{\\bigsf {self.pitches}}} etex, inn_pit) withcolor clr;\n"
            f"    label(btex {{\\bigsf {self.strikes}}} etex, inn_str) withcolor clr;\n\n"
        )

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

        if self.walks:
            result += f" {self.walks} BB"

        if self.strikeouts:
            result += f" {self.strikeouts} K"

        if self.pitches:
            result += f" {self.pitches} P"

        if self.strikes:
            result += f" {self.strikes} S"

        result += "\n"

        return result
