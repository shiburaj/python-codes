"""
Problem Statement:  WAP to make a Vehicle class which will have following 
                    properties make, brand, mileage and make a constructor 
                    to initialize these values. Also make a method which 
                    will calculate the kilometer covered for a given fuel. 
Author:             Prof. Shiburaj
INPUT: 
Santro LXi, Maruti, 20Km/L
10L

OUTPUT:
200Km
"""
class Vehicle:
    make = ''
    brand = ''
    mileage = 0

    def __init__(self, make, brand, mileage):
        self.make = make
        self.brand = brand
        if(mileage.endswith('Km/L')):
            self.mileage = int(mileage[:-4])
        else:
            self.mileage = int(mileage)

    def calDistance(self, fuel):
        if(fuel.endswith('L')):
            fuel = int(fuel[:-1])
        else:
            fuel = int(fuel)
        return self.mileage * fuel

make, brand, mileage = input().split(", ")
v1 = Vehicle(make, brand, mileage)
fuel = input()
distance = v1.calDistance(fuel)
print(f"{distance}Km")
