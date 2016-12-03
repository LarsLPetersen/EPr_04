"""Comprises the various print statements for the game 'Hotelmanagement'"""

__author__ = "6360278: Qasim Raza, 6290157: Lars Petersen"
__copyright__ = ""
__credits__ = "" 
__email__ = "qasimr@icloud.com, petersen@informatik.uni-frankfurt.de"


# built-in modules
import os

# game specific modules
import constants


def clear():
    """Clear the screen"""
    
    os.system(constants.CLEAR)

    
def headline(day):
    """Prints header in console for each day, containing mini instructions"""
    
    print(constants.MAIN_INSTRUCTIONS)
    
    main_line = 3 * "#" + 5 * " " + "SPIELTAG " + str(day) + 5 * " " + 3 * "#"
    print(len(main_line) * "#")
    print(main_line)
    print(len(main_line) * "#")
    

def status(distribution):
    """Prints the status of the game after the last move"""

    result = ""
    width_column1 = max([len(distribution[i][0]) for i in range(len(distribution))])
    
    # build the first row
    result += "\n" + "Stadt".ljust(width_column1) + " " + \
                "[# Manager  Hotel?  Potential  Gewinn]\n"
    
    for item in distribution.items():
        result += str(item[1][0]).ljust(width_column1) + " " + \
                  "[" + str(item[1][1]).rjust(9) + \
                  str(item[1][2]).rjust(8) + \
                  str(item[1][3]).rjust(11) + \
                  str(item[1][4]).rjust(8) + "]\n"

    print(result)


def infrastructure(state):
    """Prints the adjacency matrix of the network"""

    rng_towns = range(len(state))
    result = ""

    # less than 10 cities to be displayed
    if len(state) < 11:
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
            
    # more than 10 cities to be displayed        
    else:
        # determine the width of each column
        width_first_column = max([len(state[i][0]) for i in rng_towns]) + 1
        
        # build the first row of the matrix
        result = (width_first_column + 5) * " "
        for i in rng_towns:
            result += " [" + str(i + 1) + "] "
        result += "\n"

        # build the following rows, so that the entries of the matrix
        # appear approximately in the middle of each column
        for town_index in rng_towns:
            result += ("[" + str(town_index + 1) + "] ").rjust(5) + \
                       state[town_index][0].ljust(width_first_column)
            for adjacency_index in rng_towns:
                if adjacency_index < 8:
                    result += "  " + \
                              str(state[town_index][5][adjacency_index]) + \
                              "  "
                else:
                    result += "  " + \
                              str(state[town_index][5][adjacency_index]) + \
                              "   "   
            result += "\n"
            
    #print("\nDas Straßennetz:\n")
    print(result)


def scores(highscores):
    """Prints the current highscores of the game to the console"""
    
    table = ""
    magnitude = len(str(highscores[0][0]))
    
    for i in range(len(highscores)):
        table += str(i + 1) + "." + min(2, 3 - len(str(i + 1))) * " " + \
                str(highscores[i][0]).rjust(magnitude) + \
                " " + highscores[i][1] + "\n"
                    
    print("\nHighscores:")
    print(table) 


def choice():
    """Prints the possible choices for initialising the values to the console"""
    
    text = "\nOptionen:\n" + \
           "0 -> Werte werden zufällig erzeugt.\n" + \
           "1 -> Sie geben die Werte manuell ein.\n"
    
    print(text)
           