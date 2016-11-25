"""Module for elementary user interactions like help, quit, new round"""

__author__ = "6360278: Qasim Raza, 6290157: Lars Petersen"
__copyright__ = ""
__credits__ = "" 
__email__ = "qasimr@icloud.com, petersen@informatik.uni-frankfurt.de"


import hotelmanagement
import echo


def help():
    """

    try:
        user_input = input("\nSie haben folgende Optionen:\n" +
                         "0  ->  Sie beenden das Spiel.\n" +
                         "1  ->  Sie spielen eine neue Runde.\n" +
                         "2  ->  Hilfe?\n" +
                         "Bitte wählen Sie: ")
        action_type = int(user_input)
        assert (action_type in [0, 1, 2])
        
        if action_type == 0:
            pass
        elif action_type == 1:
            hotelmanagement.main()
        elif action_type == 2:
            echo.help()
        else:
            pass
        
    except ValueError:
        os.system("cls") if os.name =="nt" else os.system("clear")
        print("\nIhre Eingabe hatte nicht das Format einer ganzen Zahl.\n"
            "Bitte versuchen Sie es erneut.")
    except AssertionError:
        os.system("cls") if os.name =="nt" else os.system("clear")
        print("\nIhre Eingabe war keine der angegebenen Optionen. \n"
            "Bitte versuchen Sie es erneut.")
    except KeyboardInterrupt:
        pass
    """
    
def play_round(state, days_left):
    """..."""

    for i in range(len(state)):
        state[i][4] += 1 

    echo.status(state)
    return [state, 1]



    
def quit():
    """...quit_value..."""
    
    pass


def new_game():
    """...new_game_value..."""

    pass
