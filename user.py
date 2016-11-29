"""Module for elementary user interactions like help, quit, new round"""

__author__ = "6360278: Qasim Raza, 6290157: Lars Petersen"
__copyright__ = ""
__credits__ = "" 
__email__ = "qasimr@icloud.com, petersen@informatik.uni-frankfurt.de"


# built-in modules
import os
import sys

# game specific modules
import hotelmanagement
import echo
import constants


def special_move(move_index, state, days_left):
    """Controls user actions not concerning real game moves"""

    # quit!
    if move_index == 0:
        sys.exit()
    # new game!
    elif move_index == 1:
        hotelmanagement.main()
    # help!
    elif move_index == 2:
        print(constants.MOVES)
    # status!
    elif move_index == 3:
        print()
        echo.infrastructure(state)
        print("Aktueller Status:")
        echo.status(state)
        print("Verbleibende Tage: " + str(days_left + 1))
        
    else:
        pass


    
def play_round(state, days_left, towns):
    """Controls user actions concerning game moves"""

    rng_towns = range(len(state))
    
    # print the network to help the user plan the next move
    echo.infrastructure(state)

    # set profit at beginning of day to 0
    for town in rng_towns:
        state[town][4] = 0

    is_correct_move = False

    while not is_correct_move:
        user_input = input("Ihr Spielzug: \n>> ")
        
        # special move
        if user_input in constants.SPECIAL_MOVES:
            special_move(constants.SPECIAL_MOVES.index(user_input), state, \
                        days_left)
            input()
            continue
            
        # pass
        if user_input == "pass":
            state = evaluate_pass(state)
            is_correct_move = True
            return [state, constants.DAYSHIFT_PASS, None]

        # build
        elif user_input[0:7] == "build: " and user_input[7:] in towns.keys():
            town = user_input[7:]
            if state[towns[town]][2] == 1:
                print("\nEs existiert bereits ein Hotel in " + town + ".\n" + \
                      "Sie können dort kein weiteres errichten.\n" + \
                      "Wählen Sie einen anderen Zug.")
                print("Neuer Versuch...\n")
                continue

            else:
                state = evaluate_build(state, towns[town])
                is_correct_move = True
                return [state, constants.DAYSHIFT_BUILD, None]
        
        #move
        elif user_input[0:6] == "move: ":
            move_parameters = user_input[6:].split(sep=", ")
            try:
                num_managers = int(move_parameters[0])
                if num_managers < 0:
                    print("\nAnzahl der Manager muss >= 0 sein.")
                    print("Neuer Versuch...\n")
                    continue
    
                assert (move_parameters[1] in towns.keys() and \
                       move_parameters[2] in towns.keys())

                town1 = move_parameters[1]
                if num_managers > state[towns[town1]][1]:
                    print("\nAnzahl der Manager zu groß für " + town1 + ".\n")
                    print("Neuer Versuch...\n")
                    continue
                
                town2 = move_parameters[2]
                state = evaluate_move(state, num_managers, \
                                  towns[town1], towns[town2])
                is_correct_move = True
                return [state, constants.DAYSHIFT_MOVE, None]

            except ValueError:
                print("\nIhre Angabe zur Anzahl der Manager ist nicht " + \
                        "korrekt.\n")
                print("Neuer Versuch...\n")
                continue
            except AssertionError:
                print("\nIhre Angabe zu den Städten ist nicht korrekt.\n")
                print("Neuer Versuch...\n")
                continue
            except IndexError:
                print("\nNicht genügend Parameter angegeben.\n")
                print("Neuer Versuch...\n")
                continue
  
        #hire
        elif user_input[0:6] == "hire: " and user_input[6:] in towns.keys():           
            town = user_input[6:]
            if days_left < constants.DAYSHIFT_HIRE - 1:
                print("\nEs sind nur noch " + str(days_left) + " Runden " + \
                      "zu spielen.\n" +
                      "Dieser Zug benötigt mehr Zeit.\n" + \
                      "Wählen Sie einen anderen Zug.\n")
                continue

            state = evaluate_hire(state, towns[town])
            is_correct_move = True
            return [state, constants.DAYSHIFT_HIRE, towns[town]]

        
        else:
            print("\nSpielzug nicht gemäß Vorgaben!")
            print("Neuer Versuch...\n")
            continue


def calculate_profit(state):
    """Calculates daily profit in the game given the current state"""

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
    """Updates game state by doing nothing"""

    state = calculate_profit(state)
    return state


def evaluate_build(state, town):
    """Updates game state by adding a hotel to the respective town"""

    state[town][2] += 1
    state = calculate_profit(state)
    return state

    
def evaluate_move(state, num_managers, town1, town2):
    """Updates game state by shifting num_managers from town1 to town2"""

    state[town1][1] -= num_managers
    state[town2][1] += num_managers
    state = calculate_profit(state)
    return state

    
def evaluate_hire(state, town):
    """Updates game state by raising the num of managers in town by one"""

    #state[town][1] += 1
    state = calculate_profit(state)
    return state
                                  