"""Controls the overall flow of the game"""

__author__ = "6360278: Qasim Raza, 6290157: Lars Petersen"
__copyright__ = ""
__credits__ = "" 
__email__ = "qasimr@icloud.com, petersen@informatik.uni-frankfurt.de"


# built-in modules
import time
import os
import csv

# game specific modules
import constants
import game   
import echo
import init


def save_score(score, name):
    """Saves highscores to csv-file highscores_hotelmanagement

    Maximum number of entries in file is 10."""
    
    file_name_csv = "highscores_hotelmanagement.csv"
    highscores = []
    
    # csv-file already exists - reading scores into a list for later comparison
    if os.path.isfile(file_name_csv):
        with open(file_name_csv, newline = '') as csvfile:
            score_reader = csv.reader(csvfile, delimiter = " ")
            for row in score_reader:
                if row[0] == "Punkte":
                    continue
                highscores.append([int(row[0]), row[1]])

        # less than 10 scores up to now; [score, name] not already in list
        if len(highscores) < 10 and [score, name] not in highscores:
            highscores.append([score, name])
            highscores.sort(reverse=True)
            with open(file_name_csv, "w") as csvfile:
                score_writer = csv.writer(csvfile, delimiter = " ")
                score_writer.writerow(["Punkte"] + ["Name"])
                for entry in highscores:
                        score_writer.writerow([entry[0]] + [entry[1]])
            print(constants.NEW_HIGHSCORE_MESSAGE)
                
        # less than 10 scores up to now; [score, name] already in list
        elif len(highscores) < 10 and [score, name] in highscores:
            print(constants.NEW_HIGHSCORE_MESSAGE)

        # 10 or more scores up to now; [score, name] already in list
        elif len(highscores) >= 10 and [score, name] in highscores:
            print(constants.REPEATING_HIGHSCORE_MESSAGE)

        # 10 or more scores up to now: [score, name] not in list
        else:
            current_min = min(highscores)
            index_min = highscores.index(current_min)
            # score is greater than minimum in list
            if score > current_min[0]:
                highscores[index_min] = [score, name]
                highscores.sort(reverse=True)
                with open(file_name_csv, "w") as csvfile:
                    score_writer = csv.writer(csvfile, delimiter = " ")
                    score_writer.writerow(["Punkte"] + ["Name"])
                    for entry in highscores:
                        score_writer.writerow([entry[0]] + [entry[1]])
                print(constants.NEW_HIGHSCORE_MESSAGE)
            # score is equal or less than minimum in list
            else:
                print(constants.NO_HIGHSCORE_MESSAGE)

    # csv-file has to be created with a first entry
    else:
        highscores.append([score, name])
        with open(file_name_csv, "w") as csvfile:
            score_writer = csv.writer(csvfile, delimiter = " ")
            score_writer.writerow(["Punkte"] + ["Name"])
            score_writer.writerow([score] + [name])
        print(constants.NEW_HIGHSCORE_MESSAGE)
    
    echo.scores(highscores)


def get_name():
    """Returns name of the player - used later on for the highscore list"""
    
    is_real_name = False

    while not is_real_name:
    
        print("Bitte geben Sie Ihren Namen für die Aufnahme in\n" + \
              "die Highscore-Liste an:")
        user_input = input(">> ")
   
    
        # user performs special input (quit!, help!, new game!)
        if user_input in constants.SPECIAL_INPUT:
            game.special_input(constants.SPECIAL_INPUT.index(user_input))
            input()
            echo.clear()
            continue
    
        # input is interpreted as a name
        else:
            name = user_input
            is_real_name = True
            return name


def main():
    """Controlling the game flow"""

    echo.clear()
    print(constants.WELCOME_MESSAGE)
    
    # getting towns
    towns = init.get_towns()
    num_towns = len(towns)
    rng_towns = range(num_towns)
    
    # getting hometown and number of managers in hometown
    managers = [0 for town in rng_towns]
    (hometown, num_managers) = init.get_managers(towns)
    
    managers[towns.index(hometown)] = num_managers
    
    # getting the number of days to be played
    period = init.get_timeframe()
    
    # getting possible wins for each city
    potentials = init.get_potentials(towns)
    
    # getting the network (adjacency)
    network = init.get_network(towns)

    hotels = [0 for town in rng_towns]
    
    score_of_today = [0 for town in rng_towns]
    score = 0
    
    # mapping cities to integers (inverse of towns)
    cities = dict((town, towns.index(town)) for town in towns)
    
    # mapping integers to towns (inverse of cities)
    towns = dict((towns.index(town), town) for town in towns)
    
    state = dict((town,[towns[town], managers[town], hotels[town], \
                potentials[town], score_of_today[town], network[town]]) \
                for town in rng_towns)
    
    day = 1
    echo.clear()
    
    # main loop over the number of days to be played        
    while day < period + 1:
        
        echo.headline(day)
        
        print("\nStatus am Beginn von Tag (" + str(day) + \
              "/" + str(period) + "):")
        echo.status(state)
        
        days_left = period - day
        [state, day_shift, city] = game.play_round(state, days_left, \
                                                    towns, cities)

        # special case: hire -> day_shift > 1
        if day_shift > 1:
            for shift in range(day_shift):
                profit_today = sum([state[town][4] for town in rng_towns])
                if shift > 0:
                    print("Automatische Berechnung ...\n")
                    time.sleep(.5)
                # new manager is active with the beginning of day d + 2
                # where d is the day he was hired (in the morning)
                if shift == 2:
                    state[city][1] += 1
                print("\nStatus am Ende von Tag " + str(day + shift))
                echo.status(state)
                print("Gewinn an Tag " + str(day + shift) + ": " + \
                        str(profit_today))
                
                # adding the profit of the current day to the overall score
                score += profit_today
                print("Gesamtgewinn mit Ende von Tag " + str(day + shift) + \
                        ": " + str(score) + "\n")
                shift += 1
                
                # resetting the score of the day
                for town in rng_towns:
                    state[town][4] = 0
                
                game.calculate_profit(state)
                
                input()
                echo.clear()

        # every other case
        else:
            profit_today = sum([state[town][4] for town in rng_towns])

            print("\nStatus am Ende von Tag (" + str(day) + \
              "/" + str(period) + "):")
            echo.status(state)

            print("Gewinn an Tag " + str(day) + ": " + str(profit_today))
            score += profit_today

            print("Gesamtgewinn mit Ende von Tag " + str(day) + ": " + \
                  str(score) + "\n")
            
            # setting the score of the day to 0 for beginning of next day
            for town in rng_towns:
                state[town][4] = 0
            
            input()
            echo.clear()
        
        day += day_shift
      
    print("Spielende!\n")
    print("Gesamtgewinn im Spiel: " + str(score) + "\n")    
    
    name = get_name()
    save_score(score, name)

    print(constants.GOODBYE_MESSAGE)



if __name__ == "__main__":
     main()