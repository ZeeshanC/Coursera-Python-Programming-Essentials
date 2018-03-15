#-*- coding: utf-8 -*-
#@Filename : Exeecise 1
#@Date : 2018-03-15-19-30
#@Poject: Coursera-Python-Programming-Essentials
#@AUTHOR : Antero Maripuu

#Write a Python function is_even that takes as input the parameter number (an integer) and returns True if number is
#even and False if number is odd. Hint: Apply the remainder operator to n (i.e., number % 2) and compare to zero.

def is_even(x):
    if x%2==0:
        return True
    else:
        return False

inp=int(input("Enter an integral "))
print(is_even(inp))

