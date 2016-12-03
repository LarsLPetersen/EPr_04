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


def special_input(input_index):
    """Controls user actions during initialization of game parameters"""

    # quit!
    if input_index == 0:
        sys.exit()
    # new game!
    elif input_index == 1:
        hotelmanagement.main()
    # help!
    elif input_index == 2:
        print(constants.INPUTS)    
    
    else:
        pass


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

    
def play_round(state, days_left, towns, cities):
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
        elif user_input[0:7] == "build: " and user_input[7:] in cities.keys():
            city = user_input[7:]
            if state[cities[city]][2] == 1:
                print("\nEs existiert bereits ein Hotel in " + city + ".\n" + \
                      "Sie können dort kein weiteres errichten.\n" + \
                      "Wählen Sie einen anderen Zug.")
                print("Neuer Versuch...\n")
                continue

            else:
                state = evaluate_build(state, cities[city])
                is_correct_move = True
                return [state, constants.DAYSHIFT_BUILD, None]
        
        #move
        elif user_input[0:6] == "move: ":
            move_parameters = user_input[6:].split(sep=", ")
            try:
                num_managers = int(move_parameters[0])
                if num_managers < 1:
                    print("\nAnzahl der Manager muss >= 0 sein.")
                    print("Neuer Versuch...\n")
                    continue
    
                assert (move_parameters[1] in cities.keys() and \
                       move_parameters[2] in cities.keys())

                city1 = move_parameters[1]
                if num_managers > state[cities[city1]][1]:
                    print("\nAnzahl der Manager zu groß für " + city1 + ".")
                    print("Neuer Versuch...\n")
                    continue
                
                city2 = move_parameters[2]
                
                if state[cities[city1]][5][cities[city2]] == 0:
                    print("\nKeine Verbindung zwischen " + city1 + " und " + \
                            city2 + ".")
                    print("Neuer Versuch...\n")
                    continue
                    
                state = evaluate_move(state, num_managers, \
                                  cities[city1], cities[city2])
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
        elif user_input[0:6] == "hire: " and user_input[6:] in cities.keys():           
            city = user_input[6:]
            if days_left < constants.DAYSHIFT_HIRE - 1:
                print("\nEs sind nur noch " + str(days_left) + " Runden " + \
                      "zu spielen.\n" +
                      "Dieser Zug benötigt mehr Zeit.\n" + \
                      "Wählen Sie einen anderen Zug.\n")
                continue

            state = evaluate_hire(state, cities[city])
            is_correct_move = True
            return [state, constants.DAYSHIFT_HIRE, cities[city]]

        
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


def evaluate_build(state, city):
    """Updates game state by adding a hotel to the respective town"""

    state[city][2] += 1
    state = calculate_profit(state)
    return state

    
def evaluate_move(state, num_managers, city1, city2):
    """Updates game state by shifting num_managers from town1 to town2"""

    state[city1][1] -= num_managers
    state[city2][1] += num_managers
    state = calculate_profit(state)
    return state

    
def evaluate_hire(state, city):
    """Updates game state by raising the num of managers in town by one"""

    #state[city][1] += 1
    state = calculate_profit(state)
    return state
                                  