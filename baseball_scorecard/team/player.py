from baseball_scorecard.stats.batter_stats import BatterStats
from baseball_scorecard.stats.pitcher_stats import PitcherStats


class Player:

    lineup_info_template = (
        "    label.urt(btex {{\\bigsf {}}} etex, ({},player_y)) withcolor clr;\n"
    )
    lineup_extras_info_template = (
        "    label.urt(btex {{\\bigsf {} ({})}} etex, ({},player_y)) withcolor clr;\n"
    )

    bench_info_template = "    label(btex {{\\bigsf {}}} etex, {}) withcolor clr;\n"
    pitcher_info_template = (
        "    label.urt(btex {{\\bigsf {}}} etex, {}) withcolor clr;\n"
    )

    def __init__(self, id: int, number: int, name: str, is_lefty: bool = False):
        self.id: int = id
        self.number: int = number
        self.name: str = name
        self.handedness: str = "L" if is_lefty else "R"
        self.defensive_position: list[str] = []
        self.primary_position: str = ""
        self.is_bullpen: bool = False
        self.in_lineup: bool = False
        self.inning_entered: int = 0

        self.batter_stats: BatterStats = BatterStats()
        self.pitcher_stats: PitcherStats = PitcherStats()

    def set_lineup_position(self, position: str, inning: int):
        self.in_lineup = True
        self.defensive_position = [position]
        self.inning_entered = inning

    def add_defensive_position(self, position: str):
        self.defensive_position.append(position)

    def set_primary_position(self, position: str):
        self.primary_position = position

    def set_as_bullpen(self):
        self.set_primary_position("P")
        self.is_bullpen = True

    def add_pitch(self, is_strike: bool = True):
        self.pitcher_stats.pitches += 1
        if is_strike:
            self.pitcher_stats.strikes += 1

    def add_decision(self, decision: str):
        self.pitcher_stats.add_decision(decision)

    def get_lineup_metapost_data(
        self,
        positon_idx: int,
        spot_idx: int,
        is_extra: bool = False,
        original_postion_idx: int = 0,
    ) -> str:
        result = f"    %% lineup {positon_idx}-{spot_idx}\n"
        result += f"    set_batter_name_vars({positon_idx}, {spot_idx});\n"
        if is_extra:
            result += f"    label(btex {{\\sf {original_postion_idx}}} etex, (-324,player_y+32-6)) withcolor clr;\n"
        result += Player.lineup_info_template.format(self.number, "number_x")

        if is_extra:
            result += Player.lineup_extras_info_template.format(
                self.name, self.inning_entered, "name_x"
            )
        else:
            result += Player.lineup_info_template.format(self.name, "name_x")
            result += Player.lineup_info_template.format(self.inning_entered, "inn_x")

        result += Player.lineup_info_template.format(
            "/".join(self.defensive_position), "pos_x"
        )
        result += "\n"
        return result

    def get_bench_metapost_data(self, idx: int) -> str:
        result = f"    %% bench #{idx}\n"
        result += f"    set_bench_name_vars({idx});\n"
        result += Player.bench_info_template.format(self.number, "bench_no")
        result += Player.bench_info_template.format(self.name, "bench_name")
        result += Player.bench_info_template.format(
            self.primary_position, "bench_extra"
        )
        if self.in_lineup:
            result += f"    strikethrough_bench_name({idx}, clr);\n"
        result += "\n"
        return result

    def get_bullpen_metapost_data(self, idx) -> str:
        result = f"    %% bullpen #{idx}\n"
        result += f"    set_bullpen_name_vars({idx});\n"
        result += Player.bench_info_template.format(self.number, "bullpen_no")
        result += Player.bench_info_template.format(self.name, "bullpen_name")
        result += Player.bench_info_template.format(self.handedness, "bullpen_extra")
        if self.in_lineup:
            result += f"    strikethrough_bullpen_name({idx}, clr);\n"
        result += "\n"
        return result

    def get_pitcher_metapost_data(self, idx) -> str:
        result = f"    %% pitcher #{idx}\n"
        result += f"    set_pitcher_name_vars({idx});\n"
        result += Player.pitcher_info_template.format(self.number, "pitcher_no")
        result += Player.pitcher_info_template.format(self.name, "pitcher_name")
        result += Player.pitcher_info_template.format(
            self.handedness, "pitcher_handedness"
        )
        result += Player.pitcher_info_template.format(
            self.inning_entered, "pitcher_inn"
        )
        result += "\n"
        return result

    def get_reserves_str(self) -> str:
        if self.in_lineup:
            return f"~~#{self.number} {self.name} ({self.primary_position})~~\n"
        else:
            return f"#{self.number} {self.name} ({self.primary_position})\n"

    def get_lineup_str(self) -> str:
        return f"{self.__codes_to_position(self.defensive_position)} {str(self)} ({self.inning_entered}) {str(self.batter_stats)}\n"

    def __codes_to_position(self, position_codes) -> str:
        codes = {
            "1": "P",
            "2": "C",
            "3": "1B",
            "4": "2B",
            "5": "3B",
            "6": "SS",
            "7": "LF",
            "8": "CF",
            "9": "RF",
            "0": "DH",
            "10": "DH",
            "PH": "PH",
            "PR": "PR",
        }

        positions = []
        for position_code in position_codes:
            positions.append(codes[position_code])

        return "/".join(positions)

    def get_pitcher_str(self) -> str:
        return f"{str(self)} ({self.inning_entered}) {str(self.pitcher_stats)}\n"

    def __str__(self):
        return f"#{self.number} {self.name}"
