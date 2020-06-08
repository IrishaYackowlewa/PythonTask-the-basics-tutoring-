#-*- coding: utf-8 -*- 
j=0
str = input("Введите строку: ")
masstr = str.split()
for i in range(len(masstr)):
    if masstr[i].find('Б')!= -1 or masstr[i].find('б')!= -1: j = j+1
print(j)