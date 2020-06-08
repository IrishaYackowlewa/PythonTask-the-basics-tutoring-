a = [[0 for n in range(5)] for nn in range(5)]
print(a)
for i in range(5):
    for j in range(5):
        a[i][j] = int(input("Введите элемент массива и нажмите Enter: "))
print(a)

