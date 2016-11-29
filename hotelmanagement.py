"""Controls the overall game_test flow"""

__author__ = "6360278: Qasim Raza, 6290157: Lars Petersen"
__copyright__ = ""
__credits__ = "" 
__email__ = "qasimr@icloud.com, petersen@informatik.uni-frankfurt.de"


# built-in modules
import time
import os

# game specific modules
import constants
import scores
import user    
import echo
import game_test


def main():
    """Controlling the game flow"""

    echo.clear()
    print(constants.WELCOME_MESSAGE)
    
    name = game_test.get_name()
    
    towns = game_test.get_towns()
    num_towns = len(towns)
    rng_towns = range(num_towns)
    
    (hometown, num_managers) = game_test.get_managers(towns)
    managers = [0 for town in rng_towns]
    managers[towns.index(hometown)] = num_managers

    period = game_test.get_timeframe()
    potentials = game_test.get_potentials(towns)
    network = game_test.get_network(towns)

    hotels = [0 for town in rng_towns]

    score_of_today = [0 for town in rng_towns]
    score = 0
    
    state = dict((town,[towns[town], managers[town], hotels[town], \
                potentials[town], score_of_today[town], network[town]]) \
                for town in rng_towns)
    towns = dict((town, towns.index(town)) for town in towns)

    day = 1
    echo.clear()
            
    while day < period + 1:
        
        echo.headline(day)
        
        print("\nStatus am Beginn von Tag " + str(day) + ":")
        echo.status(state)
        
        days_left = period - day
        [state, day_shift, city] = user.play_round(state, days_left, towns)

        # special case: hire -> day_shift > 1
        if day_shift > 1:
            for shift in range(day_shift):
                profit_today = sum([state[town][4] for town in rng_towns])
                if shift > 0:
                    print("Automatische Berechnung ...\n")
                    time.sleep(.5)
                # new manager is active with the beginning of day d + 2
                # where d is the day he was hired
                if shift == 2:
                    state[city][1] += 1
                print("\nStatus am Ende von Tag " + str(day + shift))
                echo.status(state)
                print("Gewinn an Tag " + str(day + shift) + ": " + \
                        str(profit_today))
                score += profit_today
                print("Gesamtgewinn mit Ende von Tag " + str(day + shift) + \
                        ": " + str(score) + "\n")
                shift += 1
                for town in rng_towns:
                    state[town][4] = 0
                user.calculate_profit(state)
                input()
                echo.clear()

        # every other case
        else:
            profit_today = sum([state[town][4] for town in rng_towns])

            print("\nStatus am Ende von Tag " + str(day) + ":")
            echo.status(state)

            print("Gewinn an Tag " + str(day) + ": " + str(profit_today))
            score += profit_today

            print("Gesamtgewinn mit Ende von Tag " + str(day) + ": " + \
                  str(score) + "\n")
            
            input()
            echo.clear()
        
        day += day_shift
    
            
    
    print("Spielende!\n")
    print("Gesamtgewinn im Spiel: " + str(score) + "\n")    
    
    scores.save_score(score, name)

    print(constants.GOODBYE_MESSAGE)


if __name__ == "__main__":
    
    main()