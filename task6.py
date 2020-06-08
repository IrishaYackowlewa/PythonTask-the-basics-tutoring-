def S(a,b):
    sp = 0.5*a*b
    return int(sp)

n = int(input('Введите количество прямоугольников: '))
a = []
for i in range(n):
    a.append([int(j) for j in input("Введите ширину и высоту через пробел: ").split()])

for i in range(n):
    print(S(a[i][0],a[i][1]))  

