"""..."""

__author__ = "6360278: Qasim Raza, 6290157: Lars Petersen"
__copyright__ = ""
__credits__ = "" 
__email__ = "qasimr@icloud.com, petersen@informatik.uni-frankfurt.de"


# game specific modules
import echo
import constants
import random
import user


def get_towns():
    """Returns an n-tuple of pairwise different towns (strings of length > 0)"""
    
    choice = choose(0)
    
    if choice == 0:
        num_towns = random.randint(5, 20)
        towns = tuple([("Stadt" + str(i)) for i in range(1, num_towns + 1)])
        print("\nZufällig erzeugte Stödte:")
        print(towns)
        input()
        echo.clear()
        return towns
        
    elif choice == 1:
        towns = choose_towns()
        print("\nIhre eingegebenen Stödte:")
        print(towns)
        input()
        echo.clear()
        return towns
        
    else:
        pass
    

def choose_towns():
    """Lets the user choose its own towns"""
    
    is_correct_input = False
    print()
    
    while not is_correct_input:
        
        print("\nNamensliste der Städte angeben\n\n" + \
              "Geben Sie eine [Leerzeichen + Komma]-separierte Liste von\n" + \
              "mindestens 5 und maximal 20 verschiedenen Namen an, z.B.\n" + \
              "Stadt1, Stadt2, Stadt3, ..., Stadt 16\n")
        user_input = input("Ihre Wahl:\n>> ")
    
        if user_input in constants.SPECIAL_INPUT:
            user.special_input(constants.SPECIAL_INPUT.index(user_input))
            input()
            echo.clear
            continue
        
        else:
            try:
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


def get_managers(towns):
    """Returns a 2-tuple (hometown, m) where m = # managers"""
    
    choice = choose(1)
    
    if choice == 0:
        num_managers = random.randint(5, 20)
        hometown_index = random.randint(0,len(towns)-1)
        print("\nZufällig gewählte Heimatstadt und Anzahl Manager:")
        print((towns[hometown_index], num_managers)) 
        input()
        echo.clear()
        return (towns[hometown_index], num_managers)
    
    elif choice == 1:
        hometown = towns[choose_hometown(towns) - 1]
        num_managers = choose_num_managers()
        print("\nIhre gewählte Heimatstadt und Anzahl Manager:")
        print((towns[hometown_index], num_managers)) 
        input()
        echo.clear()
        return (hometown, num_managers)
        
    else:
        pass


def choose_num_managers():
    """Lets the user choose the number of managers in his hometown"""
    
    is_correct_input = False
    print()
    
    while not is_correct_input:
        
        print("\nAnzahl der Manager in Ihrer Heimatstadt (>= 5 und <= 20) " + \
              "festlegen\n")
        user_input = input("Ihre Wahl:\n>> ")
    
        if user_input in constants.SPECIAL_INPUT:
            user.special_input(constants.SPECIAL_INPUT.index(user_input))
            input()
            echo.clear
            continue
        else:
            try:
                num_managers = int(user_input)
                assert (num_managers <= 20 and num_managers >= 5)
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


def choose_hometown(towns):
    """Lets the user choose the hometown of his managers"""
    
    is_correct_input = False
    print()
    
    while not is_correct_input:
        
        print("\nHeimatstadt der Manager festlegen\n" + \
              "Geben Sie dazu den Index der festzulegenden Heimatstadt an\n" + \
              "(>= 1 und <= " + str(len(towns)) + ")\n")
        print("Liste der Städte:")
        print(towns)
        print()
        
        user_input = input("Ihre Wahl:\n>> ")
    
        if user_input in constants.SPECIAL_INPUT:
            user.special_input(constants.SPECIAL_INPUT.index(user_input))
            input()
            echo.clear
            continue
        else:
            try:
                hometown = int(user_input)
                assert (hometown <= len(towns) and hometown >= 1)
                is_correct_input = True
                return hometown
            
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
                        
            
def get_time_frame():
    """Returns the number of days to be played"""

    choice = choose(2)
    
    if choice == 0:
        time_frame = random.randint(5, 40)
        print("\nZufällig gewählte Spieldauer: " + str(time_frame) + " Tage")
        input()
        echo.clear()
        return time_frame
        
    elif choice == 1:
        time_frame = choose_time_frame()
        print("\nIhre gewählte Spieldauer: " + str(time_frame) + " Tage")
        input()
        echo.clear()
        return time_frame
        
    else:
        pass
        
        
