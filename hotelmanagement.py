"""Module controlling the overall game_test flow"""

__author__ = "6360278: Qasim Raza, 6290157: Lars Petersen"
__copyright__ = ""
__credits__ = "" 
__email__ = "qasimr@icloud.com, petersen@informatik.uni-frankfurt.de"

import random

import scores
import user    
import echo
import game_test



def main():
    """Controlling the game flow"""

    echo.welcome()

    towns = game_test.set_towns()

    (hometown, num_managers) = game_test.set_managers(towns)
    managers = [0 for i in range(len(towns))]
    managers[towns.index(hometown)] = num_managers

    period = game_test.set_timeframe()
    potentials = game_test.set_potentials(towns)
    network = game_test.set_network(towns)

    hotels = [0 for i in range(len(towns))]
    
    score_of_today = [0 for i in range(len(towns))]
    score = 0
    
    #global state
    state = dict((i,[towns[i], managers[i], hotels[i], potentials[i], \
                     score_of_today[i], network[i]]) for i in range(len(towns)))
    print(state)

    #global day
    day = 1
    
    while day < period + 1:
        [state, day_shift] = user.play_round(state, period - day)
        score += sum([state[i][4] for i in range(len(state))])
        day += day_shift
        
    
    echo.network(network, towns)
    #echo.status(distribution)

    echo.result(score)
    scores.save_score(score, "")

    
    echo.goodbye()
    #user.help()

    


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
            echo.network(adjacency, towns)
            user_input = input("Geben Sie etwas ein: ")
        except KeyboardInterrupt:
            user.help()
    """
    main()
