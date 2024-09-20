import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ MIA, 2018-04-03
# https://www.baseball-reference.com/boxes/MIA/MIA201804030.shtml
# https://www.mlb.com/gameday/red-sox-vs-marlins/2018/04/03/529472/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-04-03 18:10-22:37",
        "at": "Marlins Park, Miami, FL",
        "att": "14,953",
        "temp": "77F, Partly Cloudy",
        "wind": "10mph, In From CF",
        "away": {
            "team": "Boston Red Sox",
            "starter": 41,
            "roster": {
                # Lineup
                36: "Eduardo Núñez",
                16: "Andrew Benintendi",
                13: "Hanley Ramirez",
                28: "J.D. Martinez",
                2: "Xander Bogaerts",
                11: "Rafael Devers",
                7: "Christian Vázquez",
                19: "Jackie Bradley Jr.",
                41: "Chris Sale",
                # Starting pitcher
                41: "Chris Sale",
                # Bench
                18: "Mitch Moreland",
                12: "Brock Holt",
                23: "Blake Swihart",
                50: "Mookie Betts",
                3: "Sandy León",
                # Bullpen
                39: "Carson Smith",
                22: "Rick Porcello",
                61: "Brian Johnson",
                66: "Bobby Poyner",
                37: "Heath Hembree",
                24: "David Price",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                64: "Marcus Walden",
                56: "Joe Kelly",
                32: "Matt Barnes",
            },
            "lefties": [41, 61, 66, 24],
            "lineup": [
                [36, "4"],
                [16, "7"],
                [13, "3"],
                [28, "9"],
                [2, "6"],
                [11, "5"],
                [7, "2"],
                [19, "8"],
                [41, "1"],
            ],
            "bench": [
                [18, "1B"],
                [12, "2B"],
                [23, "C"],
                [50, "SS"],
                [3, "C"],
            ],
            "bullpen": [39, 22, 61, 66, 37, 24, 46, 76, 64, 56, 32],
        },
        "home": {
            "team": "Miami Marlins",
            "starter": 62,
            "roster": {
                # Lineup
                9: "Lewis Brinson",
                32: "Derek Dietrich",
                13: "Starlin Castro",
                15: "Brian Anderson",
                41: "Justin Bour",
                1: "Cameron Maybin",
                19: "Miguel Rojas",
                17: "Chad Wallach",
                62: "José Ureña",
                # Starting pitcher
                62: "José Ureña",
                # Bench
                30: "Garrett Cooper",
                28: "Bryan Holaday",
                18: "Tomás Telis",
                2: "Yadiel Rivera",
                # Bullpen
                56: "Tayron Guerrero",
                44: "Jacob Turner",
                46: "Kyle Barraclough",
                66: "Jarlín García",
                76: "Dillon Peters",
                25: "Junichi Tazawa",
                63: "Trevor Richards",
                50: "Chris O'Grady",
                43: "Odrisamer Despaigne",
                29: "Brad Ziegler",
                31: "Caleb Smith",
                71: "Drew Steckenrider",
            },
            "lefties": [66, 76, 50, 31],
            "lineup": [
                [9, "8"],
                [32, "7"],
                [13, "4"],
                [15, "5"],
                [41, "3"],
                [1, "9"],
                [19, "6"],
                [17, "2"],
                [62, "1"],
            ],
            "bench": [
                [30, "1B"],
                [28, "C"],
                [18, "C"],
                [2, "3B"],
            ],
            "bullpen": [56, 44, 46, 66, 76, 25, 63, 50, 43, 29, 31, 71],
        },
        "umpires": {
            "HP": "Ben May",
            "1B": "Ron Kulpa",
            "2B": "Ed Hickox",
            "3B": "Jerry Meals",
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
# Pitching: MIA #62 José Ureña
t1 = game.new_inning()

# 1. BOS #36 Eduardo Núñez (X - X - X)
t1.new_ab()
t1.pitch_list("b b")
t1.out("P3")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t1.new_ab()
t1.pitch_list("b f b b b")
t1.reach("BB")
t1.advance(2, "13 SB")
t1.advance(4, "28 1B")

# 3. BOS #13 Hanley Ramirez (X - X - 16)
t1.new_ab()
t1.pitch_list("b c f b f")
t1.out("F7")

# 4. BOS #28 J.D. Martinez (X - 16 - X)
t1.new_ab()
t1.pitch_list("b b d")
t1.hit(1, rbis=1)

# 5. BOS #2  Xander Bogaerts (X - X - 28)
t1.new_ab()
t1.pitch_list("b c s b f f b s")
t1.out("K")


# Bot 1st
# Pitching: BOS #41 Chris Sale
b1 = game.new_inning()

# 1. MIA #9  Lewis Brinson (X - X - X)
b1.new_ab()
b1.pitch_list("c b s f")
b1.out("G1-3")

# 2. MIA #32 Derek Dietrich (X - X - X)
b1.new_ab()
b1.pitch_list("s b s b c")
b1.out("!K")

# 3. MIA #13 Starlin Castro (X - X - X)
b1.new_ab()
b1.pitch_list("b b c c f b f f f f")
b1.hit(1)

# 4. MIA #15 Brian Anderson (X - X - 13)
b1.new_ab()
b1.pitch_list("d c b s b c")
b1.out("!K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: MIA #62 José Ureña
t2 = game.new_inning()

# 6. BOS #11 Rafael Devers (X - X - X)
t2.new_ab()
t2.pitch_list("c c b b")
t2.out("G4-3")

# 7. BOS #7  Christian Vázquez (X - X - X)
t2.new_ab()
t2.pitch_list("c b f b")
t2.out("G6-3")

# 8. BOS #19 Jackie Bradley Jr. (X - X - X)
t2.new_ab()
t2.pitch_list("c")
t2.out("G4-3")


# Bot 2nd
# Pitching: BOS #41 Chris Sale
b2 = game.new_inning()

# 5. MIA #41 Justin Bour (X - X - X)
b2.new_ab()
b2.pitch_list("s s")
b2.out("L8")

# 6. MIA #1  Cameron Maybin (X - X - X)
b2.new_ab()
b2.pitch_list("c s b b b")
b2.hit(1)
b2.thrown_out(1, "19 DP9-3", 3, 41)

# 7. MIA #19 Miguel Rojas (X - X - 1)
b2.new_ab()
b2.pitch_list("b b f 1 b f f")
b2.out("DP9-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: MIA #62 José Ureña
t3 = game.new_inning()

# 9. BOS #41 Chris Sale (X - X - X)
t3.new_ab()
t3.pitch_list("s f f c")
t3.out("!K")

# 1. BOS #36 Eduardo Núñez (X - X - X)
t3.new_ab()
t3.pitch_list("s")
t3.out("P4")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t3.new_ab()
t3.pitch_list("b f t c")
t3.out("!K")


# Bot 3rd
# Pitching: BOS #41 Chris Sale
b3 = game.new_inning()

# 8. MIA #17 Chad Wallach (X - X - X)
b3.new_ab()
b3.pitch_list("b b s c f")
b3.out("F9")

# 9. MIA #62 José Ureña (X - X - X)
b3.new_ab()
b3.pitch_list("c m b f s")
b3.out("K")

# 1. MIA #9  Lewis Brinson (X - X - X)
b3.new_ab()
b3.pitch_list("s s s")
b3.out("K")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: MIA #62 José Ureña
t4 = game.new_inning()

# 3. BOS #13 Hanley Ramirez (X - X - X)
t4.new_ab()
t4.pitch_list("c f f b")
t4.out("F9")

# 4. BOS #28 J.D. Martinez (X - X - X)
t4.new_ab()
t4.pitch_list("c b f b b c")
t4.out("!K")

# 5. BOS #2  Xander Bogaerts (X - X - X)
t4.new_ab()
t4.pitch_list("c c s")
t4.out("K")


# Bot 4th
# Pitching: BOS #41 Chris Sale
b4 = game.new_inning()

# 2. MIA #32 Derek Dietrich (X - X - X)
b4.new_ab()
b4.pitch_list("b b s")
b4.hit(1)
b4.thrown_out(2, "13 DP6-4-3", 1, 41)

# 3. MIA #13 Starlin Castro (X - X - 32)
b4.new_ab()
b4.pitch_list("b c b b")
b4.out("DP6-4-3")

# 4. MIA #15 Brian Anderson (X - X - X)
b4.new_ab()
b4.pitch_list("s s")
b4.hit(1)
b4.advance(4, "41 2B")

# 5. MIA #41 Justin Bour (X - X - 15)
b4.new_ab()
b4.pitch_list("b c s")
b4.hit(2, rbis=1)

# 6. MIA #1  Cameron Maybin (X - 41 - X)
b4.new_ab()
b4.pitch_list("c c b b s")
b4.out("K")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: MIA #62 José Ureña
t5 = game.new_inning()

# 6. BOS #11 Rafael Devers (X - X - X)
t5.new_ab()
t5.pitch_list("c b f f b f f")
t5.hit(2)
t5.thrown_out(3, "7 FC1-5", 1, 62)

# 7. BOS #7  Christian Vázquez (X - 11 - X)
t5.new_ab()
t5.reach("FC1-5")

# 8. BOS #19 Jackie Bradley Jr. (X - X - 7)
t5.new_ab()
t5.pitch_list("c d 1 s f s")
t5.out("K")

# 9. BOS #41 Chris Sale (X - X - 7)
t5.new_ab()
t5.pitch_list("s b f s")
t5.out("K")


# Bot 5th
# Pitching: BOS #41 Chris Sale
b5 = game.new_inning()

# 7. MIA #19 Miguel Rojas (X - X - X)
b5.new_ab()
b5.pitch_list("b b c b")
b5.out("(F)P5")

# 8. MIA #17 Chad Wallach (X - X - X)
b5.new_ab()
b5.pitch_list("c c f f b c")
b5.out("!K")

# 9. MIA #62 José Ureña (X - X - X)
b5.new_ab()
b5.pitch_list("c b s")
b5.out("B2-3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: MIA #62 José Ureña
t6 = game.new_inning()

# 1. BOS #36 Eduardo Núñez (X - X - X)
t6.new_ab()
t6.pitch_list("c b")
t6.out("F9")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t6.new_ab()
t6.pitch_list("c b b f b")
t6.hit(1)
t6.advance(2, "13 1B")

# 3. BOS #13 Hanley Ramirez (X - X - 16)
t6.new_ab()
t6.pitch_list("1 1")
t6.hit(1)
t6.thrown_out(2, "28 DP6-4-3", 2, 62)

# 4. BOS #28 J.D. Martinez (X - 16 - 13)
t6.new_ab()
t6.pitch_list("s b b f f")
t6.out("DP6-4-3")


# Bot 6th
# Pitching: BOS #66 Bobby Poyner
b6 = game.new_inning()

# Pitching change (BOS): #66 Bobby Poyner replaces #41 Chris Sale, batting 9th
b6.pitching_substitution(66)
b6.defensive_substitution(9, 66, "1")

# 1. MIA #9  Lewis Brinson (X - X - X)
b6.new_ab()
b6.pitch_list("c f b f b c")
b6.out("!K")

# 2. MIA #32 Derek Dietrich (X - X - X)
b6.new_ab()
b6.pitch_list("b b c f s")
b6.out("K")

# 3. MIA #13 Starlin Castro (X - X - X)
b6.new_ab()
b6.pitch_list("b b c s f b f f")
b6.out("G6-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: MIA #62 José Ureña
t7 = game.new_inning()

# 5. BOS #2  Xander Bogaerts (X - X - X)
t7.new_ab()
t7.pitch_list("f")
t7.out("G6-3")

# 6. BOS #11 Rafael Devers (X - X - X)
t7.new_ab()
t7.pitch_list("f f b b")
t7.out("G6-3")

# 7. BOS #7  Christian Vázquez (X - X - X)
t7.new_ab()
t7.pitch_list("b c b f f")
t7.out("G5-3")


# Bot 7th
# Pitching: BOS #66 Bobby Poyner
b7 = game.new_inning()

# 4. MIA #15 Brian Anderson (X - X - X)
b7.new_ab()
b7.pitch_list("b f b f")
b7.out("F7")

# 5. MIA #41 Justin Bour (X - X - X)
b7.new_ab()
b7.pitch_list("c c s")
b7.out("K")

# 6. MIA #1  Cameron Maybin (X - X - X)
b7.new_ab()
b7.pitch_list("c b")
b7.hit(1)
b7.advance(2, "19 SB")

# Pitching change (BOS): #39 Carson Smith replaces #66 Bobby Poyner, batting 9th
b7.pitching_substitution(39)
b7.defensive_substitution(9, 39, "1")

# 7. MIA #19 Miguel Rojas (X - X - 1)
b7.new_ab()
b7.pitch_list("1 1 c 1 b c f s")
b7.out("K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: MIA #71 Drew Steckenrider
t8 = game.new_inning()

# Pitching change (MIA): #71 Drew Steckenrider replaces #62 José Ureña, batting 9th
t8.pitching_substitution(71)
t8.defensive_substitution(9, 71, "1")

# 8. BOS #19 Jackie Bradley Jr. (X - X - X)
t8.new_ab()
t8.pitch_list("f b b")
t8.hit(2)
t8.advance(3, "18 F8")
t8.thrown_out(4, "36 FC4-2", 2, 71)

# Offensive change (BOS): Pinch-hitter #18 Mitch Moreland replaces #39 Carson Smith, batting 9th
t8.offensive_substitution(9, 18, "PH")

# 9. BOS #18 Mitch Moreland (X - 19 - X)
t8.new_ab()
t8.pitch_list("b b f 2 f b")
t8.out("F8")

# 1. BOS #36 Eduardo Núñez (19 - X - X)
t8.new_ab()
t8.reach("FC4-2")
t8.thrown_out(2, "16 CS", 3, 71)

# 2. BOS #16 Andrew Benintendi (X - X - 36)
t8.new_ab()
t8.pitch_list("1 b 1 c c")
t8.no_ab("CS")


# Bot 8th
# Pitching: BOS #56 Joe Kelly
b8 = game.new_inning()

# Pitching change (BOS): #56 Joe Kelly replaces #39 Carson Smith, batting 9th
b8.pitching_substitution(56)
b8.defensive_substitution(9, 56, "1")

# 8. MIA #17 Chad Wallach (X - X - X)
b8.new_ab()
b8.pitch_list("b c")
b8.out("G6-3")

# Offensive change (MIA): Pinch-hitter #18 Tomás Telis replaces #71 Drew Steckenrider, batting 9th
b8.offensive_substitution(9, 18, "PH")

# 9. MIA #18 Tomás Telis (X - X - X)
b8.new_ab()
b8.pitch_list("b f c f b f f s")
b8.out("K")

# 1. MIA #9  Lewis Brinson (X - X - X)
b8.new_ab()
b8.pitch_list("c c")
b8.out("L5")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: MIA #46 Kyle Barraclough
t9 = game.new_inning()

# Pitching change (MIA): #46 Kyle Barraclough replaces #71 Drew Steckenrider, batting 9th
t9.pitching_substitution(46)
t9.defensive_substitution(9, 46, "1")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t9.new_ab()
t9.pitch_list("c")
t9.out("G1-3")

# 3. BOS #13 Hanley Ramirez (X - X - X)
t9.new_ab()
t9.pitch_list("b f b b c s")
t9.out("K")

# 4. BOS #28 J.D. Martinez (X - X - X)
t9.new_ab()
t9.pitch_list("b f")
t9.out("G3-1")


# Bot 9th
# Pitching: BOS #56 Joe Kelly
b9 = game.new_inning()

# 2. MIA #32 Derek Dietrich (X - X - X)
b9.new_ab()
b9.out("(F)P5")

# 3. MIA #13 Starlin Castro (X - X - X)
b9.new_ab()
b9.pitch_list("f b")
b9.out("F9")

# 4. MIA #15 Brian Anderson (X - X - X)
b9.new_ab()
b9.pitch_list("b b c b f b")
b9.reach("BB")

# 5. MIA #41 Justin Bour (X - X - 15)
b9.new_ab()
b9.pitch_list("b c b c")
b9.out("L6")


##########################################################
# 10th Inning
##########################################################
# Top 10th
# Pitching: MIA #29 Brad Ziegler
t10 = game.new_inning()

# Pitching change (MIA): #29 Brad Ziegler replaces #46 Kyle Barraclough, batting 9th
t10.pitching_substitution(29)
t10.defensive_substitution(9, 29, "1")

# 5. BOS #2  Xander Bogaerts (X - X - X)
t10.new_ab()
t10.pitch_list("c b b")
t10.out("G4-3")

# 6. BOS #11 Rafael Devers (X - X - X)
t10.new_ab()
t10.out("F7")

# 7. BOS #7  Christian Vázquez (X - X - X)
t10.new_ab()
t10.pitch_list("c b f")
t10.hit(1)

# 8. BOS #19 Jackie Bradley Jr. (X - X - 7)
t10.new_ab()
t10.pitch_list("f b f b b")
t10.out("G5-3")


# Bot 10th
# Pitching: BOS #46 Craig Kimbrel
b10 = game.new_inning()

# Pitching change (BOS): #46 Craig Kimbrel replaces #56 Joe Kelly, batting 9th
b10.pitching_substitution(46)
b10.defensive_substitution(9, 46, "1")

# 6. MIA #1  Cameron Maybin (X - X - X)
b10.new_ab()
b10.pitch_list("c b")
b10.out("G4-3")

# 7. MIA #19 Miguel Rojas (X - X - X)
b10.new_ab()
b10.hit(1)
b10.advance(2, "2 SB")

# 8. MIA #17 Chad Wallach (X - X - 19)
b10.new_ab()
b10.pitch_list("f 1 s f s")
b10.out("K")

# Offensive change (MIA): Pinch-hitter #2 Yadiel Rivera replaces #29 Brad Ziegler, batting 9th
b10.offensive_substitution(9, 2, "PH")

# 9. MIA #2  Yadiel Rivera (X - X - 19)
b10.new_ab()
b10.pitch_list("b s b f b b")
b10.reach("BB")

# 1. MIA #9  Lewis Brinson (X - 19 - 2)
b10.new_ab()
b10.pitch_list("b b")
b10.out("F9")


##########################################################
# 11th Inning
##########################################################
# Top 11th
# Pitching: MIA #43 Odrisamer Despaigne
t11 = game.new_inning()

# Pitching change (MIA): #43 Odrisamer Despaigne replaces #29 Brad Ziegler, batting 9th
t11.pitching_substitution(43)
t11.defensive_substitution(9, 43, "1")

# Offensive change (BOS): Pinch-hitter #50 Mookie Betts replaces #46 Craig Kimbrel, batting 9th
t11.offensive_substitution(9, 50, "PH")

# 9. BOS #50 Mookie Betts (X - X - X)
t11.new_ab()
t11.pitch_list("b f c b b")
t11.out("F8")

# 1. BOS #36 Eduardo Núñez (X - X - X)
t11.new_ab()
t11.pitch_list("c f b b")
t11.hit(2)
t11.advance(4, "16 1B")

# 2. BOS #16 Andrew Benintendi (X - 36 - X)
t11.new_ab()
t11.pitch_list("t")
t11.hit(1, rbis=1)
t11.advance(2, "T")

# 3. BOS #13 Hanley Ramirez (X - 16 - X)
t11.new_ab()
t11.pitch_list("s")
t11.out("L1")

# 4. BOS #28 J.D. Martinez (X - 16 - X)
t11.new_ab()
t11.pitch_list("s s b b s")
t11.out("K")


# Bot 11th
# Pitching: BOS #32 Matt Barnes
b11 = game.new_inning()

# Pitching change (BOS): #32 Matt Barnes replaces #46 Craig Kimbrel, batting 4th
b11.pitching_substitution(32)
b11.defensive_substitution(4, 32, "1")

# Defensive switch (BOS): #50 Mookie Betts moves to RF
b11.defensive_switch(50, "9")

# 2. MIA #32 Derek Dietrich (X - X - X)
b11.new_ab()
b11.pitch_list("b f f s")
b11.out("K2-3")

# 3. MIA #13 Starlin Castro (X - X - X)
b11.new_ab()
b11.pitch_list("f")
b11.out("L9")

# 4. MIA #15 Brian Anderson (X - X - X)
b11.new_ab()
b11.pitch_list("b b c f b b")
b11.reach("BB")
b11.advance(2, "41 BB")
b11.advance(4, "1 2B")

# 5. MIA #41 Justin Bour (X - X - 15)
b11.new_ab()
b11.pitch_list("b s b b c b")
b11.reach("BB")
b11.thrown_out(4, "1 7-6-2", 3, 32)
b11.advance(3, "1 2B")

# 6. MIA #1  Cameron Maybin (X - 15 - 41)
b11.new_ab()
b11.pitch_list("b")
b11.hit(2, rbis=1)


##########################################################
# 12th Inning
##########################################################
# Top 12th
# Pitching: MIA #43 Odrisamer Despaigne
t12 = game.new_inning()

# 5. BOS #2  Xander Bogaerts (X - X - X)
t12.new_ab()
t12.pitch_list("f s f")
t12.out("G4-3")

# 6. BOS #11 Rafael Devers (X - X - X)
t12.new_ab()
t12.pitch_list("s")
t12.hit(1)
t12.thrown_out(2, "7 DP4-6-3", 2, 43)

# 7. BOS #7  Christian Vázquez (X - X - 11)
t12.new_ab()
t12.pitch_list("c s d")
t12.out("DP4-6-3")


# Bot 12th
# Pitching: BOS #37 Heath Hembree
b12 = game.new_inning()

# Pitching change (BOS): #37 Heath Hembree replaces #32 Matt Barnes, batting 7th
b12.pitching_substitution(37)
b12.defensive_substitution(7, 37, "1")

# Defensive change (BOS): #3 Sandy León replaces #32 Matt Barnes (P), playing C, batting 4th
b12.defensive_substitution(4, 3, "2")

# 7. MIA #19 Miguel Rojas (X - X - X)
b12.new_ab()
b12.pitch_list("b b c f")
b12.out("G3")

# 8. MIA #17 Chad Wallach (X - X - X)
b12.new_ab()
b12.pitch_list("f b s s")
b12.out("K")

# Offensive change (MIA): Pinch-hitter #28 Bryan Holaday replaces #43 Odrisamer Despaigne, batting 9th
b12.offensive_substitution(9, 28, "PH")

# 9. MIA #28 Bryan Holaday (X - X - X)
b12.new_ab()
b12.pitch_list("c s s")
b12.out("K")


##########################################################
# 13th Inning
##########################################################
# Top 13th
# Pitching: MIA #56 Tayron Guerrero
t13 = game.new_inning()

# Pitching change (MIA): #56 Tayron Guerrero replaces #43 Odrisamer Despaigne, batting 9th
t13.pitching_substitution(56)
t13.defensive_substitution(9, 56, "1")

# 8. BOS #19 Jackie Bradley Jr. (X - X - X)
t13.new_ab()
t13.pitch_list("b f")
t13.out("G1-4-3")

# 9. BOS #50 Mookie Betts (X - X - X)
t13.new_ab()
t13.pitch_list("b")
t13.hit(1)
t13.advance(2, "36 G5-3")
t13.advance(4, "13 2B")

# 1. BOS #36 Eduardo Núñez (X - X - 50)
t13.new_ab()
t13.pitch_list("1 f f 1")
t13.out("G5-3")

# 2. BOS #16 Andrew Benintendi (X - 50 - X)
t13.new_ab()
t13.pitch_list("b b v v")
t13.reach("IBB")
t13.advance(4, "13 2B")

# 3. BOS #13 Hanley Ramirez (X - 50 - 16)
t13.new_ab()
t13.pitch_list("b f")
t13.hit(2, rbis=2)
t13.advance(3, "3 1B")

# 4. BOS #3  Sandy León (X - 13 - X)
t13.new_ab()
t13.pitch_list("c f")
t13.hit(1)

# 5. BOS #2  Xander Bogaerts (13 - X - 3)
t13.new_ab()
t13.out("L9")


# Bot 13th
# Pitching: BOS #37 Heath Hembree
b13 = game.new_inning()

# 1. MIA #9  Lewis Brinson (X - X - X)
b13.new_ab()
b13.pitch_list("c b")
b13.out("G5-3")

# 2. MIA #32 Derek Dietrich (X - X - X)
b13.new_ab()
b13.pitch_list("b c f f")
b13.hit(1)
b13.thrown_out(2, "13 FC4", 2, 37)

# 3. MIA #13 Starlin Castro (X - X - 32)
b13.new_ab()
b13.pitch_list("f b s")
b13.reach("FC4")

# 4. MIA #15 Brian Anderson (X - X - 13)
b13.new_ab()
b13.pitch_list("c d s f b f f t")
b13.out("KT")

# Winning team: BOS
# WP: BOS #37 Heath Hembree
game.winning_pitcher(37, is_away_team=True)

# Loser team: MIA
# LP: MIA #56 Tayron Guerrero
game.losing_pitcher(56)

# print(game)
game.generate_scorecard()
