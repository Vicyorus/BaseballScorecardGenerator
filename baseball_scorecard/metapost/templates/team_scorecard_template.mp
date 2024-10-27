%prologues:=2;
verbatimtex
\documentclass{article}
\usepackage[utf8]{inputenc}
\begin{document}
etex
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
% Copyright (C) 2005, Christopher Swingley
%
% Licensed under the terms of the GNU General Public License, Version 2
% available from http://www.gnu.org/copyleft/gpl.html
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
% The following Metapost program draws baseball scorecards as well as
% allows you to record plays on the same card.  It contains two figures.
% Figure 0 is a complete, unfilled scorecard that can be converted to PDF
% and printed.
%
% Figure 2 is an example, showing the Cardinals scoring from the game
% where Mark McGwire broke Roger Maris' home run record.
%
% Figure 1 is the Cubs scoring from the same game
%
% A few variables can be set at the beginning of the card to adjust
% colors and line thicknesses and other parameters.  Also note that
% I am using Adobe's Myriad Condensed fonts for the scorecard, so
% you will need to modify the font names to suit your own preferences
% and fonts.
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
% Manual for metapost:
%   $ texdoc mpman
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
% Locations for stuff:
%
%    ballone, balltwo, ballthree, ballfour,
%    strikeone, striketwo, strikethree, strikefour, strikefive, strikesix
%    strikeseven, strikeeight, strikenine, striketen, strikeeleven, striketwelve
%    strikethirteen, strikefourteen, strikefifteen, strikesixteen, strikeseventeen, strikeeighteen
%    strikenineteen, striketwenty, striketwentyone, striketwentytwo
%
%       These are the locations for writing in the pitch counts to each
%       batter:
%           draw_strike_dot(ballone, clr);
%           draw_strike_circle(strikeone, clr);
%
%    rbione, rbitwo, rbithree, rbifour, rundot, outlabel
%
%       These are the locations for RBI diamonds, run dots/cross (in the middle
%       of the diamond), and the out labels (which also go in the middle
%       of the diamond):
%           draw_diamond(rbione, clr);
%           draw_diamond(rbitwo, clr);
%           draw_dot(rundot, clr);
%           draw_cross(rundot, clr);
%           label(btex {\bigsf G6-3} etex, outlabel) withcolor clr;
%
%    playloc
%
%       Location for the main play, primarily for hits, walks and hit by pitches.
%           label(btex {\midsf 1B} etex, playloc) withcolor hit;
%
%    first, second, third, home
%
%       Locations of the bases.  Mostly used for building the paths,
%       but also useful for pinch runners:
%           label.top(btex {\sf PR} etex, second) withcolor clr;
%
%    wayfirst, waysecond, waythird, wayhome
%
%       The half-way points between bases.  Used as part of the CS and
%       TO paths, but also useful for labelling CS and TO plays:
%           label.lft(btex {\sf TO 7-2} etex, wayhome) withcolor clr;
%
% Paths available:
%    single, double, triple, homerun
%
%       Paths showing a runner's progress on the bases:
%           draw(double) withcolor clr;
%
%    firstsecond, firstthird, firsthome, secondthird, secondhome,
%    thirdhome
%
%       Paths for runners along the bases:
%           draw(secondhome) withcolor clr;
%
%    ifleft, ifright, ifcenter, ofleft, ofleftc, ofcenterl, ofcenterr,
%    ofrightc, ofright
%
%       Paths for various type of hits (infield, outfield):
%           draw(ofleftc) withcolor clr;
%
%    hrleft, hrleftc, hrcenterl, hrcenterr, hrrightc, hrright;
%
%       Paths for home runs:
%           draw(hrleftc) withcolor clr;
%
%    cs_second, cs_third, to_home,
%    cs_firstthird, to_firsthome, to_secondhome,
%
%       Paths for caught stealing and thrown out:
%           draw(cs_second) withcolor clr;
%
%    new_hitter, new_pitcher
%
%       Paths for new hitters (left side of box) and pitchers
%       (top of box)
%           draw(new_hitter) withcolor clr;
%           draw(new_pitcher) withcolor clr;
%
% Fonts:
%
%   \tiny   - used for tallying pitches.
%   \sf     - used for various labelling and basepath plays.
%   \midsf  - used for various labelling and batter results.
%   \bigsf  - used for various labelling and out labels.
%
% Normal functions:
%
%   draw(path) withcolor clr;                       - stroke a path
%   label(btex {\sf 1} etex, pair) withcolor clr;   - label
%       directional suffixes: lft,rt,top,bot,ulft,urt,llft,lrt
%   label(btex {\sf (6 empty boxes)} etex,                  \
%       1/2[(xstart, ystart-25),(xstart+100,ystart-25)]) \
%       withcolor clr;  - use this when the lineup turns over
%
% User functions:
%
%
%   def set_game_info_vars(expr innings) =
%       Sets the locations for all the general info about the game (location, team, scorer, etc).
%       Expects the number of innings that the scorecard will hold.
%
%   def set_batter_name_vars(expr lineup_pos, lineup_line) =
%
%       Sets the location variables for a batter's information in the lineup.
%       Expects the position in the lineup (1-9), and the specific spot in the position (1-4).
%
%   def set_extra_batter_name_vars(expr extra_num) =
%
%       Sets the location variables for a batter's information in the extra batters spot.
%       Expects the number of row to use for the extra batter (1-6).
%
%   def set_pitcher_name_vars(expr pitcher_num) =
%
%       Sets the location variables for a pitcher's information in the pitcher lineup.
%       Expects the position in the lineup (1-12).
%
%   def set_bench_name_vars(expr bench_num) =
%
%       Sets the location variables for a player's information in the bench.
%       Expects the position in the bench (1-7).
%
%   def set_bullpen_name_vars(expr bullpen_num) =
%
%       Sets the location variables for a pitcher's information in the bullpen.
%       Expects the position in the bullpen (1-14).
%
%   def set_batter_total_vars(expr lineup_pos, lineup_line, innings) =
%
%       Sets the location variables for a batter's game totals.
%       Expects the position in the lineup (1-9), the specific spot in the position (1-4),
%       and the number of innings that the scorecard will hold.
%
%   def set_pitcher_total_vars(expr pitcher_num) =
%
%       Sets the location variables for a pitcher's game totals.
%       Expects the position in the lineup (1-12).
%
%   def set_inning_num_label_vars(expr xstart) =
%
%       Sets the location variables for the inning numbering labels (both top and bottom).
%       Expects the xstart of the inning column to use.
%
%   def set_inning_total_vars(expr xstart) =
%
%       Sets the location variables for the inning numbering labels (both top and bottom).
%       Expects the xstart of the inning column to use.
%
%   def set_game_total_vars(innings) =
%
%       Sets the location variables for tallying the game's totals (runs, hits, errors, etc).
%       Expects the number of innings that the scorecard will hold.
%
%   def set_basepath_total_vars(innings) =
%
%       Sets the location varaibles to tally a team's basepath's totals (hits, sacrifices, stolen bases, etc).
%       Expects the number of innings that the scorecard will hold.
%
%   def set_vars(expr xstart, ystart) =
%
%       Used to initialize all the locations and paths for a new
%       starting locations.  Needs to be called right after setting
%       xstart and ystart.  These should be multiples of 128.
%
%   def draw_at_bat_box(expr xstart, ystart) =
%
%       Draws an at-bat box in cyan
%
%   def draw_out_[one|two|three](expr xstart, ystart, clr) =
%
%       Indicates the first (second or third) out with the out number
%       in a circle.
%
%   def draw_dot(expr loc, clr) =
%
%       Draws a 7pt dot at the location indicated.
%       Used for noting an earned run.
%
%   def draw_cross(expr loc, clr) =
%
%       Draws an X at the location indicated.
%       Used for noting an unearned run.
%
%   def draw_strike_dot(expr loc, clr) =
%
%       Draws a 5pt dot at the location indicated.
%       Used for pitches, recommended for swinging strikes.
%
%   def draw_strike_circle(expr loc, clr) =
%
%       Draws a circle at the location indicated.
%       Used for pitches, recommended for called strikes.
%
%   def draw_diamond(expr loc, clr) =
%
%       Draws a diamond with a radius of 3.75 at the location indicated.
%       Recommended to be used for RBIs.
%
%   def draw_inning_end(expr xstart, ystart, clr) =
%
%       Draws the slash in the lower right that signals the end of
%       the inning.
%
%   def draw_inning_start(expr xstart, ystart, clr) =
%
%       Draws the slash in the upper left that signals the start of
%       the inning.
%
%   def draw_strikeout_looking(expr outlabel, clr) =
%
%       Draws a backwards K
%
% Consult the Makefile for the commands used to turn the code in  this
% file into PDF, EPS or PNG files.
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
%   Sun Oct 20 12:41 UTC-6 2024
%       * Removed the basepath error stat, replaced it with RISP.
%       * Vicyorus
%
%   Tue Sep 11 15:33 UTC-6 2024
%       * Rewrote the scorecard function to allow for a variable
%         number of innings.
%       * Moved the location of the out numbers to the top right
%         corner of the at-bat box, to avoid colissions with longer
%         texts in the basepath from home to 1B.
%       * Vicyorus
%
%   Thu Aug 22 23:00 UTC-6 2024
%       * Rewrote the at-bat box to include the following:
%           * Boxes for pitch tracking of balls and strikes.
%           * Functions to draw dots, circles and crosses in the
%             balls and strikes boxes.
%           * Function to draw RBI diamonds to tally RBIs in a play.
%           * Elimination of the circled plays, replaced by a box to
%             place the result of the play (barring outs).
%       * Added missing documentation for several new methods.
%       * Vicyorus
%
%   Fri May 5 22:00 UTC-6 2024
%       * Rewrote the scorecard code to include the following:
%           * One additional batter per position in the lineup.
%           * Bigger at-bat boxes, to allow for proper labelling
%                of runner movements.
%           * Totals for batter results (AB/H/R/RBI/K/BB).
%           * Box for pitching totals.
%       * Vicyorus
%
%   Wed Apr 20 07:58:23 AKDT 2005
%       * Reversed figures 1 and 2 so the scoring of the game is in
%           order
%       * Added more comments to the beginning of the file
%       * Christopher Swingley, cswingle@iarc.uaf.edu
%
%   Sat Apr 16 13:33:14 AKDT 2005
%       * scoring.mp Version 0.2
%       * Pulled out a bunch of variables
%       * Finished the full scorecard code
%       * Christopher Swingley, cswingle@iarc.uaf.edu
%
%   Thu Apr 14 14:37:29 AKDT 2005
%       * scoring.mp Version 0.1
%       * Initial release
%       * Christopher Swingley, cswingle@iarc.uaf.edu
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% FONTS
verbatimtex \font\tiny     phvrrn at 8pt etex
verbatimtex \font\sf       phvbrn at 12pt etex
verbatimtex \font\midsf    phvbrn at 16pt etex
verbatimtex \font\bigsf    phvbrn at 18pt etex

