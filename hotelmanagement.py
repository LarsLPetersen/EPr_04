"""Module controlling the overall game flow"""

__author__ = "6360278: Qasim Raza, 6290157: Lars Petersen"
__copyright__ = ""
__credits__ = "" 
__email__ = "qasimr@icloud.com, petersen@informatik.uni-frankfurt.de"

import random
import scores
import user    
import echo
import game

def main():
    """Controlling the game flow"""

    echo.welcome()

    towns = game.set_towns()
    managers = game.set_managers(towns)
    timeframe = game.set_timeframe()
    potentials = game.set_potentials(towns)
    network = game.set_network(towns)

    score = 0
    distribution = {}
    
    #echo.network(network, towns)
    echo.status(distribution)

    echo.result(score)
    scores.save_score(score, "")

    echo.goodbye()
    user.help()

    


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
