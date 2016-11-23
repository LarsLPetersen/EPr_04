"""Module for elementary user interactions like help, quit, new round"""

__author__ = "6360278: Qasim Raza, 6290157: Lars Petersen"
__copyright__ = ""
__credits__ = "" 
__email__ = "qasimr@icloud.com, petersen@informatik.uni-frankfurt.de"


def help():
    """..."""

    print("Die help()-Methode im Modul user wurde aufgerufen.")
    pass


def quit():
    """..."""
    pass


def new_game():
    """..."""
    pass

def status(distribution):
    """..."""
    distribution_string = ""
    print("Die distribution()-Methode im Modul user wurde aufgerufen.")
    for item in distribution.items():
        distribution_string += item[0] + "  " + str(item[1]) + "\n"
    print(distribution_string)
    
