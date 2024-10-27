import os
from baseball_scorecard.baseball_scorecard import Scorecard

# LAA @ BOS, 2023-04-17
# https://www.baseball-reference.com/boxes/BOS/BOS202304170.shtml
# https://www.mlb.com/gameday/angels-vs-red-sox/2023/04/17/718540/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2023-04-17 12:06-17:30 (2:21 delay)",
        "at": "Fenway Park, Boston, MA",
        "att": "34,942",
        "temp": "50F, Cloudy",
        "wind": "3mph, Out To RF",
        "away": {
            "team": "Los Angeles Angels",
            "starter": 17,
            "roster": {
                # Lineup
                9: "Zach Neto",
                17: "Shohei Ohtani",
                3: "Taylor Ward",
                12: "Hunter Renfroe",
                10: "Gio Urshela",
                18: "Jake Lamb",
                23: "Brandon Drury",
                14: "Logan O'Hoppe",
                8: "Brett Phillips",
                # Starting pitcher
                17: "Shohei Ohtani",
                # Bench
                2: "Luis Rengifo",
                21: "Matt Thaiss",
                27: "Mike Trout",
                6: "Anthony Rendon",
                # Bullpen
                28: "Aaron Loup",
                43: "Patrick Sandoval",
                46: "Jimmy Herget",
                54: "José Suarez",
                47: "Griffin Canning",
                55: "Matt Moore",
                60: "Andrew Wantz",
                51: "Jaime Barria",
                53: "Carlos Estévez",
                32: "Tucker Davidson",
                48: "Reid Detmers",
                31: "Tyler Anderson",
                65: "José Quijada",
            },
            "lefties": [28, 43, 54, 55, 32, 48, 31, 65],
            "lineup": [
                [9, "6"],
                [17, "1"],
                [3, "7"],
                [12, "9"],
                [10, "5"],
                [18, "3"],
                [23, "4"],
                [14, "2"],
                [8, "8"],
            ],
            "bench": [
                [2, "3B"],
                [21, "C"],
                [27, "CF"],
                [6, "3B"],
            ],
            "bullpen": [28, 43, 46, 54, 47, 55, 60, 51, 53, 32, 48, 31, 65],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 66,
            "roster": {
                # Lineup
                17: "Raimel Tapia",
                11: "Rafael Devers",
                30: "Rob Refsnyder",
                7: "Masataka Yoshida",
                36: "Triston Casas",
                5: "Enrique Hernández",
                3: "Reese McGuire",
                39: "Christian Arroyo",
                16: "Jarren Duran",
                # Starting pitcher
                66: "Brayan Bello",
                # Bench
                20: "Yu Chang",
                12: "Connor Wong",
                99: "Alex Verdugo",
                2: "Justin Turner",
                # Bullpen
                61: "Kaleb Ort",
                41: "Chris Sale",
                74: "Kenley Jansen",
                22: "Garrett Whitlock",
                25: "Josh Winckowski",
                50: "Kutter Crawford",
                37: "Nick Pivetta",
                70: "Ryan Brasier",
                89: "Tanner Houck",
                28: "Corey Kluber",
                46: "John Schreiber",
            },
            "lefties": [41],
            "lineup": [
                [17, "9"],
                [11, "5"],
                [30, "7"],
                [7, "0"],
                [36, "3"],
                [5, "6"],
                [3, "2"],
                [39, "4"],
                [16, "8"],
            ],
            "bench": [
                [20, "2B"],
                [12, "C"],
                [99, "LF"],
                [2, "1B"],
            ],
            "bullpen": [61, 41, 74, 22, 25, 50, 37, 70, 89, 28, 46],
        },
        "umpires": {
            "HP": "Jansen Visconti",
            "1B": "Ron Kulpa",
            "2B": "Cory Blaser",
            "3B": "Carlos Torres",
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

# 1. LAA #9  Zach Neto (X - X - X)
t1.new_ab()
t1.pitch_list("s c b f c")
t1.out("!K")

# 2. LAA #17 Shohei Ohtani (X - X - X)
t1.new_ab()
t1.hit(1)
t1.advance(2, "3 HBP")
t1.advance(4, "12 HR")

# 3. LAA #3  Taylor Ward (X - X - 17)
t1.new_ab()
t1.pitch_list("c f b b")
t1.reach("HBP")
t1.advance(4, "12 HR")

# 4. LAA #12 Hunter Renfroe (X - 17 - 3)
t1.new_ab(is_risp=True)
t1.pitch_list("b")
t1.hit(4, rbis=3)

# 5. LAA #10 Gio Urshela (X - X - X)
t1.new_ab()
t1.pitch_list("c b b b c b")
t1.reach("BB")
t1.advance(3, "18 1B")
t1.advance(4, "23 SF7")

# 6. LAA #18 Jake Lamb (X - X - 10)
t1.new_ab()
t1.pitch_list("c b")
t1.hit(1)
t1.advance(2, "14 1B")

# 7. LAA #23 Brandon Drury (10 - X - 18)
t1.new_ab(is_risp=True)
t1.out("SF7", rbis=1)

# 8. LAA #14 Logan O'Hoppe (X - X - 18)
t1.new_ab()
t1.pitch_list("c b s f b b f f f f")
t1.hit(1)

# 9. LAA #8  Brett Phillips (X - 18 - 14)
t1.new_ab(is_risp=True)
t1.pitch_list("c s s")
t1.out("K")


# Bot 1st
# Pitching: LAA #17 Shohei Ohtani
b1 = game.new_inning()

# 1. BOS #17 Raimel Tapia (X - X - X)
b1.new_ab()
b1.pitch_list("b b b b")
b1.reach("BB")
b1.advance(2, "11 WP")
b1.advance(3, "11 WP")
b1.advance(4, "30 G6-3")

# 2. BOS #11 Rafael Devers (X - X - 17)
b1.new_ab(is_risp=True)
b1.pitch_list("f b f b f b")
b1.wp()
b1.wp()
b1.out("(F)P5")

# 3. BOS #30 Rob Refsnyder (17 - X - X)
b1.new_ab(is_risp=True)
b1.pitch_list("c s b")
b1.out("G6-3", rbis=1)

# 4. BOS #7  Masataka Yoshida (X - X - X)
b1.new_ab()
b1.pitch_list("c f b s")
b1.out("K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #66 Brayan Bello
t2 = game.new_inning()

# 1. LAA #9  Zach Neto (X - X - X)
t2.new_ab()
t2.hit(1)
t2.advance(3, "17 1B")
t2.advance(4, "12 G6-3")

# 2. LAA #17 Shohei Ohtani (X - X - 9)
t2.new_ab()
t2.pitch_list("b b")
t2.hit(1)
t2.advance(2, "12 G6-3")

# 3. LAA #3  Taylor Ward (9 - X - 17)
t2.new_ab(is_risp=True)
t2.pitch_list("s b s b s")
t2.out("K")

# 4. LAA #12 Hunter Renfroe (9 - X - 17)
t2.new_ab(is_risp=True)
t2.out("G6-3", rbis=1)

# 5. LAA #10 Gio Urshela (X - 17 - X)
t2.new_ab(is_risp=True)
t2.pitch_list("f f")
t2.out("L7")


# Bot 2nd
# Pitching: LAA #17 Shohei Ohtani
b2 = game.new_inning()

# 5. BOS #36 Triston Casas (X - X - X)
b2.new_ab()
b2.pitch_list("b s")
b2.out("F8")

# 6. BOS #5  Enrique Hernández (X - X - X)
b2.new_ab()
b2.pitch_list("c s c")
b2.out("!K")

# 7. BOS #3  Reese McGuire (X - X - X)
b2.new_ab()
b2.pitch_list("b s s f f s")
b2.out("K2-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #66 Brayan Bello
t3 = game.new_inning()

# 6. LAA #18 Jake Lamb (X - X - X)
t3.new_ab()
t3.pitch_list("c f b f")
t3.hit(1)
t3.advance(2, "23 1B")

# 7. LAA #23 Brandon Drury (X - X - 18)
t3.new_ab()
t3.pitch_list("c f b")
t3.hit(1)

# 8. LAA #14 Logan O'Hoppe (X - 18 - 23)
t3.new_ab(is_risp=True)
t3.pitch_list("c s pso s")
t3.out("K")

# 9. LAA #8  Brett Phillips (X - 18 - 23)
t3.new_ab(is_risp=True)
t3.pitch_list("b b b c 2 c s")
t3.out("K")

# Pitching change (BOS): #50 Kutter Crawford replaces #66 Brayan Bello
t3.pitching_substitution(50)

# 1. LAA #9  Zach Neto (X - 18 - 23)
t3.new_ab(is_risp=True)
t3.pitch_list("l b b f")
t3.out("F9")


# Bot 3rd
# Pitching: LAA #32 Tucker Davidson
b3 = game.new_inning()

# Pitching change (LAA): #32 Tucker Davidson replaces #17 Shohei Ohtani
b3.pitching_substitution(32)

# Defensive switch (LAA): #17 Shohei Ohtani moves to DH
b3.defensive_switch(17, "0")

# 8. BOS #39 Christian Arroyo (X - X - X)
b3.new_ab()
b3.pitch_list("b")
b3.out("G6-3")

# 9. BOS #16 Jarren Duran (X - X - X)
b3.new_ab()
b3.pitch_list("l f c")
b3.out("!K")

# 1. BOS #17 Raimel Tapia (X - X - X)
b3.new_ab()
b3.pitch_list("b c f s")
b3.out("K")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #50 Kutter Crawford
t4 = game.new_inning()

# 2. LAA #17 Shohei Ohtani (X - X - X)
t4.new_ab()
t4.pitch_list("b c")
t4.out("F8")

# 3. LAA #3  Taylor Ward (X - X - X)
t4.new_ab()
t4.out("G6-3")

# 4. LAA #12 Hunter Renfroe (X - X - X)
t4.new_ab()
t4.pitch_list("c c s")
t4.out("K")


# Bot 4th
# Pitching: LAA #32 Tucker Davidson
b4 = game.new_inning()

# 2. BOS #11 Rafael Devers (X - X - X)
b4.new_ab()
b4.pitch_list("b b")
b4.hit(2)
b4.advance(3, "36 BB")

# 3. BOS #30 Rob Refsnyder (X - 11 - X)
b4.new_ab(is_risp=True)
b4.pitch_list("b c s f")
b4.out("G4-3")

# 4. BOS #7  Masataka Yoshida (X - 11 - X)
b4.new_ab(is_risp=True)
b4.pitch_list("b b b c f b")
b4.reach("BB")
b4.advance(2, "36 BB")

# 5. BOS #36 Triston Casas (X - 11 - 7)
b4.new_ab(is_risp=True)
b4.pitch_list("b f c d b b")
b4.reach("BB")

# 6. BOS #5  Enrique Hernández (11 - 7 - 36)
b4.new_ab(is_risp=True)
b4.pitch_list("f")
b4.out("L3")

# 7. BOS #3  Reese McGuire (11 - 7 - 36)
b4.new_ab(is_risp=True)
b4.pitch_list("f b s")
b4.out("F8")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #50 Kutter Crawford
t5 = game.new_inning()

# 5. LAA #10 Gio Urshela (X - X - X)
t5.new_ab()
t5.pitch_list("f f")
t5.out("G4-3")

# 6. LAA #18 Jake Lamb (X - X - X)
t5.new_ab()
t5.pitch_list("b f")
t5.hit(1)

# 7. LAA #23 Brandon Drury (X - X - 18)
t5.new_ab()
t5.pitch_list("b")
t5.out("F9")

# 8. LAA #14 Logan O'Hoppe (X - X - 18)
t5.new_ab()
t5.pitch_list("b c f d f b f f f")
t5.out("G5-3")


# Bot 5th
# Pitching: LAA #32 Tucker Davidson
b5 = game.new_inning()

# 8. BOS #39 Christian Arroyo (X - X - X)
b5.new_ab()
b5.out("G3-1")

# 9. BOS #16 Jarren Duran (X - X - X)
b5.new_ab()
b5.pitch_list("b c")
b5.hit(2)

# 1. BOS #17 Raimel Tapia (X - 16 - X)
b5.new_ab(is_risp=True)
b5.pitch_list("b b 2 s f s")
b5.out("K")

# 2. BOS #11 Rafael Devers (X - 16 - X)
b5.new_ab(is_risp=True)
b5.pitch_list("c")
b5.out("G5-3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #50 Kutter Crawford
t6 = game.new_inning()

# 9. LAA #8  Brett Phillips (X - X - X)
t6.new_ab()
t6.pitch_list("s c b s")
t6.out("K")

# 1. LAA #9  Zach Neto (X - X - X)
t6.new_ab()
t6.pitch_list("c f b")
t6.error(6)
t6.reach("E6")
t6.error(1)
t6.advance(2, "17 POE1")
t6.advance(3, "17 E1")

# 2. LAA #17 Shohei Ohtani (X - X - 9)
t6.new_ab(is_risp=True)
t6.pitch_list("b 1")
t6.error(1)
t6.reach("E1")
t6.thrown_out(2, "3 CS", 2, 50)

# 3. LAA #3  Taylor Ward (9 - X - 17)
t6.new_ab(is_risp=True)
t6.pitch_list("t s")
t6.out("G5-3")


# Bot 6th
# Pitching: LAA #32 Tucker Davidson
b6 = game.new_inning()

# 3. BOS #30 Rob Refsnyder (X - X - X)
b6.new_ab()
b6.pitch_list("f s")
b6.hit(1)
b6.advance(3, "36 2B")
b6.advance(4, "5 SF8")

# 4. BOS #7  Masataka Yoshida (X - X - 30)
b6.new_ab()
b6.pitch_list("b b s f")
b6.out("F9")

# Pitching change (LAA): #28 Aaron Loup replaces #32 Tucker Davidson
b6.pitching_substitution(28)

# 5. BOS #36 Triston Casas (X - X - 30)
b6.new_ab()
b6.hit(2)
b6.advance(3, "5 SF8")
b6.advance(4, "3 1B")

# 6. BOS #5  Enrique Hernández (30 - 36 - X)
b6.new_ab(is_risp=True)
b6.out("SF8", rbis=1)

# 7. BOS #3  Reese McGuire (36 - X - X)
b6.new_ab(is_risp=True)
b6.pitch_list("b f")
b6.hit(1, rbis=1)

# 8. BOS #39 Christian Arroyo (X - X - 3)
b6.new_ab()
b6.pitch_list("b s s")
b6.out("G5-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #50 Kutter Crawford
t7 = game.new_inning()

# 4. LAA #12 Hunter Renfroe (X - X - X)
t7.new_ab()
t7.pitch_list("f s f b f f f b b c")
t7.out("!K")

# 5. LAA #10 Gio Urshela (X - X - X)
t7.new_ab()
t7.out("G4-3")

# 6. LAA #18 Jake Lamb (X - X - X)
t7.new_ab()
t7.pitch_list("c")
t7.out("G3-1")


# Bot 7th
# Pitching: LAA #55 Matt Moore
b7 = game.new_inning()

# Pitching change (LAA): #55 Matt Moore replaces #28 Aaron Loup
b7.pitching_substitution(55)

# Defensive change (LAA): #2 Luis Rengifo replaces #18 Jake Lamb (1B), playing 2B, batting 6th
b7.defensive_substitution(6, 2, "4")

# Defensive switch (LAA): #23 Brandon Drury moves to 1B
b7.defensive_switch(23, "3")

# 9. BOS #16 Jarren Duran (X - X - X)
b7.new_ab()
b7.pitch_list("b c b b b")
b7.reach("BB")
b7.advance(2, "17 SB")
b7.advance(3, "11 L8")

# 1. BOS #17 Raimel Tapia (X - X - 16)
b7.new_ab(is_risp=True)
b7.pitch_list("pso s f 1 f f f b s")
b7.out("K")

# 2. BOS #11 Rafael Devers (X - 16 - X)
b7.new_ab(is_risp=True)
b7.pitch_list("c f f d f f d")
b7.out("L8")

# 3. BOS #30 Rob Refsnyder (16 - X - X)
b7.new_ab(is_risp=True)
b7.pitch_list("d f f d f")
b7.out("L8")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #50 Kutter Crawford
t8 = game.new_inning()

# 7. LAA #23 Brandon Drury (X - X - X)
t8.new_ab()
t8.pitch_list("f f")
t8.out("F9")

# 8. LAA #14 Logan O'Hoppe (X - X - X)
t8.new_ab()
t8.pitch_list("b c b")
t8.out("(F)P3")

# 9. LAA #8  Brett Phillips (X - X - X)
t8.new_ab()
t8.pitch_list("c f s")
t8.out("K")


# Bot 8th
# Pitching: LAA #65 José Quijada
b8 = game.new_inning()

# Pitching change (LAA): #65 José Quijada replaces #55 Matt Moore
b8.pitching_substitution(65)

# 4. BOS #7  Masataka Yoshida (X - X - X)
b8.new_ab()
b8.pitch_list("b s c f f")
b8.out("G4-3")

# 5. BOS #36 Triston Casas (X - X - X)
b8.new_ab()
b8.pitch_list("b c f b f f f")
b8.out("F8")

# 6. BOS #5  Enrique Hernández (X - X - X)
b8.new_ab()
b8.pitch_list("f b b")
b8.hit(1)

# Offensive change (BOS): Pinch-hitter #2 Justin Turner replaces #3 Reese McGuire, batting 7th
b8.offensive_substitution(7, 2, "PH")

# 7. BOS #2  Justin Turner (X - X - 5)
b8.new_ab()
b8.out("F8")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #50 Kutter Crawford
t9 = game.new_inning()

# Defensive change (BOS): #12 Connor Wong replaces #2 Justin Turner (PH), playing C, batting 7th
t9.defensive_substitution(7, 12, "2")

# 1. LAA #9  Zach Neto (X - X - X)
t9.new_ab()
t9.pitch_list("b b s b")
t9.out("F9")

# 2. LAA #17 Shohei Ohtani (X - X - X)
t9.new_ab()
t9.pitch_list("b")
t9.out("L8")

# 3. LAA #3  Taylor Ward (X - X - X)
t9.new_ab()
t9.pitch_list("c f s")
t9.out("K")


# Bot 9th
# Pitching: LAA #53 Carlos Estévez
b9 = game.new_inning()

# Pitching change (LAA): #53 Carlos Estévez replaces #65 José Quijada
b9.pitching_substitution(53)

# Offensive change (BOS): Pinch-hitter #99 Alex Verdugo replaces #39 Christian Arroyo, batting 8th
b9.offensive_substitution(8, 99, "PH")

# 8. BOS #99 Alex Verdugo (X - X - X)
b9.new_ab()
b9.pitch_list("b t")
b9.hit(1)
b9.advance(2, "17 BB")
b9.advance(4, "11 1B")

# 9. BOS #16 Jarren Duran (X - X - 99)
b9.new_ab()
b9.pitch_list("c b c f b t")
b9.out("KT")

# 1. BOS #17 Raimel Tapia (X - X - 99)
b9.new_ab()
b9.pitch_list("b b b c b")
b9.reach("BB")
b9.advance(2, "11 1B")

# 2. BOS #11 Rafael Devers (X - 99 - 17)
b9.new_ab(is_risp=True)
b9.pitch_list("f")
b9.hit(1, rbis=1)

# 3. BOS #30 Rob Refsnyder (X - 17 - 11)
b9.new_ab(is_risp=True)
b9.pitch_list("b b b c f s")
b9.out("K")

# 4. BOS #7  Masataka Yoshida (X - 17 - 11)
b9.new_ab(is_risp=True)
b9.pitch_list("c b f")
b9.out("P5")

# Winning team: LAA
# WP: LAA #32 Tucker Davidson
game.winning_pitcher(32, is_away_team=True)
# SV: LAA #53 Carlos Estévez
game.save_pitcher(53, is_away_team=True)

# Loser team: BOS
# LP: BOS #66 Brayan Bello
game.losing_pitcher(66)

# print(game)
game.generate_scorecard()
