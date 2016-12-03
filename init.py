"""Initialization of the names and parameters for the game"""

__author__ = "6360278: Qasim Raza, 6290157: Lars Petersen"
__copyright__ = ""
__credits__ = "" 
__email__ = "qasimr@icloud.com, petersen@informatik.uni-frankfurt.de"


# built-in modules
import sys
import time

# game specific modules
import echo
import constants
import random
import game
import hotelmanagement


def special_input(input_index):
    """Controls user actions during initialization of game parameters"""

    # quit!
    if input_index == 0:
        print("\nAbbruch...\n")
        sys.exit()
    # new game!
    elif input_index == 1:
        echo.clear()
        print("\n\nNeues Spiel...")
        time.sleep(1.5)
        hotelmanagement.main()
    # help!
    elif input_index == 2:
        print(constants.INPUTS)
    
    else:
        pass


def get_towns():
    """Returns tuple of pairwise different towns (user or random output)"""
    
    choice = choose(0)
    
    if choice == 0:
        num_towns = random.randint(5, 20)
        towns = tuple(random.sample(constants.LIST_OF_TOWNS, num_towns))
        echo.clear()
        print("\n\nZufällig gewählt...\n")
        for town in towns:
            print(("[" + str(towns.index(town) + 1) + "]").rjust(4) + " " + \
                    town)
        input()
        echo.clear()
        return towns
        
    elif choice == 1:
        echo.clear()
        towns = choose_towns()
        print("\n\nIhre Eingaben...\n")
        for town in towns:
            print(("[" + str(towns.index(town) + 1) + "]").rjust(4) + " " + \
                    town)
        input()
        echo.clear()
        return towns
        
    else:
        pass
    

def choose_towns():
    """Lets the user choose its own towns for the game"""
    
    is_correct_input = False
    
    while not is_correct_input:
        print()
        print(constants.INSTRUCTIONS)
        print("\nNamensliste der Städte angeben\n\n" + \
              "Geben Sie eine [Leerzeichen + Komma]-separierte Liste von\n" + \
              "mindestens 5 und maximal 20 verschiedenen Namen an, z.B.\n" + \
              "'Stadt1, Stadt2, Stadt3, ..., Stadt16'\n")
        
        try:
            user_input = input("Ihre Wahl:\n>> ")
    
            if user_input in constants.SPECIAL_INPUT:
                special_input(constants.SPECIAL_INPUT.index(user_input))
                input()
                echo.clear()
                continue
        
            else:
                towns = user_input.split(sep = ", ")
                if (len(towns) != len(set(towns))):
                    print("\nStädte müssen verschieden benannt sein!")
                    print("Neuer Versuch ...\n")
                    input()
                    echo.clear()
                    continue
                
                if not (5 <= len(towns) <= 20):
                    print("\nAnzahl der Städte nicht gemäß Vorgabe!")
                    print("Neuer Versuch ...\n")
                    input()
                    echo.clear()
                    continue
                    
                is_correct_input = True
                return tuple(towns)
            
        except ValueError:
            print("\nEingabe nicht gemäß Vorgabe!")
            print("Neuer Versuch ...\n")
            input()
            echo.clear()
            continue
        
        except KeyboardInterrupt:
            print("\nKeyboardInterrupt!")
            print("Abbruch...\n")
            sys.exit()


def get_managers(towns):
    """Returns tuple (hometown, number of managers) - user or random output"""
    
    choice = choose(1)
    
    if choice == 0:
        echo.clear()
        hometown_index = random.randint(0,len(towns)-1)
        num_managers = random.randint(5, 20)
        print("\n\nZufällig gewählt...")
        print("\nHeimatstadt:    " + towns[hometown_index])
        print("Anzahl Manager: " + str(num_managers)) 
        input()
        echo.clear()
        
    elif choice == 1:
        echo.clear()
        hometown_index = choose_hometown(towns)
        num_managers = choose_num_managers(towns[hometown_index])
        print("\n\nIhre Eingaben...")
        print("\nHeimatstadt:    " + towns[hometown_index])
        print("Anzahl Manager: " + str(num_managers)) 
        input()
        echo.clear()
        
    else:
        pass

    return (towns[hometown_index], num_managers)
    

