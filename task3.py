"""
Problem Statement:  WAP to read two numbers from user in single line and print the result of operations in the given sequence.
Author:             Prof. Shiburaj

INPUT:
10 3

OUTPUT:
10 + 3 = 13
10 - 3 = 7
10 * 3 = 30
10 / 3 = 3.3333333333333335
10 ** 3 = 1000
10 % 3 = 1
"""

a, b = list(map(int, input().split(' ')))
print(f"{a} + {b} = {a+b}")
print(f"{a} - {b} = {a-b}")
print(f"{a} * {b} = {a*b}")
print(f"{a} / {b} = {a/b}")
print(f"{a} ** {b} = {a**b}")
print(f"{a} % {b} = {a%b}")
