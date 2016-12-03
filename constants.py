"""Lists the 'hyper'parameters for the game 'Hotelmanagement'"""

__author__ = "6360278: Qasim Raza, 6290157: Lars Petersen"
__copyright__ = ""
__credits__ = "" 
__email__ = "qasimr@icloud.com, petersen@informatik.uni-frankfurt.de"


# built-in modules
import os


CLEAR = "cls" if os.name =="nt" else "clear"

MIN_NUM_TOWNS = 5
MAX_NUM_TOWNS = 20
LIST_OF_TOWNS = ["Berlin", "Hamburg", "München", "Köln", "Frankfurt", \
                 "Stuttgart", "Düsseldorf", "Dortmund", "Essen", "Leipzig", \
                 "Bremen", "Dresden", "Hannover", "Nürnberg", "Duisburg", \
                 "Bochum", "Wuppertal", "Bielefeld", "Bonn", "Münster", \
                 "Kiel", "Lübeck", "Karlsruhe", "Darmstadt", "Kassel", \
                 "Würzburg", "Aachen", "Wolfsburg", "Hildesheim", "Gießen", \
                 "Saarbrücken", "Kaiserslautern", "Mainz", "Wiesbaden", \
                 "Potsdam", "Cottbus", "Chemnitz", "Schwerin", "Rostock", \
                 "Magdeburg", "Erfurt", "Gotha"]
                 
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

CHOICE_MESSAGE = "\nOptionen:\n" + \
                 "0 -> Werte werden zufällig erzeugt.\n" + \
                 "1 -> Sie geben die Werte manuell ein.\n"
                 
INSTRUCTIONS = "\n------------ Kurzinfo -----------\n" + \
               "| 'quit!'     -> Spielende      |\n" + \
               "| 'new game!' -> Neue Runde     |\n" + \
               "| 'help!'     -> Anzeige Hilfe  |\n" + \
               "---------------------------------\n"
                     
INPUTS = "\nEingaben:\n" + \
         "Sie sind gerade in der Initialisierungsphase des Spiels.\n" + \
         "Hier werden Sie zur manuellen Eingabe der Spielparameter " + \
         "aufgefordert.\n" + \
         "Wahlweise kann dies auch der Computer übernehmen.\n\n" + \
         "Sie haben auch immer die Möglichkeit, folgende Eingaben zu " + \
         "machen:\n" + \
         "a) 'quit!'<ENTER>     -> Spielende\n" + \
         "b) 'new game!'<ENTER> -> Neue Runde\n" + \
         "c) 'help!'<ENTER>     -> Aufruf dieser Hilfe\n\n" + \
         "ACHTUNG:\n" + \
         "Sie müssen sich immer exakt an die geforderte Syntax halten.\n\n" + \
         "Durch <ENTER> können Sie auch zwischendurch weiterschalten.\n"

MOVES = "\nSpielzüge:\n" + \
        "1. 'pass'<ENTER>\n" + \
        "    -> Nichts tun.\n" + \
        "2. 'build: city'<ENTER>\n" + \
        "    -> Bauen Sie ein Hotel in city.\n" + \
        "3. 'move: number, city1, city2'<ENTER>\n" + \
        "    -> Bewegen Sie number Manager aus city1 in city2.\n" + \
        "4. 'hire: city'<ENTER>\n" + \
        "    -> Stellen Sie einen Manager in city ein.\n\n" + \
        "Weitere Optionen:\n" + \
        "a) 'quit!'<ENTER>     -> Spielende\n" + \
        "b) 'new game!'<ENTER> -> Neue Runde\n" + \
        "c) 'help!'<ENTER>     -> Aufruf dieser Hilfe\n\n" + \
        "ACHTUNG:\n" + \
        "Sie müssen sich exakt an die Syntax halten.\n" + \
        "Es werden außerdem Konsistenzprüfungen durchgeführt.\n\n" + \
        "Durch <ENTER> können Sie auch zwischendurch weiterschalten.\n"

NEW_HIGHSCORE_MESSAGE = "\nGlückwunsch!\n" + \
                        "Ihr Spiel wird in die Highscore-Liste aufgenommen."

NO_HIGHSCORE_MESSAGE = "\nLeider erhalten Sie für dieses Spiel keinen " + \
                       "Eintrag in die Highscore-Liste."

REPEATING_HIGHSCORE_MESSAGE = "\nEs existiert bereits ein identischer " + \
                              "in der Highscore-Liste."

WELCOME_MESSAGE = "\nWillkommen zum Spiel 'Hotelmanagement'!\n"

GOODBYE_MESSAGE = "Auf Wiedersehen!\n"