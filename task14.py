"""
Problem Statement:  WAP to find the second largest number.
Author:             Prof. Shiburaj

INPUT:
2 3 4 2 1 5 6 4 7 8

OUTPUT:
7
"""

a = sorted(list(set(map(int,input().split()))))
print(a[-2])