def choose_num_managers(hometown):
    """Lets the user choose the number of managers in his hometown"""
    
    is_correct_input = False
    
    while not is_correct_input:
        echo.clear()
        print(constants.INSTRUCTIONS)
        print("\nAnzahl der Manager (Min: 5, Max: 20) in Ihrer Heimatstadt" + \
              " " + hometown + " festlegen\n")
        try:
            user_input = input("Ihre Wahl:\n>> ")
    
            if user_input in constants.SPECIAL_INPUT:
                special_input(constants.SPECIAL_INPUT.index(user_input))
                input()
                echo.clear()
                continue
            else:
                num_managers = int(user_input)
                assert (num_managers <= 20 and num_managers >= 5)
                echo.clear()
                is_correct_input = True
                return num_managers
            
        except ValueError:
            print("\nEingabe nicht gemäß Vorgabe!")
            print("Neuer Versuch ...\n")
            input()
            echo.clear()
            continue

        except AssertionError:
            print("\nEingabe nicht gemäß Vorgabe!")
            print("Neuer Versuch ...\n")
            input()
            echo.clear()
            continue

        except KeyboardInterrupt:
            print("\nKeyboardInterrupt!")
            print("Abbruch...\n")
            sys.exit()


def choose_hometown(towns):
    """Lets the user choose the hometown of his managers"""
    
    is_correct_input = False
    
    while not is_correct_input:
        print()
        print(constants.INSTRUCTIONS)
        print("\nHeimatstadt der Manager festlegen\n\n" + \
              "Geben Sie dazu den Index der festzulegenden Heimatstadt an.\n")
        print("Liste der Städte:")
        for town in towns:
            print(("[" + str(towns.index(town) + 1) + "]").rjust(4) + " " + \
                  town)
        print()
        
        try:
            user_input = input("Ihre Wahl:\n>> ")
    
            if user_input in constants.SPECIAL_INPUT:
                special_input(constants.SPECIAL_INPUT.index(user_input))
                input()
                echo.clear
                continue
            
            else:
                hometown_index = int(user_input) - 1
                assert (hometown_index < len(towns) and hometown_index >= 0)
                echo.clear()
                is_correct_input = True
                return hometown_index
            
        except ValueError:
            print("\nEingabe nicht gemäß Vorgabe!")
            print("Neuer Versuch ...\n")
            input()
            echo.clear()
            continue

        except AssertionError:
            print("\nEingabe nicht gemäß Vorgabe!")
            print("Neuer Versuch ...\n")
            input()
            echo.clear()
            continue
            
        except KeyboardInterrupt:
            print("\nKeyboardInterrupt!")
            print("Abbruch...\n")
            sys.exit()
                        
            
def get_timeframe():
    """Returns the number of days to be played (user or random output)"""

    choice = choose(2)
    
    if choice == 0:
        timeframe = random.randint(5, 40)
        print("\nZufällig gewählt: " + str(timeframe) + " Tage")
        input()
        echo.clear()
        return timeframe
        
    elif choice == 1:
        timeframe = choose_timeframe()
        print("\nIhre Eingabe: " + str(timeframe) + " Tage")
        input()
        echo.clear()
        return timeframe
        
    else:
        pass        

        
def choose_timeframe():
    """Lets the user choose the timeframe of the game (number of days)"""
    
    is_correct_input = False
    
    while not is_correct_input:
        echo.clear()
        print()
        print(constants.INSTRUCTIONS)
        print("\nAnzahl der Spieltage (Min: 5, Max: 40) festlegen\n")
        user_input = input("Ihre Wahl:\n>> ")
    
        if user_input in constants.SPECIAL_INPUT:
            special_input(constants.SPECIAL_INPUT.index(user_input))
            input()
            echo.clear()
            continue
            
        else:
            try:
                timeframe = int(user_input)
                assert (timeframe <= 40 and timeframe >= 5)
                is_correct_input = True
                return timeframe
            
            except ValueError:
                print("\nEingabe nicht gemäß Vorgabe!")
                print("Neuer Versuch ...\n")
                input()
                echo.clear()
                continue

            except AssertionError:
                print("\nEingabe nicht gemäß Vorgabe!")
                print("Neuer Versuch ...\n")
                input()
                echo.clear()
                continue


