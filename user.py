"""Module for elementary user interactions like help, quit, new round"""

__author__ = "6360278: Qasim Raza, 6290157: Lars Petersen"
__copyright__ = ""
__credits__ = "" 
__email__ = "qasimr@icloud.com, petersen@informatik.uni-frankfurt.de"

import os
import sys

import hotelmanagement
import echo
import constants


def special_move(move_index):
    """..."""

    # 
    if move_index == 0:
        sys.exit()
    elif move_index == 1:
        hotelmanagement.main()
    elif move_index == 2:
        print(constants.MOVES)
    else:
        pass


    
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
        user_input = input("Ihr Spielzug: \n>> ")
        
        # special move
        if user_input in constants.SPECIAL_MOVES:
            special_move(constants.SPECIAL_MOVES.index(user_input))
            
        # pass
        if user_input == "pass":
            state = evaluate_pass(state)
            is_correct_move = True
            return [state, constants.DAYSHIFT_PASS]

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
                return [state, constants.DAYSHIFT_BUILD]
        
        #move
        elif user_input[0:6] == "move: ":
            move_parameters = user_input[6:].split(sep=", ")
            try:
                num_managers = int(move_parameters[0])
                if num_managers < 0:
                    print("Anzahl der Manager muss >= 0 sein.")
                    continue
    
                assert (move_parameters[1] in towns.keys() and \
                       move_parameters[2] in towns.keys())

                town1 = move_parameters[1]
                if num_managers > state[towns[town1]][1]:
                    print("Anzahl der Manager zu groß für " + town1 + ".\n")
                    continue
                
                town2 = move_parameters[2]
                state = evaluate_move(state, num_managers, \
                                  towns[town1], towns[town2])
                is_correct_move = True
                return [state, constants.DAYSHIFT_MOVE]

            except ValueError:
                print("Ihre Angabe zur Anzahl der Manager ist nicht korrekt.")
                continue
            except AssertionError:
                print("Ihre Angabe zu den Städten ist nicht korrekt.")
                continue
            except IndexError:
                print("Nicht genügend Parameter angegeben.")
                continue
  
        #hire
        elif user_input[0:6] == "hire: " and user_input[6:] in towns.keys():           
            town = user_input[6:]
            if days_left < constants.DAYSHIFT_HIRE + 1:
                print("Es sind nur noch " + str(days_left) + " Runden " + \
                      "zu spielen.\n" +
                      "Dieser Zug benoetigt mehr Zeit.\n" + \
                      "Waehlen Sie einen anderen Zug.")
                continue

            state = evaluate_hire(state, towns[town])
            is_correct_move = True
            return [state, constants.DAYSHIFT_HIRE]

        
        else:
            print("Ihr Spielzug entspricht nicht einer der Vorgaben!")
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
            state[town][4] += constants.COSTS_HOTEL
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

    state[town][2] += 1
    state = calculate_profit(state)
    return state

    
def evaluate_move(state, num_managers, town1, town2):
    """..."""

    state[town1][1] -= num_managers
    state[town2][1] += num_managers
    state = calculate_profit(state)
    return state

    
def evaluate_hire(state, town):
    """..."""

    state[town][1] += 1
    state = calculate_profit(state)
    return state
                                  

    
def quit():
    """...quit_value..."""
    
    pass


def new_game():
    """...new_game_value..."""

    pass
