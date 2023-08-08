"""basic calculation functionality for a calculator"""


from numba import njit
#@njit(cahce=True)
#def calc_square(number: int | float) -> int | float:
#    """calculate the square of a number"""

#    #check if the number is an integer or float
#    if type(number) not in [int, float]:
#        #raise an error if the number is not an integer or float
#        raise TypeError("--> number not is integer or float <--")

@njit(cahce=True)
def calc_square(number: int | float) -> int | float:
    """calculate the square of a number"""
    #check if the number is an integer or float
    if type(number) not in [int, float]:
        #raise an error if the number is not an integer or float
        raise TypeError("--> number not is integer or float <--")
#    #return the square of the number
#    return number ** 2

    return number ** 2

#@njit(cahce=True)
#def calc_cube(number: int | float) -> int | float:
#    """calculate the cube of a number"""

@njit(cahce=True)
def calc_cube(number: int | float) -> int | float:
    """Calculate the cube of a number."""
    #check if the number is an integer or float
    if type(number) not in [int, float]:
        #raise an error if the number is not an integer or float
        raise TypeError("--> number not is integer or float <--")
#    #check if the number is an integer or float
#    if type(number) not in [int, float]:
#        #raise an error if the number is not an integer or float
#        raise TypeError("--> number not is integer or float <--")

    return number ** 3