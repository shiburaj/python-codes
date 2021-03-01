"""
Problem Statement:  WAP to find the sum and average of a list of number 
                    entered by the user. Average should be approximated 
                    to 1 decimal places only.
Author:             Prof. Shiburaj

INPUT:
1 2 3 4 5 6

OUTPUT:
Sum = 21
Average = 3.5
"""

l = list(map(int,input().split(" ")))
r = sum(l)
print(f"Sum = {r}")
print("Average = {0:.1f}".format(r/len(l)))