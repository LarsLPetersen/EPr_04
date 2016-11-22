"""Module controlling the main game flow"""

__author__ = "6360278: Qasim Raza, 6290157: Lars Petersen"
__copyright__ = ""
__credits__ = "" 
__email__ = "qasimr@icloud.com, petersen@informatik.uni-frankfurt.de"

import scores
    
    
if __name__ == "__main__":
    scores.save_score(1000, "Laura")
    print(scores.highscores_as_string())

    
