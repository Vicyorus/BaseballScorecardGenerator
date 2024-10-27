#!/usr/bin/python3.10
import os
from baseball_scorecard.baseball_scorecard import Scorecard

# TEX @ BOS, 2024-08-12
# https://www.baseball-reference.com/boxes/BOS/BOS202408120.shtml
# https://www.mlb.com/gameday/rangers-vs-red-sox/2024/08/12/746921/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2024-08-12 19:12-22:46",
        "at": "Fenway Park, Boston, MA",
        "att": "35,715",
        "temp": "71F, Cloudy",
        "wind": "3mph, R To L",
        "away": {
            "team": "Texas Rangers",
            "starter": 51,
            "roster": {
                # Lineup
                2: "Marcus Semien",
                5: "Corey Seager",
                8: "Josh Smith",
                53: "Adolis García",
                30: "Nathaniel Lowe",
                6: "Josh Jung",
                36: "Wyatt Langford",
                28: "Jonah Heim",
                3: "Leody Taveras",
                # Starting pitcher
                51: "Tyler Mahle",
                # Bench
                18: "Carson Kelly",
                20: "Ezequiel Duran",
                16: "Travis Jankowski",
                4: "Robbie Grossman",
                # Bullpen
                33: "Dane Dunning",
                54: "José Ureña",
                59: "Andrew Chafin",
                63: "Matt Festa",
                58: "Gerson Garabito",
                44: "Andrew Heaney",
                52: "Walter Pennington",
                39: "Kirby Yates",
                61: "Cody Bradford",
                17: "Nathan Eovaldi",
                25: "José Leclerc",
                37: "David Robertson",
            },
            "lefties": [59, 44, 52, 61],
            "lineup": [
                [2, "4"],
                [5, "6"],
                [8, "5"],
                [53, "9"],
                [30, "3"],
                [6, "0"],
                [36, "7"],
                [28, "2"],
                [3, "8"],
            ],
            "bench": [
                [18, "C"],
                [20, "3B"],
                [16, "RF"],
                [4, "RF"],
            ],
            "bullpen": [33, 54, 59, 63, 58, 44, 52, 39, 61, 17, 25, 37],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 66,
            "roster": {
                # Lineup
                70: "David Hamilton",
                7: "Masataka Yoshida",
                30: "Rob Refsnyder",
                11: "Rafael Devers",
                12: "Connor Wong",
                52: "Wilyer Abreu",
                2: "Dominic Smith",
                75: "Nick Sogard",
                43: "Ceddanne Rafaela",
                # Starting pitcher
                66: "Brayan Bello",
                # Bench
                23: "Romy Gonzalez",
                77: "Mickey Gasper",
                28: "Danny Jansen",
                47: "Enmanuel Valdez",
                # Bullpen
                61: "Chase Shugart",
                76: "Zack Kelly",
                71: "Cam Booser",
                74: "Kenley Jansen",
                25: "Josh Winckowski",
                78: "Bailey Horn",
                50: "Kutter Crawford",
                37: "Nick Pivetta",
                39: "Lucas Sims",
                40: "Luis García",
                89: "Tanner Houck",
                55: "Chris Martin",
            },
            "lefties": [71, 78],
            "lineup": [
                [70, "6"],
                [7, "0"],
                [30, "7"],
                [11, "5"],
                [12, "2"],
                [52, "9"],
                [2, "3"],
                [75, "4"],
                [43, "8"],
            ],
            "bench": [
                [23, "1B"],
                [77, "C"],
                [28, "C"],
                [47, "2B"],
            ],
            "bullpen": [61, 76, 71, 74, 25, 78, 50, 37, 39, 40, 89, 55],
        },
        "umpires": {
            "HP": "Mike Estabrook",
            "1B": "Erich Bacchus",
            "2B": "Laz Diaz",
            "3B": "Tripp Gibson",
        },
    },
)

##########################################################
# PLAY BALL!
##########################################################


##########################################################
# 1st Inning
##########################################################
# Top 1st
# Pitching: BOS #66 Brayan Bello
t1 = game.new_inning()

