import os
from baseball_scorecard.baseball_scorecard import Scorecard

# TBR @ TOR, 2018-08-11
# https://www.baseball-reference.com/boxes/TOR/TOR201808110.shtml
# https://www.mlb.com/gameday/rays-vs-blue-jays/2018/08/11/531169/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-08-11 16:34-19:30",
        "at": "Rogers Centre, Toronto, ON",
        "att": "38,797",
        "temp": "79F, Sunny",
        "wind": "4mph, Out To CF",
        "away": {
            "team": "Tampa Bay Rays",
            "starter": 55,
            "roster": {
                # Lineup
                0: "Mallex Smith",
                5: "Matt Duffy",
                18: "Joey Wendle",
                44: "C.J. Cron",
                26: "Ji Man Choi",
                39: "Kevin Kiermaier",
                1: "Willy Adames",
                35: "Brandon Lowe",
                45: "Jesús Sucre",
                # Starting pitcher
                55: "Ryne Stanek",
                # Bench
                9: "Jake Bauers",
                27: "Carlos Gómez",
                43: "Michael Pérez",
                # Bullpen
                46: "José Alvarado",
                20: "Tyler Glasnow",
                61: "Hunter Wood",
                48: "Ryan Yarbrough",
                68: "Jalen Beeks",
                56: "Adam Kolarek",
                57: "Jaime Schultz",
                34: "Jake Faria",
                42: "Blake Snell",
                72: "Yonny Chirinos",
                63: "Diego Castillo",
                54: "Sergio Romo",
            },
            "lefties": [46, 48, 68, 56, 42],
            "lineup": [
                [0, "9"],
                [5, "5"],
                [18, "4"],
                [44, "3"],
                [26, "0"],
                [39, "8"],
                [1, "6"],
                [35, "7"],
                [45, "2"],
            ],
            "bench": [
                [9, "1B"],
                [27, "CF"],
                [43, "C"],
            ],
            "bullpen": [46, 20, 61, 48, 68, 56, 57, 34, 42, 72, 63, 54],
        },
        "home": {
            "team": "Toronto Blue Jays",
            "starter": 43,
            "roster": {
                # Lineup
                15: "Randal Grichuk",
                29: "Devon Travis",
                14: "Justin Smoak",
                37: "Teoscar Hernández",
                8: "Kendrys Morales",
                26: "Yangervis Solarte",
                55: "Russell Martin",
                1: "Aledmys Díaz",
                11: "Kevin Pillar",
                # Starting pitcher
                43: "Sam Gaviglio",
                # Bench
                7: "Richard Urena",
                21: "Luke Maile",
                18: "Curtis Granderson",
                # Bullpen
                51: "Ken Giles",
                57: "Jaime García",
                31: "Joe Biagini",
                24: "Danny Barnes",
                71: "Luis Santos",
                25: "Marco Estrada",
                39: "Jake Petricka",
                56: "Ryan Borucki",
                36: "Tyler Clippard",
                45: "Thomas Pannone",
                6: "Marcus Stroman",
                52: "Ryan Tepera",
            },
            "lefties": [57, 56, 45],
            "lineup": [
                [15, "9"],
                [29, "4"],
                [14, "3"],
                [37, "7"],
                [8, "0"],
                [26, "5"],
                [55, "2"],
                [1, "6"],
                [11, "8"],
            ],
            "bench": [
                [7, "SS"],
                [21, "C"],
                [18, "CF"],
            ],
            "bullpen": [51, 57, 31, 24, 71, 25, 39, 56, 36, 45, 6, 52],
        },
        "umpires": {
            "HP": "Tony Randazzo",
            "1B": "Ryan Additon",
            "2B": "Bill Welke",
            "3B": "Lance Barrett",
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
# Pitching: TOR #43 Sam Gaviglio
t1 = game.new_inning()

# 1. TBR #0  Mallex Smith (X - X - X)
t1.new_ab()
t1.pitch_list("c f f b")
t1.hit(2)
t1.advance(3, "5 G6-3")
t1.advance(4, "18 2B")

# 2. TBR #5  Matt Duffy (X - 0 - X)
t1.new_ab(is_risp=True)
t1.pitch_list("c b")
t1.out("G6-3")

# 3. TBR #18 Joey Wendle (0 - X - X)
t1.new_ab(is_risp=True)
t1.pitch_list("d d c s f f")
t1.hit(2, rbis=1)

# 4. TBR #44 C.J. Cron (X - 18 - X)
t1.new_ab(is_risp=True)
t1.pitch_list("b b f s s")
t1.out("K")

# 5. TBR #26 Ji Man Choi (X - 18 - X)
t1.new_ab(is_risp=True)
t1.pitch_list("b c")
t1.out("L9")


# Bot 1st
# Pitching: TBR #55 Ryne Stanek
b1 = game.new_inning()

# 1. TOR #15 Randal Grichuk (X - X - X)
b1.new_ab()
b1.pitch_list("c s f c")
b1.out("!K")

# 2. TOR #29 Devon Travis (X - X - X)
b1.new_ab()
b1.pitch_list("f")
b1.out("P6")

# 3. TOR #14 Justin Smoak (X - X - X)
b1.new_ab()
b1.pitch_list("b")
b1.out("P5")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: TOR #43 Sam Gaviglio
t2 = game.new_inning()

# 6. TBR #39 Kevin Kiermaier (X - X - X)
t2.new_ab()
t2.pitch_list("c")
t2.hit(1)
t2.error(8)
t2.advance(2, "E8")
t2.advance(3, "1 SB")
t2.advance("U", "1 G6-3")

# 7. TBR #1  Willy Adames (X - 39 - X)
t2.new_ab(is_risp=True)
t2.pitch_list("d s b f d")
t2.out("G6-3", rbis=1)

# 8. TBR #35 Brandon Lowe (X - X - X)
t2.new_ab()
t2.pitch_list("b b t s f b s")
t2.out("K")

# 9. TBR #45 Jesús Sucre (X - X - X)
t2.new_ab()
t2.pitch_list("c")
t2.out("P4")


# Bot 2nd
# Pitching: TBR #55 Ryne Stanek
b2 = game.new_inning()

# 4. TOR #37 Teoscar Hernández (X - X - X)
b2.new_ab()
b2.hit(2)
b2.advance(3, "55 HBP")

# 5. TOR #8  Kendrys Morales (X - 37 - X)
b2.new_ab(is_risp=True)
b2.pitch_list("b b d c d")
b2.reach("BB")
b2.advance(2, "55 HBP")

# 6. TOR #7  Richard Urena (X - 37 - 8)
b2.new_ab(is_risp=True)
b2.pitch_list("c f d b f f f f f f s")
b2.out("K")

# Offensive change (TOR): Pinch-hitter #7 Richard Urena replaces #26 Yangervis Solarte, batting 6th
# Note: this substitution came under a 2-strike count and ended with a strikeout.
b2.offensive_substitution(6, 7, "PH")

# Pitching change (TBR): #63 Diego Castillo replaces #55 Ryne Stanek
b2.pitching_substitution(63)

# 7. TOR #55 Russell Martin (X - 37 - 8)
b2.new_ab(is_risp=True)
b2.pitch_list("b s")
b2.reach("HBP")

# 8. TOR #1  Aledmys Díaz (37 - 8 - 55)
b2.new_ab(is_risp=True)
b2.pitch_list("b f b b s")
b2.out("(F)P2")

# 9. TOR #11 Kevin Pillar (37 - 8 - 55)
b2.new_ab(is_risp=True)
b2.pitch_list("c")
b2.out("G4-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: TOR #43 Sam Gaviglio
t3 = game.new_inning()

# Defensive switch (TOR): #7 Richard Urena moves to 3B
t3.defensive_switch(7, "5")

# 1. TBR #0  Mallex Smith (X - X - X)
t3.new_ab()
t3.pitch_list("f b")
t3.out("F7")

# 2. TBR #5  Matt Duffy (X - X - X)
t3.new_ab()
t3.pitch_list("c b c s")
t3.out("K")

# 3. TBR #18 Joey Wendle (X - X - X)
t3.new_ab()
t3.pitch_list("b c c f b b")
t3.hit(1)

# 4. TBR #44 C.J. Cron (X - X - 18)
t3.new_ab()
t3.pitch_list("1 c c f b s")
t3.out("K")


# Bot 3rd
# Pitching: TBR #63 Diego Castillo
b3 = game.new_inning()

# 1. TOR #15 Randal Grichuk (X - X - X)
b3.new_ab()
b3.pitch_list("f b f s")
b3.out("K2-3")

# 2. TOR #29 Devon Travis (X - X - X)
b3.new_ab()
b3.pitch_list("b")
b3.out("G4-3")

# 3. TOR #14 Justin Smoak (X - X - X)
b3.new_ab()
b3.pitch_list("c f b b b b")
b3.reach("BB")

# 4. TOR #37 Teoscar Hernández (X - X - 14)
b3.new_ab()
b3.pitch_list("s s s")
b3.out("K")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: TOR #43 Sam Gaviglio
t4 = game.new_inning()

# 5. TBR #26 Ji Man Choi (X - X - X)
t4.new_ab()
t4.pitch_list("c b")
t4.hit(2)
t4.advance(3, "39 F9")

# 6. TBR #39 Kevin Kiermaier (X - 26 - X)
t4.new_ab(is_risp=True)
t4.pitch_list("b c l f f f b b f")
t4.out("F9")

# 7. TBR #1  Willy Adames (26 - X - X)
t4.new_ab(is_risp=True)
t4.pitch_list("s f d d s")
t4.out("K")

# 8. TBR #35 Brandon Lowe (26 - X - X)
t4.new_ab(is_risp=True)
t4.pitch_list("f")
t4.out("L3")


# Bot 4th
# Pitching: TBR #63 Diego Castillo
b4 = game.new_inning()

# 5. TOR #8  Kendrys Morales (X - X - X)
b4.new_ab()
b4.pitch_list("b")
b4.hit(1)
b4.thrown_out(2, "7 DP6-4-3", 1, 63)

# 6. TOR #7  Richard Urena (X - X - 8)
b4.new_ab()
b4.pitch_list("f")
b4.out("DP6-4-3")

# 7. TOR #55 Russell Martin (X - X - X)
b4.new_ab()
b4.pitch_list("f b b")
b4.out("G4-3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: TOR #43 Sam Gaviglio
t5 = game.new_inning()

# 9. TBR #45 Jesús Sucre (X - X - X)
t5.new_ab()
t5.pitch_list("f f s")
t5.out("K")

# 1. TBR #0  Mallex Smith (X - X - X)
t5.new_ab()
t5.pitch_list("b b c s b s")
t5.out("K")

# 2. TBR #5  Matt Duffy (X - X - X)
t5.new_ab()
t5.pitch_list("b c")
t5.out("G5-3")


# Bot 5th
# Pitching: TBR #57 Jaime Schultz
b5 = game.new_inning()

# Pitching change (TBR): #57 Jaime Schultz replaces #63 Diego Castillo
b5.pitching_substitution(57)

# 8. TOR #1  Aledmys Díaz (X - X - X)
b5.new_ab()
b5.pitch_list("b b")
b5.hit(4)

# 9. TOR #11 Kevin Pillar (X - X - X)
b5.new_ab()
b5.pitch_list("b s b")
b5.out("P2")

# 1. TOR #15 Randal Grichuk (X - X - X)
b5.new_ab()
b5.pitch_list("c c")
b5.out("G5-3")

# 2. TOR #29 Devon Travis (X - X - X)
b5.new_ab()
b5.pitch_list("b c b f b")
b5.hit(1)

# 3. TOR #14 Justin Smoak (X - X - 29)
b5.new_ab()
b5.pitch_list("1 b b")
b5.out("G3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: TOR #43 Sam Gaviglio
t6 = game.new_inning()

# 3. TBR #18 Joey Wendle (X - X - X)
t6.new_ab()
t6.pitch_list("c b")
t6.out("F8")

# 4. TBR #44 C.J. Cron (X - X - X)
t6.new_ab()
t6.pitch_list("c c b b")
t6.hit(1)
t6.thrown_out(2, "26 FC4-6", 2, 57)

# Pitching change (TOR): #57 Jaime García replaces #43 Sam Gaviglio
t6.pitching_substitution(57)

# 5. TBR #26 Ji Man Choi (X - X - 44)
t6.new_ab()
t6.pitch_list("c b b")
t6.reach("FC4-6")

# 6. TBR #39 Kevin Kiermaier (X - X - 26)
t6.new_ab()
t6.pitch_list("c f s")
t6.out("K")


# Bot 6th
# Pitching: TBR #57 Jaime Schultz
b6 = game.new_inning()

# 4. TOR #37 Teoscar Hernández (X - X - X)
b6.new_ab()
b6.pitch_list("b f b b c b")
b6.reach("BB")
b6.thrown_out(2, "8 DP6-4-3", 1, 57)

# 5. TOR #8  Kendrys Morales (X - X - 37)
b6.new_ab()
b6.pitch_list("c f 1 f b 1 f f")
b6.out("DP6-4-3")

# 6. TOR #7  Richard Urena (X - X - X)
b6.new_ab()
b6.pitch_list("c f s")
b6.out("K")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: TOR #39 Jake Petricka
t7 = game.new_inning()

# Pitching change (TOR): #39 Jake Petricka replaces #57 Jaime García
t7.pitching_substitution(39)

# 7. TBR #1  Willy Adames (X - X - X)
t7.new_ab()
t7.pitch_list("b")
t7.hit(1)
t7.advance(2, "0 SB")

# 8. TBR #35 Brandon Lowe (X - X - 1)
t7.new_ab()
t7.pitch_list("f 1 b 1 c b b")
t7.out("F7")

# 9. TBR #45 Jesús Sucre (X - X - 1)
t7.new_ab()
t7.pitch_list("c 1 f t")
t7.out("KT")

# 1. TBR #0  Mallex Smith (X - X - 1)
t7.new_ab(is_risp=True)
t7.pitch_list("b b b b")
t7.reach("BB")

# 2. TBR #5  Matt Duffy (X - 1 - 0)
t7.new_ab(is_risp=True)
t7.pitch_list("b")
t7.out("P3")


# Bot 7th
# Pitching: TBR #61 Hunter Wood
b7 = game.new_inning()

# Pitching change (TBR): #61 Hunter Wood replaces #57 Jaime Schultz
b7.pitching_substitution(61)

# 7. TOR #55 Russell Martin (X - X - X)
b7.new_ab()
b7.pitch_list("b b c c")
b7.hit(1)
b7.thrown_out(2, "11 CS", 2, 61)

# 8. TOR #1  Aledmys Díaz (X - X - 55)
b7.new_ab()
b7.pitch_list("f b")
b7.out("L9")

# 9. TOR #11 Kevin Pillar (X - X - 55)
b7.new_ab()
b7.pitch_list("s b s b b b")
b7.reach("BB")
b7.thrown_out(1, "15 PO", 3, 61)

# 1. TOR #15 Randal Grichuk (X - X - 11)
b7.new_ab()
b7.pitch_list("c b 1")
b7.no_ab("PO")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: TOR #36 Tyler Clippard
t8 = game.new_inning()

# Pitching change (TOR): #36 Tyler Clippard replaces #39 Jake Petricka
t8.pitching_substitution(36)

# 3. TBR #18 Joey Wendle (X - X - X)
t8.new_ab()
t8.pitch_list("f")
t8.out("F7")

# 4. TBR #44 C.J. Cron (X - X - X)
t8.new_ab()
t8.pitch_list("c")
t8.hit(2)

# 5. TBR #26 Ji Man Choi (X - 44 - X)
t8.new_ab(is_risp=True)
t8.pitch_list("b f c s")
t8.out("K")

# 6. TBR #39 Kevin Kiermaier (X - 44 - X)
t8.new_ab(is_risp=True)
t8.pitch_list("s b")
t8.out("G4-3")


# Bot 8th
# Pitching: TBR #46 José Alvarado
b8 = game.new_inning()

# Pitching change (TBR): #46 José Alvarado replaces #61 Hunter Wood
b8.pitching_substitution(46)

# Defensive switch (TBR): #0 Mallex Smith moves to LF
b8.defensive_switch(0, "7")

# Defensive change (TBR): #9 Jake Bauers replaces #35 Brandon Lowe (LF), playing 1B, batting 8th
b8.defensive_substitution(8, 9, "3")

# Defensive change (TBR): #27 Carlos Gómez replaces #44 C.J. Cron (1B), playing RF, batting 4th
b8.defensive_substitution(4, 27, "9")

# 1. TOR #15 Randal Grichuk (X - X - X)
b8.new_ab()
b8.pitch_list("c c s")
b8.out("K")

# 2. TOR #29 Devon Travis (X - X - X)
b8.new_ab()
b8.pitch_list("f")
b8.out("F9")

# 3. TOR #14 Justin Smoak (X - X - X)
b8.new_ab()
b8.pitch_list("s f b b c")
b8.out("!K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: TOR #52 Ryan Tepera
t9 = game.new_inning()

# Pitching change (TOR): #52 Ryan Tepera replaces #36 Tyler Clippard
t9.pitching_substitution(52)

# 7. TBR #1  Willy Adames (X - X - X)
t9.new_ab()
t9.pitch_list("b b f")
t9.hit(1)
t9.advance(2, "9 G4-3")
t9.advance(4, "45 1B")

# 8. TBR #9  Jake Bauers (X - X - 1)
t9.new_ab()
t9.pitch_list("d b s")
t9.out("G4-3")

# 9. TBR #45 Jesús Sucre (X - 1 - X)
t9.new_ab(is_risp=True)
t9.hit(1, rbis=1)
t9.thrown_out(2, "8-2-6", 2, 52)

# 1. TBR #0  Mallex Smith (X - X - X)
t9.new_ab()
t9.pitch_list("b b f f c")
t9.out("!K")


# Bot 9th
# Pitching: TBR #54 Sergio Romo
b9 = game.new_inning()

# Pitching change (TBR): #54 Sergio Romo replaces #46 José Alvarado
b9.pitching_substitution(54)

# 4. TOR #37 Teoscar Hernández (X - X - X)
b9.new_ab()
b9.pitch_list("s b b s b s")
b9.out("K")

# 5. TOR #8  Kendrys Morales (X - X - X)
b9.new_ab()
b9.pitch_list("b b")
b9.out("L8")

# Offensive change (TOR): Pinch-hitter #18 Curtis Granderson replaces #7 Richard Urena, batting 6th
b9.offensive_substitution(6, 18, "PH")

# 6. TOR #18 Curtis Granderson (X - X - X)
b9.new_ab()
b9.pitch_list("c b")
b9.out("F8")

# Winning team: TBR
# WP: TBR #63 Diego Castillo
game.winning_pitcher(63, is_away_team=True)
# SV: TBR #54 Sergio Romo
game.save_pitcher(54, is_away_team=True)

# Loser team: TOR
# LP: TOR #43 Sam Gaviglio
game.losing_pitcher(43)

# print(game)
game.generate_scorecard()
