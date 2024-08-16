#!/usr/bin/python3.10
import os
from scorecard.scorecard import Scorecard

# SEA @ BOS, 2024-07-29
# https://www.baseball-reference.com/boxes/BOS/BOS202407290.shtml
# https://www.mlb.com/gameday/mariners-vs-red-sox/2024/07/29/746928/final

game = Scorecard(os.path.dirname(os.path.abspath(__file__)),
{
    "extended_roster": True,
    "scorer": "Vicyorus",
    "date":   "2024-07-29 19:11-21:58",
    "at":     "Fenway Park, Boston, MA",
    "att":    "35,007",
    "temp":   "72F, Partly Cloudy",
    "wind":   "4mph, Out To RF",
    "away"   : {
        "team":    "Seattle Mariners",
        "starter": 669302,
        "roster":  {
            # Lineup
            645302 : { "jersey" : 10, "name" : "Victor Robles" },
            668227 : { "jersey" : 56, "name" : "Randy Arozarena" },
            663728 : { "jersey" : 29, "name" : "Cal Raleigh" },
            593871 : { "jersey" : 7,  "name" : "Jorge Polanco" },
            670042 : { "jersey" : 20, "name" : "Luke Raley" },
            664238 : { "jersey" : 25, "name" : "Dylan Moore" },
            613564 : { "jersey" : 35, "name" : "Jason Vosler" },
            571745 : { "jersey" : 17, "name" : "Mitch Haniger" },
            668942 : { "jersey" : 4,  "name" : "Josh Rojas" },

            # Starting pitcher
            669302 : { "jersey" : 36, "name" : "Logan Gilbert" },

            # Bench
            682988 : { "jersey" : 27, "name" : "Tyler Locklear" },
            641598 : { "jersey" : 18, "name" : "Mitch Garver" },
            687799 : { "jersey" : 2,  "name" : "Cade Marlowe" },
            660844 : { "jersey" : 76, "name" : "Leo Rivas" },

            # Bullpen
            676092 : { "jersey" : 52, "name" : "Collin Snider" },
            608723 : { "jersey" : 30, "name" : "Austin Voth" },
            666619 : { "jersey" : 48, "name" : "Gregory Santos" },
            693433 : { "jersey" : 22, "name" : "Bryan Woo" },
            554340 : { "jersey" : 93, "name" : "Yimi García" },
            663423 : { "jersey" : 46, "name" : "Trent Thornton" },
            622491 : { "jersey" : 58, "name" : "Luis Castillo" },
            669923 : { "jersey" : 68, "name" : "George Kirby" },
            662253 : { "jersey" : 75, "name" : "Andrés Muñoz" },
            642048 : { "jersey" : 60, "name" : "Tayler Saucedo" },
            642100 : { "jersey" : 55, "name" : "Gabe Speier" },
            682243 : { "jersey" : 50, "name" : "Bryce Miller" },
        },
        "lefties" : [
            642048, 642100
        ],
        "lineup" : [
            [645302, "8"],
            [668227, "7"],
            [663728, "2"],
            [593871, "4"],
            [670042, "9"],
            [664238, "6"],
            [613564, "3"],
            [571745, "0"],
            [668942, "5"],
        ],
        "bench" : [
            [682988, "1B"],
            [641598, "DH"],
            [687799, "LF"],
            [660844, "SS"],
        ],
        "bullpen" : [
            676092, 608723, 666619, 693433, 554340, 663423, 622491, 669923, 662253, 642048, 642100, 682243
        ],
    },
    "home"   : {
        "team":    "Boston Red Sox",
        "starter": 601713,
        "roster":  {
            # Lineup
            680776 : { "jersey" : 16, "name" : "Jarren Duran" },
            677800 : { "jersey" : 52, "name" : "Wilyer Abreu" },
            807799 : { "jersey" : 7,  "name" : "Masataka Yoshida" },
            646240 : { "jersey" : 11, "name" : "Rafael Devers" },
            641933 : { "jersey" : 17, "name" : "Tyler O'Neill" },
            642086 : { "jersey" : 2,  "name" : "Dominic Smith" },
            657136 : { "jersey" : 12, "name" : "Connor Wong" },
            666152 : { "jersey" : 70, "name" : "David Hamilton" },
            678882 : { "jersey" : 43, "name" : "Ceddanne Rafaela" },

            # Starting pitcher
            601713 : { "jersey" : 37, "name" : "Nick Pivetta" },

            # Bench
            642197 : { "jersey" : 73, "name" : "Jamie Westbrook" },
            663853 : { "jersey" : 23, "name" : "Romy Gonzalez" },
            608701 : { "jersey" : 30, "name" : "Rob Refsnyder" },
            643376 : { "jersey" : 28, "name" : "Danny Jansen" },

            # Bullpen
            677161 : { "jersey" : 76, "name" : "Zack Kelly" },
            572020 : { "jersey" : 65, "name" : "James Paxton" },
            678394 : { "jersey" : 66, "name" : "Brayan Bello" },
            592155 : { "jersey" : 71, "name" : "Cam Booser" },
            445276 : { "jersey" : 74, "name" : "Kenley Jansen" },
            670174 : { "jersey" : 25, "name" : "Josh Winckowski" },
            657514 : { "jersey" : 83, "name" : "Brennan Bernardino" },
            690544 : { "jersey" : 78, "name" : "Bailey Horn" },
            676710 : { "jersey" : 50, "name" : "Kutter Crawford" },
            622259 : { "jersey" : 61, "name" : "Trey Wingenter" },
            681867 : { "jersey" : 64, "name" : "Cooper Criswell" },
            656557 : { "jersey" : 89, "name" : "Tanner Houck" },
        },
        "lefties" : [
            572020, 592155, 657514, 690544
        ],
        "lineup" : [
            [680776, "8"],
            [677800, "9"],
            [807799, "0"],
            [646240, "5"],
            [641933, "7"],
            [642086, "3"],
            [657136, "2"],
            [666152, "4"],
            [678882, "6"],
        ],
        "bench" : [
            [642197, "2B"],
            [663853, "SS"],
            [608701, "RF"],
            [643376, "C" ],
        ],
        "bullpen" : [
            677161, 572020, 678394, 592155, 445276, 670174, 657514, 690544, 676710, 622259, 681867, 656557
        ],
    },
    "umpires" : {
        "HP" : "Andy Fletcher",
        "1B" : "Jansen Visconti",
        "2B" : "Cory Blaser",
        "3B" : "John Bacon",
    },
}
)

