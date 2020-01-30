####################
# Header
# Jan. 22 2020
# Shizhang Wang
# 0027521360
# this program finds greatest common divisor given two inputs in exercise 6.5 
# in thinkpython 2
"""
Created on Tue Jan 28 11:02:57 2020

@author: wang2846
"""

def gcd(a, b):
    # print for sanity check
    print('Original a and b are', str(a), str(b))
    r = a % b    # calculate the remainder
    print('The remainder is:', str(r))
    if r == 0:    # if remainder is 0, b is the greatest common divisor
        print('The GCD is:', str(b))
        return b
    else:
        # otherwise, call function gcd again until remainder become 0 
        # and find the GCD
        return gcd(b, r)
    
#print(gcd(16, 8))
#print(gcd(160, 27))