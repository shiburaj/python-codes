"""
Problem Statement:  WAP to print following pattern.
Author:             Prof. Shiburaj

INPUT:
5

OUTPUT:
    *
   **
  ***
 ****
*****
"""

n = int(input())

for i in range(1,n+1):
    print(f"{'*'*i:>{n}}")