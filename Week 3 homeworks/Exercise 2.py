#-*- coding: utf-8 -*-
#@Filename : Exercise 2
#@Date : 2018-03-15-19-40
#@Poject: Coursera-Python-Programming-Essentials
#@AUTHOR : Antero Maripuu

#Write a Python function is_cool that takes as input the string name and returns True if name is either "Joe", "John" or
#"Stephen" and returns False otherwise. (Let's see if Scott manages to catch this. ☺ )

inp=str(input("Please enter a name: "))

def is_cool(name):
    if name == 'Joe' or name == 'John' or name == 'Stephen':
        return True
    else:
        return False

print(is_cool(inp))