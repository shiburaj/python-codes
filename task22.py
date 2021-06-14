"""
Problem Statement:  WAP to make a Building class which will have one number_of_floors 
                    property and make a constructor to initialize the value. Also make 
                    a method which will tell if the building is a tower 
                    ( more than 5 floors = tower). make another method which will print whether 
                    the building requires lift facility ( any building having morethan 7 floors 
                    should have lift facility).
Author:             Prof. Shiburaj
INPUT: 
6
OUTPUT:
Tower
No Lift Required

INPUT: 
12
OUTPUT:
Tower
Lift Required
"""
class Building:
    number_of_floors = 0

    def __init__(self, floors):
        self.number_of_floors = floors

    def is_tower(self):
        if self.number_of_floors > 5:
            print("Tower")
            return
        print("Not a Tower")

    def is_lift(self):
        if self.number_of_floors > 7:
            print("Lift Required")
            return
        print("No Lift Required")

floors = int(input())
b1 = Building(floors)
b1.is_tower()
b1.is_lift()