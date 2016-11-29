"""Module listing constants for the game 'Hotelmanagement'"""

__author__ = "6360278: Qasim Raza, 6290157: Lars Petersen"
__copyright__ = ""
__credits__ = "" 
__email__ = "qasimr@icloud.com, petersen@informatik.uni-frankfurt.de"

import os

CLEAR = "cls" if os.name =="nt" else "clear"

MIN_NUM_TOWNS = 5
MAX_NUM_TOWNS = 20

MIN_NUM_MANAGERS_HOME = 5
MAX_NUM_MANAGERS_HOME = 20

MIN_PERIOD = 5
MAX_PERIOD = 40

MIN_PROFIT = -20
MAX_PROFIT = 90

MAX_NUM_HOTELS = 1
COSTS_HOTEL = -20

DAYSHIFT_PASS = 1
DAYSHIFT_BUILD = 1
DAYSHIFT_MOVE = 1
DAYSHIFT_HIRE = 3
    
INSTRUCTIONS = "Minianleitung:\n" + \
               "'quit!'     -> Spielende\n" + \
               "'new game!' -> Neue Runde\n" + \
               "'help!'     -> Anzeige der Hilfe\n"

SPECIAL_MOVES = ["quit!", "new game!", "help!"]

MOVES = "Erlaubte Spielzüge:\n" + \
        "'pass'        -> Nichts tun."
