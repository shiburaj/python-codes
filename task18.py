"""
Problem Statement:  WAP to find all the prime numbers from 1 to the given number.
Author:             Prof. Shiburaj
SAMPLE INPUT:
12
EXPECTED SAMPLE OUTPUT:
1 2 3 5 7 11 
"""

def is_prime(n):
    for i in range(2,n):
        if(n%i == 0):
            return False
    return True

a = int(input())

for x in range(1,a+1):
    if(is_prime(x)):
        print(x, end=" ")