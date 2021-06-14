"""
Problem Statement:  WAP to make a Faculty class with properties name, department and subjects.
                     also add a method to return all the subjects taken by the faculty in a 
                    comma seperated format. Now create a new class Hod which should extend the Faculty class
                    and it should have a property experience and is_doctorate. both classes should have a 
                    profile method which would print all the properties of the class in a proper way
Author:             Prof. Shiburaj
INPUT1: 
Faculty
Shiburaj EXTC CCL MP CN

OUTPUT1:
** Profile **
Name : Shibu
Department : EXTC
Subjects: CCL,MP,CN 

INPUT2: 
Hod
Sameer ESC 12 True DCE RD

OUTPUT2:
** Profile **
Name : Sameer
Department : ESC
Subjects : DCE,RD
Experience : 12 years
Is Doctorate : Yes
"""
class Faculty:
    name = ''
    department = ''
    subjects = []

    def __init__(self, name, department, subjects):
        self.name = name
        self.department = department
        self.subjects = subjects

    def getSubjects(self):
        return ",".join(self.subjects)

    def profile(self):
        print(f"** Profile **")
        print(f"Name : {self.name}")
        print(f"Department : {self.department}")
        print(f"Subjects : {self.getSubjects()}")

class Hod(Faculty):
    experience = 0
    is_doctorate = False

    def __init__(self, name, department, experience, is_doc, subjects):
        self.experience = experience
        if is_doc == "True":
            self.is_doctorate = "Yes"
        else:
            self.is_doctorate = "No"
        super().__init__(name, department, subjects)

    def profile(self):
        super().profile()
        print(f"Experience : {self.experience} years")
        print(f"Is Doctorate : {self.is_doctorate}")


type = input() 
if(type == 'Faculty'):
    name, department, *subjects = input().split()
    f1 = Faculty(name, department, subjects)
    f1.profile()
elif type == 'Hod':
    name, department, exp, is_doc, *subjects = input().split()
    f1 = Hod(name, department, exp, is_doc, subjects)
    f1.profile()