def choose_time_frame():
    """Lets the user choose the timeframe of the game (number of days"""
    
    is_correct_input = False
    print()
    
    while not is_correct_input:
        
        print("\nAnzahl der Spieltage (>= 5 und <= 40) festlegen\n")
        user_input = input("Ihre Wahl:\n>> ")
    
        if user_input in constants.SPECIAL_INPUT:
            user.special_input(constants.SPECIAL_INPUT.index(user_input))
            input()
            echo.clear
            continue
            
        else:
            try:
                time_frame = int(user_input)
                assert (time_frame <= 40 and time_frame >= 5)
                is_correct_input = True
                return time_frame
            
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
    """Returns tuple containing potential wins to be be made in each town"""
    
    choice = choose(3)
    
    if choice == 0:
        potentials = [random.randint(-20, 90) for i in range(len(towns))]
        print("\nZufällig gewählte potentielle Gewinne:")
        print(potentials)
        input()
        echo.clear()
        return tuple(potentials)
        
    elif choice == 1:
        potentials = choose_potentials(towns)
        print("\nIhre gewählten potentiellen Gewinne:")
        print(potentials)
        input()
        echo.clear()
        return tuple(potentials)
        
    else:
        pass


def choose_potentials(towns):
    """Lets the user choose the potential win to be made in each town"""
    
    is_correct_input = False
    print()
    
    while not is_correct_input:
        
        print("\nPotentiellen Gewinn je Stadt angeben\n\n" + \
              "Geben Sie eine [Leerzeichen + Komma]-separierte Liste von\n" + \
              str(len(towns)) + " ganzen Zahlen (>= -20 und <= 90) an, " + \
              "z.B.\n0, -2, 88, ..., -17\n")
        print("Ihre Städte:")
        print(towns)
        
        user_input = input("Ihre Wahl:\n>> ")
    
        if user_input in constants.SPECIAL_INPUT:
            user.special_input(constants.SPECIAL_INPUT.index(user_input))
            input()
            echo.clear
            continue
        
        else:
            try:
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
                    
                is_correct_input = True
                return tuple(potentials)
            
            except ValueError:
                print("\nEingabe nicht gemäß Vorgabe!")
                print("Neuer Versuch ...\n")
                input()
                echo.clear()
                continue

            
def get_network(towns):
    """Returns a tuple representing the network of streets between the towns"""
    
    choice = choose(4)
    
    if choice == 0:
        network = [[random.randint(0, 1) for i in range(len(towns))] \
                    for j in range(len(towns))]
        
        for i in range(len(towns)):
            for j in range(i + 1):
                if i == j:
                    network[i][j] = 1
                else:
                    network[i][j] = network[j][i]
                j += 1
            i += 1
        
        print("\nZufällig gewähltes Straßennetz:")
        print(tuple(network))
        input()
        echo.clear()
        return tuple(network)
        
    elif choice == 1:
        network = choose_network(towns)
        print("\nIhr gewähltes Straßennetz:")
        print(network)
        input()
        echo.clear()
        return network
        
    else:
        pass
    

def choose_network(towns):
    """Lets the user choose the network parameters"""
    
    is_correct_input = False
    print()
    
    while not is_correct_input:
        
        print("\nParameter für das Straßennetz angeben\n\n" + \
              "Geben Sie eine [Leerzeichen + Komma]-separierte Liste von\n" + \
              "Nullen und Einsen für die obere Dreiecksmatrix der " + \
              "Adjazenzmatrix an, also für Indexpaare von Städten " + \
              "(Stadt1, Stadt2),\nwobei index_Stadt2 > index_Stadt1 ist:\n")
        print("Ihre Städte:")
        print(towns)
        
        user_input = input("Ihre Wahl:\n>> ")
    
        if user_input in constants.SPECIAL_INPUT:
            user.special_input(constants.SPECIAL_INPUT.index(user_input))
            input()
            echo.clear
            continue
        
        else:
            try:
                network = user_input.split(sep = ", ")
                if (len(network) != (len(towns) ** 2 - len(towns)) / 2):
                    print("\nEingabe hat nicht richtige Anzahl an Werten!")
                    print("Neuer Versuch ...\n")
                    input()
                    echo.clear()
                    continue
                
                network = [int(street) for street in network]
                if not (min(potentials) >= 0 and max(potentials) <= 1):
                    print("\nMindestens ein Wert liegt nicht im " + \
                          "vorgegebenen Bereich.")
                    print("Neuer Versuch ...\n")
                    input()
                    echo.clear()
                    continue
                    
                is_correct_input = True
                return tuple(network)
            
            except ValueError:
                print("\nEingabe nicht gemäß Vorgabe!")
                print("Neuer Versuch ...\n")
                input()
                echo.clear()
                continue


def get_name():
    """returns user naem"""
    
    name = input("Ihr Name: ")
    
    return name


def choose(index):
    """Lets the user choose between random and manual input of parameters"""
    
    is_correct_input = False
    print()
    
    while not is_correct_input:
        
        print(constants.GAME_PARAMETERS[index])
        echo.choice()
        user_input = input("Ihre Wahl:\n>> ")
    
        if user_input in constants.SPECIAL_INPUT:
            user.special_input(constants.SPECIAL_INPUT.index(user_input))
            input()
            echo.clear
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