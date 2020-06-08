s = set(input().lower())
s1 = set(input().lower())
vow = set("уеыаоэяию")
print(*sorted(s1  & s & vow), sep = '')