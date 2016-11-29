"""Module controlling the overall game_test flow"""

__author__ = "6360278: Qasim Raza, 6290157: Lars Petersen"
__copyright__ = ""
__credits__ = "" 
__email__ = "qasimr@icloud.com, petersen@informatik.uni-frankfurt.de"

import time
import os

import constants
import scores
import user    
import echo
import game_test


def main():
    """Controlling the game flow"""

    echo.clear()
    echo.welcome()

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
    
    state = dict((town,[towns[town], managers[town], hotels[town], potentials[town], \
                     score_of_today[town], network[town]]) for town in rng_towns)
    towns = dict((town, towns.index(town)) for town in towns)

    print("AUSGANGSSTATUS")
    echo.status(state)

    day = 1
        
    while day < period + 1:
        print(constants.INSTRUCTIONS)
        print("SPIELTAG " + str(day) + "\n")
        days_left = period - day
        [state, day_shift] = user.play_round(state, days_left, towns)

        # special case: hire -> day_shift > 1
        if day_shift > 1:
            for shift in range(day_shift):
                profit_today = sum([state[town][4] for town in rng_towns])
                if shift > 0:
                    print("Automatische Berechnung ...\n")
                    time.sleep(1)
                print("STATUS am Ende von Tag " + str(day + shift))
                echo.status(state)
                print("Gewinn an Tag " + str(day + shift) + ": " + str(profit_today))
                score += profit_today
                print("Gesamtgewinn mit Ende von Tag " + str(day + shift) + ": " + \
                      str(score) + "\n")
                shift += 1
                for town in rng_towns:
                    state[town][4] = 0
                user.calculate_profit(state)

        # every other case
        else:
            profit_today = sum([state[town][4] for town in rng_towns])

            print("SITUATION am Ende von Tag " + str(day))
            echo.status(state)

            print("Gewinn an Tag " + str(day) + ": " + str(profit_today))
            score += profit_today

            print("Gesamtgewinn mit Ende von Tag " + str(day) + ": " + \
                  str(score) + "\n")

        day += day_shift
        
    echo.result(score)
    scores.save_score(score, name)

    echo.goodbye()
    


if __name__ == "__main__":
    """while True:
        try: 
            towns = ["S1", "S", "S3", "S4444"]
            distribution = {"Hamburg" : (0, 1, 20, 17), "Berlin" : (14, 12, 9, 18)}
            adjacency = [[1, 0, 1, 0], [0, 1, 1, 1], [1, 1, 1, 0], [0, 1, 0, 1]]
            #scores.save_score(1000, "Laura")
            #print(scores.highscores_as_string())
            #echo.status(distribution)
            #user.help()
            user_input = input("Geben Sie etwas ein: ")
        except KeyboardInterrupt:
            user.help()
    """
    main()
