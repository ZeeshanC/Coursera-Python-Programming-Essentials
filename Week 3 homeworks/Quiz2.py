#-*- coding: utf-8 -*-
#@Filename : Test_question 1
#@Date : 2018-03-19-14-04
#@Poject: Coursera-Python-Programming-Essentials
#@AUTHOR : Antero Maripuu

#In Python, conditional statements may be nested. Consider the following function that takes two Boolean values as input
#and returns a Boolean value.

def nand(bool1, bool2):
    """
    Take two Boolean values bool1 and bool2
    and return the specified Boolean values
    """

    if bool1: # Always checks TRUE value first (e.g if FALSE skips the inner loop)
        if bool2:
            return False
        else:
            return True
    else:
        return True