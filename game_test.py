"""..."""

__author__ = "6360278: Qasim Raza, 6290157: Lars Petersen"
__copyright__ = ""
__credits__ = "" 
__email__ = "qasimr@icloud.com, petersen@informatik.uni-frankfurt.de"


def get_towns():
    """returns n-tuple, elements pairewise different strings of length > 0"""

    return ("town1", "town2")
    

def get_managers(towns):
    """returns a 2-tuple (hometown, m) where m = # managers"""

    return ("town1", 5)    


def get_timeframe():
    """returns d"""

    return 5
    

def get_potentials(towns):
    """returns n-tuple with values p_i"""

    return (-20, 90)


def get_network(towns):
    """retruns n-tuple of n-tuples with values s_ij"""

    return ((1, 1), (1, 1))


def get_name():
    """returns user naem"""
    
    name = input("Ihr Name: ")
    return name

