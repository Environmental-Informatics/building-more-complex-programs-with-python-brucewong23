####################
# Header
# Jan. 22 2020
# Shizhang Wang
# 0027521360
# this program tests and compares the square root estimation provided by textbook
# and the actual function and print out a table of calculated values and difference
# in exercise 7.1 in thinkpython 2
"""
Created on Thu Jan 30 13:11:29 2020

@author: wang2846
"""
# import libraries needed
import math
import pandas as pd

# epsilon provided by textbook, should explain the difference from my output
# to the table in the textbook
epsilon = 10**-7 
# function in textbook, give a value (a) and estimate of square root (x)
# the function should find a close enough value to the actual square root
def mysqrt(a, x):
    while True:
        y = (x+a/x)/2
        if abs(y-x)< epsilon:
            break
        x = y
    return x

def test_square_root(x):  # prompt to ask for an estimate value(x)
    a = list(range(1, 10)) # a values suggested by textbook
    # create empty lists to store calculated value
    mysqrt_value = list()
    sqrt_value = list()
    diff = list()
    # call function, calculated and append value to list
    for i in a:
        mysqrt_value.append(mysqrt(i, x))
        sqrt_value.append(math.sqrt(i))
        diff.append(abs(mysqrt(i, x) - math.sqrt(i)))
    # create dictionary for dataframe conversion and easy printing
    d = {'a': a, 'mysqrt(a)': mysqrt_value, 'math.sqrt(a)': sqrt_value, 
         'diff': diff}
    # had to specify order since spyder didn't print out the same order as pycharm
    df = pd.DataFrame(d, columns=['a', 'mysqrt(a)', 'math.sqrt(a)', 'diff'])
    return df

#print(test_square_root(2))
    