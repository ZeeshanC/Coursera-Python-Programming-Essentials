#-*- coding: utf-8 -*-
#@Filename : Homework 2
#@Date : 2018-03-13-20-47
#@Poject: Python Programming Essentials 2018
#@AUTHOR : Antero Maripuu

#Implement the mathematical function f(x)=−5x5+67x2−47 as a Python function. Then use Python to compute the function
#values f(0), f(1), f(2), and f(3). Enter the maximum (largest) of these four values calculated below.

#A common error for this question is to fail to read the directions above carefully and submit your answer in the
#incorrect form. As a coder, always remember to note exactly what answers your code (and quiz questions) should produce.

def homework_2(x):
    result=(-5*(x**5))+(67*(x**2))-47
    return result

print(homework_2(0))
print(homework_2(1))
print(homework_2(2))
print(homework_2(3))