# 1. TEX #2  Marcus Semien (X - X - X)
t1.new_ab()
t1.out("F4")

# 2. TEX #5  Corey Seager (X - X - X)
t1.new_ab()
t1.pitch_list("s")
t1.hit(1)
t1.advance(2, "8 BB")
t1.advance(3, "53 FC6-4")
t1.thrown_out(4, "30 CS", 3, 66)

# 3. TEX #8  Josh Smith (X - X - 5)
t1.new_ab()
t1.pitch_list("b f f b b b")
t1.reach("BB")
t1.thrown_out(2, "53 FC6-4", 2, 66)

# 4. TEX #53 Adolis García (X - 5 - 8)
t1.new_ab(is_risp=True)
t1.pitch_list("s")
t1.reach("FC6-4")

# 5. TEX #30 Nathaniel Lowe (5 - X - 53)
t1.new_ab(is_risp=True)
t1.pitch_list("b b b")
t1.no_ab("CS")


# Bot 1st
# Pitching: TEX #51 Tyler Mahle
b1 = game.new_inning()

# 1. BOS #70 David Hamilton (X - X - X)
b1.new_ab()
b1.pitch_list("b")
b1.out("F9")

# 2. BOS #7  Masataka Yoshida (X - X - X)
b1.new_ab()
b1.pitch_list("c b c")
b1.out("F7")

# 3. BOS #30 Rob Refsnyder (X - X - X)
b1.new_ab()
b1.pitch_list("b s s b b b")
b1.reach("BB")