##########################################################
# PLAY BALL!
##########################################################


##########################################################
# 1st Inning
##########################################################
# Top 1st
# Pitching: BOS #37 Nick Pivetta
inn = game.new_inning()

# 1. SEA #10 Victor Robles (X - X - X)
inn.new_ab()
inn.pitch_list("s")
inn.out("L9")

# 2. SEA #56 Randy Arozarena (X - X - X)
inn.new_ab()
inn.pitch_list("b c b c f")
inn.out("!K")

# 3. SEA #29 Cal Raleigh (X - X - X)
inn.new_ab()
inn.pitch_list("s c b b b")
inn.out("K")


# Bot 1st
# Pitching: SEA #36 Logan Gilbert
inn = game.new_inning()

# 1. BOS #16 Jarren Duran (X - X - X)
inn.new_ab()
inn.pitch_list("f f b f")
inn.out("K")

# 2. BOS #52 Wilyer Abreu (X - X - X)
inn.new_ab()
inn.pitch_list("c b s b")
inn.out("K")

# 3. BOS #7  Masataka Yoshida (X - X - X)
inn.new_ab()
inn.pitch_list("c")
inn.out("G3-1")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #37 Nick Pivetta
inn = game.new_inning()

# 4. SEA #7  Jorge Polanco (X - X - X)
inn.new_ab()
inn.pitch_list("b b b c c")
inn.out("F9")

# 5. SEA #20 Luke Raley (X - X - X)
inn.new_ab()
inn.pitch_list("c")
inn.out("P6")

