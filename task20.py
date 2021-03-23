import calculator

opr, *x = input().split()

x = list(map(int, x))

if(opr == 'add'):
    print(calculator.add(x))
elif(opr == 'sub'):
    print(calculator.sub(x[0],x[1]))
elif(opr == 'div'):
    print(calculator.div(x[0],x[1]))
elif(opr == 'mul'):
    print(calculator.mul(x))
else:
    print("Invalid Operation")