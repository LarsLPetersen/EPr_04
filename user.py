"""Module for elementary user interactions like help, quit, new round"""

__author__ = "6360278: Qasim Raza, 6290157: Lars Petersen"
__copyright__ = ""
__credits__ = "" 
__email__ = "qasimr@icloud.com, petersen@informatik.uni-frankfurt.de"


import hotelmanagement
import echo
import os
import sys
import constants
import re


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
    
def play_round(state, days_left, towns):
    """..."""

    rng_towns = range(len(state))
    
    # print the network to help the user plan the next move
    print("Das Straßennetz:\n")
    echo.infrastructure(state)

    # set profit at beginning of day to 0
    for town in rng_towns:
        state[town][4] = 0

    is_correct_move = False

    while not is_correct_move:
        user_input = input("Ihr Spielzug: ")
        
        # pass
        if user_input == "pass":
            state = evaluate_pass(state)
            is_correct_move = True
            return [state, 1]

        # build
        elif user_input[0:7] == "build: " and user_input[7:] in towns.keys():
            town = user_input[7:]
            if state[towns[town]][2] == 1:
                print("Es existiert bereits ein Hotel in " + town + ".\n" + \
                      "Sie können dort kein weiteres errichten.\n" + \
                      "Waehlen Sie einen anderen Zug.")
                continue

            else:
                state = evaluate_build(state, towns[town])
                is_correct_move = True
                return [state, 1]
        
        #hire
        elif user_input[0:6] == "hire: " and user_input[6:] in towns.keys():           
            town = user_input[6:]
            if days_left < 3:
                print("Es sind nur noch " + str(days_left) + " Runden" + \
                      "zu spielen.\n" +
                      "Dieser Zug benoetigt mehr Zeit.\n" + \
                      "Waehlen Sie einen anderen Zug.")
                continue

            state = evaluate_hire(state, towns[town])
            is_correct_move = True
            return [state, 3]


        else:
            print("Eingabe nicht gemaess den Vorgaben.")
            continue
    """

         user_input = input("0 -> new game\n" + \
                           "1 -> quit\n" + \
                           "Ihre Wahl: ")
        if user_input == "0":
            hotelmanagement.main()
        elif user_input == "1":
            sys.exit()
        else:
            pass
            """

def calculate_profit(state):
    """..."""

    rng_towns = range(len(state))

    for town in rng_towns:
        # town has a hotel and at least one manager
        if state[town][2] == 1 and state[town][1] > 0:
            state[town][4] += state[town][3]
        # town has a hotel but no manager
        elif state[town][2] == 1 and state[town][1] == 0:
            state[town][4] -= 20
        # town has no hotel
        elif state[town][2] == 0:
            pass

    return state

    
def evaluate_pass(state):
    """..."""

    state = calculate_profit(state)
    return state


def evaluate_build(state, town):
    """..."""

    state[town][2] = 1
    state = calculate_profit(state)
    return state

    
def evaluate_move():
    """..."""
    pass

    
def evaluate_hire(state, town):
    """..."""

    state[town][1] += 1
    state = calculate_profit(state)
    """
    state = evaluate_pass(state)
    state = evaluate_pass(state)
    """
    return state
                                  

    
def quit():
    """...quit_value..."""
    
    pass


def new_game():
    """...new_game_value..."""

    pass
