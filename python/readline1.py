import os
S = open('myfile.txt','r')
print(S)
i=0
while True:
    i=i+1
    line=S.readline()
    if not line:
        break
    m1=int(line.split(","))[0]
    m2=int(line.split(","))[1]
    m3=int(line.split(","))[2]
    print(f"marks of student {i} maths is:{m1}")
    print(f"marks of student {i} maths is:{m2}")
    print(f"marks of student {i} maths is:{m3}")
    print(line)