def get_potentials(towns):
    """Returns tpotential wins for each town (user or randomto output)"""
    
    choice = choose(3)
    # generate random potentials
    if choice == 0:
        echo.clear()
        potentials = tuple([random.randint(-20, 90) for i in \
                            range(len(towns))])
        print("\n\nZufällig gewählt...\n")
        max_length_town_name = max([len(town) for town in towns])
        for i in range(len(towns)):
            print(("[" + str(i + 1) + "]").rjust(4) + " " + \
                    towns[i].ljust(max_length_town_name + 1) + \
                    str(potentials[i]).rjust(3))
        input()
        echo.clear()
        return potentials
    # user defined potentials    
    elif choice == 1:
        potentials = tuple(choose_potentials(towns))
        print("\n\nIhre Eingaben...\n")
        max_length_town_name = max([len(town) for town in towns])
        for i in range(len(towns)):
            print(("[" + str(i + 1) + "]").rjust(4) + " " + \
                    towns[i].ljust(max_length_town_name + 1) + \
                    str(potentials[i]).rjust(3))
        input()
        echo.clear()
        return potentials
        
    else:
        pass


def choose_potentials(towns):
    """Lets the user choose the potential win to be made in each town"""
    
    is_correct_input = False
    
    while not is_correct_input:
        echo.clear()
        print(constants.INSTRUCTIONS)
        print("\nPotentiellen Gewinn je Stadt angeben\n\n" + \
              "Geben Sie eine [Leerzeichen + Komma]-separierte Liste von\n" + \
              str(len(towns)) + " ganzen Zahlen (Min: -20, Max: 90) an, " + \
              "z.B.\n0, -2, 88, ..., -17\n")
        print("Städte:\n")
        for town in towns:
            print(("[" + str(towns.index(town) + 1) + "]").rjust(4) + " " + \
                    town)
        
        try:
            user_input = input("\nIhre Wahl:\n>> ")
    
            if user_input in constants.SPECIAL_INPUT:
                special_input(constants.SPECIAL_INPUT.index(user_input))
                input()
                echo.clear()
                continue
        
            else:
                potentials = user_input.split(sep = ", ")
                if (len(potentials) != len(towns)):
                    print("\nEingabe hat nicht richtige Anzahl an Werten!")
                    print("Neuer Versuch ...\n")
                    input()
                    echo.clear()
                    continue
                
                potentials = [int(potential) for potential in potentials]
                if not (min(potentials) >= -20 and max(potentials) <= 90):
                    print("\nMindestens ein Wert liegt nicht im " + \
                          "vorgegebenen Bereich.")
                    print("Neuer Versuch ...\n")
                    input()
                    echo.clear()
                    continue
                    
                echo.clear()
                is_correct_input = True
                return tuple(potentials)
            
        except ValueError:
            print("\nEingabe nicht gemäß Vorgabe!")
            print("Neuer Versuch ...\n")
            input()
            echo.clear()
            continue

        except KeyboardInterrupt:
            print("\nKeyboardInterrupt!")
            print("Abbruch...\n")
            sys.exit()
            

def get_network(towns):
    """Returns adjacency tuple for the towns (user or random output)"""
    
    choice = choose(4)
    
    # random choice for adjacency matrix
    if choice == 0:
        network = [[random.randint(0, 1) for i in range(len(towns))] \
                    for j in range(len(towns))]
        
        # assures adjacency matrix to be symmetric
        for i in range(len(towns)):
            for j in range(i + 1):
                if i == j:
                    network[i][j] = 1
                else:
                    network[i][j] = network[j][i]
                j += 1
            i += 1
        
        network = tuple(network)
        echo.clear()
        print("\n\nZufälliges Straßennetz:\n")
        # define artificial pre_state to reuse echo.infrastructure for printing
        pre_state = dict([(towns.index(town), [town, None, None, None, None, \
                        network[towns.index(town)]]) for town in towns])
        
        echo.infrastructure(pre_state)
        input()
        echo.clear()
        return network
    
    # user defined adjacency matrix     
    elif choice == 1:
        network = choose_network(towns)
        print("\n\nIhr Straßennetz:\n")
        
        # define artificial pre_state to reuse echo.infrastructure for printing
        pre_state = dict([(towns.index(town), [town, None, None, None, None, \
                        network[towns.index(town)]]) for town in towns])
        
        echo.infrastructure(pre_state)
        input()
        echo.clear()
        return network
        
    else:
        pass


