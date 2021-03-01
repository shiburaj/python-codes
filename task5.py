"""
Problem Statement:  WAP to read name from user with firstname and lastname 
                    seperated by space and print the upper case name of the 
                    same followed by number of characters in the names
Author:             Prof. Shiburaj

INPUT:
will smith

OUTPUT:
WILL SMITH (9)
"""

first_name, last_name = input().split(' ')
print(f'{first_name.upper()} {last_name.upper()} ({len(first_name)+len(last_name)})')
