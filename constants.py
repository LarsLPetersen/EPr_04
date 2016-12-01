"""Lists the constant parameters for the game 'Hotelmanagement'"""

__author__ = "6360278: Qasim Raza, 6290157: Lars Petersen"
__copyright__ = ""
__credits__ = "" 
__email__ = "qasimr@icloud.com, petersen@informatik.uni-frankfurt.de"


# built-in modules
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

GAME_PARAMETERS = ["Städte initialisieren", "Anzahl der Manager und deren " + \
                    "Heimatstadt festlegen", \
                    "Spieldauer festlegen", "Gewinn je Stadt festlegen", \
                    "Straßennetzwerk festlegen"]
                     
SPECIAL_MOVES = ["quit!", "new game!", "help!", "status!"]
SPECIAL_INPUT = ["quit!", "new game!", "help!"]

INPUT_INSTRUCTIONS = "------------------------------------\n" + \
                     "| 'quit!'     -> Spielende         |\n" + \
                     "| 'new game!' -> Neue Runde        |\n" + \
                     "| 'help!'     -> Anzeige Hilfe     |\n" + \
                     "------------------------------------\n"
                     
INSTRUCTIONS = "------------------------------------\n" + \
               "| 'quit!'     -> Spielende         |\n" + \
               "| 'new game!' -> Neue Runde        |\n" + \
               "| 'status!'   -> Anzeige Status    |\n" + \
               "| 'help!'     -> Anzeige Hilfe     |\n" + \
               "------------------------------------\n"

MOVES = "\nSpielzüge:\n" + \
        "----------\n" + \
        "1. 'pass<ENTER>'\n" + \
        "    -> Nichts tun.\n" + \
        "2. 'build: city<ENTER>'\n" + \
        "    -> Bauen Sie ein Hotel in city.\n" + \
        "3. 'move: number, city1, city2<ENTER>'\n" + \
        "    -> Bewegen Sie number Manager aus city1 in city2.\n" + \
        "4. 'hire: city<ENTER>'\n" + \
        "    -> Stellen Sie einen Manager in city ein.\n\n" + \
        "ACHTUNG:\n" + \
        "Sie müssen sich exakt an die Syntax halten.\n" + \
        "Es werden außerdem Konsistenzprüfungen durchgeführt.\n\n" + \
        "Weitere Optionen:\n" + \
        "-----------------\n" + \
        "a) 'quit!<ENTER>'     -> Spielende\n" + \
        "b) 'new game!<ENTER>' -> Neue Runde\n" + \
        "c) 'status!'<ENTER>'  -> Status anzeigen\n" + \
        "d) 'help!<ENTER>'     -> Aufruf dieser Hilfe\n\n" + \
        "Durch <ENTER> können Sie zwischendurch weiterschalten.\n"

NEW_HIGHSCORE_MESSAGE = "Glückwunsch!\n" + \
                        "Ihr Spiel wird in die Highscore-Liste aufgenommen."

NO_HIGHSCORE_MESSAGE = "Leider erhalten Sie für dieses Spiel keinen " + \
                       "Eintrag in die Highscore-Liste."

REPEATING_HIGHSCORE_MESSAGE = "Es existiert bereits ein identischer " + \
                              "in der Highscore-Liste."

WELCOME_MESSAGE = \
        33 * "#" + "\n" + \
        4 * "#" + 5 * " " + "Hotelmanagement" + 5 * " " + 4 * "#" + "\n" + \
        33 * "#" + "\n\n" + \
        "Herzlich Willkommen zum Spiel!\n"

GOODBYE_MESSAGE = "Auf Wiedersehen!\n"