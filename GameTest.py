"""..."""

__author__ = "6360278: Qasim Raza, 6290157: Lars Petersen"
__copyright__ = ""
__credits__ = "" 
__email__ = "qasimr@icloud.com, petersen@informatik.uni-frankfurt.de"

import random

def get_towns():
    town_amount=input("Geben Sie eine Anzahl von Städten an: ")
    town_amount=int
    if town_amount <= 20 or town_amount >= 5:
        town1=Berlin
        town2=Hamburg
        town3=München
        town4=Köln
        town5=Frankfurt
        town6=Stuttgart
        town7=Düsseldorf
        town8=Dortmund
        town9=Essen
        town10=Leipzig
        town11=Bremen
        town12=Dresden
        town13=Hannover
        town14=Nürnberg
        town15=Duisburg
        town16=Bochum
        town17=Wuppertal
        town18=Bielefeld
        town19=Bonn
        town20=Münster
        
        return (town1, town2, town3, town4, town5, town6, town7, town8, town9, town10, town11, town12, town13, town14, town15, town16, town17, town18, town,19, town20)


    hometown=input("Suchen sie sich eine Heimatstadt aus: ")
    if input=="town1" or input=="town2" or input=="town3" or input=="town4" or input=="town5" or input=="town6" or input=="town7" or input=="town8" or input=="town9" or input=="town10" or input=="town11" or input=="town12" or input=="town13" or input=="town14" or input=="town15" or input=="town16" or input=="town17" or input=="town18" or input=="town19" or input=="town20":
        return (hometown)

    else:
        return ("Ungültige Eingabe")
        
def get_managers(towns):
    """returns a 2-tuple (hometown, m) where m = # managers"""
    manager_amount=input("Geben sie die Anzahl an Managern für die Heimatstadt an: ")
    manager_amount=int
    if manager_amount < 5 or manager_amount > 20:
        print("Ungültige Eingabe")
    else:
        hometown_mananger == input



def get_timeframe():
    rounds=int(input("Geben sie die Anzahl der Runden: "))
    ("Sie können 5 bis 40 Runden spielen")
    
    return 5
    

def get_potentials(towns):
    
    town_pot=input("Wollen Sie den Gewinn der Städte bestimmen?")

if input == Ja:
    town1_potencial=random.randint(-20,90)
    town2_potencial=random.randint(-20,90)
    town3_potencial=random.randint(-20,90)
    town4_potencial=random.randint(-20,90)
    town5_potencial=random.randint(-20,90)
    town6_potencial=random.randint(-20,90)
    town7_potencial=random.randint(-20,90)
    town8_potencial=random.randint(-20,90)
    town9_potencial=random.randint(-20,90)
    town10_potencial=random.randint(-20,90)
    town11_potencial=random.randint(-20,90)
    town12_potencial=random.randint(-20,90)
    town13_potencial=random.randint(-20,90)
    town14_potencial=random.randint(-20,90)
    town15_potencial=random.randint(-20,90)
    town16_potencial=random.randint(-20,90)
    town17_potencial=random.randint(-20,90)
    town18_potencial=random.randint(-20,90)
    town19_potencial=random.randint(-20,90)
    town20_potencial=random.randint(-20,90)

return (town1_potencial, town2_potencial, town3_potencial, town4_potencial, town5_potencial, town6_potencial, town7_potencial, town8_potencial, town9_potencial, town10_potencial, town11_potencial, town12_potencial, town13_potencial, town14_potencial, town15_potencial, town16_potencial, town17_potencial, town18_potencial, town19_potencial, town20_potencial)

