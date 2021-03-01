"""
Problem Statement:  WAP to take space separated input from user and 
                    print the output in list, tuple and dict.
Author:             Prof. Shiburaj

INPUT:
1 2

OUTPUT:
['1', '2']
('1', '2')
{0: '1', 1: '2'}
"""

s = input().split()
print(s)
print(tuple(s))
print(set(sorted(s)))
print(dict(s))
