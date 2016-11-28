"""Module controlling the overall game flow"""

__author__ = "6360278: Qasim Raza, 6290157: Lars Petersen"
__copyright__ = ""
__credits__ = "" 
__email__ = "qasimr@icloud.com, petersen@informatik.uni-frankfurt.de"

import os
import constants


def clear():
    """Clear the screen"""
    os.system(constants.CLEAR)
    
    
def welcome():
    """Print welcome message"""

    print("""Herzlich Willkommen zum Spiel 'Hotelmanagement'!\n""")

    
def goodbye():
    """Prints goodbye message"""

    print("Das Spiel ist beendet.")
    print("Auf Wiedersehen!\n")

    
def status(distribution):
    """Prints the status of the game after the last move"""

    result = "\nStadt [# Manager, Hotel?, Potential, Gewinn]\n"

    for item in distribution.items():
        result += str(item[1][0]) + " " + str(item[1][1:-1]) + "\n"

    print(result)


def infrastructure(state):
    """Prints the adjacency matrix of the network"""

    rng_towns = range(len(state))
    
    # determine the width of each column
    width_columns = [len(state[i][0]) for i in rng_towns]
    max_length_town = max(width_columns)
    
    # build the first row of the matrix
    result = (max_length_town + 1) * " "

    for i in rng_towns:
        result += state[i][0] + " "
    result += "\n"
    
    # build the following rows, so that the entries of matrix
    # appear approximately in the middle of each column
    for town_index in rng_towns:
        result += state[town_index][0].ljust(max_length_town) + " "
        for adjacency_index in rng_towns:
            w = width_columns[adjacency_index]
            result += " " * (w // 2) + \
                      str(state[town_index][5][adjacency_index]) + \
                      " " * (w - w // 2 - 1) + " "
        result += "\n"
        
    print(result)
    

def result(score):
    """Prints the final result"""

    print("Ihr Gesamtgewinn beträgt: " + str(score))


def help():
    """Prints the possible options for a move"""

    print("Erlaubte Aktionen sind:")
