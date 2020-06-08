s = input()
arr_words = s.split()
arr = []
for i in range (2, len(arr_words) + 1 ,2): #прибавляем 1 так как иначе не захватывает 2 последних слова строки с четной длиной, так как строка заканчивается и он завершает цикл и не делает еще один повтор, который нужен
    arr.append(arr_words[i-2])
    arr.append(arr_words[i-1])
    arr.append("мир")

if len(arr_words) % 2 == 0:#проверяем четная была длина или нет
    print((' ').join(arr))
else:
    arr.append(arr_words[len(arr_words)-1])#если нет то добавляем последнее слово
    print((' ').join(arr))
