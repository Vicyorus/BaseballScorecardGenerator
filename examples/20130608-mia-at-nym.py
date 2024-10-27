import os
from baseball_scorecard.baseball_scorecard import Scorecard

# MIA @ NYM, 2013-06-08
# https://www.baseball-reference.com/boxes/NYN/NYN201306080.shtml
# https://www.mlb.com/gameday/marlins-vs-mets/2013/06/08/347669/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-06-08 13:12-19:37",
        "at": "Citi Field, Flushing, NY",
        "att": "20,338",
        "temp": "77F, Cloudy",
        "wind": "9mph, Out To RF",
        "away": {
            "team": "Miami Marlins",
            "starter": 16,
            "roster": {
                # Lineup
                9: "Juan Pierre",
                59: "Ed Lucas",
                51: "Derek Dietrich",
                48: "Marcell Ozuna",
                8: "Chris Coghlan",
                30: "Placido Polanco",
                19: "Rob Brantly",
                3: "Adeiny Hechavarría",
                16: "José Fernández",
                # Starting pitcher
                16: "José Fernández",
                # Bench
                29: "Greg Dobbs",
                20: "Justin Ruggiano",
                18: "Casey Kotchman",
                6: "Jeff Mathis",
                21: "Miguel Olivo",
                # Bullpen
                31: "Steve Cishek",
                44: "AJ Ramos",
                33: "Jacob Turner",
                40: "Mike Dunn",
                50: "Chad Qualls",
                34: "Tom Koehler",
                45: "Kevin Slowey",
                67: "Edgar Olmos",
                58: "Ryan Webb",
                43: "Dan Jennings",
                47: "Ricky Nolasco",
            },
            "lefties": [40, 67, 43],
            "lineup": [
                [9, "7"],
                [59, "3"],
                [51, "4"],
                [48, "9"],
                [8, "8"],
                [30, "5"],
                [19, "2"],
                [3, "6"],
                [16, "1"],
            ],
            "bench": [
                [29, "3B"],
                [20, "CF"],
                [18, "1B"],
                [6, "C"],
                [21, "C"],
            ],
            "bullpen": [31, 44, 33, 40, 50, 34, 45, 67, 58, 43, 47],
        },
        "home": {
            "team": "New York Mets",
            "starter": 33,
            "roster": {
                # Lineup
                3: "Omar Quintanilla",
                28: "Daniel Murphy",
                5: "David Wright",
                21: "Lucas Duda",
                6: "Marlon Byrd",
                29: "Ike Davis",
                44: "John Buck",
                12: "Juan Lagares",
                33: "Matt Harvey",
                # Starting pitcher
                33: "Matt Harvey",
                # Bench
                1: "Jordany Valdespin",
                23: "Mike Baxter",
                20: "Anthony Recker",
                16: "Rick Ankiel",
                2: "Justin Turner",
                # Bullpen
                35: "Dillon Gee",
                49: "Jonathon Niese",
                73: "Robert Carson",
                56: "Scott Rice",
                38: "Shaun Marcum",
                34: "Brandon Lyon",
                46: "Greg Burke",
                32: "LaTroy Hawkins",
                39: "Bobby Parnell",
                53: "Jeremy Hefner",
                30: "David Aardsma",
            },
            "lefties": [49, 73, 56],
            "lineup": [
                [3, "6"],
                [28, "4"],
                [5, "5"],
                [21, "7"],
                [6, "9"],
                [29, "3"],
                [44, "2"],
                [12, "8"],
                [33, "1"],
            ],
            "bench": [
                [1, "2B"],
                [23, "RF"],
                [20, "C"],
                [16, "CF"],
                [2, "1B"],
            ],
            "bullpen": [35, 49, 73, 56, 38, 34, 46, 32, 39, 53, 30],
        },
        "umpires": {
            "HP": "Alfonso Márquez",
            "1B": "Dan Bellino",
            "2B": "Mike DiMuro",
            "3B": "Ted Barrett",
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
# Pitching: NYM #33 Matt Harvey
t1 = game.new_inning()

# 1. MIA #9  Juan Pierre (X - X - X)
t1.new_ab()
t1.pitch_list("c f b")
t1.out("G4-3")

# 2. MIA #59 Ed Lucas (X - X - X)
t1.new_ab()
t1.pitch_list("c s b f b b c")
t1.out("!K")

# 3. MIA #51 Derek Dietrich (X - X - X)
t1.new_ab()
t1.pitch_list("b c b s b f")
t1.out("F9")


# Bot 1st
# Pitching: MIA #16 José Fernández
b1 = game.new_inning()

# 1. NYM #3  Omar Quintanilla (X - X - X)
b1.new_ab()
b1.pitch_list("c")
b1.out("P6")

# 2. NYM #28 Daniel Murphy (X - X - X)
b1.new_ab()
b1.hit(1)
b1.advance(3, "21 1B")

# 3. NYM #5  David Wright (X - X - 28)
b1.new_ab()
b1.pitch_list("b b")
b1.out("L9")

# 4. NYM #21 Lucas Duda (X - X - 28)
b1.new_ab()
b1.pitch_list("1 1 b f b f f b f")
b1.hit(1)

# 5. NYM #6  Marlon Byrd (28 - X - 21)
b1.new_ab(is_risp=True)
b1.pitch_list("c f c")
b1.out("!K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: NYM #33 Matt Harvey
t2 = game.new_inning()

# 4. MIA #48 Marcell Ozuna (X - X - X)
t2.new_ab()
t2.pitch_list("b f")
t2.out("G4-3")

# 5. MIA #8  Chris Coghlan (X - X - X)
t2.new_ab()
t2.pitch_list("c b f c")
t2.out("!K")

# 6. MIA #30 Placido Polanco (X - X - X)
t2.new_ab()
t2.pitch_list("c")
t2.out("G5-3")


# Bot 2nd
# Pitching: MIA #16 José Fernández
b2 = game.new_inning()

# 6. NYM #29 Ike Davis (X - X - X)
b2.new_ab()
b2.pitch_list("b b c b s f b")
b2.reach("BB")
b2.advance(4, "12 2B")

# 7. NYM #44 John Buck (X - X - 29)
b2.new_ab()
b2.pitch_list("b")
b2.out("L6")

# 8. NYM #12 Juan Lagares (X - X - 29)
b2.new_ab()
b2.pitch_list("b b c f f")
b2.hit(2, rbis=1)

# 9. NYM #33 Matt Harvey (X - 12 - X)
b2.new_ab(is_risp=True)
b2.pitch_list("f f s")
b2.out("K")

# 1. NYM #3  Omar Quintanilla (X - 12 - X)
b2.new_ab(is_risp=True)
b2.out("F7")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: NYM #33 Matt Harvey
t3 = game.new_inning()

# 7. MIA #19 Rob Brantly (X - X - X)
t3.new_ab()
t3.hit(1)

# 8. MIA #3  Adeiny Hechavarría (X - X - 19)
t3.new_ab()
t3.pitch_list("c")
t3.out("F9")

# 9. MIA #16 José Fernández (X - X - 19)
t3.new_ab()
t3.pitch_list("m l l")
t3.out("K")

# 1. MIA #9  Juan Pierre (X - X - 19)
t3.new_ab()
t3.out("F7")


# Bot 3rd
# Pitching: MIA #16 José Fernández
b3 = game.new_inning()

# 2. NYM #28 Daniel Murphy (X - X - X)
b3.new_ab()
b3.pitch_list("c b c b f f")
b3.out("L7")

# 3. NYM #5  David Wright (X - X - X)
b3.new_ab()
b3.pitch_list("f b")
b3.out("F8")

# 4. NYM #21 Lucas Duda (X - X - X)
b3.new_ab()
b3.pitch_list("b b b b")
b3.reach("BB")

# 5. NYM #6  Marlon Byrd (X - X - 21)
b3.new_ab()
b3.pitch_list("s f f f b")
b3.out("L9")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: NYM #33 Matt Harvey
t4 = game.new_inning()

# 2. MIA #59 Ed Lucas (X - X - X)
t4.new_ab()
t4.pitch_list("c b")
t4.out("G5-3")

# 3. MIA #51 Derek Dietrich (X - X - X)
t4.new_ab()
t4.hit(1)
t4.advance(3, "48 1B")
t4.advance(4, "8 SF9")

# 4. MIA #48 Marcell Ozuna (X - X - 51)
t4.new_ab()
t4.pitch_list("c d b s b")
t4.hit(1)
t4.thrown_out(2, "30 POCS", 3, 33)

# 5. MIA #8  Chris Coghlan (51 - X - 48)
t4.new_ab(is_risp=True)
t4.pitch_list("b b")
t4.out("SF9", rbis=1)

# 6. MIA #30 Placido Polanco (X - X - 48)
t4.new_ab()
t4.pitch_list("c 1")
t4.no_ab("POCS")


# Bot 4th
# Pitching: MIA #16 José Fernández
b4 = game.new_inning()

# 6. NYM #29 Ike Davis (X - X - X)
b4.new_ab()
b4.pitch_list("c f c")
b4.out("!K")

# 7. NYM #44 John Buck (X - X - X)
b4.new_ab()
b4.pitch_list("f s f c")
b4.out("!K")

# 8. NYM #12 Juan Lagares (X - X - X)
b4.new_ab()
b4.pitch_list("c c c")
b4.out("!K")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: NYM #33 Matt Harvey
t5 = game.new_inning()

# 6. MIA #30 Placido Polanco (X - X - X)
t5.new_ab()
t5.pitch_list("b")
t5.out("G6-3")

# 7. MIA #19 Rob Brantly (X - X - X)
t5.new_ab()
t5.pitch_list("s b b")
t5.hit(1)
t5.advance(2, "3 1B")
t5.thrown_out(3, "16 FC1-5", 2, 33)

# 8. MIA #3  Adeiny Hechavarría (X - X - 19)
t5.new_ab()
t5.hit(1)
t5.advance(2, "16 FC1-5")
t5.advance(3, "9 1B")
t5.thrown_out(4, "9 8-2", 3, 33)

# 9. MIA #16 José Fernández (X - 19 - 3)
t5.new_ab(is_risp=True)
t5.pitch_list("m")
t5.reach("FC1-5")
t5.advance(2, "9 8-2")

# 1. MIA #9  Juan Pierre (X - 3 - 16)
t5.new_ab(is_risp=True)
t5.pitch_list("c b b b")
t5.hit(1)


# Bot 5th
# Pitching: MIA #16 José Fernández
b5 = game.new_inning()

# 9. NYM #33 Matt Harvey (X - X - X)
b5.new_ab()
b5.pitch_list("b c s")
b5.out("G6-3")

# 1. NYM #3  Omar Quintanilla (X - X - X)
b5.new_ab()
b5.pitch_list("c b f f")
b5.out("F7")

# 2. NYM #28 Daniel Murphy (X - X - X)
b5.new_ab()
b5.pitch_list("c b c")
b5.out("G3-1")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: NYM #33 Matt Harvey
t6 = game.new_inning()

# 2. MIA #59 Ed Lucas (X - X - X)
t6.new_ab()
t6.pitch_list("c c f b s")
t6.out("K")

# 3. MIA #51 Derek Dietrich (X - X - X)
t6.new_ab()
t6.pitch_list("f b b c f s")
t6.out("K")

# 4. MIA #48 Marcell Ozuna (X - X - X)
t6.new_ab()
t6.pitch_list("b s b")
t6.out("G4-3")


# Bot 6th
# Pitching: MIA #16 José Fernández
b6 = game.new_inning()

# 3. NYM #5  David Wright (X - X - X)
b6.new_ab()
b6.pitch_list("c c b")
b6.out("G4-3")

# 4. NYM #21 Lucas Duda (X - X - X)
b6.new_ab()
b6.pitch_list("b b b b")
b6.reach("BB")

# 5. NYM #6  Marlon Byrd (X - X - 21)
b6.new_ab()
b6.pitch_list("f f f c")
b6.out("!K")

# 6. NYM #29 Ike Davis (X - X - 21)
b6.new_ab()
b6.pitch_list("b f s b f s")
b6.out("K")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: NYM #33 Matt Harvey
t7 = game.new_inning()

# 5. MIA #8  Chris Coghlan (X - X - X)
t7.new_ab()
t7.pitch_list("b c b f")
t7.out("(F)P5")

# 6. MIA #30 Placido Polanco (X - X - X)
t7.new_ab()
t7.pitch_list("b c b f")
t7.out("F8")

# 7. MIA #19 Rob Brantly (X - X - X)
t7.new_ab()
t7.pitch_list("c s b f b s")
t7.out("K")


# Bot 7th
# Pitching: MIA #50 Chad Qualls
b7 = game.new_inning()

# Pitching change (MIA): #50 Chad Qualls replaces #16 José Fernández, batting 9th
b7.pitching_substitution(50)
b7.defensive_substitution(9, 50, "1")

# 7. NYM #44 John Buck (X - X - X)
b7.new_ab()
b7.pitch_list("c")
b7.reach("HBP")
b7.thrown_out(2, "12 DP6-3", 1, 50)

# 8. NYM #12 Juan Lagares (X - X - 44)
b7.new_ab()
b7.pitch_list("l")
b7.out("DP6-3")

# 9. NYM #33 Matt Harvey (X - X - X)
b7.new_ab()
b7.pitch_list("c b s b")
b7.hit(1)

# 1. NYM #3  Omar Quintanilla (X - X - 33)
b7.new_ab()
b7.pitch_list("c")
b7.out("G6-3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: NYM #34 Brandon Lyon
t8 = game.new_inning()

# Pitching change (NYM): #34 Brandon Lyon replaces #33 Matt Harvey, batting 9th
t8.pitching_substitution(34)
t8.defensive_substitution(9, 34, "1")

# 8. MIA #3  Adeiny Hechavarría (X - X - X)
t8.new_ab()
t8.pitch_list("c c b f")
t8.hit(1)
t8.advance(2, "29 SB")
t8.thrown_out(3, "9 POCS", 1, 34)

# Offensive change (MIA): Pinch-hitter #29 Greg Dobbs replaces #50 Chad Qualls, batting 9th
t8.offensive_substitution(9, 29, "PH")

# 9. MIA #29 Greg Dobbs (X - X - 3)
t8.new_ab(is_risp=True)
t8.pitch_list("f 1 f b d b f b")
t8.reach("BB")
t8.thrown_out(2, "9 DP4-6-3", 2, 34)

# 1. MIA #9  Juan Pierre (X - 3 - 29)
t8.new_ab()
t8.pitch_list("m 2")
t8.out("DP4-6-3")


# Bot 8th
# Pitching: MIA #40 Mike Dunn
b8 = game.new_inning()

# Pitching change (MIA): #40 Mike Dunn replaces #50 Chad Qualls, batting 9th
b8.pitching_substitution(40)
b8.defensive_substitution(9, 40, "1")

# 2. NYM #28 Daniel Murphy (X - X - X)
b8.new_ab()
b8.out("P6")

# 3. NYM #5  David Wright (X - X - X)
b8.new_ab()
b8.pitch_list("b b f f b b")
b8.reach("BB")
b8.advance(2, "21 SB")

# 4. NYM #21 Lucas Duda (X - X - 5)
b8.new_ab()
b8.pitch_list("1 b s b c f f f 1 b s")
b8.out("K")

# 5. NYM #6  Marlon Byrd (X - 5 - X)
b8.new_ab(is_risp=True)
b8.pitch_list("i i i i")
b8.reach("IBB")

# Pitching change (MIA): #58 Ryan Webb replaces #40 Mike Dunn, batting 9th
b8.pitching_substitution(58)
b8.defensive_substitution(9, 58, "1")

# Offensive change (NYM): Pinch-hitter #2 Justin Turner replaces #29 Ike Davis, batting 6th
b8.offensive_substitution(6, 2, "PH")

# 6. NYM #2  Justin Turner (X - 5 - 6)
b8.new_ab(is_risp=True)
b8.pitch_list("c b b f")
b8.out("F8")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: NYM #39 Bobby Parnell
t9 = game.new_inning()

# Pitching change (NYM): #39 Bobby Parnell replaces #34 Brandon Lyon, batting 9th
t9.pitching_substitution(39)
t9.defensive_substitution(9, 39, "1")

# Defensive switch (NYM): #2 Justin Turner moves to 1B
t9.defensive_switch(2, "3")

# 2. MIA #59 Ed Lucas (X - X - X)
t9.new_ab()
t9.pitch_list("c")
t9.out("G3")

# 3. MIA #51 Derek Dietrich (X - X - X)
t9.new_ab()
t9.pitch_list("c c b b f b s")
t9.out("K")

# 4. MIA #48 Marcell Ozuna (X - X - X)
t9.new_ab()
t9.pitch_list("c b")
t9.hit(1)

# 5. MIA #8  Chris Coghlan (X - X - 48)
t9.new_ab()
t9.pitch_list("1")
t9.out("G1-3")


# Bot 9th
# Pitching: MIA #58 Ryan Webb
b9 = game.new_inning()

# 7. NYM #44 John Buck (X - X - X)
b9.new_ab()
b9.hit(1)
b9.advance(2, "12 SAC1-3")

# 8. NYM #12 Juan Lagares (X - X - 44)
b9.new_ab()
b9.pitch_list("l")
b9.out("SAC1-3")

# Pitching change (MIA): #43 Dan Jennings replaces #58 Ryan Webb, batting 5th
b9.pitching_substitution(43)
b9.defensive_substitution(5, 43, "1")

# Offensive change (NYM): Pinch-hitter #23 Mike Baxter replaces #39 Bobby Parnell, batting 9th
b9.offensive_substitution(9, 23, "PH")

# Defensive change (MIA): #20 Justin Ruggiano replaces #58 Ryan Webb (P), playing CF, batting 9th
b9.defensive_substitution(9, 20, "8")

# Offensive change (NYM): Pinch-hitter #20 Anthony Recker replaces #23 Mike Baxter, batting 9th
b9.offensive_substitution(9, 20, "PH")

# 9. NYM #20 Anthony Recker (X - 44 - X)
b9.new_ab(is_risp=True)
b9.pitch_list("c b c s")
b9.out("K")

# 1. NYM #3  Omar Quintanilla (X - 44 - X)
b9.new_ab(is_risp=True)
b9.pitch_list("b b b c b")
b9.reach("BB")

# 2. NYM #28 Daniel Murphy (X - 44 - 3)
b9.new_ab(is_risp=True)
b9.pitch_list("f")
b9.out("G4-3")


##########################################################
# 10th Inning
##########################################################
# Top 10th
# Pitching: NYM #32 LaTroy Hawkins
t10 = game.new_inning()

# Pitching change (NYM): #32 LaTroy Hawkins replaces #39 Bobby Parnell, batting 9th
t10.pitching_substitution(32)
t10.defensive_substitution(9, 32, "1")

# 6. MIA #30 Placido Polanco (X - X - X)
t10.new_ab()
t10.pitch_list("b")
t10.out("F9")

# 7. MIA #19 Rob Brantly (X - X - X)
t10.new_ab()
t10.pitch_list("b s b")
t10.out("G6-3")

# 8. MIA #3  Adeiny Hechavarría (X - X - X)
t10.new_ab()
t10.pitch_list("b c s b b b")
t10.reach("BB")
t10.advance(3, "20 1B")

# 9. MIA #20 Justin Ruggiano (X - X - 3)
t10.new_ab()
t10.pitch_list("c 1")
t10.hit(1)

# Pitching change (NYM): #56 Scott Rice replaces #32 LaTroy Hawkins, batting 9th
t10.pitching_substitution(56)
t10.defensive_substitution(9, 56, "1")

# 1. MIA #9  Juan Pierre (3 - X - 20)
t10.new_ab(is_risp=True)
t10.pitch_list("l")
t10.out("F7")


# Bot 10th
# Pitching: MIA #43 Dan Jennings
b10 = game.new_inning()

# 3. NYM #5  David Wright (X - X - X)
b10.new_ab()
b10.pitch_list("c b c")
b10.out("F8")

# 4. NYM #21 Lucas Duda (X - X - X)
b10.new_ab()
b10.pitch_list("c s b f s")
b10.out("K")

# 5. NYM #6  Marlon Byrd (X - X - X)
b10.new_ab()
b10.pitch_list("b b b f f b")
b10.reach("BB")
b10.advance(2, "2 BB")

# 6. NYM #2  Justin Turner (X - X - 6)
b10.new_ab()
b10.pitch_list("b f 1 f d b b")
b10.reach("BB")

# Pitching change (MIA): #44 AJ Ramos replaces #43 Dan Jennings, batting 1st
b10.pitching_substitution(44)
b10.defensive_substitution(1, 44, "1")

# Defensive switch (MIA): #59 Ed Lucas moves to LF
b10.defensive_switch(59, "7")

# Defensive change (MIA): #18 Casey Kotchman replaces #43 Dan Jennings (P), playing 1B, batting 5th
b10.defensive_substitution(5, 18, "3")

# 7. NYM #44 John Buck (X - 6 - 2)
b10.new_ab(is_risp=True)
b10.pitch_list("b")
b10.out("(F)P5")


##########################################################
# 11th Inning
##########################################################
# Top 11th
# Pitching: NYM #56 Scott Rice
t11 = game.new_inning()

# 2. MIA #59 Ed Lucas (X - X - X)
t11.new_ab()
t11.hit(1)

# 3. MIA #51 Derek Dietrich (X - X - 59)
t11.new_ab()
t11.pitch_list("s")
t11.out("F9")

# Pitching change (NYM): #46 Greg Burke replaces #56 Scott Rice, batting 9th
t11.pitching_substitution(46)
t11.defensive_substitution(9, 46, "1")

# 4. MIA #48 Marcell Ozuna (X - X - 59)
t11.new_ab()
t11.pitch_list("f b 1 f b f s")
t11.out("K")

# 5. MIA #18 Casey Kotchman (X - X - 59)
t11.new_ab()
t11.pitch_list("c b")
t11.out("G4-3")


# Bot 11th
# Pitching: MIA #44 AJ Ramos
b11 = game.new_inning()

# 8. NYM #12 Juan Lagares (X - X - X)
b11.new_ab()
b11.pitch_list("c f b")
b11.out("L4")

# Offensive change (NYM): Pinch-hitter #1 Jordany Valdespin replaces #46 Greg Burke, batting 9th
b11.offensive_substitution(9, 1, "PH")

# 9. NYM #1  Jordany Valdespin (X - X - X)
b11.new_ab()
b11.pitch_list("c")
b11.out("G6-3")

# 1. NYM #3  Omar Quintanilla (X - X - X)
b11.new_ab()
b11.pitch_list("b f b c b")
b11.out("F7")


##########################################################
# 12th Inning
##########################################################
# Top 12th
# Pitching: NYM #30 David Aardsma
t12 = game.new_inning()

# Pitching change (NYM): #30 David Aardsma replaces #46 Greg Burke, batting 9th
t12.pitching_substitution(30)
t12.defensive_substitution(9, 30, "1")

# 6. MIA #30 Placido Polanco (X - X - X)
t12.new_ab()
t12.pitch_list("b c f f b b")
t12.out("F7")

# 7. MIA #19 Rob Brantly (X - X - X)
t12.new_ab()
t12.pitch_list("c")
t12.out("G6-3")

# 8. MIA #3  Adeiny Hechavarría (X - X - X)
t12.new_ab()
t12.pitch_list("s b b f s")
t12.out("K")


# Bot 12th
# Pitching: MIA #44 AJ Ramos
b12 = game.new_inning()

# 2. NYM #28 Daniel Murphy (X - X - X)
b12.new_ab()
b12.pitch_list("b b b b")
b12.reach("BB")
b12.advance(2, "5 FC5")
b12.advance(3, "21 L8")
b12.thrown_out(4, "6 DP9-2", 3, 44)

# 3. NYM #5  David Wright (X - X - 28)
b12.new_ab()
b12.pitch_list("s")
b12.reach("FC5")

# 4. NYM #21 Lucas Duda (X - 28 - 5)
b12.new_ab(is_risp=True)
b12.out("L8")

# 5. NYM #6  Marlon Byrd (28 - X - 5)
b12.new_ab(is_risp=True)
b12.pitch_list("s f f")
b12.out("DP9-2")


##########################################################
# 13th Inning
##########################################################
# Top 13th
# Pitching: NYM #38 Shaun Marcum
t13 = game.new_inning()

# Pitching change (NYM): #38 Shaun Marcum replaces #30 David Aardsma, batting 5th
t13.pitching_substitution(38)
t13.defensive_substitution(5, 38, "1")

# Defensive change (NYM): #16 Rick Ankiel replaces #30 David Aardsma (P), playing RF, batting 9th
t13.defensive_substitution(9, 16, "9")

# 9. MIA #20 Justin Ruggiano (X - X - X)
t13.new_ab()
t13.pitch_list("f f f f")
t13.out("F7")

# Offensive change (MIA): Pinch-hitter #21 Miguel Olivo replaces #44 AJ Ramos, batting 1st
t13.offensive_substitution(1, 21, "PH")

# 1. MIA #21 Miguel Olivo (X - X - X)
t13.new_ab()
t13.pitch_list("c b b t s")
t13.out("K")

# 2. MIA #59 Ed Lucas (X - X - X)
t13.new_ab()
t13.pitch_list("c f")
t13.out("P4")


# Bot 13th
# Pitching: MIA #45 Kevin Slowey
b13 = game.new_inning()

# Pitching change (MIA): #45 Kevin Slowey replaces #44 AJ Ramos, batting 1st
b13.pitching_substitution(45)
b13.defensive_substitution(1, 45, "1")

# 6. NYM #2  Justin Turner (X - X - X)
b13.new_ab()
b13.pitch_list("b b b c")
b13.hit(1)
b13.advance(2, "12 1B")

# 7. NYM #44 John Buck (X - X - 2)
b13.new_ab()
b13.out("B2")

# 8. NYM #12 Juan Lagares (X - X - 2)
b13.new_ab()
b13.pitch_list("c f")
b13.hit(1)

# 9. NYM #16 Rick Ankiel (X - 2 - 12)
b13.new_ab(is_risp=True)
b13.pitch_list("b c")
b13.out("(F)P5")

# 1. NYM #3  Omar Quintanilla (X - 2 - 12)
b13.new_ab(is_risp=True)
b13.pitch_list("c f b f t")
b13.out("KT")


##########################################################
# 14th Inning
##########################################################
# Top 14th
# Pitching: NYM #38 Shaun Marcum
t14 = game.new_inning()

# 3. MIA #51 Derek Dietrich (X - X - X)
t14.new_ab()
t14.pitch_list("f f")
t14.out("F7")

# 4. MIA #48 Marcell Ozuna (X - X - X)
t14.new_ab()
t14.pitch_list("s c f")
t14.hit(1)

# 5. MIA #18 Casey Kotchman (X - X - 48)
t14.new_ab()
t14.pitch_list("1 b f 1 1 d f f f 1 b 1")
t14.out("F8")

# 6. MIA #30 Placido Polanco (X - X - 48)
t14.new_ab()
t14.pitch_list("c 1 f b")
t14.out("G5-3")


# Bot 14th
# Pitching: MIA #45 Kevin Slowey
b14 = game.new_inning()

# 2. NYM #28 Daniel Murphy (X - X - X)
b14.new_ab()
b14.pitch_list("b c f s")
b14.out("K")

# 3. NYM #5  David Wright (X - X - X)
b14.new_ab()
b14.pitch_list("f")
b14.hit(1)
b14.advance(2, "6 HBP")

# 4. NYM #21 Lucas Duda (X - X - 5)
b14.new_ab()
b14.pitch_list("b b f c f c")
b14.out("!K")

# 5. NYM #6  Marlon Byrd (X - X - 5)
b14.new_ab()
b14.pitch_list("c 1 c f")
b14.reach("HBP")
b14.thrown_out(2, "2 FC5-4", 3, 45)

# 6. NYM #2  Justin Turner (X - 5 - 38)
b14.new_ab(is_risp=True)
b14.pitch_list("c b")
b14.reach("FC5-4")


##########################################################
# 15th Inning
##########################################################
# Top 15th
# Pitching: NYM #38 Shaun Marcum
t15 = game.new_inning()

# 7. MIA #19 Rob Brantly (X - X - X)
t15.new_ab()
t15.pitch_list("c b f")
t15.hit(1)

# 8. MIA #3  Adeiny Hechavarría (X - X - 19)
t15.new_ab()
t15.pitch_list("c")
t15.out("P4")

# 9. MIA #20 Justin Ruggiano (X - X - 19)
t15.new_ab()
t15.pitch_list("c f f f f b b s")
t15.out("K")

# 1. MIA #21 Miguel Olivo (X - X - 19)
t15.new_ab()
t15.pitch_list("f s f b s")
t15.out("K")


# Bot 15th
# Pitching: MIA #45 Kevin Slowey
b15 = game.new_inning()

# 7. NYM #44 John Buck (X - X - X)
b15.new_ab()
b15.pitch_list("b f b")
b15.hit(1)
b15.advance(2, "12 G4-3")

# 8. NYM #12 Juan Lagares (X - X - 44)
b15.new_ab()
b15.out("G4-3")

# 9. NYM #16 Rick Ankiel (X - 44 - X)
b15.new_ab(is_risp=True)
b15.pitch_list("b s s d f s")
b15.out("K")

# 1. NYM #3  Omar Quintanilla (X - 44 - X)
b15.new_ab(is_risp=True)
b15.pitch_list("c d s c")
b15.out("!K")


##########################################################
# 16th Inning
##########################################################
# Top 16th
# Pitching: NYM #38 Shaun Marcum
t16 = game.new_inning()

# 2. MIA #59 Ed Lucas (X - X - X)
t16.new_ab()
t16.out("P4")

# 3. MIA #51 Derek Dietrich (X - X - X)
t16.new_ab()
t16.pitch_list("f")
t16.out("P4")

# 4. MIA #48 Marcell Ozuna (X - X - X)
t16.new_ab()
t16.pitch_list("b b f")
t16.out("F8")


# Bot 16th
# Pitching: MIA #45 Kevin Slowey
b16 = game.new_inning()

# 2. NYM #28 Daniel Murphy (X - X - X)
b16.new_ab()
b16.pitch_list("b")
b16.out("F7")

# 3. NYM #5  David Wright (X - X - X)
b16.new_ab()
b16.hit(1)

# 4. NYM #21 Lucas Duda (X - X - 5)
b16.new_ab()
b16.out("(F)P5")

# 5. NYM #6  Marlon Byrd (X - X - 5)
b16.new_ab()
b16.pitch_list("b")
b16.out("L7")


##########################################################
# 17th Inning
##########################################################
# Top 17th
# Pitching: NYM #38 Shaun Marcum
t17 = game.new_inning()

# 5. MIA #18 Casey Kotchman (X - X - X)
t17.new_ab()
t17.pitch_list("b")
t17.out("G1-3")

# 6. MIA #30 Placido Polanco (X - X - X)
t17.new_ab()
t17.pitch_list("f c f s")
t17.out("K")

# 7. MIA #19 Rob Brantly (X - X - X)
t17.new_ab()
t17.pitch_list("b f b")
t17.out("P4")


# Bot 17th
# Pitching: MIA #45 Kevin Slowey
b17 = game.new_inning()

# 6. NYM #2  Justin Turner (X - X - X)
b17.new_ab()
b17.pitch_list("c f f f f f")
b17.hit(2)

# 7. NYM #44 John Buck (X - 2 - X)
b17.new_ab(is_risp=True)
b17.out("F9")

# 8. NYM #12 Juan Lagares (X - 2 - X)
b17.new_ab(is_risp=True)
b17.pitch_list("c f")
b17.out("P3")

# 9. NYM #16 Rick Ankiel (X - 2 - X)
b17.new_ab(is_risp=True)
b17.pitch_list("b f b s s")
b17.out("K")


##########################################################
# 18th Inning
##########################################################
# Top 18th
# Pitching: NYM #38 Shaun Marcum
t18 = game.new_inning()

# 8. MIA #3  Adeiny Hechavarría (X - X - X)
t18.new_ab()
t18.pitch_list("c b f")
t18.out("P4")

# 9. MIA #20 Justin Ruggiano (X - X - X)
t18.new_ab()
t18.pitch_list("f c s")
t18.out("K")

# 1. MIA #21 Miguel Olivo (X - X - X)
t18.new_ab()
t18.pitch_list("b c s b")
t18.out("(F)P3")


# Bot 18th
# Pitching: MIA #45 Kevin Slowey
b18 = game.new_inning()

# 1. NYM #3  Omar Quintanilla (X - X - X)
b18.new_ab()
b18.hit(1)
b18.advance(2, "5 1B")

# 2. NYM #28 Daniel Murphy (X - X - 3)
b18.new_ab()
b18.pitch_list("c b b")
b18.out("F7")

# 3. NYM #5  David Wright (X - X - 3)
b18.new_ab()
b18.hit(1)

# 4. NYM #21 Lucas Duda (X - 3 - 5)
b18.new_ab(is_risp=True)
b18.pitch_list("s f s")
b18.out("K")

# 5. NYM #6  Marlon Byrd (X - 3 - 5)
b18.new_ab(is_risp=True)
b18.pitch_list("f b")
b18.out("(F)F9")


##########################################################
# 19th Inning
##########################################################
# Top 19th
# Pitching: NYM #38 Shaun Marcum
t19 = game.new_inning()

# 2. MIA #59 Ed Lucas (X - X - X)
t19.new_ab()
t19.pitch_list("c b")
t19.out("L7")

# 3. MIA #51 Derek Dietrich (X - X - X)
t19.new_ab()
t19.pitch_list("c c s")
t19.out("K")

# 4. MIA #48 Marcell Ozuna (X - X - X)
t19.new_ab()
t19.pitch_list("f b c f f s")
t19.out("K")


# Bot 19th
# Pitching: MIA #45 Kevin Slowey
b19 = game.new_inning()

# 6. NYM #2  Justin Turner (X - X - X)
b19.new_ab()
b19.pitch_list("b c f")
b19.out("F8")

# 7. NYM #44 John Buck (X - X - X)
b19.new_ab()
b19.pitch_list("f b f c")
b19.out("!K")

# 8. NYM #12 Juan Lagares (X - X - X)
b19.new_ab()
b19.out("F8")


##########################################################
# 20th Inning
##########################################################
# Top 20th
# Pitching: NYM #38 Shaun Marcum
t20 = game.new_inning()

# 5. MIA #18 Casey Kotchman (X - X - X)
t20.new_ab()
t20.pitch_list("c s f b f f")
t20.out("F7")

# 6. MIA #30 Placido Polanco (X - X - X)
t20.new_ab()
t20.pitch_list("f")
t20.hit(1)
t20.advance(2, "19 1B")
t20.advance(4, "3 1B")

# 7. MIA #19 Rob Brantly (X - X - 30)
t20.new_ab()
t20.hit(1)
t20.advance(2, "3 1B")
t20.thrown_out(3, "3 8-5", 2, 38)

# 8. MIA #3  Adeiny Hechavarría (X - 30 - 19)
t20.new_ab(is_risp=True)
t20.pitch_list("c")
t20.hit(1, rbis=1)

# 9. MIA #20 Justin Ruggiano (X - X - 3)
t20.new_ab()
t20.out("F8")


# Bot 20th
# Pitching: MIA #31 Steve Cishek
b20 = game.new_inning()

# Pitching change (MIA): #31 Steve Cishek replaces #45 Kevin Slowey, batting 1st
b20.pitching_substitution(31)
b20.defensive_substitution(1, 31, "1")

# 9. NYM #16 Rick Ankiel (X - X - X)
b20.new_ab()
b20.pitch_list("s b s s")
b20.out("K")

# 1. NYM #3  Omar Quintanilla (X - X - X)
b20.new_ab()
b20.pitch_list("b")
b20.out("G4-3")

# 2. NYM #28 Daniel Murphy (X - X - X)
b20.new_ab()
b20.out("F7")

# Winning team: MIA
# WP: MIA #45 Kevin Slowey
game.winning_pitcher(45, is_away_team=True)
# SV: MIA #31 Steve Cishek
game.save_pitcher(31, is_away_team=True)

# Loser team: NYM
# LP: NYM #38 Shaun Marcum
game.losing_pitcher(38)

# print(game)
game.generate_scorecard()
