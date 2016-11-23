"""Module controlling the overall game flow"""

__author__ = "6360278: Qasim Raza, 6290157: Lars Petersen"
__copyright__ = ""
__credits__ = "" 
__email__ = "qasimr@icloud.com, petersen@informatik.uni-frankfurt.de"


def welcome():
    """Print welcome message"""

    print("""Herzlich Willkommen zum Spiel 'Hotelmanagement'!""")

    
def goodbye():
    """Prints goodbye message"""

    print("Das Spiel ist nun beendet.")
    print("Auf Wiedersehen!")

    
def status(distribution):
    """Prints the status of the game after the last move"""

    result = "\nStadt (Manager?, Hotel?, Potential, Gewinn)\n"

    for item in distribution.items():
        output += item[0] + "  " + str(item[1]) + "\n"

    print(result)


def network(adjacency, towns):
    """Prints the adjacency matrix of the network"""

    # determine the width of each column
    width_columns = [0]

    for town in towns:
        width_columns.append(len(town))
    width_columns[0] = max(width_columns)
    
    # build the first row of the matrix
    result = (width_columns[0] + 1) * " "
    
    for town in towns:
        result += town + " "
    result += "\n"
    
    # build the following rows
    num1_town = 0
    for row in adjacency:
        result += towns[num1_town].ljust(width_columns[0]) + " "
        num2_town = 1
        for element in row:
            result += " " * (width_columns[num2_town] // 2) + \
                      str(element) + \
                      " " * (width_columns[num2_town] - \
                             width_columns[num2_town] // 2 - 1) + " "
            num2_town += 1
        num1_town += 1
        result += "\n"
        
    print(result)
    

def result(score):
    """Prints the final result"""

    print("Ihr Gesamtgewinn beträgt: " + str(score))


def help():
    """Prints the possible options for a move"""

    print("Erlaubte Aktionen sind:")
