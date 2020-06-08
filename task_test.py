a = []
for i in range(4):
    a.append([int(j) for j in input().split()])
result = []
for i in range(4):
    count = 0
    for j in range(4):
        if a[i][j]%4 == 0 and a[i][j] != 0:
            count = count +1
    result.append(count)
print(*result) 
