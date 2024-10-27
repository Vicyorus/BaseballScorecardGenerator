#!/bin/bash

mpost -tex=latex scorecard_away.mp
mptopdf scorecard_away.*

mpost -tex=latex scorecard_home.mp
mptopdf scorecard_home.*

pdflatex scorecard.tex
