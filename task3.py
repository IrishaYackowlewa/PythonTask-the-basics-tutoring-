#-*- coding: utf-8 -*- 
a = [[0 for n in range(5)] for nn in range(5)]
for i in range(5):
    for j in range(5):
        a[i][j] = int(input("Введите элемент массива и нажмите Enter: "))
print(a)
#for i in range(5):
#    a.append([int(j) for j in input().split()])
min = a[2][0]
for j in range(5):
    if a[2][j] < min:
        min = a[2][j]
print(min)