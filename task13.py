"""
Problem Statement:  WAP to find the factorial of the entered number.
Author:             Prof. Shiburaj

SAMPLE INPUT:
3

EXPECTED OUTPUT:
6
"""

a = int(input())

fct = a
while a>1:
    a -= 1
    fct = fct * a
    
print(fct)