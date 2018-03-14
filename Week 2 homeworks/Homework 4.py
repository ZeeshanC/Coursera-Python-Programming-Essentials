#-*- coding: utf-8 -*-
#@Filename : Homework 4
#@Date : 2018-03-13-21-40
#@Poject: Python Programming Essentials
#@AUTHOR : Antero Maripuu

#For this final question, your task is to find the formula for a simple geometric problem using Google and then implement
#that formula in Python. While you may think that it is silly that we don't ' \

#Write a Python function that computes the area of an equilateral triangle given the length of one of its sides.
#Search for a mathematical formula that specifies this relation and translate that formula into Python. Hint:

#As a test, your area function should return an area of 1.73205080757 for an equilateral triangle with sides of length
#2. Now, use this function to compute the area of equilateral triangle with sides of length 5. Enter this area as a number
#(and not the units) with at least four digits of precision after the decimal point.

import math

value=int(input("Please give the length of an equilateral triangle side: "))

def equilateral_triangle(x):
    result = ((math.sqrt(3))/4)*(x**2)
    return result
print("Are of equilateral triangle is ", equilateral_triangle(value))