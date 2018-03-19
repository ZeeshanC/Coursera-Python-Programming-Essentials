#-*- coding: utf-8 -*-
#@Filename : Exercise 3
#@Date : 2018-03-15-20-00
#@Poject: Coursera-Python-Programming-Essentials
#@AUTHOR : Antero Maripuu

#Write a Python function is_lunchtime that takes as input the parameters hour (an integer in the range [1,12]) and is_am
#(a Boolean “flag” that represents whether the hour is before noon). The function should return True when the input
#corresponds to 11am or 12pm (noon) and False otherwise. If the problem specification is unclear, look at the test cases
#in the provided template. Our solution does not use conditional statements.

inp=int(input("Please enter an integer in the range [1,12] "))
inp2=int(input("Please enter AM or PM: "))


def is_lunchtime(time, am_pm):