% COLOR VARIABLES
color card;
color scoring;
color hit;
color homer;
color walk;
color error;
color outclr;
color pitcherclr;
color batterclr;
color innendclr;
% Cyan card - modify first number to control lightness
% (0 - 1, dark - light):
% card:=(0.10,1,1);  % Darker
% card:=(0.25,1,1);  % Lighter
% Grey card:
% card:=(0.4,0.4,0.4);
% Black card:
% card:=(0.0,0.0,0.0);
card:=(0,0,0);
% Black scoring color
scoring:=(0,0,0);
% Out color = red
outclr:=(1,0,0);
% Hit color = blue
hit:=(0,0,1);
% Home Run color = Purple
homer:=(0.321568627,0,0.717647059);
% Walk color = Green
walk:=(0,0.560784314,0.223529412);
% Error color = Orange
error:=(1,0.505882353,0);
% New pitcher color
pitcherclr:=walk;
% New batter color
batterclr:=hit;
% Inning end color
innendclr:=outclr;

% VARIABLES
% Diameter of circles (outs)
outcircle_d := 7;
% Size of dots (rbi, runs scored)
dotsize := 7pt;
% Thickness of play lines
playline_t := 1.5pt;
% Thickness of thick card lines
thickline_t := 0.5pt;
% Thickness of thin card lines
thinline_t := 0.05pt;
% Thickness of strikethrough lines
strikethrough_t := 1.0pt;
% Size of strike dots
strikedot := 5pt;
% Diameter of called strike circles
called_strike_d := 2;

def draw_at_bat_box(expr xstart, ystart) =
    begingroup
        pickup pencircle scaled thickline_t;

        % Outer box
        box_size := 128;
        draw (xstart,ystart)--(xstart,ystart+box_size)--(xstart+box_size,ystart+box_size)--(xstart+box_size,ystart)--cycle withcolor card;
        pickup pencircle scaled thinline_t;

        % Diamond
        dsize := 28;
        basesize := 5;
        dxstart := xstart+64;
        dystart := ystart+38;
        ofactor := 1.5;

        % New diamond
        %% Home
        draw (dxstart-basesize,dystart+basesize)--(dxstart,dystart)--(dxstart+basesize,dystart+basesize) withcolor card;
        %% 1B
        draw (dxstart+dsize-basesize,dystart+dsize-basesize)--(dxstart+dsize,dystart+dsize)--(dxstart+dsize-basesize,dystart+dsize+basesize) withcolor card;
        %% 2B
        draw (dxstart-basesize,dystart+dsize*2-basesize)--(dxstart,dystart+dsize*2)--(dxstart+basesize,dystart+dsize*2-basesize) withcolor card;
        %% 3B
        draw (dxstart-dsize+basesize,dystart+dsize+basesize)--(dxstart-dsize,dystart+dsize)--(dxstart-dsize+basesize,dystart+dsize-basesize) withcolor card;

        % Outfield
        draw (dxstart+dsize,dystart+dsize)--(dxstart+(dsize*ofactor),dystart+(dsize*ofactor))..(dxstart,dystart+(2*dsize*ofactor))..(dxstart-(dsize*ofactor),dystart+(dsize*ofactor))--(dxstart-dsize,dystart+dsize) withcolor card;

        % Pitches
        pitch_box_size := 10;
        pitch_box_label_xoffset := 9;
        strike_box_width := 98;
        play_box_size := 30;
        ball_box_width := 50;

        %% Pitch boxes
        draw (xstart,ystart)--(xstart,ystart+pitch_box_size*2)--(xstart+strike_box_width,ystart+pitch_box_size*2)--(xstart+strike_box_width,ystart)--cycle withcolor card;
        draw (xstart,ystart+pitch_box_size*2)--(xstart,ystart+pitch_box_size*3)--(xstart+ball_box_width,ystart+pitch_box_size*3)--(xstart+ball_box_width,ystart+pitch_box_size*2)--cycle withcolor card;
                draw (xstart+ball_box_width,ystart+pitch_box_size*2)--(xstart+ball_box_width,ystart+pitch_box_size*3)--(xstart+ball_box_width+48,ystart+pitch_box_size*3)--(xstart+ball_box_width+48,ystart+pitch_box_size*2)--cycle withcolor card;
        draw (xstart+strike_box_width,ystart)--(xstart+strike_box_width,ystart+play_box_size)--(xstart+strike_box_width+play_box_size,ystart+play_box_size)--(xstart+strike_box_width+play_box_size,ystart)--cycle withcolor card;

        draw (xstart+pitch_box_label_xoffset,ystart+pitch_box_size)--(xstart+strike_box_width,ystart+pitch_box_size) dashed evenly withcolor card;
        draw (xstart+pitch_box_label_xoffset,ystart)--(xstart+pitch_box_label_xoffset,ystart+pitch_box_size*3) withcolor card;

        label.urt(btex {\tiny B} etex, (xstart,ystart+pitch_box_size*2)) withcolor clr;
        label.urt(btex {\tiny S} etex, (xstart,ystart+pitch_box_size/2)) withcolor clr;

        pickup pencircle scaled playline_t;
    endgroup
enddef;

def draw_player_box(expr xstart, ystart, clr, inncol) =
    % Intended to draw to the *left* of xstart, ystart
    begingroup
        iposwidth := 40;
        namewidth := 250;
        pickup pencircle scaled thickline_t;

        % Inning and Position box
        if inncol:
            draw (xstart,ystart)--(xstart-iposwidth*2,ystart)--(xstart-iposwidth*2,ystart+128)--(xstart,ystart+128)--cycle withcolor clr;
            draw (xstart-iposwidth,ystart)--(xstart-iposwidth,ystart+128) withcolor clr;
        else:
            draw (xstart-iposwidth,ystart)--(xstart-iposwidth*2,ystart)--(xstart-iposwidth*2,ystart+224)--(xstart-iposwidth,ystart+224)--cycle withcolor clr;
        fi

        % Player name box
        if inncol:
        draw (xstart-iposwidth*2,ystart)--(xstart-iposwidth*2-namewidth,ystart)--(xstart-iposwidth*2-namewidth,ystart+128)--
                (xstart-iposwidth*2,ystart+128)--cycle withcolor clr;
        else:
        draw (xstart-iposwidth*2,ystart)--(xstart-iposwidth*2-namewidth,ystart)--(xstart-iposwidth*2-namewidth,ystart+224)--
                (xstart-iposwidth*2,ystart+224)--cycle withcolor clr;
        fi

        % Number box
        if inncol:
        draw (xstart-iposwidth*2-namewidth,ystart)--(xstart-iposwidth*3-namewidth,ystart)--(xstart-iposwidth*3-namewidth,ystart+128)--
                (xstart-iposwidth*2-namewidth,ystart+128)--cycle withcolor clr;
        else:
        draw (xstart-iposwidth*2-namewidth,ystart)--(xstart-iposwidth*3-namewidth,ystart)--(xstart-iposwidth*3-namewidth,ystart+224)--
                (xstart-iposwidth*2-namewidth,ystart+224)--cycle withcolor clr;
        fi
        pickup pencircle scaled thinline_t;

        % other player lines
        if inncol:
            draw (xstart,ystart+128/4)--(xstart-iposwidth*3-namewidth,ystart+128/4) withcolor clr;
            draw (xstart,ystart+128/4+128/4)--(xstart-iposwidth*3-namewidth,ystart+128/4+128/4) withcolor clr;
            draw (xstart,ystart+128/4+128/4+128/4)--(xstart-iposwidth*3-namewidth,ystart+128/4+128/4+128/4) withcolor clr;
        else:
            for offset := 32 step 32 until 192:
                draw (xstart-iposwidth,ystart+offset)--(xstart-iposwidth*3-namewidth,ystart+offset) withcolor clr;
            endfor
        fi
    endgroup
