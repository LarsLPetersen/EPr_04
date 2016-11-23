"""..."""


__author__ = "6360278: Qasim Raza, 6290157: Lars Petersen"
__copyright__ = ""
__credits__ = "" 
__email__ = "qasimr@icloud.com, petersen@informatik.uni-frankfurt.de"


import os.path
import csv


def save_score(score, name):
    """..."""

    file_name_csv = "highscores_hotelmanagement.csv"

    # csv-file already exists
    if os.path.isfile(file_name_csv):
        with open(file_name_csv, newline='') as csvfile:
            score_reader = csv.reader(csvfile, delimiter=" ")
            current_scores = []
            for row in score_reader:
                if row[0] == "Punkte":
                    continue
                current_scores.append([int(row[0]), row[1]])

        # less than 10 scores up to now; [score, name] not already in list
        if len(current_scores) < 10 and [score, name] not in current_scores:
            current_scores.append([score, name])
            current_scores.sort(reverse=True)
            with open(file_name_csv, "w") as csvfile:
                score_writer = csv.writer(csvfile, delimiter=" ")
                score_writer.writerow(["Punkte"] + ["Name"])
                for entry in current_scores:
                        score_writer.writerow([entry[0]] + [entry[1]])
                
        # less than 10 scores up to now; [score, name] already in list
        elif len(current_scores) < 10 and [score, name] in current_scores:
            pass

        # 10 or more scores up to now; [score, name] already in list
        elif len(current_scores) >= 10 and [score, name] in current_scores:
            pass

        # 10 or more scores up to now: [score, name] not in list
        else:
            current_min = min(current_scores)
            index_min = current_scores.index(current_min)
            # score is greater than minimum in list
            if score > current_min[0]:
                current_scores[index_min] = [score, name]
                current_scores.sort(reverse=True)
                with open(file_name_csv, "w") as csvfile:
                    score_writer = csv.writer(csvfile, delimiter = " ")
                    score_writer.writerow(["Punkte"] + ["Name"])
                    for entry in current_scores:
                        score_writer.writerow([entry[0]] + [entry[1]])
            # score is equal or less than minimum in list
            else:
                pass

    # csv-file has to be created with a first entry
    else:
        with open(file_name_csv, "w") as csvfile:
            score_writer = csv.writer(csvfile, delimiter = " ")
            score_writer.writerow(["Punkte"] + ["Name"])
            score_writer.writerow([score] + [name])


def highscores_as_string(file_name_csv="highscores_hotel_management.csv"):
    """..."""
    
    file_name_csv = "highscores_hotel_management.csv"
    highscores = "\n"
    
    # csv-file aready exists
    if os.path.isfile(file_name_csv):
        with open(file_name_csv, newline='') as csvfile:
            score_reader = csv.reader(csvfile, delimiter=" ")
            for row in score_reader:
                score = row[0].rjust(8)
                name = row[1][0:16].ljust(16)
                highscores += score + "  |  " + name + "\n"
                highscores += 29 * "-" + "\n"

    # csv-file doesn't exist
    else:
        pass
    
    return highscores 