# 6. SEA #25 Dylan Moore (X - X - X)
inn.new_ab()
inn.pitch_list("f t b")
inn.out("K")


# Bot 2nd
# Pitching: SEA #36 Logan Gilbert
inn = game.new_inning()

# 4. BOS #11 Rafael Devers (X - X - X)
inn.new_ab()
inn.pitch_list("b s b")
inn.out("G3-1")

# 5. BOS #17 Tyler O'Neill (X - X - X)
inn.new_ab()
inn.pitch_list("b t b c b")
inn.out("L7")

# 6. BOS #2  Dominic Smith (X - X - X)
inn.new_ab()
inn.pitch_list("c s b")
inn.out("K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #37 Nick Pivetta
inn = game.new_inning()

# 7. SEA #35 Jason Vosler (X - X - X)
inn.new_ab()
inn.pitch_list("c f b")
inn.out("K")

# 8. SEA #17 Mitch Haniger (X - X - X)
inn.new_ab()
inn.pitch_list("c b")
inn.hit(1)
inn.advance(2, '4 1B')

# 9. SEA #4  Josh Rojas (X - X - 17)
inn.new_ab()
inn.pitch_list("b b")
inn.hit(1)
inn.thrown_out(2, "10 DP5-4-3", 2, 601713)

# 1. SEA #10 Victor Robles (X - 17 - 4)
inn.new_ab()
inn.pitch_list("f")
inn.out("DP5-4-3")


# Bot 3rd
# Pitching: SEA #36 Logan Gilbert
inn = game.new_inning()

# 7. BOS #12 Connor Wong (X - X - X)
inn.new_ab()
inn.pitch_list("c b f")
inn.hit(1)
inn.advance(2, '43 1B')
inn.advance(3, '16 FC1-6')
inn.advance(4, '52 WP')

# 8. BOS #70 David Hamilton (X - X - 12)
inn.new_ab()
inn.pitch_list("c b b f")
inn.out("!K")

# 9. BOS #43 Ceddanne Rafaela (X - X - 12)
inn.new_ab()
inn.pitch_list("s d s 1")
inn.hit(1)
inn.thrown_out(2, "16 FC1-6", 2, 669302)

# 1. BOS #16 Jarren Duran (X - 12 - 43)
inn.new_ab()
inn.pitch_list("f b d s f")
inn.reach('FC1-6')
inn.advance(2, '52 SB')
inn.advance(3, '52 WP')
inn.advance(4, '52 1B')

# 2. BOS #52 Wilyer Abreu (12 - X - 16)
inn.new_ab()
inn.pitch_list("s s f b b b f pso f f f f")
inn.wp()
inn.hit(1, rbis=1)
inn.advance(4, '7 HR')

# 3. BOS #7  Masataka Yoshida (X - X - 52)
inn.new_ab()
inn.hit(4, rbis=2)

# 4. BOS #11 Rafael Devers (X - X - X)
inn.new_ab()
inn.pitch_list("c b s")
inn.hit(2)
inn.advance(4, '17 2B')

# 5. BOS #17 Tyler O'Neill (X - 11 - X)
inn.new_ab()
inn.hit(2, rbis=1)
inn.advance(4, '2 2B')

# 6. BOS #2  Dominic Smith (X - 17 - X)
inn.new_ab()
inn.pitch_list("b s d c b")
inn.hit(2, rbis=1)
inn.advance(3, '12 PB')
inn.advance(4, '12 2B')

# Pitching change (SEA): #46 Trent Thornton replaces #36 Logan Gilbert
inn.pitching_substitution(663423)

# 7. BOS #12 Connor Wong (X - 2 - X)
inn.new_ab()
inn.pitch_list("b")
inn.pb()
inn.hit(2, rbis=1)
inn.thrown_out(3, "70 CS", 3, 663423)

# 8. BOS #70 David Hamilton (X - 12 - X)
inn.new_ab()
inn.pitch_list("c")
inn.no_ab("CS")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #37 Nick Pivetta
inn = game.new_inning()

# 2. SEA #56 Randy Arozarena (X - X - X)
inn.new_ab()
inn.pitch_list("c")
inn.hit(2)
inn.advance(3, '29 G6-3')
inn.advance(4, '7 SF7')

# 3. SEA #29 Cal Raleigh (X - 56 - X)
inn.new_ab()
inn.pitch_list("b")
inn.out("G6-3")

# 4. SEA #7  Jorge Polanco (56 - X - X)
inn.new_ab()
inn.out("SF7", rbis=1)

# 5. SEA #20 Luke Raley (X - X - X)
inn.new_ab()
inn.pitch_list("c s b")
inn.out("K")


# Bot 4th
# Pitching: SEA #46 Trent Thornton
inn = game.new_inning()

# 8. BOS #70 David Hamilton (X - X - X)
inn.new_ab()
inn.pitch_list("b b c s")
inn.out("G6-3")

# 9. BOS #43 Ceddanne Rafaela (X - X - X)
inn.new_ab()
inn.hit(1)
inn.advance(3, '16 2B')
inn.advance(4, '52 2B')

# 1. BOS #16 Jarren Duran (X - X - 43)
inn.new_ab()
inn.pitch_list("1 f b")
inn.hit(2)
inn.advance(3, '52 2B')
inn.advance(4, '7 1B')

# 2. BOS #52 Wilyer Abreu (43 - 16 - X)
inn.new_ab()
inn.pitch_list("b")
inn.hit(2, rbis=1)
inn.advance(4, '7 1B')

# 3. BOS #7  Masataka Yoshida (16 - 52 - X)
inn.new_ab()
inn.pitch_list("c b b")
inn.hit(1, rbis=2)

# 4. BOS #11 Rafael Devers (X - X - 7)
inn.new_ab()
inn.pitch_list("b b")
inn.out("(F)P5")

# 5. BOS #17 Tyler O'Neill (X - X - 7)
inn.new_ab()
inn.pitch_list("c s")
inn.out("F9")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #37 Nick Pivetta
inn = game.new_inning()

# 6. SEA #25 Dylan Moore (X - X - X)
inn.new_ab()
inn.pitch_list("c b f b")
inn.out("F8")

# 7. SEA #35 Jason Vosler (X - X - X)
inn.new_ab()
inn.pitch_list("f f b b f")
inn.hit(1)

# 8. SEA #17 Mitch Haniger (X - X - 35)
inn.new_ab()
inn.pitch_list("c f b b")
inn.out("!K")

# 9. SEA #4  Josh Rojas (X - X - 35)
inn.new_ab()
inn.pitch_list("c b s b b")
inn.out("K")


# Bot 5th
# Pitching: SEA #46 Trent Thornton
inn = game.new_inning()

# 6. BOS #2  Dominic Smith (X - X - X)
inn.new_ab()
inn.pitch_list("c")
inn.hit(4)

# 7. BOS #12 Connor Wong (X - X - X)
inn.new_ab()
inn.pitch_list("b f t f b f")
inn.out("!K")

# 8. BOS #70 David Hamilton (X - X - X)
inn.new_ab()
inn.pitch_list("f b")
inn.out("F8")

# 9. BOS #43 Ceddanne Rafaela (X - X - X)
inn.new_ab()
inn.pitch_list("c c")
inn.error(4)
inn.reach('E4')
inn.advance(3, '16 2B')
inn.advance('U', '16 2B')

# 1. BOS #16 Jarren Duran (X - X - 43)
inn.new_ab()
inn.pitch_list("f b")
inn.hit(2, rbis=1)

# Pitching change (SEA): #55 Gabe Speier replaces #46 Trent Thornton
inn.pitching_substitution(642100)

# 2. BOS #52 Wilyer Abreu (X - 16 - X)
inn.new_ab()
inn.pitch_list("c f b d b")
inn.out("K")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #37 Nick Pivetta
inn = game.new_inning()

# 1. SEA #10 Victor Robles (X - X - X)
inn.new_ab()
inn.pitch_list("c f b")
inn.out("K")

# 2. SEA #56 Randy Arozarena (X - X - X)
inn.new_ab()
inn.pitch_list("b b c")
inn.hit(4)

# 3. SEA #29 Cal Raleigh (X - X - X)
inn.new_ab()
inn.pitch_list("c s b")
inn.hit(4)

# 4. SEA #7  Jorge Polanco (X - X - X)
inn.new_ab()
inn.pitch_list("f b f b")
inn.out("K")

# 5. SEA #20 Luke Raley (X - X - X)
inn.new_ab()
inn.pitch_list("f")
inn.out("L6")


# Bot 6th
# Pitching: SEA #55 Gabe Speier
inn = game.new_inning()

# Defensive change (SEA): #76 Leo Rivas replaces #7 Jorge Polanco (2B), playing 2B, batting 4th
inn.defensive_substitution(4, 660844, "4")

# 3. BOS #7  Masataka Yoshida (X - X - X)
inn.new_ab()
inn.hit(2)
inn.advance(4, '23 HR')

# Offensive change (BOS): Pinch-hitter #23 Romy Gonzalez replaces #11 Rafael Devers, batting 4th
inn.offensive_substitution(4, 663853, "PH")

# 4. BOS #23 Romy Gonzalez (X - 7 - X)
inn.new_ab()
inn.pitch_list("b")
inn.hit(4, rbis=2)

# 5. BOS #17 Tyler O'Neill (X - X - X)
inn.new_ab()
inn.pitch_list("c f b b f b")
inn.out("K")

# 6. BOS #2  Dominic Smith (X - X - X)
inn.new_ab()
inn.pitch_list("c c b")
inn.out("K")

# 7. BOS #12 Connor Wong (X - X - X)
inn.new_ab()
inn.pitch_list("f c b b f b")
inn.out("L7")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #37 Nick Pivetta
inn = game.new_inning()

# Defensive switch (BOS): #23 Romy Gonzalez moves to 3B
inn.defensive_switch(663853, "5")

# 6. SEA #25 Dylan Moore (X - X - X)
inn.new_ab()
inn.pitch_list("c f b f")
inn.error(5)
inn.reach('E5')
inn.advance(2, '4 DI')
inn.thrown_out(3, "10 FC5", 3, 622259)

# 7. SEA #35 Jason Vosler (X - X - 25)
inn.new_ab()
inn.pitch_list("c f f")
inn.out("K")

# 8. SEA #17 Mitch Haniger (X - X - 25)
inn.new_ab()
inn.pitch_list("c b b b s f pso")
inn.out("(F)P5")

# 9. SEA #4  Josh Rojas (X - X - 25)
inn.new_ab()
inn.pitch_list("d b b c")
inn.reach('BB')

# Pitching change (BOS): #61 Trey Wingenter replaces #37 Nick Pivetta
inn.pitching_substitution(622259)

# 1. SEA #10 Victor Robles (X - 25 - 4)
inn.new_ab()
inn.pitch_list("f f b b")
inn.reach('FC5')


# Bot 7th
# Pitching: SEA #52 Collin Snider
inn = game.new_inning()

# Pitching change (SEA): #52 Collin Snider replaces #55 Gabe Speier
inn.pitching_substitution(676092)

# Defensive switch (SEA): #10 Victor Robles moves to LF
inn.defensive_switch(645302, "7")

# Defensive change (SEA): #2 Cade Marlowe replaces #56 Randy Arozarena (LF), playing CF, batting 2nd
inn.defensive_substitution(2, 687799, "8")

# 8. BOS #70 David Hamilton (X - X - X)
inn.new_ab()
inn.pitch_list("f b b c")
inn.out("G3-1")

# 9. BOS #43 Ceddanne Rafaela (X - X - X)
inn.new_ab()
inn.pitch_list("s")
inn.out("(F)P3")

# Offensive change (BOS): Pinch-hitter #73 Jamie Westbrook replaces #16 Jarren Duran, batting 1st
inn.offensive_substitution(1, 642197, "PH")

# 1. BOS #73 Jamie Westbrook (X - X - X)
inn.new_ab()
inn.pitch_list("b c b c b f")
inn.out("KT")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #61 Trey Wingenter
inn = game.new_inning()

# Defensive switch (BOS): #73 Jamie Westbrook moves to 2B
inn.defensive_switch(642197, "4")

# Defensive switch (BOS): #70 David Hamilton moves to SS
inn.defensive_switch(666152, "6")

# Defensive switch (BOS): #43 Ceddanne Rafaela moves to CF
inn.defensive_switch(678882, "8")

# 2. SEA #2  Cade Marlowe (X - X - X)
inn.new_ab()
inn.pitch_list("f b b s f")
inn.out("!K")

# 3. SEA #29 Cal Raleigh (X - X - X)
inn.new_ab()
inn.pitch_list("s b s b f b")
inn.hit(1)
inn.advance(2, '76 1B')
inn.advance(3, '20 BB')
inn.advance(4, '25 2B')

# 4. SEA #76 Leo Rivas (X - X - 29)
inn.new_ab()
inn.hit(1)
inn.advance(2, '20 BB')
inn.advance(4, '25 2B')

# 5. SEA #20 Luke Raley (X - 29 - 76)
inn.new_ab()
inn.pitch_list("b d b c")
inn.reach('BB')
inn.advance(3, '25 2B')
inn.advance(4, '35 WP')

# 6. SEA #25 Dylan Moore (29 - 76 - 20)
inn.new_ab()
inn.pitch_list("b")
inn.hit(2, rbis=2)
inn.advance(3, '35 WP')
inn.advance(4, '35 G4-3')

# 7. SEA #35 Jason Vosler (20 - 25 - X)
inn.new_ab()
inn.pitch_list("s s b")
inn.wp()
inn.out("G4-3", rbis=1)

# 8. SEA #17 Mitch Haniger (X - X - X)
inn.new_ab()
inn.pitch_list("f b b s b")
inn.out("K")


# Bot 8th
# Pitching: SEA #60 Tayler Saucedo
inn = game.new_inning()

# Pitching change (SEA): #60 Tayler Saucedo replaces #52 Collin Snider
inn.pitching_substitution(642048)

# Defensive switch (SEA): #35 Jason Vosler moves to LF
inn.defensive_switch(613564, "7")

# Defensive change (SEA): #27 Tyler Locklear replaces #10 Victor Robles (LF), playing 1B, batting 1st
inn.defensive_substitution(1, 682988, "3")

# 2. BOS #52 Wilyer Abreu (X - X - X)
inn.new_ab()
inn.pitch_list("c")
inn.out("P6")

# 3. BOS #7  Masataka Yoshida (X - X - X)
inn.new_ab()
inn.out("G4-3")

# 4. BOS #23 Romy Gonzalez (X - X - X)
inn.new_ab()
inn.pitch_list("c b b b")
inn.reach('BB')

# 5. BOS #17 Tyler O'Neill (X - X - 23)
inn.new_ab()
inn.out("G4-3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #78 Bailey Horn
inn = game.new_inning()

# Pitching change (BOS): #78 Bailey Horn replaces #61 Trey Wingenter
inn.pitching_substitution(690544)

# 9. SEA #4  Josh Rojas (X - X - X)
inn.new_ab()
inn.hit(1)

# 1. SEA #27 Tyler Locklear (X - X - 4)
inn.new_ab()
inn.pitch_list("s c")
inn.out("!K")

# 2. SEA #2  Cade Marlowe (X - X - 4)
inn.new_ab()
inn.pitch_list("s")
inn.out("F7")

# 3. SEA #29 Cal Raleigh (X - X - 4)
inn.new_ab()
inn.out("(F)P5")

# Winning team: BOS
# WP: BOS #37 Nick Pivetta
game.winning_pitcher(601713)

# Loser team: SEA
# LP: SEA #36 Logan Gilbert
game.losing_pitcher(669302, is_away_team=True)

#print(game)
game.generate_scorecard()