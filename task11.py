n = int(input())
s_city = set()
for i in range(n):
    s_city.add(input())
new_city = input()
if new_city not in s_city:
    print("Ok")
else:
    print("TRY ANOTHER")