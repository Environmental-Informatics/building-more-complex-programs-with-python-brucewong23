####################
# Header
# Jan. 22 2020
# Shizhang Wang
# 0027521360
# this program checks Fermat's last theorem in exercise 5.2 in thinkpython 2
"""
Created on Wed Jan 22 14:28:19 2020

@author: wang2846
"""
### prompt to ask for user input after providing basic information
def user_input():
    print('Enter a, b, c, n to check the Fermat\'s Last Theorem : a^n + b^n = c^n:\n')
    a = int(input('a: '))    # ask for indivdual input and convert to integer
    b = int(input('b: '))
    c = int(input('c: '))
    n = int(input('n: '))
    check_fermat(a, b, c, n)    # call to check the theorem
    
def check_fermat(a, b, c, n):
    # calculate the difference between the left and right side of the Theorem
    difference = a**n+b**n-c**n
    # need to satisfy both conditon, n = 1 or 2 is valid for some case, i.e. 
    # (1, 2, 3, 1) or (3, 4, 5, 2)
    if n > 2 and difference == 0:
        print('Holy Smokes, Fermat was wrong!')
    else:
        print('No, that doesn\'t work.')
    
user_input()