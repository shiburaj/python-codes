"""
Problem Statement:  WAP to make a calculator
Author:             Prof. Shiburaj

INPUT:
add 5 5 5

OUTPUT:
15
"""
def add(x):
    return sum(x)

def mul(x):
    prod = 1
    for i in x:
        prod *= i
    return prod

def sub(x):
    return x[0] - x[1]

def div(x):
    return x[0] / x[1]


opr, *x = input().split()
x = list(map(int, x))
if opr == 'add':
    print(add(x))
elif opr == 'mul':
    print(mul(x))
elif opr == 'sub':
    print(sub(x))
elif opr == 'div':
    print(div(x))
else:
    print("Invalid Operation")