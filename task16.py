"""
Problem Statement:  Write a program to make a function to find b^2 - 4ac value for different a,b and c values
Author:             Prof. Shiburaj

INPUT:
4 4 1

OUTPUT:

"""

def formula(a, b, c):
    return b*b - 4*a*c

a, b, c = list(map(int, input().split()))
print(f"Result of {b}^2 - 4*{a}*{c} = {formula(a, b, c)}")