def choose_network(towns):
    """Lets the user choose the network parameters"""
    
    is_correct_input = False
    
    # pre-define the adjacency matrix as fully connected
    network = [[1 for i in range(len(towns))] \
                    for j in range(len(towns))]
    
    # define artificial pre_state to reuse echo.infrastructure for printing
    pre_state = dict([(towns.index(town), [town, None, None, None, None, \
                        [1 for town in towns]]) for town in towns])
    
    # let the user change the adjacency matrix entry by entry
    while not is_correct_input:
        echo.clear()
        print()
        print(constants.INSTRUCTIONS)
        echo.infrastructure(pre_state)
        print("Geben Sie exakt '<Zeile>, <Spalte>' des zu ändernden " + \
              "Eintrags an.\n" + "Der Wert wird dann 'invertiert'.\n" + \
              "Gleichzeitig wird der Eintrag 'Spalte, Zeile' invertiert " + \
              "(-> Symmetrie).\n"
              "Eine Eingabe mit <Zeile> == <Spalte> wird nicht akzeptiert.\n"
              "Beenden Sie Ihre Modifikationen mit 'end!'.\n")
              
        try:
            user_input = input("Ihre Wahl:\n>> ")
        
            # user performs special input (quit!, help!, new game!)
            if user_input in constants.SPECIAL_INPUT:
                special_input(constants.SPECIAL_INPUT.index(user_input))
                input()
                echo.clear()
                continue
        
            # user terminates modifications
            elif user_input == "end!":
                print("\nÄnderungen abgeschlossen...\n")
                input()
                echo.clear()
                is_correct_input = True
                return tuple(network)
        
            # user enters coordinates for the entry to be changed
            else:
                index = user_input.split(sep = ", ")
                
                # check whether two 'coordinate-like' like literals are passed
                if (len(index) != 2):
                    print("\nEingabe hat nicht richtige Anzahl an Werten!")
                    print("Neuer Versuch ...\n")
                    input()
                    echo.clear()
                    continue
                
                index = [int(i) for i in index]
                
                # check whether the two 'coordinates' lie in range of matrix
                if not ((1 <= index[0] <= len(towns)) and \
                        (1 <= index[1] <= len(towns))):
                    print("\nKoordinaten außerhalb gültigen Bereichs!")
                    print("Neuer Versuch ...\n")
                    input()
                    echo.clear()
                    continue
                    
                # coordinates are different and within range
                if not index[0] == index[1]:
                    value = network[index[0] - 1][index[1] - 1] + 1
                    value %= 2
                    network[index[0] - 1][index[1] - 1] = value
                    network[index[1] - 1][index[0] - 1] = value
                    
                    pre_state[index[0] - 1][5][index[1] - 1] = value
                    pre_state[index[1] - 1][5][index[0] - 1] = value
                    
                else:
                    print("\Eintrag auf Hauptdiagonale nicht veränderbar!")
                    print("Neuer Versuch ...\n")
                    input()
                    echo.clear()
                    continue
                       
        except ValueError:
            print("\nEingabe nicht gemäß Vorgabe!")
            print("Neuer Versuch ...\n")
            input()
            echo.clear()
            continue        
        
        except KeyboardInterrupt:
            print("\nKeyboardInterrupt!")
            print("Abbruch...\n")
            sys.exit()


def choose(index):
    """Lets the user choose between random and manual input of parameters"""
    
    is_correct_input = False
    print()
    
    while not is_correct_input:
        
        print(constants.INSTRUCTIONS)
        print(constants.GAME_PARAMETERS[index])
        echo.choice()
        
        try:
            user_input = input("Ihre Wahl:\n>> ")

            if user_input in constants.SPECIAL_INPUT:
                special_input(constants.SPECIAL_INPUT.index(user_input))
                input()
                echo.clear()
                continue
            elif user_input == "0":
                return 0
            elif user_input == "1":
                return 1
            else:
                print("\nEingabe nicht gemäß Vorgabe!")
                print("Neuer Versuch ...\n")
                input()
                echo.clear()
                continue
                
        except KeyboardInterrupt:
                print("\nKeyboardInterrupt!")
                print("Abbruch...\n")
                sys.exit()