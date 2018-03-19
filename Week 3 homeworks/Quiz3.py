# -*- coding: utf-8 -*-
# @Filename : Test_question 2
# @Date : 2018-03-19-14-07
# @Poject: Coursera-Python-Programming-Essentials
# @AUTHOR : Antero Maripuu

# The Collatz conjecture is an example of a simple computational process whose behavior is so unpredictable
# that the world's best mathematicians still don't understand it.

# Consider the simple function f(n) (as defined in the Wikipedia page above) that takes an integer n and divides it by
# two if n is even and multiplies n by 3 and then adds one to the result if n is odd. The conjecture involves studying
# the value of expressions of the form f(f(f(...f(f(n))))) as the number of calls to the function f increases.
# The conjecture is that, for any non-negative integer n, repeated application of f to n yields a sequence of integers
# that always includes 1.

# Your task for this question is to implement the Collatz function f in Python. The key to your implementation is to
# build a test that determines whether n is even or odd by checking whether the remainder when n is divided by 2 is
# either zero or one. Hint: You can compute this remainder in Python using the remainder opertor % via the expression
# n % 2. Note you will also need to use integer division // when computing f.

# Once you have implemented f, test the your implementation on the expression f(f(f(f(f(f(f(674))))))). This
# expression should evaluate to 190. Finally, compute the value of the expression f(f(f(f(f(f(f(f(f(f(f(f(f(f(1071))))))))))))))
# andenter the result below as an integer. Remember to use copy and paste when moving the expressions above into
# your Python environment. Never try to retype expressions by hand.


inp = int(input("Please give a positive number: "))
inp2 = int(input("How many iterations you would like to calculate: "))
while (inp < 0 or inp2 < 0):
    inp = int(input("Please give a positive number: "))


def collatz(numb, iter):
      iterations=0
      while (numb != 1): #Always checks True  value first
              if iterations == iter:
                  break
              elif (numb % 2 == 0):
                  numb /= 2
                  print(str(iterations + 1) + ") " + str(numb))
                  iterations += 1
              else:
                  numb = (numb * 3) + 1
                  print(str(iterations + 1) + ") " + str(numb))
                  iterations += 1

print(collatz(inp,inp2))
