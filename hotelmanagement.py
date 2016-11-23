"""Module controlling the main game flow"""

__author__ = "6360278: Qasim Raza, 6290157: Lars Petersen"
__copyright__ = ""
__credits__ = "" 
__email__ = "qasimr@icloud.com, petersen@informatik.uni-frankfurt.de"

import scores
import user    
    
if __name__ == "__main__":
    distribution = {"Hamburg" : (0, 1, 20, 17), "Berlin" : (14, 12, 9, 18)}
    #scores.save_score(1000, "Laura")
    #print(scores.highscores_as_string())
    user.status(distribution)
    user.help()
