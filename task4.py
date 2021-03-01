"""
Problem Statement:  WAP to read Temperature and print Celsius. output is rounded to 1 decimal place.
Author:             Prof. Shiburaj

INPUT:
45

OUTPUT:
45 Fahrenheit = 7.2 Celsius
"""

f = int(input())
print(f'{f} Fahrenheit = {(f-32)*5/9:.1f} Celsius')
