# Baseball Scorecard Generator

Baseball Scorecard Generator offers a Python API to generate a series of
Metapost files that can be compiled into a scorecard PDF.

* 1. [How to score a game](#Howtoscoreagame)
	* 1.1. [Setting up the game data](#Settingupthegamedata)
		* 1.1.1. [Roster](#Roster)
	* 1.2. [Play ball!](#Playball)
		* 1.2.1. [Pitching substitution](#Pitchingsubstitution)
		* 1.2.2. [Defensive substitution](#Defensivesubstitution)
		* 1.2.3. [Defensive switch](#Defensiveswitch)
		* 1.2.4. [Offensive substitution](#Offensivesubstitution)
		* 1.2.5. [At-bat](#At-bat)
	* 1.3. [Noting win/loss/save pitchers](#Notingwinlosssavepitchers)
	* 1.4. [Generating the Metapost files](#GeneratingtheMetapostfiles)
	* 1.5. [Generating the PDF](#GeneratingthePDF)
* 2. [Appendix](#Appendix)
	* 2.1. [Normal game data example](#Normalgamedataexample)
	* 2.2. [Extended roster game data example](#Extendedrostergamedataexample)
* 3. [Credits](#Credits)

##  1. <a name='Howtoscoreagame'></a>How to score a game

_Note: Example games and how to score certain plays are provided in the_
_`examples` folder._

In order to start scoring a game, import the `scorecard` module on your
Python script, and create a `Scorecard` object:

```
from scorecard import Scorecard

score = Scorecard(...)
```

The `Scorecard` class expects two parameters:

- `output_dir`: The location where the Metapost files will be deposited.
- `data`: The data for the game to be scored.

###  1.1. <a name='Settingupthegamedata'></a>Setting up the game data

The game data expects the following information:

- `extended_roster` (optional): If set to True, a different format for the roster
  is expected for each team. Check the [roster section](#roster) of this
  document for more information.
- `scorer`: Name of the scorer.
- `date`: Date of the game.
- `at`: Baseball stadium where the game took place.
- `att`: Official attendance.
- `temp`: Temperature and weather at first pitch.
- `wind`: Wind at first pitch.
- `away`: Information about the away team.
- `home`: Information about the home team.
- `umpires`: Information about the umpires.

For each team, the following information is expected:
- `team`: Name of the team.
- `starter`: Player ID for the starting pitcher.
- `roster`: Dictionary of the players in the team.
- `lefties`: List of player IDs for all left-handed pitchers.
- `lineup`: List representing the lineup, each item is a list containing
  the player ID and their fielding position.
- `bench`: List of player IDs that start the game in the bench.
- `bullpen`: List of player IDs that start the game in the bullpen.

For the umpire information, a dictionary is expected, where the keys are the
position, and the value is the name of the umpire.
Valid keys are `HP`, `1B`, `2B`, `3B`, `LF` and `RF`.

####  1.1.1. <a name='Roster'></a>Roster

The `roster` for a team is expected to be a key-value pair, where the key
represents the **Player ID**, and the value is the player information.

The format for the player information varies whether the `extended_roster`
key on the data dictionary was set or not:

- If the key is not set, the **Player ID** can be their jersey number, and the
  player data can be their name.
- If the key is set, the format becomes the following:
  `1000: {"jersey": 1, "name": "John Doe"}`.
  `1000` becomes the **Player ID**, and the jersey number and name of the
  player can be specified in the inner dictionary.

###  1.2. <a name='Playball'></a>Play ball!

Once the `Scorecard` object is created, the game can be recorded.

Start each frame by calling the `Scorecard.new_inning` method.

```
inn = score.new_inning()
```

From here, you can call the following functions:

####  1.2.1. <a name='Pitchingsubstitution'></a>Pitching substitution

To register a pitching substitution, call the `pitching_substitution` method.

```
inn.pitching_substitution(PITCHER_ID)
```

Arguments:
- `PITCHER_ID` (int): Player ID for the entering pitcher.

####  1.2.2. <a name='Defensivesubstitution'></a>Defensive substitution

To register a defensive substitution, call the `defensive_substitution` method.

```
inn.defensive_substitution(ORDER, PLAYER_ID, POSITION)
```

Arguments:
- `ORDER` (int): Order in the lineup where the fielder will bat (1-9).
- `PLAYER_ID` (int): Player ID for the entering fielder.
- `POSITION` (str): Position in the field for the new player.

####  1.2.3. <a name='Defensiveswitch'></a>Defensive switch

To register a defensive switch, call the `defensive_switch` method.

```
inn.defensive_switch(PLAYER_ID, POSITION)
```

Arguments:
- `PLAYER_ID` (int): Player ID for the fielder.
- `POSITION` (str): New defensive position for the fielder.

####  1.2.4. <a name='Offensivesubstitution'></a>Offensive substitution

To register a offensive substitution, call the `offensive_substitution` method.

```
inn.offensive_substitution(ORDER, PLAYER_ID, POSITION)
```

Arguments:
- `ORDER` (int): Order in the lineup where the batter will bat (1-9).
- `PLAYER_ID` (int): Player ID for the entering batter.
- `POSITION` (str): Position for the new player, can be either `PH` for a
  pinch-hitter, or `PR` for a pinch-runner.

####  1.2.5. <a name='At-bat'></a>At-bat

To start a new at-bat, call the `new_ab` method. This will automatically start
an at-bat for the next batter on the batting team.

```
inn.new_ab()
```

Once an at-bat is started, the following methods can be called:

##### Pitches

To register the pitches a batter received, use the `pitch_list` method.

```
inn.pitch_list(PITCHES)
```

Arguments:
- `PITCHES` (str): List of pitches, each pitch separated by a space.
  The following codes are recognized:
  - `pso`: Pitcher step-off.
  - `1`, `2` or `3`: Pickoff attempts at 1B, 2B or 3B.
  - `vp`: Pitch clock violation on the pitcher, counts as a ball.
  - `ab`: Pitch clock violation on the batter, counts as a strike.
  - `s`: Swinging strike.
  - `c`: Called strike.
  - `f`: Foul.
  - `b`: Ball.
  - `d`: Ball in dirt.
  - `p`: Pitchout, counts as a ball.
  - `m`: Missed bunt attempt.
  - `t`: Foul tip.
  - `l`: Foul bunt.
  ***NOTE***: For balls put in play, it is not necessary to add a pitch, the
  batter functions will handle the pitch count automatically.

##### Hit

To register a hit on the at-bat, use the `hit` method.

```
inn.hit(BASES, [RBIS])
```

Arguments:
- `BASES` (int/str): The amount of bases the hit allowed, from 1-4.
  In case the hit is classified as an unearned home run, use `"U"`.
- `RBIS` (int, optional): If the play resulted in runs batted in, set the
  number of RBIs. Default is 0.

##### Out

To register an out on the batter, use the `out` method.

```
inn.out(PLAY, [RBIS])
```

Arguments:
- `PLAY` (str): The play on which the out was made.
  Starting the play with the following codes will automatically tally
  certain statistics:
  - `K`: Swinging strikeout.
  - `!K`: Called strikeout.
  - `SAC`: Sacrifice bunt.
  - `SF`: Sacrifice fly.
  - `DP`: Double play.
  - `TP`: Triple play.
- `RBIS` (int, optional): If the play resulted in runs batted in, set the
  number of RBIs. Default is 0.

##### Reach base

To register the batter reaching base in a non-hit play, use the `reach` method.

```
inn.reach(PLAY, [END_BASE], [RBIS])
```

Arguments:
- `PLAY` (str): The play on which the batter reached base.
  Starting the play with the following codes will automatically tally
  certain statistics:
  - `E`: Fielding error.
  - `BB`: Base on Balls.
  - `IBB`: Intent walk.
  - `HBP`: Hit by pitch.
  - `CI`: Catcher's interference.
  - `K`: Strikeout.
- `END_BASE` (int, optional): If the batter-runner reached past 1B, use this
  argument. Default is 1 for 1B.
- `RBIS` (int, optional): If the play resulted in runs batted in, set the
  number of RBIs. Default is 0.

##### Advance bases

To register a runner advancing bases, use the `advance` method.

```
inn.advance(END_BASE, PLAY)
```

Arguments:
- `END_BASE` (int/str): The final base reached by the batter on a play.
  - `2`: Second base.
  - `3`: Third base.
  - `4`: Home, for an earned run.
  - `U`: Home, for an unearned run.
- `PLAY` (str): The play on which the runner advanced. If `SB` is used in the
  play, a stolen base is credited to the runner.

##### Thrown out

To register a runner getting thrown out in the basepaths,
use the `thrown_out` method.

```
inn.thrown_out(OUT_BASE, PLAY, [OUT_NUMBER], [PITCHER_ID])
```

Arguments:
- `OUT_BASE` (int): The final base reached by the batter on a play.
  - `2`: Second base.
  - `3`: Third base.
  - `4`: Home, for an earned run.
  - `U`: Home, for an unearned run.
- `PLAY` (str): The play on which the runner advanced.
  If `CS` is used in the play, a caught stealing is credited to the runner.
  IF `PO` is used in the play, a pickoff is credited to the runner.
- `OUT_NUMBER` (int, optional): Specific out number to use, otherwise the
  scorecard will assign the next available out.
- `PITCHER_ID` (int, optional): Player ID of the pitcher that made the out.
  Useful for when pitching changes occur mid-inning and the new pitcher makes
  an out on an inherited runner.

##### Error

To register a fielding error, use the `error` method.

```
inn.error(POSITION)
```

Arguments:
- `POSITION`: Position of the fielder who made the error (1-9).

##### Balk

To register a balk, use the `balk` method.

```
inn.balk()
```

##### Wild pitch

To register a wild pitch, use the `wp` method.

```
inn.wp([QUANTITY])
```

Arguments:
- `QUANTITY` (int, optional): The number of wild pitches in the at-bat.
  Defaults to 1.

##### Passed ball

To register a passed ball, use the `pb` method.

```
inn.pb([QUANTITY])
```

Arguments:
- `QUANTITY` (int, optional): The number of passed balls in the at-bat.
  Defaults to 1.

##### At base

To make a comment at any given base, use the `atbase` method. Useful for
noting down pinch-runners.

```
inn.atbase(LABEL, [BASE])
```

Arguments:
- `LABEL` (str): The label to put at a given base.
- `BASE` (int, optional): The base to put the label at. By default, it will be
  placed at 1B.

##### No at-bat

To register that the batter was unable to complete their at-bat, likely
due to the third out made on one of the runners in the middle of an at-bat,
call the `no_ab` method.

```
inn.no_ab(LABEL)
```

Arguments:
- `LABEL` (str): Label to put in the center of the diamond.

###  1.3. <a name='Notingwinlosssavepitchers'></a>Noting win/loss/save pitchers

Once the game has been recorded, note down the winning pitcher, losing pitcher
and save pitcher with the following methods:

```
score.winning_pitcher(PITCHER_ID, [IS_AWAY_TEAM])
score.losing_pitcher(PITCHER_ID, [IS_AWAY_TEAM])
score.save_pitcher(PITCHER_ID, [IS_AWAY_TEAM])
```

Arguments:
- `PITCHER_ID` (int): The player ID for the pitcher.
- `IS_AWAY_TEAM` (bool): If the pitcher is from the away team, set this to `True`.
  Defaults to `False`, which credits a pitcher from the home team.

###  1.4. <a name='GeneratingtheMetapostfiles'></a>Generating the Metapost files

Once all the plays have been registered, and the winning/losing/save pitchers
have been registered, run the `generate_scorecard` method to generate
the Metapost scorecards.

```
score.generate_scorecard()
```

###  1.5. <a name='GeneratingthePDF'></a>Generating the PDF

Currently, integration with the Metapost compiler is not available.
A compilation script is provided in the `examples` folder.

##  2. <a name='Appendix'></a>Appendix

###  2.1. <a name='Normalgamedataexample'></a>Normal game data example

Below is an example of a complete game data dictionary, taken from the
New York Yankees @ Boston Red Sox 2018-08-03 game.

```
{
    "scorer": "Vicyorus",
    "date":   "2018-08-03 19:10-21:25",
    "at":     "Fenway Park, Boston, MA",
    "att":    "37,231",
    "temp":   "87F, Partly Cloudy",
    "wind":   "21mph, Out To CF",
    "away"   : {
        "team":    "New York Yankees",
        "starter": 40,
        "roster":  {
            # Lineup
            11 : "Brett Gardner",
            27 : "Giancarlo Stanton",
            18 : "Didi Gregorius",
            31 : "Aaron Hicks",
            25 : "Gleyber Torres",
            33 : "Greg Bird",
            41 : "Miguel Andujar",
            28 : "Austin Romine",
            14 : "Neil Walker",

            # Starting pitcher
            40 : "Luis Severino",

            # Bench
            66 : "Kyle Higashioka",
            38 : "Shane Robinson",
            45 : "Luke Voit",

            # Bullpen
            67 : "A.J. Cole",
            68 : "Dellin Betances",
            36 : "Lance Lynn",
            55 : "Sonny Gray",
            56 : "Jonathan Holder",
            52 : "CC Sabathia",
            53 : "Zack Britton",
            19 : "Masahiro Tanaka",
            57 : "Chad Green",
            48 : "Tommy Kahnle",
            30 : "David Robertson",
            54 : "Aroldis Chapman",
        },
        "lefties" : [
            52, 53, 54
        ],
        "lineup" : [
            [11, "7"],
            [27, "9"],
            [18, "6"],
            [31, "8"],
            [25, "4"],
            [33, "3"],
            [41, "0"],
            [28, "2"],
            [14, "5"],
        ],
        "bench" : [
            [66, "C" ],
            [38, "CF"],
            [45, "1B"],
        ],
        "bullpen" : [
            67, 68, 36, 55, 56, 52, 53, 19, 57, 48, 30, 54
        ],
    },
    "home"   : {
        "team":    "Boston Red Sox",
        "starter": 22,
        "roster":  {
            # Lineup
            50 : "Mookie Betts",
            16 : "Andrew Benintendi",
            25 : "Steve Pearce",
            28 : "J.D. Martinez",
            5  : "Ian Kinsler",
            36 : "Eduardo Núñez",
            12 : "Brock Holt",
            3  : "Sandy León",
            19 : "Jackie Bradley Jr.",

            # Starting pitcher
            22 : "Rick Porcello",

            # Bench
            18 : "Mitch Moreland",
            68 : "Dan Butler",
            2  : "Xander Bogaerts",

            # Bullpen
            47 : "Tyler Thornburg",
            44 : "Brandon Workman",
            31 : "Drew Pomeranz",
            61 : "Brian Johnson",
            37 : "Heath Hembree",
            24 : "David Price",
            46 : "Craig Kimbrel",
            76 : "Hector Velázquez",
            70 : "Ryan Brasier",
            56 : "Joe Kelly",
            17 : "Nathan Eovaldi",
            32 : "Matt Barnes",
        },
        "lefties" : [
            31, 61, 24
        ],
        "lineup" : [
            [50, "9"],
            [16, "7"],
            [25, "3"],
            [28, "0"],
            [5,  "4"],
            [36, "5"],
            [12, "6"],
            [3,  "2"],
            [19, "8"],
        ],
        "bench" : [
            [18, "1B"],
            [68, "C" ],
            [2,  "2B"],
        ],
        "bullpen" : [
            47, 44, 31, 61, 37, 24, 46, 76, 70, 56, 17, 32
        ],
    },
    "umpires" : {
        "HP" : "Adam Hamari",
        "1B" : "Phil Cuzzi",
        "2B" : "Chris Conroy",
        "3B" : "Dan Bellino",
    },
}
```

###  2.2. <a name='Extendedrostergamedataexample'></a>Extended roster game data example

The following is an example of the game data if the `extended_roster` key
is set to `True`, taken from the Seattle Mariners @ Boston Red Sox
2024-07-29 game.

The player IDs in this example correspond to the MLB.com IDs for each player.

```
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
```

##  3. <a name='Credits'></a>Credits

This project is heavily based on the work by Chris Nandor
(https://sourceforge.net/projects/pudge/files/Games_Baseball_Scorecard/),
and uses a modified version of the Metapost scorecard template created by
Christopher Swingley (https://swingleydev.com/baseball/scorecards.php).
