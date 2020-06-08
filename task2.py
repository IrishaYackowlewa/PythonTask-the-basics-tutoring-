#-*- coding: utf-8 -*- 
a = []
for i in range(4):
    a.append([int(j) for j in input().split()])
max= a[0][3]
for i in range(4):
    if a[i][3] > max:
        max = a[i][3]
print(max)