"""
Problem Statement:  WAP to check if the entered year is a leap year or not.
Author:             Prof. Shiburaj


How to determine if a year is a leap year? 
You should follow the following steps to determine whether a year is a leap year or not.
If a year is evenly divisible by 4 means having no remainder then go to next step. If it is not divisible by 4. It is not a leap year. For example: 1997 is not a leap year. 
If a year is divisible by 4, but not by 100. For example: 2012, it is a leap year. 
If a year is divisible by both 4 and 100, go to next step. If a year is divisible by 100, but not by 400. For example: 1900, then it is not a leap year. If a year is divisible by both, then it is a leap year. So 2000 is a leap year.

SAMPLE INPUT1:
2000

EXPECTED OUTPUT1:
2000 is a Leap Year

SAMPLE INPUT2:
1999

EXPECTED OUTPUT2:
1999 is not a Leap Year
"""

year = int(input())

if year % 4 == 0:
    if year % 100 != 0:
        print(f"{year} is a Leap Year")
    else:
        if year % 400 == 0:
            print(f"{year} is a Leap Year")
        else:
            print(f"{year} is not a Leap Year")        
else:
    print(f"{year} is not a Leap Year")