"""Module listing constants for the game 'Hotelmanagement'"""

__author__ = "6360278: Qasim Raza, 6290157: Lars Petersen"
__copyright__ = ""
__credits__ = "" 
__email__ = "qasimr@icloud.com, petersen@informatik.uni-frankfurt.de"

import os

def set():
    """Setting global constants"""
    
    global CLEAR 
    CLEAR = "cls" if os.name =="nt" else "clear"

    global MIN_NUM_TOWNS
    MIN_NUM_TOWNS = 5

    global MAX_NUM_TOWNS
    MAX_NUM_TOWNS = 20

    global MIN_NUM_MANAGERS_HOME
    MIN_NUM_MANAGERS_HOME = 5

    global MAX_NUM_MANAGERS_HOME
    MAX_NUM_MANAGERS_HOME = 20

    global MIN_PERIOD
    MIN_PERIOD = 5

    global MAX_PERIOD
    MAX_PERIOD = 40

    global MIN_PROFIT
    MIN_PROFIT = -20

    global MAX_PROFIT
    MAX_PROFIT = 90

    global COSTS_PASS
    COSTS_PASS = -20

    global DAYSHIFT_HIRE
    DAYSHIFT_HIRE = 3
        