if not input == Ja:
    print("Geben Sie dann nun die Gewinne der Städte selbstständig an:")

    print("Beachten sie: Die zahl muss sich zwischen -20 und 90 befinden.")

    town1_potencial=input("Gewinn Berlin= ")
    town1_potencial=int

    if town1_potencial > 90 or town1_potencial < -20:
        return ()
    else:
        return ("Ungültige Eingabe")

    town2_potencial=input("Gewinn Hamburg= ")
    town2_potencial=int

    if town2_potencial > 90 or town2_potencial < -20:
        return ()
    else:
        return ("Ungültige Eingabe")

    town3_potencial=input("Gewinn München= ")
    town3_potencial=int

    if town3_potencial > 90 or town3_potencial < -20:
        return ()
    else:
        return ("Ungültige Eingabe")

    town4_potencial=input("Gewinn Köln= ")
    town4_potencial=int

    if town4_potencial > 90 or town4_potencial < -20:
        return ()
    else:
        return ("Ungültige Eingabe")

    town5_potencial=input("Gewinn Frankfurt= ")
    town5_potencial=int

    if town5_potencial > 90 or town5_potencial < -20:
        return ()
    else:
        return ("Ungültige Eingabe")

    town6_potencial=input("Gewinn Stuttgart= ")
    town6_potencial=int

    if town6_potencial > 90 or town6_potencial < -20:
        return ()
    else:
        return ("Ungültige Eingabe")

    town7_potencial=input("Gewinn Düsseldorf= ")
    town7_potencial=int

    if town7_potencial > 90 or town7_potencial < -20:
        return ()
    else:
        return ("Ungültige Eingabe")

    town8_potencial=input("Gewinn Dortmund= ")
    town8_potencial=int

    if town8_potencial > 90 or town8_potencial < -20:
        return ()
    else:
        return ("Ungültige Eingabe")

    town9_potencial=input("Gewinn Essen= ")
    town9_potencial=int

    if town9_potencial > 90 or town9_potencial < -20:
        return ()
    else:
        return ("Ungültige Eingabe")

    town10_potencial=input("Gewinn Leipzig= ")
    town10_potencial=int

    if town10_potencial > 90 or town10_potencial < -20:
        return ()
    else:
        return ("Ungültige Eingabe")

    town11_potencial=input("Gewinn Bremen= ")
    town11_potencial=int

    if town11_potencial > 90 or town11_potencial < -20:
        return ()
    else:
        return ("Ungültige Eingabe")


    town12_potencial=input("Gewinn Dresden= ")
    town12_potencial=int

    if town12_potencial > 90 or town12_potencial < -20:
        return ()
    else:
        return ("Ungültige Eingabe")

    town13_potencial=input("Gewinn Hannover= ")
    town13_potencial=int

    if town13_potencial > 90 or town13_potencial < -20:
        return ()
    else:
        return ("Ungültige Eingabe")

    town14_potencial=input("Gewinn Nürnburg= ")
    town14_potencial=int

    if town14_potencial > 90 or town14_potencial < -20:
        return ()
    else:
        return ("Ungültige Eingabe")

    town15_potencial=input("Gewinn Duisburg= ")
    town15_potencial=int

    if town15_potencial > 90 or town15_potencial < -20:
        return ()
    else:
        return ("Ungültige Eingabe")

    town16_potencial=input("Gewinn Bochum= ")
    town16_potencial=int

    if town16_potencial > 90 or town16_potencial < -20:
        return ()
    else:
        return ("Ungültige Eingabe")

    town17_potencial=input("Gewinn Wuppertal= ")
    town17_potencial=int

    if town17_potencial > 90 or town17_potencial < -20:
        return ()
    else:
        return ("Ungültige Eingabe")

    town18_potencial=input("Gewinn Bielefeld= ")
    town18_potencial=int
    
    if town18_potencial > 90 or town18_potencial < -20:
        return ()
    else:
        return ("Ungültige Eingabe")

    town19_potencial=input("Gewinn Bonn= ")
    town19_potencial=int

    if town19_potencial > 90 or town19_potencial < -20:
        return ()
    else:
        return ("Ungültige Eingabe")
        
    town20_potencial=input("Gewinn Münster= ")
    town20_potencial=int

    if town20_potencial > 90 or town20_potencial < -20:
        return ()
    else:
        return ("Ungültige Eingabe")


