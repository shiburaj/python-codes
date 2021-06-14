"""
Problem Statement:  WAP to make a calculator with validation of the inputs with 
                    the help of try and except block. Operations to be performed
                    addition(+), subtraction(-), division(/), multiplication(*), square root(~).
                    Validation of inputs:- 
                    ValueError (Enter numbers only), 
                    ZeroDivisionError (Denominator cannot be Zero) 
                    if invalid operator (Invalid Operator)
                    any other error show (There is some error)
                    Use class for Calculator.
Author:             Prof. Shiburaj
INPUT1: 
+
4
5

OUTPUT1:
4 + 5 = 9

INPUT2: 
/
4
0

OUTPUT2:
Error : Denominator cannot be Zero
"""
import math

class Calculator:
    num1 = 0
    num2 = 0

    def __init__(self, opr):
        self.num1 = float(input())
        if opr != '~':
            self.num2 = float(input())

    def add(self):
        print(f"{self.num1} + {self.num2} = {self.num1+self.num2}")

    def sub(self):
        print(f"{self.num1} - {self.num2} = {self.num1-self.num2}")

    def div(self):
        print(f"{self.num1} / {self.num2} = {self.num1/self.num2}")
        
    def mul(self):
        print(f"{self.num1} * {self.num2} = {self.num1*self.num2}")
        
    def sqrt(self):
        print(f"sqrt({self.num1}) = {math.sqrt(self.num1)}")

try:
    opr = input()
    cal = Calculator(opr)
    if(opr == '+'):
        cal.add()
    elif opr == '-':
        cal.sub()
    elif opr == '/':
        cal.div()
    elif opr == '*':
        cal.mul()
    elif opr == '~':
        cal.sqrt()
    else:
        print("Error : Invalid Operator")
except ValueError:
    print("Error : Enter numbers only")
except ZeroDivisionError:
    print("Error : Denominator cannot be Zero")
except:
    print("Error : There is some error")