"""..."""


__author__ = "6360278: Qasim Raza, 6290157: Lars Petersen"
__copyright__ = ""
__credits__ = "" 
__email__ = "qasimr@icloud.com, petersen@informatik.uni-frankfurt.de"


# built-in modules
import os.path
import csv

# game specific modules
import constants
import scores
import echo


def save_score(score, name):
    """..."""

    file_name_csv = "highscores_hotelmanagement.csv"
    highscores = []
    
    # csv-file already exists
    if os.path.isfile(file_name_csv):
        with open(file_name_csv, newline='') as csvfile:
            score_reader = csv.reader(csvfile, delimiter=" ")
            for row in score_reader:
                if row[0] == "Punkte":
                    continue
                highscores.append([int(row[0]), row[1]])

        # less than 10 scores up to now; [score, name] not already in list
        if len(highscores) < 10 and [score, name] not in highscores:
            highscores.append([score, name])
            highscores.sort(reverse=True)
            with open(file_name_csv, "w") as csvfile:
                score_writer = csv.writer(csvfile, delimiter=" ")
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
