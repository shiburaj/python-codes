"""
Problem Statement:  WAP to read a files of marks and calculate percentage and assign ranks.
Author:             Prof. Shiburaj
INPUT: marks.csv

OUTPUT:
roll_number,name,physics,chem,maths,total,percentage,Rank
6,Rey,63,60,94,217,72.33,1
7,Khan,66,66,77,209,69.67,2
"""

f = open('marks.csv', 'r+t', encoding='utf-8')
header = f.readline()
output = []
for line in f:
    line = line[:-1]
    data = line.split(',')
    data[2] = int(data[2])
    data[3] = int(data[3])
    data[4] = int(data[4])
    data[5] = data[2]+data[3]+data[4]
    data[6] = round(data[5] / 3,2)
    output.append(data)
output.sort(key=lambda ele: ele[6], reverse=True)
strg = header
for record in range(1,len(output)+1):
    output[record-1][7] = record
    fields = list(map(str, output[record-1]))
    strg += ','.join(fields)
    strg += '\n'

print(strg)
f.close()