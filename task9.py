"""
Problem Statement:  WAP to change users profile fields stored in a dictionary. 
                    input will be given in a single line where the first word will
                    be the field name and second will be field value. print the dictionary 
                    in the given format. (Width : 40 chars per line of output)
Author:             Prof. Shiburaj

SAMPLE INPUT:
password student123

EXPECTED SAMPLE OUTPUT:
** Update Profile **
Name:                               Amit
Age:                                  33
Email:             amit@eng.rizvi.edu.in
Password:                        *******
"""

students = {"name":"Amit","age":33,"email":"amit@eng.rizvi.edu.in","password":"temp123" }
key, value = input().split()
students[key] = value

print("** Update Profile **")
print("Name: {0:>34}".format(students['name']))
print("Age: {0:>35}".format(students['age']))
print("Email: {0:>33}".format(students['email']))
print("Password: {0:>30}".format("*"*len(students['password'])))