# 4. BOS #11 Rafael Devers (X - X - 30)
b1.new_ab()
b1.pitch_list("s s b s")
b1.out("K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #66 Brayan Bello
t2 = game.new_inning()

# 5. TEX #30 Nathaniel Lowe (X - X - X)
t2.new_ab()
t2.out("L7")

# 6. TEX #6  Josh Jung (X - X - X)
t2.new_ab()
t2.pitch_list("b c f b b c")
t2.out("!K")

# 7. TEX #36 Wyatt Langford (X - X - X)
t2.new_ab()
t2.pitch_list("b c f")
t2.out("G5-3")


# Bot 2nd
# Pitching: TEX #51 Tyler Mahle
b2 = game.new_inning()

# 5. BOS #12 Connor Wong (X - X - X)
b2.new_ab()
b2.pitch_list("c")
b2.out("F9")

# 6. BOS #52 Wilyer Abreu (X - X - X)
b2.new_ab()
b2.pitch_list("c f f f s")
b2.out("K")

# 7. BOS #2  Dominic Smith (X - X - X)
b2.new_ab()
b2.pitch_list("c f b")
b2.hit(1)

# 8. BOS #75 Nick Sogard (X - X - 2)
b2.new_ab()
b2.pitch_list("b f f s")
b2.out("K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #66 Brayan Bello
t3 = game.new_inning()

# 8. TEX #28 Jonah Heim (X - X - X)
t3.new_ab()
t3.pitch_list("c")
t3.reach("HBP")
t3.advance(2, "3 1B")
t3.thrown_out(3, "2 FC5", 1, 66)

# 9. TEX #3  Leody Taveras (X - X - 28)
t3.new_ab()
t3.pitch_list("b")
t3.hit(1)
t3.advance(2, "2 FC5")
t3.advance(3, "5 FC3-6")

# 1. TEX #2  Marcus Semien (X - 28 - 3)
t3.new_ab(is_risp=True)
t3.pitch_list("c")
t3.reach("FC5")
t3.thrown_out(2, "5 FC3-6", 2, 66)

# 2. TEX #5  Corey Seager (X - 3 - 2)
t3.new_ab(is_risp=True)
t3.reach("FC3-6")

# 3. TEX #8  Josh Smith (3 - X - 5)
t3.new_ab(is_risp=True)
t3.pitch_list("f")
t3.out("G3")


# Bot 3rd
# Pitching: TEX #51 Tyler Mahle
b3 = game.new_inning()

# 9. BOS #43 Ceddanne Rafaela (X - X - X)
b3.new_ab()
b3.pitch_list("s b s")
b3.reach("HBP")
b3.advance(2, "70 SB")
b3.advance(3, "7 G6-3")

# 1. BOS #70 David Hamilton (X - X - 43)
b3.new_ab()
b3.pitch_list("d c f f 1 f f b b 1 t")
b3.out("KT")

# 2. BOS #7  Masataka Yoshida (X - 43 - X)
b3.new_ab(is_risp=True)
b3.out("G6-3")

# 3. BOS #30 Rob Refsnyder (43 - X - X)
b3.new_ab(is_risp=True)
b3.pitch_list("c b")
b3.out("F9")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #66 Brayan Bello
t4 = game.new_inning()

# 4. TEX #53 Adolis García (X - X - X)
t4.new_ab()
t4.pitch_list("b c c b s")
t4.out("K")

# 5. TEX #30 Nathaniel Lowe (X - X - X)
t4.new_ab()
t4.pitch_list("c b")
t4.out("L8")

# 6. TEX #6  Josh Jung (X - X - X)
t4.new_ab()
t4.pitch_list("c s")
t4.hit(1)

# 7. TEX #36 Wyatt Langford (X - X - 6)
t4.new_ab()
t4.pitch_list("c c b")
t4.out("G6-3")


# Bot 4th
# Pitching: TEX #51 Tyler Mahle
b4 = game.new_inning()

# 4. BOS #11 Rafael Devers (X - X - X)
b4.new_ab()
b4.pitch_list("b f f s")
b4.out("K")

# 5. BOS #12 Connor Wong (X - X - X)
b4.new_ab()
b4.hit(1)
b4.advance(3, "52 1B")
b4.advance(4, "75 SF9")

# 6. BOS #52 Wilyer Abreu (X - X - 12)
b4.new_ab()
b4.pitch_list("b s 1 f f")
b4.hit(1)
b4.advance(2, "2 BB")

# 7. BOS #2  Dominic Smith (12 - X - 52)
b4.new_ab(is_risp=True)
b4.pitch_list("b c b b b")
b4.reach("BB")

# 8. BOS #75 Nick Sogard (12 - 52 - 2)
b4.new_ab(is_risp=True)
b4.pitch_list("f f b f")
b4.out("SF9", rbis=1)

# 9. BOS #43 Ceddanne Rafaela (X - 52 - 2)
b4.new_ab(is_risp=True)
b4.pitch_list("b pso c b c")
b4.out("L4")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #66 Brayan Bello
t5 = game.new_inning()

# 8. TEX #28 Jonah Heim (X - X - X)
t5.new_ab()
t5.pitch_list("c b c f f t")
t5.out("KT")

# 9. TEX #3  Leody Taveras (X - X - X)
t5.new_ab()
t5.pitch_list("s b b b b")
t5.reach("BB")
t5.advance(2, "2 SB")
t5.advance(4, "2 1B")

# 1. TEX #2  Marcus Semien (X - X - 3)
t5.new_ab(is_risp=True)
t5.pitch_list("c b b b")
t5.hit(1, rbis=1)
t5.advance(2, "5 BB")
t5.advance(3, "8 F8")

# 2. TEX #5  Corey Seager (X - X - 2)
t5.new_ab()
t5.pitch_list("b s f b pso f b b")
t5.reach("BB")

# 3. TEX #8  Josh Smith (X - 2 - 5)
t5.new_ab(is_risp=True)
t5.pitch_list("c d f f d")
t5.out("F8")

# 4. TEX #53 Adolis García (2 - X - 5)
t5.new_ab(is_risp=True)
t5.pitch_list("f c b f b s")
t5.out("K")


# Bot 5th
# Pitching: TEX #51 Tyler Mahle
b5 = game.new_inning()

# 1. BOS #70 David Hamilton (X - X - X)
b5.new_ab()
b5.pitch_list("c b s f b f b b")
b5.reach("BB")
b5.advance(2, "7 SB")
b5.advance(3, "12 WP")
b5.advance(4, "23 BB")

# 2. BOS #7  Masataka Yoshida (X - X - 70)
b5.new_ab(is_risp=True)
b5.pitch_list("b 1 c b f f b c")
b5.out("!K")

# 3. BOS #30 Rob Refsnyder (X - 70 - X)
b5.new_ab(is_risp=True)
b5.pitch_list("b s s c")
b5.out("!K")

# Pitching change (TEX): #59 Andrew Chafin replaces #51 Tyler Mahle
b5.pitching_substitution(59)

# 4. BOS #11 Rafael Devers (X - 70 - X)
b5.new_ab(is_risp=True)
b5.pitch_list("b b b vb")
b5.reach("IBB")
b5.advance(2, "12 WP")
b5.advance(3, "23 BB")
b5.advance(4, "28 BB")

# 5. BOS #12 Connor Wong (X - 70 - 11)
b5.new_ab(is_risp=True)
b5.pitch_list("b vb vb vb")
b5.wp()
b5.reach("IBB")
b5.advance(2, "23 BB")
b5.advance(3, "28 BB")

# Offensive change (BOS): Pinch-hitter #23 Romy Gonzalez replaces #52 Wilyer Abreu, batting 6th
b5.offensive_substitution(6, 23, "PH")

# 6. BOS #23 Romy Gonzalez (70 - 11 - 12)
b5.new_ab(is_risp=True)
b5.pitch_list("b b b t b")
b5.reach("BB", rbis=1)
b5.advance(2, "28 BB")

# Offensive change (BOS): Pinch-hitter #28 Danny Jansen replaces #2 Dominic Smith, batting 7th
b5.offensive_substitution(7, 28, "PH")

# 7. BOS #28 Danny Jansen (11 - 12 - 23)
b5.new_ab(is_risp=True)
b5.pitch_list("s f d d d f d")
b5.reach("BB", rbis=1)

# Pitching change (TEX): #63 Matt Festa replaces #59 Andrew Chafin
b5.pitching_substitution(63)

# 8. BOS #75 Nick Sogard (12 - 23 - 28)
b5.new_ab(is_risp=True)
b5.pitch_list("f f f s")
b5.out("K")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #66 Brayan Bello
t6 = game.new_inning()

# Defensive switch (BOS): #12 Connor Wong moves to 1B
t6.defensive_switch(12, "3")

# Defensive switch (BOS): #23 Romy Gonzalez moves to RF
t6.defensive_switch(23, "9")

# Defensive switch (BOS): #28 Danny Jansen moves to C
t6.defensive_switch(28, "2")

# 5. TEX #30 Nathaniel Lowe (X - X - X)
t6.new_ab()
t6.out("G5-3")

# 6. TEX #6  Josh Jung (X - X - X)
t6.new_ab()
t6.pitch_list("c b s s")
t6.out("K")

# 7. TEX #36 Wyatt Langford (X - X - X)
t6.new_ab()
t6.pitch_list("c b b f b")
t6.out("G4-3")


# Bot 6th
# Pitching: TEX #63 Matt Festa
b6 = game.new_inning()

# 9. BOS #43 Ceddanne Rafaela (X - X - X)
b6.new_ab()
b6.pitch_list("s")
b6.out("G4-3")

# 1. BOS #70 David Hamilton (X - X - X)
b6.new_ab()
b6.pitch_list("b")
b6.out("F7")

# 2. BOS #7  Masataka Yoshida (X - X - X)
b6.new_ab()
b6.pitch_list("c f f b f t")
b6.out("KT")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #76 Zack Kelly
t7 = game.new_inning()

# Pitching change (BOS): #76 Zack Kelly replaces #66 Brayan Bello
t7.pitching_substitution(76)

# 8. TEX #28 Jonah Heim (X - X - X)
t7.new_ab()
t7.pitch_list("b f f b b b")
t7.reach("BB")
t7.advance(2, "2 G1-3")
t7.advance(4, "5 HR")

# 9. TEX #3  Leody Taveras (X - X - 28)
t7.new_ab()
t7.pitch_list("c b b f c")
t7.out("!K")

# 1. TEX #2  Marcus Semien (X - X - 28)
t7.new_ab()
t7.pitch_list("f b f b")
t7.out("G1-3")

# Pitching change (BOS): #78 Bailey Horn replaces #76 Zack Kelly
t7.pitching_substitution(78)

# 2. TEX #5  Corey Seager (X - 28 - X)
t7.new_ab(is_risp=True)
t7.hit(4, rbis=2)

# 3. TEX #8  Josh Smith (X - X - X)
t7.new_ab()
t7.out("L6")


# Bot 7th
# Pitching: TEX #37 David Robertson
b7 = game.new_inning()

# Pitching change (TEX): #37 David Robertson replaces #63 Matt Festa
b7.pitching_substitution(37)

# 3. BOS #30 Rob Refsnyder (X - X - X)
b7.new_ab()
b7.pitch_list("c s b")
b7.hit(1)

# 4. BOS #11 Rafael Devers (X - X - 30)
b7.new_ab()
b7.pitch_list("f s b s")
b7.out("K")

# 5. BOS #12 Connor Wong (X - X - 30)
b7.new_ab()
b7.pitch_list("t f b c")
b7.out("!K")

# 6. BOS #23 Romy Gonzalez (X - X - 30)
b7.new_ab()
b7.pitch_list("f f b f b s")
b7.out("K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #55 Chris Martin
t8 = game.new_inning()

# Pitching change (BOS): #55 Chris Martin replaces #78 Bailey Horn
t8.pitching_substitution(55)

# 4. TEX #53 Adolis García (X - X - X)
t8.new_ab()
t8.pitch_list("f f")
t8.hit(1)

# 5. TEX #30 Nathaniel Lowe (X - X - 53)
t8.new_ab()
t8.pitch_list("b")
t8.out("P5")

# 6. TEX #6  Josh Jung (X - X - 53)
t8.new_ab()
t8.pitch_list("b f f c")
t8.out("!K")

# 7. TEX #36 Wyatt Langford (X - X - 53)
t8.new_ab()
t8.pitch_list("b f f c")
t8.out("!K")


# Bot 8th
# Pitching: TEX #37 David Robertson
b8 = game.new_inning()

# 7. BOS #28 Danny Jansen (X - X - X)
b8.new_ab()
b8.pitch_list("b c b c b")
b8.out("L8")

# 8. BOS #75 Nick Sogard (X - X - X)
b8.new_ab()
b8.pitch_list("s t b f b")
b8.hit(1)
b8.advance(2, "43 1B")
b8.advance(3, "7 BB")

# 9. BOS #43 Ceddanne Rafaela (X - X - 75)
b8.new_ab()
b8.pitch_list("s b b s")
b8.hit(1)
b8.advance(2, "7 BB")

# Pitching change (TEX): #39 Kirby Yates replaces #37 David Robertson
b8.pitching_substitution(39)

# 1. BOS #70 David Hamilton (X - 75 - 43)
b8.new_ab(is_risp=True)
b8.pitch_list("f f s")
b8.out("K")

# 2. BOS #7  Masataka Yoshida (X - 75 - 43)
b8.new_ab(is_risp=True)
b8.pitch_list("b f d b pso s f b")
b8.reach("BB")

# 3. BOS #30 Rob Refsnyder (75 - 43 - 7)
b8.new_ab(is_risp=True)
b8.pitch_list("d b c c s")
b8.out("K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #74 Kenley Jansen
t9 = game.new_inning()

# Pitching change (BOS): #74 Kenley Jansen replaces #55 Chris Martin
t9.pitching_substitution(74)

# 8. TEX #28 Jonah Heim (X - X - X)
t9.new_ab()
t9.pitch_list("b b c f b s")
t9.out("K")

# 9. TEX #3  Leody Taveras (X - X - X)
t9.new_ab()
t9.pitch_list("f")
t9.out("F8")

# 1. TEX #2  Marcus Semien (X - X - X)
t9.new_ab()
t9.pitch_list("b f b s f")
t9.out("F8")


# Bot 9th
# Pitching: TEX #39 Kirby Yates
b9 = game.new_inning()

# 4. BOS #11 Rafael Devers (X - X - X)
b9.new_ab()
b9.pitch_list("s")
b9.out("F7")

# 5. BOS #12 Connor Wong (X - X - X)
b9.new_ab()
b9.pitch_list("f b s s")
b9.out("K")

# 6. BOS #23 Romy Gonzalez (X - X - X)
b9.new_ab()
b9.pitch_list("s b f")
b9.out("G6-3")


##########################################################
# 10th Inning
##########################################################
# Top 10th
# Pitching: BOS #25 Josh Winckowski
t10 = game.new_inning()

# Pitching change (BOS): #25 Josh Winckowski replaces #74 Kenley Jansen
t10.pitching_substitution(25)

# Runner placed on base: TEX #2 Marcus Semien
t10.place_runner()
t10.advance(3, "5 G4-3")
t10.advance("U", "8 G6-3")

# 2. TEX #5  Corey Seager (X - 2 - X)
t10.new_ab(is_risp=True)
t10.pitch_list("b")
t10.out("G4-3")

# 3. TEX #8  Josh Smith (2 - X - X)
t10.new_ab(is_risp=True)
t10.pitch_list("s f f f")
t10.out("G6-3", rbis=1)

# 4. TEX #53 Adolis García (X - X - X)
t10.new_ab()
t10.pitch_list("s b f")
t10.out("G6-3")


# Bot 10th
# Pitching: TEX #58 Gerson Garabito
b10 = game.new_inning()

# Pitching change (TEX): #58 Gerson Garabito replaces #39 Kirby Yates
b10.pitching_substitution(58)

# Runner placed on base: BOS #23 Romy Gonzalez
b10.place_runner(player_id=23, base=2, label="GR")  # GR for ghost runner.
b10.advance("U", "47 2B")

# Offensive change (BOS): Pinch-hitter #47 Enmanuel Valdez replaces #28 Danny Jansen, batting 7th
b10.offensive_substitution(7, 47, "PH")

# 7. BOS #47 Enmanuel Valdez (X - 23 - X)
b10.new_ab(is_risp=True)
b10.pitch_list("c f b f d")
b10.hit(2, rbis=1)
b10.advance(3, "75 1B")
b10.thrown_out(4, "7 FC4-2", 2, 52)

# 8. BOS #75 Nick Sogard (X - 47 - X)
b10.new_ab(is_risp=True)
b10.pitch_list("b b b c")
b10.hit(1)
b10.thrown_out(2, "43 FC4-6", 1, 58)

# 9. BOS #43 Ceddanne Rafaela (47 - X - 75)
b10.new_ab(is_risp=True)
b10.reach("FC4-6")
b10.advance(2, "77 DI")
b10.advance(3, "7 FC4-2")
b10.advance(4, "30 1B")

# Pitching change (TEX): #52 Walter Pennington replaces #58 Gerson Garabito
b10.pitching_substitution(52)

# Offensive change (BOS): Pinch-hitter #77 Mickey Gasper replaces #70 David Hamilton, batting 1st
b10.offensive_substitution(1, 77, "PH")

# 1. BOS #77 Mickey Gasper (47 - X - 43)
b10.new_ab(is_risp=True)
b10.pitch_list("b f c d b f b")
b10.reach("BB")
b10.advance(2, "7 FC4-2")
b10.advance(3, "30 1B")

# 2. BOS #7  Masataka Yoshida (47 - 43 - 77)
b10.new_ab(is_risp=True)
b10.reach("FC4-2")
b10.advance(2, "30 1B")

# 3. BOS #30 Rob Refsnyder (43 - 77 - 7)
b10.new_ab(is_risp=True)
b10.pitch_list("b b")
b10.hit(1, rbis=1)

# Winning team: BOS
# WP: BOS #25 Josh Winckowski
game.winning_pitcher(25)

# Loser team: TEX
# LP: TEX #58 Gerson Garabito
game.losing_pitcher(58, is_away_team=True)

# print(game)
game.generate_scorecard()
