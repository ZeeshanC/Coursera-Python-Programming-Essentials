#-*- coding: utf-8 -*-
#@Filename : Quiz1
#@Date : 2018-03-19-22-00
#@Poject: Coursera-Python-Programming-Essentials
#@AUTHOR : Antero Maripuu

#'Consider the Boolean expression not (p or not q). Give the four following values in order, separated only by spaces:
#the value of the expression when p is True, and q is True,
#the value of the expression when p is True, and q is False,
#the value of the expression when p is False, and q is True,
#the value of the expression when p is False, and q is False,
#Remember, each of the four results you provide should be True or False with the proper capitalization.

print(not(True or not True))
print(not(True or not False))
print(not(False or not True))
print(not(False or not False))