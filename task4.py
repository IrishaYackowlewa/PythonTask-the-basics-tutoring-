#-*- coding: utf-8 -*- 
j=0
str = input("Введите строку: ")
for i in range(len(str)):
    if str[i] == ' ': j = j+1
    if j == 4: 
        str = str[:i] + "и т.д."
        break
print(str)
 