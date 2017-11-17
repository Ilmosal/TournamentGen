#!/usr/bin/env python3
# -*-encoding=utf8-*-
import os
import sys

MODULE_PATH = os.path.realpath(__file__)[:-len("/bin/TournamentGen.py")]

os.chdir(MODULE_PATH)
sys.path = sys.path + [""]

print(MODULE_PATH)

from tournamentgen.tournament.teams import Team, Player
from tournamentgen.graphics import graphics

def run():
	pelaaja_1 = Player("Tommi")
	pelaaja_2 = Player("Tuuli")

	pelaajat = [pelaaja_1, pelaaja_2]
	joukkue = Team("Tuulispäät", pelaajat, [0.6, 0.0, 0.0])

	print(joukkue.toString())	
	
	graphics.window()
