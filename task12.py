"""
Problem Statement:  WAP to read the marks obtained by the student in the format 
                    given below. each subject is out of 80 marks. so calculate 
                    the total marks obtained and the percentage (2 decimal places). 
                    Also find the class of the student.(>=70 then Distinction, >=60 
                    then First Class, >=50 then Second Class, >=40 then Pass Class and 
                    less than 40 the Fail ) (Note: Individual subject passing need 
                    not be checked)
Author:             Prof. Shiburaj

SAMPLE INPUT:
56 78 67 79 75 76

EXPECTED OUTPUT:
Total : 246 / 320
Percentage : 76.88
Class : Distinction
"""

marks = list(map(int,input().split()))
total = sum(marks)
out_off = len(marks)*80
percent = (total/out_off)*100
print(f"Total : {total} / {out_off}")
print(f"Percentage : {percent:.2f}")

if percent >= 70:
    print("Class : Distinction")
elif percent >= 60:
    print("Class : First Class")
elif percent >= 50:
    print("Class : Second Class")
elif percent >= 40:
    print("Class : Pass Class")
else:
    print("Class : Fail")