enddef;

def draw_column_totals_key(expr xstart, ystart, clr) =
    begingroup
        pickup pencircle scaled thickline_t;
        draw (xstart,ystart)--(xstart,ystart+96)--(xstart-iposwidth,ystart+96)--(xstart-iposwidth,ystart)--cycle withcolor clr;
        draw (xstart,ystart+96/2)--(xstart-iposwidth,ystart+96/2)--(xstart,ystart+96) withcolor clr;
        draw (xstart,ystart+96/2)--(xstart-iposwidth,ystart) withcolor clr;
    endgroup
enddef;

def draw_totals_box(expr xstart, ystart, clr) =
    begingroup
        pickup pencircle scaled thickline_t;
        draw (xstart,ystart)--(xstart,ystart+48)--(xstart+128,ystart+48)--(xstart+128,ystart)--cycle withcolor clr;
        pickup pencircle scaled thinline_t;
        draw 1/3[(xstart,ystart),(xstart+128,ystart)]-- 2/3[(xstart,ystart+48),(xstart+128,ystart+48)] withcolor clr;
    endgroup
enddef;

def draw_row_summary_box(expr xstart,ystart,rows,clr) =
    begingroup
        pickup pencircle scaled thickline_t;

        box_h := 32;

        % Box
        draw (xstart,ystart)--(xstart,ystart+box_h * rows)--(xstart+96,ystart+box_h * rows)--(xstart+96,ystart)--cycle withcolor clr;
        pickup pencircle scaled thinline_t;

        % Vertical lines
        draw (xstart+96/3,ystart)--(xstart+96/3,ystart+box_h * rows) withcolor clr;
        draw (xstart+96/3*2,ystart)--(xstart+96/3*2,ystart+box_h * rows) withcolor clr;

        % Horizontal lines
        for row := 1 step 1 until rows:
            draw (xstart,ystart+box_h * row)--(xstart+96,ystart+box_h * row) withcolor clr;
        endfor

    endgroup
enddef;

def draw_game_summary_box(expr xstart,ystart,clr) =
    begingroup
        pickup pencircle scaled thickline_t;
        draw (xstart,ystart)--(xstart,ystart+48)--(xstart+64,ystart+48)--(xstart+64,ystart)--cycle withcolor clr;
        pickup pencircle scaled thinline_t;
        draw (xstart,ystart)--(xstart+64,ystart+48) withcolor clr;
    endgroup
enddef;

def draw_play_total_box(expr xstart,ystart,clr) =
    begingroup
        pickup pencircle scaled thickline_t;
        draw (xstart+64,ystart)--(xstart+64,ystart+48)--(xstart+64+256,ystart+48)--(xstart+64+256,ystart)--cycle withcolor clr;
        draw (xstart+64,ystart+25)--(xstart+64+256,ystart+25) withcolor clr;
    endgroup
enddef;

def draw_pitcher_box(expr xstart,ystart,clr) =
    begingroup
        iposwidth := 40;
        namewidth := 250;
        boxwidth  := 32;
        rows      := 7;

        pickup pencircle scaled thickline_t;

        % TODO: Fix me!
        % Handedness and inning box
        draw (xstart,ystart)--(xstart-iposwidth*2,ystart)--(xstart-iposwidth*2,ystart+boxwidth*rows)--(xstart,ystart+boxwidth*rows)--cycle withcolor clr;
        draw (xstart-iposwidth,ystart)--(xstart-iposwidth,ystart+boxwidth*rows) withcolor clr;

        % Player name box
        draw (xstart-iposwidth*2,ystart)--(xstart-iposwidth*2-namewidth,ystart)--(xstart-iposwidth*2-namewidth,ystart+boxwidth*rows)--
                (xstart-iposwidth*2,ystart+boxwidth*rows)--cycle withcolor clr;

        % Number box
        draw (xstart-iposwidth*2-namewidth,ystart)--(xstart-iposwidth*3-namewidth,ystart)--(xstart-iposwidth*3-namewidth,ystart+boxwidth*rows)--
                (xstart-iposwidth*2-namewidth,ystart+boxwidth*rows)--cycle withcolor clr;
        pickup pencircle scaled thinline_t;

        % Row division
        for row := 1 step 1 until rows:
            draw (xstart,ystart+boxwidth*row)--(xstart-iposwidth*3-namewidth,ystart+boxwidth*row) withcolor clr;
        endfor

        % Stats boxes
        for nxstart := xstart step 96 until xstart+400:
            draw_row_summary_box(nxstart,ystart,7,clr);
        endfor

    endgroup
enddef;

