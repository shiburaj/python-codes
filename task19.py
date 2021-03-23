"""
Problem Statement:  Write the previous program using recursive function.
Author:             Prof. Shiburaj
SAMPLE INPUT:
12
EXPECTED SAMPLE OUTPUT:
1 2 3 5 7 11 
"""

def is_prime(n):
    for i in range(2,n):
        if(n%i == 0):
            return False
    return True

def make_prime_str(m,n):
    if(m>n):
        return ""
    
    if(is_prime(m)):
        return str(m)+" "+make_prime_str(m+1,n)
    else:
        return make_prime_str(m+1,n)


a = int(input())

print(make_prime_str(1,a))