class WayBase:

    waybase_locations = {
        "0-1": {"location": "wayfirst", "reversed": True, "label_offset": ".lrt"},
        "0-2": {"location": "waysecond", "reversed": True, "label_offset": ".urt"},
        "0-3": {"location": "waythird", "reversed": True, "label_offset": ".ulft"},
        "0-4": {"location": "wayhome", "reversed": True, "label_offset": ".llft"},
        "0-U": {"location": "wayhome", "reversed": True, "label_offset": ".llft"},
        "1-1": {
            "location": "waysecond",
            "reversed": True,
            "number_offset": ".urt",
            "label_offset": ".urt",
        },
        "1-2": {
            "location": "waysecond",
            "reversed": True,
            "number_offset": ".urt",
            "label_offset": ".urt",
        },
        "1-3": {
            "location": "waythird",
            "reversed": True,
            "number_offset": ".ulft",
            "label_offset": ".ulft",
        },
        "1-4": {
            "location": "wayhome",
            "reversed": True,
            "number_offset": ".lft",
            "label_offset": ".llft",
        },
        "1-U": {
            "location": "wayhome",
            "reversed": True,
            "number_offset": ".lft",
            "label_offset": ".llft",
        },
        "2-2": {
            "location": "waythird",
            "reversed": True,
            "number_offset": ".ulft",
            "label_offset": ".ulft",
        },
        "2-3": {
            "location": "waythird",
            "reversed": True,
            "number_offset": ".ulft",
            "label_offset": ".ulft",
        },
        "2-4": {
            "location": "wayhome",
            "reversed": True,
            "number_offset": ".lft",
            "label_offset": ".llft",
        },
        "2-U": {
            "location": "wayhome",
            "reversed": True,
            "number_offset": ".lft",
            "label_offset": ".llft",
        },
        "3-3": {
            "location": "wayhome",
            "reversed": True,
            "number_offset": ".lft",
            "label_offset": ".llft",
        },
        "3-4": {
            "location": "wayhome",
            "reversed": True,
            "number_offset": ".lft",
            "label_offset": ".llft",
        },
        "3-U": {
            "location": "wayhome",
            "reversed": True,
            "number_offset": ".lft",
            "label_offset": ".llft",
        },
    }

    waybase_template = "    label{}(btex {{\\sf {}}} etex, {}) withcolor clr;\n"

    def __init__(self, label: str, start_base: int, end_base: int | str):
        split_label = label.split(" ")
        if len(split_label) == 2:
            self.number = label.split()[0]
            self.label = label.split()[1]
        else:
            self.label = label
            self.number = None

        self.start = start_base
        self.end = end_base

    def get_metapost_data(self):
        result = ""
        waybase_key = f"{self.start}-{self.end}"
        waybase_info = WayBase.waybase_locations[waybase_key]

        # If the start is 0 (batter), use only the label.
        if self.start == 0:
            # In case the end of this play is at home plate, add to the location the home plate offset.
            offset = ""
            if self.end in [4, "U"]:
                offset = "+(-1,-2)"

            result += WayBase.waybase_template.format(
                waybase_info["label_offset"],
                self.label,
                waybase_info["location"] + offset,
            )

        # Otherwise, set up the correct offsets for each label depending on the base reached (2nd, 3rd or home).
        elif self.end in [4, "U"] or (self.start == self.end == 3):
            label_offset = "+(-1,-2)"
            if self.number:
                label_offset = "+(-1,-5)"
                result += WayBase.waybase_template.format(
                    waybase_info["number_offset"],
                    self.number,
                    waybase_info["location"] + "+(-1,-2)",
                )
            result += WayBase.waybase_template.format(
                waybase_info["label_offset"],
                self.label,
                waybase_info["location"] + label_offset,
            )

        else:
            result += WayBase.waybase_template.format(
                waybase_info["label_offset"], self.label, waybase_info["location"]
            )
            if self.number:
                result += WayBase.waybase_template.format(
                    waybase_info["number_offset"],
                    self.number,
                    waybase_info["location"] + "+(0,10)",
                )

        return result