def get_network(towns):
    """retruns n-tuple of n-tuples with values s_ij"""
    roads=input("Wollen Sie die Straße zufällig bestimmt bekommen?")
    if input==Ja:
        Berlin + Berlin==1
        road_Berlin_Hamburg=random.randint(0,1)
        road_Berlin_München=random.randint(0,1)
        road_Berlin_Köln=random.randint(0,1)
        road_Berlin_Frankfurt=random.randint(0,1)
        road_Berlin_Stuttgart=random.randint(0,1)
        road_Berlin_Düsselforf=random.randint(0,1)
        road_Berlin_Dortmund=random.randint(0,1)
        road_Berlin_Essen=random.randint(0,1)
        road_Berlin_Leipzig=random.randint(0,1)
        road_Berlin_Bremen=random.randint(0,1)
        road_Berlin_Dresden=random.randint(0,1)
        road_Berlin_Hannover=random.randint(0,1)
        road_Berlin_Nürnberg=random.randint(0,1)
        road_Berlin_Duisburg=random.randint(0,1)
        road_Berlin_Bochum=random.randint(0,1)
        road_Berlin_Wuppertal=random.randint(0,1)
        road_Berlin_Bielefeld=random.randint(0,1)
        road_Berlin_Bonn=random.randint(0,1)
        road_Berlin_Münster=random.randint(0,1)

        road_Hamburg_Hamburg=1
        road_Hamburg_Berlin=random.randint(0,1)
        road_Hamburg_München=random.randint(0,1)
        road_Hamburg_Köln=random.randint(0,1)
        road_Hamburg_Frankfurt=random.randint(0,1)
        road_Hamburg_Stuttgart=random.randint(0,1)
        road_Hamburg_Düsseldorf=random.randint(0,1)
        road_Hamburg_Dortmund=random.randint(0,1)
        road_Hamburg_Essen=random.randint(0,1)
        road_Hamburg_Leipzig=random.randint(0,1)
        road_Hamburg_Bremen=random.randint(0,1)
        road_Hamburg_Dresden=random.randint(0,1)
        road_Hamburg_Hannover=random.randint(0,1)
        road_Hamburg_Nürnberg=random.randint(0,1)
        road_Hamburg_Duisburg=random.randint(0,1)
        road_Hamburg_Bochum=random.randint(0,1)
        road_Hamburg_Wuppertal=random.randint(0,1)
        road_Hamburg_Bielefeld=random.randint(0,1)
        road_Hamburg_Bonn=random.randint(0,1)
        road_Hamburg_Münster=random.randint(0,1)

        road_München_München=random.randint(0,1)
        road_München_Berlin=random.randint(0,1)
        road_München_Hamburg=random.randint(0,1)
        road_München_Köln=random.randint(0,1)
        road_München_Frankfurt=random.randint(0,1)
        road_München_Stuttgart=random.randint(0,1)
        road_München_Düsseldorf=random.randint(0,1)
        road_München_Dortmund=random.randint(0,1)
        road_München_Essen=random.randint(0,1)
        road_München_Leipzig=random.randint(0,1)
        road_München_Bremen=random.randint(0,1)
        road_München_Dresden=random.randint(0,1)
        road_München_Hannover=random.randint(0,1)
        road_München_Nürnberg=random.randint(0,1)
        road_München_Duisburg=random.randint(0,1)
        road_München_Bochum=random.randint(0,1)
        road_München_Wuppertal=random.randint(0,1)
        road_München_Bielefeld=random.randint(0,1)
        road_München_Bonn=random.randint(0,1)
        road_München_Münster=random.randint(0,1)
  
        road_Köln_Köln==1
        road_Köln_Berlin=random.randint(0,1)
        road_Köln_Hamburg=random.randint(0,1)
        road_Köln_München=random.randint(0,1)
        road_Köln_Frankfurt=random.randint(0,1)
        road_Köln_Stuttgart=random.randint(0,1)
        road_Köln_Düsseldort=random.randint(0,1)
        road_Köln_Dortmund=random.randint(0,1)
        road_Köln_Essen=random.randint(0,1)
        road_Köln_Leipzig=random.randint(0,1)
        road_Köln_Bremen=random.randint(0,1)
        road_Köln_Dresden=random.randint(0,1)
        road_Köln_Hannover=random.randint(0,1)
        road_Köln_Nürnberg=random.randint(0,1)
        road_Köln_Duisburg=random.randint(0,1)
        road_Köln_Bochum=random.randint(0,1)
        road_Köln_Wuppertal=random.randint(0,1)
        road_Köln_Bielefeld=random.randint(0,1)
        road_Köln_Bonn=random.randint(0,1)
        road_Köln_Münster=random.randint(0,1)

        road_Frankfurt_Berlin=random.randint(0,1)
        road_Frankfurt_Hamburg=random.randint(0,1)
        road_Frankfurt_München=random.randint(0,1)
        road_Frankfurt_Köln=random.randint(0,1)
        road_Frankfurt_Frankfurt==1
        road_Frankfurt_Stuttgart=random.randint(0,1)
        road_Frankfurt_Düsseldorf=random.randint(0,1)
        road_Frankfurt_Dortmund=random.randint(0,1)
        road_Frankfurt_Essen=random.randint(0,1)
        road_Frankfurt_Leipzig=random.randint(0,1)
        road_Frankfurt_Bremen=random.randint(0,1)
        road_Frankfurt_Dresden=random.randint(0,1)
        road_Frankfurt_Hannover=random.randint(0,1)
        road_Frankfurt_Nürnberg=random.randint(0,1)
        road_Frankfurt_Duisburg=random.randint(0,1)
        road_Frankfurt_Bochum=random.randint(0,1)
        road_Frankfurt_Wuppertal=random.randint(0,1)
        road_Frankfurt_Bielefeld=random.randint(0,1)
        road_Frankfurt_Bonn=random.randint(0,1)
        road_Frankfurt_Münster=random.randint(0,1)

        road_Stuttgart_Berlin=random.randint(0,1)
        road_Stuttgart_Hamburg=random.randint(0,1)
        road_Stuttgart_München=random.randint(0,1)
        road_Stuttgart_Köln=random.randint(0,1)
        road_Stuttgart_Frankfurt=random.randint(0,1)
        road_Stuttgart_Stuttgart==1
        road_Stuttgart_Düsseldorf=random.randint(0,1)
        road_Stuttgart_Dortmund=random.randint(0,1)
        road_Stuttgart_Essen=random.randint(0,1)
        road_Stuttgart_Leipzig=random.randint(0,1)
        road_Stuttgart_Bremen=random.randint(0,1)
        road_Stuttgart_Dresden=random.randint(0,1)
        road_Stuttgart_Hannover=random.randint(0,1)
        road_Stuttgart_Nürnberg=random.randint(0,1)
        road_Stuttgart_Duisburg=random.randint(0,1)
        road_Stuttgart_Bochum=random.randint(0,1)
        road_Stuttgart_Wuppertal=random.randint(0,1)
        road_Stuttgart_Bielefeld=random.randint(0,1)
        road_Stuttgart_Bonn=random.randint(0,1)
        road_Stuttgart_Münster=random.randint(0,1)

        road_Düsseldorf_Berlin=random.randint(0,1)
        road_Düsseldorf_Hamburg=random.randint(0,1)
        road_Düsseldorf_München=random.randint(0,1)
        road_Düsseldorf_Köln=random.randint(0,1)
        road_Düsseldorf_Frankfurt=random.randint(0,1)
        road_Düsseldorf_Stuttgart=random.randint(0,1)
        road_Düsseldorf_Düsseldorf==1
        road_Düsseldorf_Dortmund=random.randint(0,1)
        road_Düsseldorf_Essen=random.randint(0,1)
        road_Düsseldorf_Leipzig=random.randint(0,1)
        road_Düsseldorf_Bremen=random.randint(0,1)
        road_Düsseldorf_Dresden=random.randint(0,1)
        road_Düsseldorf_Hannover=random.randint(0,1)
        road_Düsseldorf_Nürnberg=random.randint(0,1)
        road_Düsseldorf_Duisburg=random.randint(0,1)
        road_Düsseldorf_Bochum=random.randint(0,1)
        road_Düsseldorf_Wuppertal=random.randint(0,1)
        road_Düsseldorf_Bielefeld=random.randint(0,1)
        road_Düsseldorf_Bonn=random.randint(0,1)
        road_Düsseldorf_Münster=random.randint(0,1)

        road_Dortmund_Berlin=random.randint(0,1)
        road_Dortmund_Hamburg=random.randint(0,1)
        road_Dortmund_München=random.randint(0,1)
        road_Dortmund_Köln=random.randint(0,1)
        road_Dortmund_Frankfurt=random.randint(0,1)
        road_Dortmund_Stuttgart=random.randint(0,1)
        road_Dortmund_Düsseldorf=random.randint(0,1)
        road_Dortmund_Dortmund==1
        road_Dortmund_Essen=random.randint(0,1)
        road_Dortmund_Leipzig=random.randint(0,1)
        road_Dortmund_Bremen=random.randint(0,1)
        road_Dortmund_Dresden=random.randint(0,1)
        road_Dortmund_Hannover=random.randint(0,1)
        road_Dortmund_Nürnberg=random.randint(0,1)
        road_Dortmund_Duisburg=random.randint(0,1)
        road_Dortmund_Bochum=random.randint(0,1)
        road_Dortmund_Wuppertal=random.randint(0,1)
        road_Dortmund_Bielefeld=random.randint(0,1)
        road_Dortmund_Bonn=random.randint(0,1)
        road_Dortmund_Münster=random.randint(0,1)

        road_Essen_Berlin=random.randint(0,1)
        road_Essen_Hamburg=random.randint(0,1)
        road_Essen_München=random.randint(0,1)
        road_Essen_Köln=random.randint(0,1)
        road_Essen_Frankfurt=random.randint(0,1)
        road_Essen_Stuttgart=random.randint(0,1)
        road_Essen_Düsseldorf=random.randint(0,1)
        road_Essen_Dortmund=random.randint(0,1)
        road_Essen_Essen==1
        road_Essen_Leipzig=random.randint(0,1)
        road_Essen_Bremen=random.randint(0,1)
        road_Essen_Dresden=random.randint(0,1)
        road_Essen_Hannover=random.randint(0,1)
        road_Essen_Nürnberg=random.randint(0,1)
        road_Essen_Duisburg=random.randint(0,1)
        road_Essen_Bochum=random.randint(0,1)
        road_Essen_Wuppertal=random.randint(0,1)
        road_Essen_Bielefeld=random.randint(0,1)
        road_Essen_Bonn=random.randint(0,1)
        road_Essen_Münster=random.randint(0,1)

        road_Leipzig_Berlin=random.randint(0,1)
        road_Leipzig_Hamburg=random.randint(0,1)
        road_Leipzig_München=random.randint(0,1)
        road_Leipzig_Köln=random.randint(0,1)
        road_Leipzig_Frankfurt=random.randint(0,1)
        road_Leipzig_Stuttgart=random.randint(0,1)
        road_Leipzig_Düsseldorf=random.randint(0,1)
        road_Leipzig_Dortmund=random.randint(0,1)
        road_Leipzig_Essen=random.randint(0,1)
        road_Leipzig_Leipzig==1
        road_Leipzig_Bremen=random.randint(0,1)
        road_Leipzig_Dresden=random.randint(0,1)
        road_Leipzig_Hannover=random.randint(0,1)
        road_Leipzig_Nürnberg=random.randint(0,1)
        road_Leipzig_Duisburg=random.randint(0,1)
        road_Leipzig_Bochum=random.randint(0,1)
        road_Leipzig_Wuppertal=random.randint(0,1)
        road_Leipzig_Bielefeld=random.randint(0,1)
        road_Leipzig_Bonn=random.randint(0,1)
        road_Leipzig_Münster=random.randint(0,1)

        road_Bremen_Berlin=random.randint(0,1)
        road_Bremen_Hamburg=random.randint(0,1)
        road_Bremen_München=random.randint(0,1)
        road_Bremen_Köln=random.randint(0,1)
        road_Bremen_Frankfurt=random.randint(0,1)
        road_Bremen_Stuttgart=random.randint(0,1)
        road_Bremen_Düsseldorf=random.randint(0,1)
        road_Bremen_Dortmund=random.randint(0,1)
        road_Bremen_Essen=random.randint(0,1)
        road_Bremen_Leipzig=random.randint(0,1)
        road_Bremen_Bremen==1
        road_Bremen_Dresden=random.randint(0,1)
        road_Bremen_Hannover=random.randint(0,1)
        road_Bremen_Nürnberg=random.randint(0,1)
        road_Bremen_Duisburg=random.randint(0,1)
        road_Bremen_Bochum=random.randint(0,1)
        road_Bremen_Wuppertal=random.randint(0,1)
        road_Bremen_Bielefeld=random.randint(0,1)
        road_Bremen_Bonn=random.randint(0,1)
        road_Bremen_Münster=random.randint(0,1)

        road_Dresden_Berlin=random.randint(0,1)
        road_Dresden_Hamburg=random.randint(0,1)
        road_Dresden_München=random.randint(0,1)
        road_Dresden_Köln=random.randint(0,1)
        road_Dresden_Frankfurt=random.randint(0,1)
        road_Dresden_Stuttgart=random.randint(0,1)
        road_Dresden_Düsseldorf=random.randint(0,1)
        road_Dresden_Dortmund=random.randint(0,1)
        road_Dresden_Essen=random.randint(0,1)
        road_Dresden_Leipzig=random.randint(0,1)
        road_Dresden_Bremen=random.randint(0,1)
        road_Dresden_Dresden==1
        road_Dresden_Hannover=random.randint(0,1)
        road_Dresden_Nürnberg=random.randint(0,1)
        road_Dresden_Duisburg=random.randint(0,1)
        road_Dresden_Bochum=random.randint(0,1)
        road_Dresden_Wuppertal=random.randint(0,1)
        road_Dresden_Bielefeld=random.randint(0,1)
        road_Dresden_Bonn=random.randint(0,1)
        road_Dresden_Münster=random.randint(0,1)

        road_Hannover_Berlin=random.randint(0,1)
        road_Hannover_Hamburg=random.randint(0,1)
        road_Hannover_München=random.randint(0,1)
        road_Hannover_Köln=random.randint(0,1)
        road_Hannover_Frankfurt=random.randint(0,1)
        road_Hannover_Stuttgart=random.randint(0,1)
        road_Hannover_Düsseldorf=random.randint(0,1)
        road_Hannover_Dortmund=random.randint(0,1)
        road_Hannover_Essen=random.randint(0,1)
        road_Hannover_Leipzig=random.randint(0,1)
        road_Hannover_Bremen=random.randint(0,1)
        road_Hannover_Dresden=random.randint(0,1)
        road_Hannover_Hannover==1
        road_Hannover_Nürnberg=random.randint(0,1)
        road_Hannover_Duisburg=random.randint(0,1)
        road_Hannover_Bochum=random.randint(0,1)
        road_Hannover_Wuppertal=random.randint(0,1)
        road_Hannover_Bielefeld=random.randint(0,1)
        road_Hannover_Bonn=random.randint(0,1)
        road_Hannover_Münster=random.randint(0,1)

        road_Nürnberg_Berlin=random.randint(0,1)
        road_Nürnberg_Hamburg=random.randint(0,1)
        road_Nürnberg_München=random.randint(0,1)
        road_Nürnberg_Köln=random.randint(0,1)
        road_Nürnberg_Frankfurt=random.randint(0,1)
        road_Nürnberg_Stuttgart=random.randint(0,1)
        road_Nürnberg_Düsseldorf=random.randint(0,1)
        road_Nürnberg_Dortmund=random.randint(0,1)
        road_Nürnberg_Essen=random.randint(0,1)
        road_Nürnberg_Leipzig=random.randint(0,1)
        road_Nürnberg_Bremen=random.randint(0,1)
        road_Nürnberg_Dresden=random.randint(0,1)
        road_Nürnberg_Hannover=random.randint(0,1)
        road_Nürnberg_Nürnberg==1
        road_Nürnberg_Duisburg=random.randint(0,1)
        road_Nürnberg_Bochum=random.randint(0,1)
        road_Nürnberg_Wuppertal=random.randint(0,1)
        road_Nürnberg_Bielefeld=random.randint(0,1)
        road_Nürnberg_Bonn=random.randint(0,1)
        road_Nürnberg_Münster=random.randint(0,1)

        road_Duisburg_Berlin=random.randint(0,1)
        road_Duisburg_Hamburg=random.randint(0,1)
        road_Duisburg_München=random.randint(0,1)
        road_Duisburg_Köln=random.randint(0,1)
        road_Duisburg_Frankfurt=random.randint(0,1)
        road_Duisburg_Stuttgart=random.randint(0,1)
        road_Duisburg_Düsseldorf=random.randint(0,1)
        road_Duisburg_Dortmund=random.randint(0,1)
        road_Duisburg_Essen=random.randint(0,1)
        road_Duisburg_Leipzig=random.randint(0,1)
        road_Duisburg_Bremen=random.randint(0,1)
        road_Duisburg_Dresden=random.randint(0,1)
        road_Duisburg_Hannover=random.randint(0,1)
        road_Duisburg_Nürnberg=random.randint(0,1)
        road_Duisburg_Duisburg==1
        road_Duisburg_Bochum=random.randint(0,1)
        road_Duisburg_Wuppertal=random.randint(0,1)
        road_Duisburg_Bielefeld=random.randint(0,1)
        road_Duisburg_Bonn=random.randint(0,1)
        road_Duisburg_Münster=random.randint(0,1)

        road_Bochum_Berlin=random.randint(0,1)
        road_Bochum_Hamburg=random.randint(0,1)
        road_Bochum_München=random.randint(0,1)
        road_Bochum_Köln=random.randint(0,1)
        road_Bochum_Frankfurt=random.randint(0,1)
        road_Bochum_Stuttgart=random.randint(0,1)
        road_Bochum_Düsseldorf=random.randint(0,1)
        road_Bochum_Dortmund=random.randint(0,1)
        road_Bochum_Essen=random.randint(0,1)
        road_Bochum_Leipzig=random.randint(0,1)
        road_Bochum_Bremen=random.randint(0,1)
        road_Bochum_Dresden=random.randint(0,1)
        road_Bochum_Hannover=random.randint(0,1)
        road_Bochum_Nürnberg=random.randint(0,1)
        road_Bochum_Duisburg=random.randint(0,1)
        road_Bochum_Bochum==1
        road_Bochum_Wuppertal=random.randint(0,1)
        road_Bochum_Bielefeld=random.randint(0,1)
        road_Bochum_Bonn=random.randint(0,1)
        road_Bochum_Münster=random.randint(0,1)

        road_Wuppertal_Berlin=random.randint(0,1)
        road_Wuppertal_Hamburg=random.randint(0,1)
        road_Wuppertal_München=random.randint(0,1)
        road_Wuppertal_Köln=random.randint(0,1)
        road_Wuppertal_Frankfurt=random.randint(0,1)
        road_Wuppertal_Stuttgart=random.randint(0,1)
        road_Wuppertal_Düsseldorf=random.randint(0,1)
        road_Wuppertal_Dortmund=random.randint(0,1)
        road_Wuppertal_Essen=random.randint(0,1)
        road_Wuppertal_Leipzig=random.randint(0,1)
        road_Wuppertal_Bremen=random.randint(0,1)
        road_Wuppertal_Dresden=random.randint(0,1)
        road_Wuppertal_Hannover=random.randint(0,1)
        road_Wuppertal_Nürnberg=random.randint(0,1)
        road_Wuppertal_Duisburg=random.randint(0,1)
        road_Wuppertal_Bochum=random.randint(0,1)
        road_Wuppertal_Wuppertal==1
        road_Wuppertal_Bielefeld=random.randint(0,1)
        road_Wuppertal_Bonn=random.randint(0,1)
        road_Wuppertal_Münster=random.randint(0,1)

        road_Bielefeld_Berlin=random.randint(0,1)
        road_Bielefeld_Hamburg=random.randint(0,1)
        road_Bielefeld_München=random.randint(0,1)
        road_Bielefeld_Köln=random.randint(0,1)
        road_Bielefeld_Frankfurt=random.randint(0,1)
        road_Bielefeld_Stuttgart=random.randint(0,1)
        road_Bielefeld_Düsseldorf=random.randint(0,1)
        road_Bielefeld_Dortmund=random.randint(0,1)
        road_Bielefeld_Essen=random.randint(0,1)
        road_Bielefeld_Leipzig=random.randint(0,1)
        road_Bielefeld_Bremen=random.randint(0,1)
        road_Bielefeld_Dresden=random.randint(0,1)
        road_Bielefeld_Hannover=random.randint(0,1)
        road_Bielefeld_Nürnberg=random.randint(0,1)
        road_Bielefeld_Duisburg=random.randint(0,1)
        road_Bielefeld_Bochum=random.randint(0,1)
        road_Bielefeld_Wuppertal=random.randint(0,1)
        road_Bielefeld_Bielefeld==1
        road_Bielefeld_Bonn
        road_Bielefeld_Münster=random.randint(0,1)


        road_Bonn_Berlin=random.randint(0,1)
        road_Bonn_Hamburg=random.randint(0,1)
        road_Bonn_München=random.randint(0,1)
        road_Bonn_Köln=random.randint(0,1)
        road_Bonn_Frankfurt=random.randint(0,1)
        road_Bonn_Stuttgart=random.randint(0,1)
        road_Bonn_Düsseldorf=random.randint(0,1)
        road_Bonn_Dortmund=random.randint(0,1)
        road_Bonn_Essen=random.randint(0,1)
        road_Bonn_Leipzig=random.randint(0,1)
        road_Bonn_Bremen=random.randint(0,1)
        road_Bonn_Dresden=random.randint(0,1)
        road_Bonn_Hannover=random.randint(0,1)
        road_Bonn_Nürnberg=random.randint(0,1)
        road_Bonn_Duisburg=random.randint(0,1)
        road_Bonn_Bochum=random.randint(0,1)
        road_Bonn_Wuppertal=random.randint(0,1)
        road_Bonn_Bielefeld=random.randint(0,1)
        road_Bonn_Bonn==1
        road_Bonn_Münster=random.randint(0,1)

        road_Münster_Berlin=random.randint(0,1)
        road_Münster_Hamburg=random.randint(0,1)
        road_Münster_München=random.randint(0,1)
        road_Münster_Köln=random.randint(0,1)
        road_Münster_Frankfurt=random.randint(0,1)
        road_Münster_Stuttgart=random.randint(0,1)
        road_Münster_Düsseldorf=random.randint(0,1)
        road_Münster_Dortmund=random.randint(0,1)
        road_Münster_Essen=random.randint(0,1)
        road_Münster_Leipzig=random.randint(0,1)
        road_Münster_Bremen=random.randint(0,1)
        road_Münster_Dresden=random.randint(0,1)
        road_Münster_Hannover=random.randint(0,1)
        road_Münster_Nürnberg=random.randint(0,1)
        road_Münster_Duisburg=random.randint(0,1)
        road_Münster_Bochum=random.randint(0,1)
        road_Münster_Wuppertal=random.randint(0,1)
        road_Münster_Bielefeld=random.randint(0,1)
        road_Münster_Bonn=random.randint(0,1)
        road_Münster_Münster==1

 
return ((1, 1), (1, 1))
    