def draw_pitcher_labels(expr xstart,ystart,clr,leftish) =
    begingroup
        iposwidth := 40;
        namewidth := 250;

        statboxwidth := 32;
        label(btex {\midsf \#} etex, 1/2[(xstart-iposwidth*2-namewidth,ystart),(xstart-iposwidth*3-namewidth,ystart-(32))]) withcolor clr;
        label(btex {\midsf Opposing Pitchers} etex, 1/2[(xstart-iposwidth*2,ystart),(xstart-iposwidth*2-namewidth,ystart-32)]) withcolor clr;
        label(btex {\midsf L/R} etex, 1/2[(xstart-iposwidth,ystart),(xstart-iposwidth*2,ystart-32)]) withcolor clr;
        label(btex {\midsf Inn} etex, 1/2[(xstart,ystart),(xstart-iposwidth,ystart-32)]) withcolor clr;
        %
        label(btex {\midsf WLS} etex, 1/2[(xstart+statboxwidth,ystart),(xstart,ystart-32)]) withcolor clr;
        label(btex {\midsf BF} etex, 1/2[(xstart+statboxwidth*2,ystart),(xstart+statboxwidth,ystart-32)]) withcolor clr;
        label(btex {\midsf IP} etex, 1/2[(xstart+statboxwidth*3,ystart),(xstart+statboxwidth*2,ystart-32)]) withcolor clr;
        %
        label(btex {\midsf H} etex, 1/2[(xstart+statboxwidth*4,ystart),(xstart+statboxwidth*3,ystart-32)]) withcolor clr;
        label(btex {\midsf R} etex, 1/2[(xstart+statboxwidth*5,ystart),(xstart+statboxwidth*4,ystart-32)]) withcolor clr;
        label(btex {\midsf ER} etex, 1/2[(xstart+statboxwidth*6,ystart),(xstart+statboxwidth*5,ystart-32)]) withcolor clr;
        %
        label(btex {\midsf BB} etex, 1/2[(xstart+statboxwidth*7,ystart),(xstart+statboxwidth*6,ystart-32)]) withcolor clr;
        label(btex {\midsf SO} etex, 1/2[(xstart+statboxwidth*8,ystart),(xstart+statboxwidth*7,ystart-32)]) withcolor clr;
        label(btex {\midsf IBB} etex, 1/2[(xstart+statboxwidth*9,ystart),(xstart+statboxwidth*8,ystart-32)]) withcolor clr;
        %
        label(btex {\midsf HBP} etex, 1/2[(xstart+statboxwidth*10,ystart),(xstart+statboxwidth*9,ystart-32)]) withcolor clr;
        label(btex {\midsf BLK} etex, 1/2[(xstart+statboxwidth*11,ystart),(xstart+statboxwidth*10,ystart-32)]) withcolor clr;
        label(btex {\midsf WP} etex, 1/2[(xstart+statboxwidth*12,ystart),(xstart+statboxwidth*11,ystart-32)]) withcolor clr;
        %
        label(btex {\midsf HR} etex, 1/2[(xstart+statboxwidth*13,ystart),(xstart+statboxwidth*12,ystart-32)]) withcolor clr;
        label(btex {\midsf P} etex, 1/2[(xstart+statboxwidth*14,ystart),(xstart+statboxwidth*13,ystart-32)]) withcolor clr;
        label(btex {\midsf S} etex, 1/2[(xstart+statboxwidth*15,ystart),(xstart+statboxwidth*14,ystart-32)]) withcolor clr;
    endgroup
enddef;

def set_game_info_vars(expr innings) =
    begingroup
        ab_box_size := 128;
        stat_box_size := 32;

        xstart := (innings * ab_box_size) + (stat_box_size * 6);

        pair game_team, game_date, game_temp;
        pair game_location, game_attendance, game_scorer, game_wind;
        pair game_hp_ump, game_second_ump, game_lf_ump;
        pair game_first_ump, game_third_ump, game_rf_ump;

        game_team := (xstart + 16, stat_box_size * 3);
        game_date := (xstart + 16, stat_box_size * 18);
        game_temp := (xstart + 16, stat_box_size * 30);

        game_location :=   (xstart + stat_box_size + 16, stat_box_size * 3);
        game_attendance := (xstart + stat_box_size + 16, stat_box_size * 18);
        game_scorer :=     (xstart + stat_box_size + 16, stat_box_size * 22 + 16);
        game_wind :=       (xstart + stat_box_size + 16, stat_box_size * 30);

        game_hp_ump :=     (xstart + stat_box_size * 2 + 16, stat_box_size * 7 + 4);
        game_second_ump := (xstart + stat_box_size * 2 + 16, stat_box_size * 18 + 2);
        game_lf_ump :=     (xstart + stat_box_size * 2 + 16, stat_box_size * 29);

        game_first_ump := (xstart + stat_box_size * 3 + 16, stat_box_size * 7 + 4);
        game_third_ump := (xstart + stat_box_size * 3 + 16, stat_box_size * 18 + 2);
        game_rf_ump :=    (xstart + stat_box_size * 3 + 16, stat_box_size * 29);

    endgroup
enddef;

def set_batter_name_vars(expr lineup_pos, lineup_line) =
    begingroup
        iposwidth := 40;
        namewidth := 250;
        box_size := 32;
        max_y := box_size * 4 * 9; % top of the topmost name box.

        player_y := max_y - (box_size * (4 * (lineup_pos - 1) + lineup_line));

        % Declare the X coordinates.
        number_x := -iposwidth*3-namewidth;
        name_x := -iposwidth*2-namewidth;
        pos_x := -iposwidth*2;
        inn_x := -iposwidth;
    endgroup
enddef;

def set_extra_batter_name_vars(expr extra_num) =
    begingroup
        iposwidth := 40;
        namewidth := 250;
        box_size := 32;

        player_y := -(box_size * extra_num);

        % Declare the X coordinates.
        number_x := -iposwidth*3-namewidth;
        name_x := -iposwidth*2-namewidth;
        pos_x := -iposwidth*2;
        inn_x := -iposwidth;
    endgroup
enddef;

def set_pitcher_name_vars(expr pitcher_num) =
    begingroup

        if pitcher_num < 7:
            xstart := 0;
            yoffset := pitcher_num;
        else:
            xstart := 850;
            yoffset := pitcher_num - 6;
        fi

        iposwidth := 40;
        namewidth := 250;

        % Declare the X coordinates.
        number_x := -iposwidth*3-namewidth;
        name_x := -iposwidth*2-namewidth;
        handedness_x := -iposwidth*2 + 10;
        inn_x := -iposwidth;

        ystart := -256;
        pair pitcher_no, pitcher_name, pitcher_handedness, pitcher_inn;

        pitcher_no := (xstart + number_x, ystart - (yoffset * 32));
        pitcher_name := (xstart + name_x, ystart - (yoffset * 32));
        pitcher_handedness := (xstart + handedness_x, ystart - (yoffset * 32));
        pitcher_inn := (xstart + inn_x, ystart - (yoffset * 32));

    endgroup
enddef;

def set_inning_num_label_vars(expr xstart) =
    begingroup
    pair top_inn_label, bot_inn_label;
    top_inn_label := 1/2[(xstart, 1152),(xstart+128,1152+32)];
    bot_inn_label := 1/2[(xstart, 0),(xstart+128,-32)];
    endgroup
enddef;

def set_inning_total_vars(expr xstart) =
    begingroup
        pair inn_run, inn_hit, inn_err, inn_lob, inn_bb, inn_so, inn_str, inn_pit;

        inn_run := (xstart + 32, -56);
        inn_hit := (xstart + 96, -56);
        inn_err := (xstart + 32, -104);
        inn_lob := (xstart + 96, -104);
        inn_bb  := (xstart + 32, -152);
        inn_so   := (xstart + 96, -152);
        inn_str := (xstart + 32, -200);
        inn_pit := (xstart + 96, -200);

    endgroup
enddef;

def set_game_total_vars(expr innings) =
    begingroup

        ynudge := 7;
        ab_box_size := 128;
        xstart := (innings * ab_box_size);
        box_h := 48;
        pair inn_run, inn_hit, inn_err, inn_lob, inn_bb, inn_so, inn_str, inn_pit;

        ystart := -32;
        inn_run := 1/2[(xstart,ystart+ynudge),(xstart+32,ystart-box_h+ynudge)];
        inn_hit := 1/2[(xstart+32,ystart-ynudge),(xstart+64,ystart-box_h-ynudge)];

        ystart := ystart - 48;
        inn_err := 1/2[(xstart,ystart+ynudge),(xstart+32,ystart-box_h+ynudge)];
        inn_lob := 1/2[(xstart+32,ystart-ynudge),(xstart+64,ystart-box_h-ynudge)];

        ystart := ystart - 48;
        inn_bb  := 1/2[(xstart,ystart+ynudge),(xstart+32,ystart-box_h+ynudge)];
        inn_so   := 1/2[(xstart+32,ystart-ynudge),(xstart+64,ystart-box_h-ynudge)];

        ystart := ystart - 48;
        inn_str := 1/2[(xstart,ystart+ynudge),(xstart+32,ystart-box_h+ynudge)];
        inn_pit := 1/2[(xstart+32,ystart-ynudge),(xstart+64,ystart-box_h-ynudge)];

    endgroup
enddef;

def set_batter_total_vars(expr lineup_pos, lineup_line, innings) =
    begingroup
        stat_box_size := 32;
        ab_box_size := 128;
        xstart := (ab_box_size * innings);
        max_y := stat_box_size * 4 * 9; % top of the topmost name box.
        player_y := max_y - (stat_box_size * (4 * (lineup_pos - 1) + lineup_line));

        pair batter_ab, batter_r, batter_h, batter_rbi, batter_bb, batter_so;

        batter_ab  := (xstart + (stat_box_size/2), player_y + (stat_box_size/2));

        xstart := xstart + stat_box_size;
        batter_r   := (xstart + (stat_box_size/2), player_y + (stat_box_size/2));

        xstart := xstart + stat_box_size;
        batter_h   := (xstart + (stat_box_size/2), player_y + (stat_box_size/2));

        xstart := xstart + stat_box_size;
        batter_rbi := (xstart + (stat_box_size/2), player_y + (stat_box_size/2));

        xstart := xstart + stat_box_size;
        batter_bb  := (xstart + (stat_box_size/2), player_y + (stat_box_size/2));

        xstart := xstart + stat_box_size;
        batter_so  := (xstart + (stat_box_size/2), player_y + (stat_box_size/2));

    endgroup
enddef;

def set_basepath_total_vars(expr innings) =
    begingroup
        % Put the key on the play total boxes
        ab_box_size := 128;
        stat_box_size := 32;
        xstart := (ab_box_size * innings) + (stat_box_size * 3) + 3;
        xoffset := 95;
        nudge := 5;
        ystart := -44;
        yoffset := 24;

        pair basepath_first_label,basepath_second_label,basepath_third_label,basepath_hr_label,basepath_sf_label,basepath_sac_label;
        pair basepath_tb_label,basepath_hbp_label,basepath_ibb_label,basepath_blk_label,basepath_wp_label,basepath_pb_label;
        pair basepath_sb_label,basepath_cs_label,basepath_po_label,basepath_dp_label,basepath_tp_label,basepath_risp_label;
        pair basepath_totals_label,basepath_run_lob_opo_label;

        basepath_first_label  := (xstart + nudge, ystart - nudge);
        basepath_second_label := (xstart + nudge, ystart - yoffset - nudge);
        basepath_third_label  := (xstart + nudge, ystart - (yoffset * 2) - nudge);
        basepath_hr_label     := (xstart + nudge, ystart - (yoffset * 3) - nudge);
        basepath_sf_label     := (xstart + nudge, ystart - (yoffset * 4) - nudge);
        basepath_sac_label    := (xstart + nudge, ystart - (yoffset * 5) - nudge);

        basepath_tb_label  := (xstart + xoffset + nudge, ystart - nudge);
        basepath_hbp_label := (xstart + xoffset + nudge, ystart - yoffset - nudge);
        basepath_ibb_label := (xstart + xoffset + nudge, ystart - (yoffset * 2) - nudge);
        basepath_blk_label := (xstart + xoffset + nudge, ystart - (yoffset * 3) - nudge);
        basepath_wp_label  := (xstart + xoffset + nudge, ystart - (yoffset * 4) - nudge);
        basepath_pb_label  := (xstart + xoffset + nudge, ystart - (yoffset * 5) - nudge);

        basepath_sb_label := (xstart + xoffset * 2 + nudge, ystart - nudge);
        basepath_cs_label := (xstart + xoffset * 2 + nudge, ystart - yoffset - nudge);
        basepath_po_label := (xstart + xoffset * 2 + nudge, ystart - (yoffset * 2) - nudge);
        basepath_dp_label := (xstart + xoffset * 2 + nudge, ystart - (yoffset * 3) - nudge);
        basepath_tp_label := (xstart + xoffset * 2 + nudge, ystart - (yoffset * 4) - nudge);
        basepath_risp_label  := (xstart + xoffset * 2 + nudge * 2, ystart - (yoffset * 5) + 1.5);

        xstart := (ab_box_size * innings) + (stat_box_size * 6);
        basepath_totals_label      := (xstart + nudge, ystart - (yoffset * 6) - nudge);
        basepath_run_lob_opo_label := (xstart + nudge, ystart - (yoffset * 7) - nudge);
    endgroup
enddef;

def set_pitcher_total_vars(expr pitcher_num) =
    begingroup
        % pitcher #13 is the totals column
        if pitcher_num = 13:
            xstart := 850;
            yoffset := 6;
        elseif pitcher_num < 7:
            xstart := 0;
            yoffset := pitcher_num - 1;
        else:
            xstart := 850;
            yoffset := pitcher_num - 7;
        fi

        ystart := -256;

        pair pitcher_wls, pitcher_bf, pitcher_ip, pitcher_h, pitcher_r, pitcher_er, pitcher_bb;
        pair pitcher_so, pitcher_ibb, pitcher_hbp, pitcher_blk, pitcher_wp, pitcher_hr, pitcher_pit, pitcher_str;

        pitcher_wls := (xstart + 16, ystart - (yoffset * 32) - 16);
        pitcher_bf :=  (xstart + (32 * 1) + 16, ystart - (yoffset * 32) - 16);
        pitcher_ip :=  (xstart + (32 * 2) + 16, ystart - (yoffset * 32) - 16);
        pitcher_h :=   (xstart + (32 * 3) + 16, ystart - (yoffset * 32) - 16);
        pitcher_r :=   (xstart + (32 * 4) + 16, ystart - (yoffset * 32) - 16);
        pitcher_er :=  (xstart + (32 * 5) + 16, ystart - (yoffset * 32) - 16);
        pitcher_bb :=  (xstart + (32 * 6) + 16, ystart - (yoffset * 32) - 16);
        pitcher_so :=  (xstart + (32 * 7) + 16, ystart - (yoffset * 32) - 16);
        pitcher_ibb := (xstart + (32 * 8) + 16, ystart - (yoffset * 32) - 16);
        pitcher_hbp := (xstart + (32 * 9) + 16, ystart - (yoffset * 32) - 16);
        pitcher_blk := (xstart + (32 * 10) + 16, ystart - (yoffset * 32) - 16);
        pitcher_wp :=  (xstart + (32 * 11) + 16, ystart - (yoffset * 32) - 16);
        pitcher_hr :=  (xstart + (32 * 12) + 16, ystart - (yoffset * 32) - 16);
        pitcher_pit := (xstart + (32 * 13) + 16, ystart - (yoffset * 32) - 16);
        pitcher_str := (xstart + (32 * 14) + 16, ystart - (yoffset * 32) - 16);

    endgroup
enddef;

def set_bench_name_vars(expr bench_num) =
    begingroup
        namewidth := 224;
        iposwidth := 40;
        xstart := 1330;
        ystart := -256;

        pair bench_no, bench_name, bench_extra;

        bench_no := 1/2[(xstart, ystart - ((bench_num - 1) * 32)),(xstart + iposwidth, ystart - (bench_num * 32))];
        bench_name :=  1/2[(xstart + iposwidth, ystart - ((bench_num - 1) * 32)),(xstart + iposwidth + namewidth, ystart - (bench_num * 32))];
        bench_extra :=  1/2[(xstart + iposwidth + namewidth, ystart - ((bench_num - 1) * 32)),(xstart + iposwidth * 2 + namewidth, ystart - (bench_num * 32))];

    endgroup
enddef;

def set_bullpen_name_vars(expr bullpen_num) =
    begingroup
        namewidth := 223;
        iposwidth := 40;
        ystart := -256;
        xstart := 1634;
        yoffset := bullpen_num;

        if bullpen_num > 7:
            xstart := xstart+iposwidth*2+namewidth;
            yoffset := bullpen_num - 7;
        fi

        pair bullpen_no, bullpen_name, bullpen_extra;

        bullpen_no := 1/2[(xstart, ystart - ((yoffset - 1) * 32)),(xstart + iposwidth, ystart - (yoffset * 32))];
        bullpen_name :=  1/2[(xstart + iposwidth, ystart - ((yoffset - 1) * 32)),(xstart + iposwidth + namewidth, ystart - (yoffset * 32))];
        bullpen_extra :=  1/2[(xstart + iposwidth + namewidth, ystart - ((yoffset - 1) * 32)),(xstart + iposwidth * 2 + namewidth, ystart - (yoffset * 32))];

    endgroup
enddef;

def set_vars(expr xstart, ystart) =
    begingroup
        % Pitch locations
        pitch_box_size := 10;
        pitch_box_label_xoffset := 6;
        strike_box_width := 98;
        play_box_size := 30;
        ball_box_width := 50;

        pair ballone, balltwo, ballthree, ballfour;
        pair strikeone, striketwo, strikethree, strikefour, strikefive, strikesix;
        pair strikeseven, strikeeight, strikenine, striketen, strikeeleven, striketwelve;
        pair strikethirteen, strikefourteen, strikefifteen, strikesixteen, strikeseventeen, strikeeighteen;
        pair strikenineteen, striketwenty, striketwentyone, striketwentytwo;

        ballone   := (xstart+pitch_box_label_xoffset+1+9*1, ystart+pitch_box_size*2.5);
        balltwo   := (xstart+pitch_box_label_xoffset+1+9*2, ystart+pitch_box_size*2.5);
        ballthree := (xstart+pitch_box_label_xoffset+1+9*3, ystart+pitch_box_size*2.5);
        ballfour  := (xstart+pitch_box_label_xoffset+1+9*4, ystart+pitch_box_size*2.5);

        strikeone       := (xstart+pitch_box_label_xoffset+8*1, ystart+pitch_box_size*1.5);
        striketwo       := (xstart+pitch_box_label_xoffset+8*2, ystart+pitch_box_size*1.5);
        strikethree     := (xstart+pitch_box_label_xoffset+8*3, ystart+pitch_box_size*1.5);
        strikefour      := (xstart+pitch_box_label_xoffset+8*4, ystart+pitch_box_size*1.5);
        strikefive      := (xstart+pitch_box_label_xoffset+8*5, ystart+pitch_box_size*1.5);
        strikesix       := (xstart+pitch_box_label_xoffset+8*6, ystart+pitch_box_size*1.5);
        strikeseven     := (xstart+pitch_box_label_xoffset+8*7, ystart+pitch_box_size*1.5);
        strikeeight     := (xstart+pitch_box_label_xoffset+8*8, ystart+pitch_box_size*1.5);
        strikenine      := (xstart+pitch_box_label_xoffset+8*9, ystart+pitch_box_size*1.5);
        striketen       := (xstart+pitch_box_label_xoffset+8*10, ystart+pitch_box_size*1.5);
        strikeeleven    := (xstart+pitch_box_label_xoffset+8*11, ystart+pitch_box_size*1.5);
        striketwelve    := (xstart+pitch_box_label_xoffset+8*1, ystart+pitch_box_size*0.5);
        strikethirteen  := (xstart+pitch_box_label_xoffset+8*2, ystart+pitch_box_size*0.5);
        strikefourteen  := (xstart+pitch_box_label_xoffset+8*3, ystart+pitch_box_size*0.5);
        strikefifteen   := (xstart+pitch_box_label_xoffset+8*4, ystart+pitch_box_size*0.5);
        strikesixteen   := (xstart+pitch_box_label_xoffset+8*5, ystart+pitch_box_size*0.5);
        strikeseventeen := (xstart+pitch_box_label_xoffset+8*6, ystart+pitch_box_size*0.5);
        strikeeighteen  := (xstart+pitch_box_label_xoffset+8*7, ystart+pitch_box_size*0.5);
        strikenineteen  := (xstart+pitch_box_label_xoffset+8*8, ystart+pitch_box_size*0.5);
        striketwenty    := (xstart+pitch_box_label_xoffset+8*9, ystart+pitch_box_size*0.5);
        striketwentyone := (xstart+pitch_box_label_xoffset+8*10, ystart+pitch_box_size*0.5);
        striketwentytwo := (xstart+pitch_box_label_xoffset+8*11, ystart+pitch_box_size*0.5);

        % Diamond dimensions
        dsize := 28;
        dxstart := xstart+64;
        dystart := ystart+38;

        pair rundot, outlabel;
        pair rbione, rbitwo, rbithree, rbifour;
        rundot := (dxstart,dystart+dsize);
        outlabel := (dxstart,dystart+dsize);

        % RBIs
        rbi_radius := 3.75;
        rbi_xstart := xstart + ball_box_width + 5.5 + rbi_radius;
        rbi_ystart := ystart + pitch_box_size * 2.5;
        rbi_offset := 10;

        rbione   := (rbi_xstart+rbi_offset*0,rbi_ystart);
        rbitwo   := (rbi_xstart+rbi_offset*1,rbi_ystart);
        rbithree := (rbi_xstart+rbi_offset*2,rbi_ystart);
        rbifour  := (rbi_xstart+rbi_offset*3,rbi_ystart);

        % Play location
        pair playloc;
        playloc := (xstart+98+15,ystart+15);

        pair first, second, third, home;
        path single, double, triple, homerun;
        home := (dxstart,dystart);
        first := (dxstart+dsize,dystart+dsize);
        second := (dxstart,dystart+dsize*2);
        third := (dxstart-dsize,dystart+dsize);
        single := home--first--(first+(-7,0));
        double := home--first--second--(second+(0,-7));
        triple := home--first--second--third--(third+(7,0));
        homerun := home--first--second--third--cycle;

        path firstsecond, firstthird, firsthome, secondthird, secondhome, thirdhome;
        firstsecond := first--second--(second+(0,-7));
        firstthird := first--second--third--(third+(7,0));
        firsthome := first--second--third--home;
        secondthird := second--third--(third+(7,0));
        secondhome := second--third--home;
        thirdhome := third--home;

        % TODO: These are unused, and unfixed.
        %path ifleft, ifright, ifcenter, ofleft, ofleftc, ofcenterl, ofcenterr, ofrightc, ofright;
        %ifleft := home--(home+(-13,18));
        %ifright := home--(home+(13,18));
        %ifcenter := home--(home+(0,18));
        %ofleft := home--(home+(-32, 36));
        %ofleftc := home--(home+(-20, 60));
        %ofright := home--(home+(32, 36));
        %ofrightc := home--(home+(20, 60));
        %ofcenterl := home--(home+(-5, 65));
        %ofcenterr := home--(home+(5, 65));

        %path hrleft, hrleftc, hrcenterl, hrcenterr, hrrightc, hrright;
        %hrleft := home--(home+(-37, 41));
        %hrleftc := home--(home+(-27, 67));
        %hrright := home--(home+(37, 41));
        %hrrightc := home--(home+(27, 67));
        %hrcenterl := home--(home+(-5, 75));
        %hrcenterr := home--(home+(5, 75));

        pair wayfirst, waysecond, waythird, wayhome;
        path cs_second, cs_third, to_home;
        path cs_firstthird, to_firsthome, to_secondhome;
        wayfirst := 1/2[home,first];
        waysecond := 1/2[first,second];
        waythird := 1/2[second,third];
        wayhome := 1/2[third,home];

        cs_second := first--waysecond--(waysecond+(1.5,1.5))--(waysecond-(1.5,1.5));
        cs_third := second--waythird--(waythird+(-1.5,1.5))--(waythird-(-1.5,1.5));
        to_home := third--wayhome--(wayhome+(1.5,1.5))--(wayhome-(1.5,1.5));
        cs_firstthird := first--second--waythird--(waythird+(-1.5,1.5))--(waythird-(-1.5,1.5));
        to_firsthome := first--second--third--wayhome--(wayhome+(1.5,1.5))--(wayhome-(1.5,1.5));
        to_secondhome := second--third--wayhome--(wayhome+(1.5,1.5))--(wayhome-(1.5,1.5));

        path new_hitter, new_pitcher;
        new_hitter := (xstart-3,ystart-3)--(xstart+3,ystart+3)--(xstart,ystart)--(xstart+3,ystart-3)--(xstart-3,ystart+3)--(xstart,ystart)--(xstart,ystart+128)--(xstart-3,ystart+125)--(xstart+3,ystart+131)--(xstart,ystart+128)--(xstart+3,ystart+125)--(xstart-3,ystart+131);
        new_pitcher := (xstart-3,ystart+125)--(xstart+3,ystart+131)--(xstart,ystart+128)--(xstart+3,ystart+125)--(xstart-3,ystart+131)--(xstart,ystart+128)--(xstart+128,ystart+128)--(xstart+125,ystart+125)--(xstart+131,ystart+131)--(xstart+128,ystart+128)--(xstart+131,ystart+125)--(xstart+125,ystart+131);
    endgroup
enddef;

def draw_out_one(expr xstart, ystart, clr) =
    begingroup
        pickup pencircle scaled playline_t;
        xoffset := 98+20;
        yoffset := 118;
        label(btex {\sf 1} etex, (xstart+xoffset, ystart+yoffset)) withcolor outclr;
        draw (xstart+xoffset,ystart+yoffset-outcircle_d)..(xstart+xoffset+outcircle_d,ystart+yoffset)..
                (xstart+xoffset,ystart+yoffset+outcircle_d)..(xstart+xoffset-outcircle_d,ystart+yoffset)..cycle withcolor outclr;
    endgroup
enddef;

def draw_out_two(expr xstart, ystart, clr) =
    begingroup
        pickup pencircle scaled playline_t;
        xoffset := 98+20;
        yoffset := 118;
        label(btex {\sf 2} etex, (xstart+xoffset, ystart+yoffset)) withcolor outclr;
        draw (xstart+xoffset,ystart+yoffset-outcircle_d)..(xstart+xoffset+outcircle_d,ystart+yoffset)..
                (xstart+xoffset,ystart+yoffset+outcircle_d)..(xstart+xoffset-outcircle_d,ystart+yoffset)..cycle withcolor outclr;
    endgroup
enddef;

def draw_out_three(expr xstart, ystart, clr) =
    begingroup
        pickup pencircle scaled playline_t;
        xoffset := 98+20;
        yoffset := 118;
        label(btex {\sf 3} etex, (xstart+xoffset, ystart+yoffset)) withcolor outclr;
        draw (xstart+xoffset,ystart+yoffset-outcircle_d)..(xstart+xoffset+outcircle_d,ystart+yoffset)..
                (xstart+xoffset,ystart+yoffset+outcircle_d)..(xstart+xoffset-outcircle_d,ystart+yoffset)..cycle withcolor outclr;
    endgroup
enddef;

def draw_dot(expr loc, clr) =
    begingroup
        pickup pencircle scaled dotsize;
        draw(loc) withcolor clr;
        pickup pencircle scaled playline_t;
    endgroup
enddef;

def draw_cross(expr loc, clr) =
    begingroup
        pickup pencircle scaled dotsize;
        label(btex {\sf X} etex, loc) withcolor clr;
        pickup pencircle scaled playline_t;
    endgroup
enddef;

def draw_strike_dot(expr loc, clr) =
    begingroup
        pickup pencircle scaled strikedot;
        draw(loc) withcolor clr;
        pickup pencircle scaled playline_t;
    endgroup
enddef;

def draw_strike_circle(expr loc, clr) =
    begingroup
        pickup pencircle scaled playline_t;
        draw (loc+(0,-called_strike_d))..(loc+(called_strike_d,0))..(loc+(0,called_strike_d))..
            (loc+(-called_strike_d,0))..cycle withcolor clr;
    endgroup
enddef;

def draw_diamond(expr loc, clr) =
    begingroup
        rbi_radius := 3.75;
        pickup pencircle scaled playline_t;
        fill loc+(-rbi_radius,0)--
                loc+(0,rbi_radius)--
                loc+(rbi_radius,0)--
                loc+(0,-rbi_radius)--cycle withcolor clr;
    endgroup
enddef;

def draw_inning_end(expr xstart, ystart, clr) =
    begingroup
        pickup pencircle scaled playline_t;
        draw (xstart+123,ystart-5)--(xstart+133,ystart+5) withcolor clr;
    endgroup
enddef;

def draw_strikeout_looking(expr outlabel, clr) =
    begingroup
        label(btex {\bigsf K} etex, outlabel) rotatedaround (outlabel, 180) withcolor clr;
    endgroup
enddef;

def draw_reserve_player_box(expr xstart, ystart, clr, bullpen) =
    begingroup
        namewidth := 224;
        if bullpen:
            namewidth := 223;
        fi
        iposwidth := 40;

        % draw main box
        draw (xstart,ystart)--(xstart+iposwidth*2+namewidth,ystart)--(xstart+iposwidth*2+namewidth,ystart-32*8)--(xstart,ystart-32*8)--cycle withcolor clr;

        % draw vertical separators
        draw (xstart+iposwidth,ystart)--(xstart+iposwidth,ystart-32*8) withcolor clr;
        draw (xstart+iposwidth+namewidth,ystart)--(xstart+iposwidth+namewidth,ystart-32*8) withcolor clr;

        % draw row separators
        for row := 1 step 1 until 7:
            draw (xstart,ystart-32*row)--(xstart+iposwidth*2+namewidth,ystart-32*row) withcolor clr;
        endfor

        % draw thick line to separate header
        pickup pencircle scaled thickline_t;
        draw (xstart,ystart-32)--(xstart+iposwidth*2+namewidth,ystart-32) withcolor clr;
        pickup pencircle scaled thinline_t;

        % write labels based on whether this is the bullpen or the bench
        label(btex {\midsf \#} etex, 1/2[(xstart,ystart),(xstart+iposwidth,ystart-32)]) withcolor clr;
        if bullpen:
            label(btex {\midsf Opposing Bullpen} etex, 1/2[(xstart+iposwidth,ystart),(xstart+iposwidth+namewidth,ystart-32)]) withcolor clr;
            label(btex {\midsf L/R} etex, 1/2[(xstart+iposwidth+namewidth,ystart),(xstart+iposwidth*2+namewidth,ystart-32)]) withcolor clr;
        else:
            label(btex {\midsf Bench} etex, 1/2[(xstart+iposwidth,ystart),(xstart+iposwidth+namewidth,ystart-32)]) withcolor clr;
            label(btex {\midsf Pos} etex, 1/2[(xstart+iposwidth+namewidth,ystart),(xstart+iposwidth*2+namewidth,ystart-32)]) withcolor clr;
        fi

    endgroup
enddef;

def strikethrough_bench_name(expr bench_num, clr) =
    begingroup
        namewidth := 224;
        iposwidth := 40;
        xstart := 1330;
        ystart := -224;
        xoffset := 5;

        pickup pencircle scaled strikethrough_t;
        draw (xstart + xoffset, ystart - (bench_num * 32 + 16))--(xstart + iposwidth * 2 + namewidth - xoffset, ystart - (bench_num * 32 + 16)) withcolor clr;
        pickup pencircle scaled thinline_t;

    endgroup
enddef;

def strikethrough_bullpen_name(expr bullpen_num, clr) =
    begingroup
        namewidth := 223;
        iposwidth := 40;
        ystart := -224;
        xstart := 1634;
        yoffset := bullpen_num;
        xoffset := 5;

        if bullpen_num > 7:
            xstart := xstart+iposwidth*2+namewidth;
            yoffset := bullpen_num - 7;
        fi

        pickup pencircle scaled strikethrough_t;
        draw (xstart + xoffset, ystart - (yoffset * 32 + 16))--(xstart + iposwidth * 2 + namewidth - xoffset, ystart - (yoffset * 32 + 16)) withcolor clr;
        pickup pencircle scaled thinline_t;

    endgroup
enddef;

def draw_full_scorecard(expr innings) =
    begingroup
        % Draw the player boxes
        color clr;
        clr := card;
        box_size := 128;
        xstart := 0;

        % Draw first nine position boxes
        for ystart := 0 step 128 until 1024:
            draw_player_box(xstart,ystart,clr,true);
        endfor

        % Draw extra player boxes (without an inning column)
        ystart := -224;
        draw_player_box(xstart,ystart,clr,false);

        % Little numbers for first nine in batting order
        ystart := 128;
        playerbox_h := 32;
        yoffset := 6;
        label(btex {\sf 1} etex, (-324, ystart * 8 + playerbox_h * 4 - yoffset)) withcolor clr;
        label(btex {\sf 2} etex, (-324, ystart * 7 + playerbox_h * 4 - yoffset)) withcolor clr;
        label(btex {\sf 3} etex, (-324, ystart * 6 + playerbox_h * 4 - yoffset)) withcolor clr;
        label(btex {\sf 4} etex, (-324, ystart * 5 + playerbox_h * 4 - yoffset)) withcolor clr;
        label(btex {\sf 5} etex, (-324, ystart * 4 + playerbox_h * 4 - yoffset)) withcolor clr;
        label(btex {\sf 6} etex, (-324, ystart * 3 + playerbox_h * 4 - yoffset)) withcolor clr;
        label(btex {\sf 7} etex, (-324, ystart * 2 + playerbox_h * 4 - yoffset)) withcolor clr;
        label(btex {\sf 8} etex, (-324, ystart * 1 + playerbox_h * 4 - yoffset)) withcolor clr;
        label(btex {\sf 9} etex, (-324, ystart * 0 + playerbox_h * 4 - yoffset)) withcolor clr;

        % Draw key for column totals
        for ystart := -224 step 96 until -128:
            draw_column_totals_key(xstart,ystart,clr);
        endfor

        % Put key into column totals
        iposwidth := 40;
        ystart := -32;
        midpoint := 48;

        % For 2-letter keys, use the offset
        pair offset;
        offset := (2,0);

        label(btex {\bigsf R} etex, 1/2[1/2[(0,ystart),(-iposwidth,ystart-midpoint)],(-iposwidth,ystart)]) withcolor clr;
        label(btex {\bigsf H} etex, 1/2[1/2[(0,ystart),(-iposwidth,ystart-midpoint)],(0,ystart-midpoint)]) withcolor clr;

        label(btex {\bigsf E}  etex, 1/2[1/2[(0,ystart-midpoint),(-iposwidth,ystart-(midpoint*2))],(-iposwidth,ystart-midpoint)]) withcolor clr;
        label(btex {\bigsf LB} etex, 1/2[1/2[(0,ystart-midpoint),(-iposwidth,ystart-(midpoint*2))],(0,ystart-(midpoint*2))] - offset) withcolor clr;

        % Move the ystart for the lower column totals
        ystart := -128;

        label(btex {\bigsf BB} etex, 1/2[1/2[(0,ystart),(-iposwidth,ystart-midpoint)],(-iposwidth,ystart)] + offset) withcolor clr;
        label(btex {\bigsf K}  etex, 1/2[1/2[(0,ystart),(-iposwidth,ystart-midpoint)],(0,ystart-midpoint)]) withcolor clr;

        label(btex {\bigsf S}  etex, 1/2[1/2[(0,ystart-midpoint),(-iposwidth,ystart-(midpoint*2))],(-iposwidth,ystart-midpoint)]) withcolor clr;
        label(btex {\bigsf P}  etex, 1/2[1/2[(0,ystart-midpoint),(-iposwidth,ystart-(midpoint*2))],(0,ystart-(midpoint*2))]) withcolor clr;

        % Draw all the at-bat boxes
        for ystart := 0 step box_size until (box_size * 8):
            for xstart := 0 step box_size until (innings - 1) * box_size:
                draw_at_bat_box(xstart, ystart);
            endfor
        endfor

        % Draw the totals boxes
        clr:=card;
        for ystart := -224 step 48 until -80:
            for xstart := 0 step box_size until (innings - 1) * box_size:
                draw_totals_box(xstart,ystart,clr);
            endfor
        endfor

        % Draw all the row totals boxes
        for ystart := 0 step 128 until 1024:
            for xstart := (innings * box_size) step 96 until ((innings * box_size) + 96):
                draw_row_summary_box(xstart,ystart,4,clr);
            endfor
        endfor

        % Draw the total boxes for the team
        xstart := (innings * box_size);
        ystart := -32;
        draw (xstart,ystart)--(xstart,ystart+32)--(xstart+192,ystart+32)--(xstart+192,ystart)--cycle withcolor clr;
        for offset := 32 step 32 until 160:
            draw (xstart+offset,ystart)--(xstart+offset,ystart+32) withcolor clr;
        endfor

        % Inning and Position box
        xstart := 0;
        draw (xstart,ystart)--(xstart-iposwidth*2,ystart)--(xstart-iposwidth*2,ystart+32)--(xstart,ystart+32)--cycle withcolor clr;

        % Inning boxes
        for xstart := 0 step box_size until (innings - 1) * box_size:
            draw (xstart,ystart)--(xstart+128,ystart)--(xstart+128,ystart+32)--(xstart,ystart+32)--cycle withcolor clr;
        endfor

        % Draw the game and play total boxes
        xstart := (innings * box_size);
        for ystart := -224 step 48 until -80:
            draw_game_summary_box(xstart,ystart,clr);
            draw_play_total_box(xstart,ystart,clr);
        endfor

        % Put the key on the play total boxes
        xstart := (innings * box_size) + 64;
        xoffset := 90;
        nudge := 5;
        ystart := -44;
        yoffset := 24;

        label.urt(btex {\sf 1B} etex,  (xstart + nudge, ystart - nudge)) withcolor clr;
        label.urt(btex {\sf 2B} etex,  (xstart + nudge, ystart - yoffset - nudge)) withcolor clr;
        label.urt(btex {\sf 3B} etex,  (xstart + nudge, ystart - (yoffset * 2) - nudge)) withcolor clr;
        label.urt(btex {\sf HR} etex,  (xstart + nudge, ystart - (yoffset * 3) - nudge)) withcolor clr;
        label.urt(btex {\sf SF} etex,  (xstart + nudge, ystart - (yoffset * 4) - nudge)) withcolor clr;
        label.urt(btex {\sf SAC} etex, (xstart + nudge, ystart - (yoffset * 5) - nudge)) withcolor clr;

        label.urt(btex {\sf TB} etex,  (xstart + xoffset + nudge, ystart - nudge)) withcolor clr;
        label.urt(btex {\sf HBP} etex, (xstart + xoffset + nudge, ystart - yoffset - nudge)) withcolor clr;
        label.urt(btex {\sf IBB} etex,  (xstart + xoffset + nudge, ystart - (yoffset * 2) - nudge)) withcolor clr;
        label.urt(btex {\sf BLK} etex,  (xstart + xoffset + nudge, ystart - (yoffset * 3) - nudge)) withcolor clr;
        label.urt(btex {\sf WP} etex,  (xstart + xoffset + nudge, ystart - (yoffset * 4) - nudge)) withcolor clr;
        label.urt(btex {\sf PB} etex,  (xstart + xoffset + nudge, ystart - (yoffset * 5) - nudge)) withcolor clr;

        label.urt(btex {\sf SB} etex,  (xstart + xoffset * 2 + nudge, ystart - nudge)) withcolor clr;
        label.urt(btex {\sf CS} etex, (xstart + xoffset * 2 + nudge, ystart - yoffset - nudge)) withcolor clr;
        label.urt(btex {\sf PO} etex,  (xstart + xoffset * 2 + nudge, ystart - (yoffset * 2) - nudge)) withcolor clr;
        label.urt(btex {\sf DP} etex,  (xstart + xoffset * 2 + nudge, ystart - (yoffset * 3) - nudge)) withcolor clr;
        label.urt(btex {\sf TP} etex,  (xstart + xoffset * 2 + nudge, ystart - (yoffset * 4) - nudge)) withcolor clr;
        label.urt(btex {\sf RISP} etex,  (xstart + xoffset * 2 + nudge, ystart - (yoffset * 5) - nudge)) withcolor clr;

        % Proof
        label.urt(btex {\sf AB+BB+HBP+SAC+SF} etex, (xstart + nudge, ystart - (yoffset * 6) - nudge)) withcolor clr;
        label.urt(btex {\sf =\quad R+LOB+OPO} etex, (xstart + nudge + 24, ystart - (yoffset * 7) - nudge)) withcolor clr;

        % Side information
        xstart := (box_size * innings) + (32 * 6);
        ystart := -32;
        yend := 1152;
        xoffset := 128;
        midpoint := 32;

        pickup pencircle scaled thickline_t;
        draw (xstart,ystart)--(xstart,yend)--(xstart + xoffset,yend)--(xstart + xoffset,ystart)--cycle withcolor clr;
        draw (xstart,yend)--(xstart,yend+32)--(xstart + xoffset,yend+32)--(xstart + xoffset,yend)--cycle withcolor clr;

        pickup pencircle scaled thinline_t;
        draw (xstart + midpoint,ystart)--(xstart + midpoint,yend) withcolor clr;
        draw (xstart + midpoint * 2,ystart)--(xstart + midpoint * 2,yend) withcolor clr;
        draw (xstart + midpoint * 3,ystart)--(xstart + midpoint * 3,yend) withcolor clr;

        label(btex {\bigsf Team} etex rotated 90, (xstart+16,20+28)) withcolor clr;
        label(btex {\bigsf FP} etex rotated 90, (xstart+16,514+28)) withcolor clr;
        label(btex {\bigsf Temp} etex rotated 90, (xstart+16,900+28)) withcolor clr;

        label(btex {\bigsf At} etex rotated 90, (xstart+48,32+28)) withcolor clr;
        label(btex {\bigsf Att} etex rotated 90, (xstart+48,514+28)) withcolor clr;
        label(btex {\bigsf Scorer} etex rotated 90, (xstart+48,650+28)) withcolor clr;
        label(btex {\bigsf Wind} etex rotated 90, (xstart+48,900+28)) withcolor clr;

        label(btex {\bigsf Umpires} etex rotated 90, (xstart+80,12+28)) withcolor clr;
        label(btex {\bigsf HP} etex rotated 90, (xstart+80,132+32+28)) withcolor clr;
        label(btex {\bigsf 2B} etex rotated 90, (xstart+80,132+382+28)) withcolor clr;
        label(btex {\bigsf LF} etex rotated 90, (xstart+80,132+732+28)) withcolor clr;

        label(btex {\bigsf 1B} etex rotated 90, (xstart+112,132+32+28)) withcolor clr;
        label(btex {\bigsf 3B} etex rotated 90, (xstart+112,132+382+28)) withcolor clr;
        label(btex {\bigsf RF} etex rotated 90, (xstart+112,132+732+28)) withcolor clr;

        % Title boxes
        xstart := 0;
        ystart := 1152;
        iposwidth := 40;

        pickup pencircle scaled thickline_t;

        % Inning and Position box
        draw (xstart,ystart)--(xstart-iposwidth*2,ystart)--(xstart-iposwidth*2,ystart+32)--(xstart,ystart+32)--cycle withcolor clr;
        draw (xstart-iposwidth,ystart)--(xstart-iposwidth,ystart+32) withcolor clr;
        label(btex {\bigsf Pos} etex, 1/2[(xstart-iposwidth*2,ystart),(xstart-iposwidth,ystart+32)]) withcolor clr;
        label(btex {\bigsf Inn} etex, 1/2[(xstart-iposwidth,ystart),(xstart,ystart+32)]) withcolor clr;

        % Title boxes
        xstart := 0;
        ystart := 1152;
        iposwidth := 40;

        pickup pencircle scaled thickline_t;

        % Number box
        draw (xstart-iposwidth*2-namewidth,ystart)--(xstart-iposwidth*3-namewidth,ystart)--(xstart-iposwidth*3-namewidth,ystart+32)--
                (xstart-iposwidth*2-namewidth,ystart+32)--cycle withcolor clr;
        label(btex {\bigsf \#} etex, 1/2[(xstart-iposwidth*2-namewidth,ystart),(xstart-iposwidth*3-namewidth,ystart+32)]) withcolor clr;

        % Player name box
        draw (xstart-iposwidth*2,ystart)--(xstart-iposwidth*2-namewidth,ystart)--(xstart-iposwidth*2-namewidth,ystart+32)--
                (xstart-iposwidth*2,ystart+32)--cycle withcolor clr;
        label(btex {\bigsf Batter} etex, 1/2[(xstart-iposwidth*2-namewidth,ystart),(xstart-iposwidth*2,ystart+32)]) withcolor clr;

        % Inning and Position box
        draw (xstart,ystart)--(xstart-iposwidth*2,ystart)--(xstart-iposwidth*2,ystart+32)--(xstart,ystart+32)--cycle withcolor clr;
        draw (xstart-iposwidth,ystart)--(xstart-iposwidth,ystart+32) withcolor clr;
        label(btex {\bigsf Pos} etex, 1/2[(xstart-iposwidth*2,ystart),(xstart-iposwidth,ystart+32)]) withcolor clr;
        label(btex {\bigsf Inn} etex, 1/2[(xstart-iposwidth,ystart),(xstart,ystart+32)]) withcolor clr;

        % Inning boxes
        ystart := 1152;
        for xstart := 0 step 128 until ((innings - 1) * box_size):
            draw (xstart,ystart)--(xstart+128,ystart)--(xstart+128,ystart+32)--(xstart,ystart+32)--cycle withcolor clr;
        endfor

        % Batter stats boxes
        ystart := 1152;
        for xstart := (box_size * innings) step 32 until (box_size * innings)+32*5:
            draw (xstart,ystart)--(xstart+32,ystart)--(xstart+32,ystart+32)--(xstart,ystart+32)--cycle withcolor clr;
        endfor

        % Labels for batter stats
        label(btex {\bigsf AB}  etex, 1/2[((box_size * innings),ystart),((box_size * innings)+32,ystart+32)]) withcolor clr;
        label(btex {\bigsf R}   etex, 1/2[((box_size * innings)+32,ystart),((box_size * innings)+32*2,ystart+32)]) withcolor clr;
        label(btex {\bigsf H}   etex, 1/2[((box_size * innings)+32*2,ystart),((box_size * innings)+32*3,ystart+32)]) withcolor clr;
        label(btex {\bigsf RBI} etex, 1/2[((box_size * innings)+32*3,ystart),((box_size * innings)+32*4,ystart+32)]) withcolor clr;
        label(btex {\bigsf BB}  etex, 1/2[((box_size * innings)+32*4,ystart),((box_size * innings)+32*5,ystart+32)]) withcolor clr;
        label(btex {\bigsf SO}  etex, 1/2[((box_size * innings)+32*5,ystart),((box_size * innings)+32*6,ystart+32)]) withcolor clr;
        pickup pencircle scaled playline_t;

        % Pitcher Rows
        ystart := -448;
        draw_pitcher_box(0,ystart,clr);
        draw_pitcher_box(850,ystart,clr);

        % Label pitcher rows (key on top line, numbers)
        ystart := -224;
        draw_pitcher_labels(0,ystart,clr,true);
        draw_pitcher_labels(850,ystart,clr,false);

        % Draw a thick line below the pitcher row label
        pickup pencircle scaled thickline_t;
        draw (-iposwidth*3-namewidth,ystart-32)--((32*30)+iposwidth*3+namewidth,ystart-32) withcolor clr;
        pickup pencircle scaled thinline_t;

        % Numbers for pitchers
        ystart := -256;
        namebox_h := 32;
        num_offset := 6;
        yoffset := 6;
        label(btex {\sf 1} etex, (-324, ystart - yoffset)) withcolor clr;
        label(btex {\sf 2} etex, (-324, ystart - namebox_h - yoffset)) withcolor clr;
        label(btex {\sf 3} etex, (-324, ystart - namebox_h * 2 - yoffset)) withcolor clr;
        label(btex {\sf 4} etex, (-324, ystart - namebox_h * 3 - yoffset)) withcolor clr;
        label(btex {\sf 5} etex, (-324, ystart - namebox_h * 4 - yoffset)) withcolor clr;
        label(btex {\sf 6} etex, (-324, ystart - namebox_h * 5 - yoffset)) withcolor clr;

        % second column of pitchers
        label(btex {\sf 7} etex,  (526, ystart - yoffset)) withcolor clr;
        label(btex {\sf 8} etex,  (526, ystart - namebox_h - yoffset)) withcolor clr;
        label(btex {\sf 9} etex,  (526, ystart - namebox_h * 2 - yoffset)) withcolor clr;
        label(btex {\sf 10} etex, (526, ystart - namebox_h * 3 - yoffset)) withcolor clr;
        label(btex {\sf 11} etex, (526, ystart - namebox_h * 4 - yoffset)) withcolor clr;
        label(btex {\sf 12} etex, (526, ystart - namebox_h * 5 - yoffset)) withcolor clr;

        % Pitcher totals
        % TODO: Check here, from 882 to 1330, final x is 1700
        ystart := -480;
        xstart := -(iposwidth*3)-namewidth;

        draw (xstart,ystart)--(xstart+1700,ystart)--(xstart+1700,ystart+32)--(xstart,ystart+32)--cycle withcolor clr;
        for xstart := 882 step 32 until 1330:
            draw (xstart,ystart)--(xstart,ystart+32) withcolor clr;
        endfor

        xstart := -(iposwidth*3)-namewidth;
        label(btex {\midsf Pitching Totals} etex, 1/2[(xstart,ystart),(882,ystart+32)]) withcolor clr;
        pickup pencircle scaled thinline_t;

        % bench lineup box
        xstart := 1330;
        ystart := -224;
        draw_reserve_player_box(xstart, ystart, clr, false);

        % bullpen 1
        xstart := xstart+iposwidth*2+namewidth;
        draw_reserve_player_box(xstart, ystart, clr, true);

        % bullpen 2
        xstart := xstart+iposwidth*2+namewidth;
        draw_reserve_player_box(xstart, ystart, clr, true);

    endgroup
enddef;