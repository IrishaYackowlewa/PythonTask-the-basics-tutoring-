s = input().split()
d = {}
for i in range(len(s)):
    d[s[i]] = len(s[i])
print(*sorted(d,key=len))

s = set(input().split())
print(*sorted(d,key=len))