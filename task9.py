#-*- coding: utf-8 -*- 
s = 'Луна, меняющая яркость от пепельной до ослепительной, дала жизнь легенде о возрождающейся птице Феникс'

arr_str = []
arr_word1 = []
arr_word2 = []

n = s.find("Феникс")
need_word = s[n:]

arr_str.append(need_word)

m = s.find('о')
if m != -1:
    arr_word1.append(s[m])
else:
    arr_word1.append('*')

m = s.find('з')
if m != -1:
    arr_word1.append(s[m])
else:
    arr_word1.append('*')

m = s.find('н')
if m != -1:
    arr_word1.append(s[m])
else:
    arr_word1.append('*')

m = s.find('а')
if m != -1:
    arr_word1.append(s[m])
else:
    arr_word1.append('*')

m = s.find('ч')
if m != -1:
    arr_word1.append(s[m])
else:
    arr_word1.append('*')

m = s.find('а')
if m != -1:
    arr_word1.append(s[m])
else:
    arr_word1.append('*')

m = s.find('е')
if m != -1:
    arr_word1.append(s[m])
else:
    arr_word1.append('*')

m = s.find('т')
if m != -1:
    arr_word1.append(s[m])
else:
    arr_word1.append('*')

arr_str.append(("").join(arr_word1))

m = s.find('п')
if m != -1:
    arr_word2.append(s[m])
else:
    arr_word2.append('*')
m = s.find('о')
if m != -1:
    arr_word2.append(s[m])
else:
    arr_word2.append('*')
m = s.find('с')
if m != -1:
    arr_word2.append(s[m])
else:
    arr_word2.append('*')
m = s.find('т')
if m != -1:
    arr_word2.append(s[m])
else:
    arr_word2.append('*')
m = s.find('о')
if m != -1:
    arr_word2.append(s[m])
else:
    arr_word2.append('*')
m = s.find('я')
if m != -1:
    arr_word2.append(s[m])
else:
    arr_word2.append('*')
m = s.find('н')
if m != -1:
    arr_word2.append(s[m])
else:
    arr_word2.append('*')
m = s.find('с')
if m != -1:
    arr_word2.append(s[m])
else:
    arr_word2.append('*')
m = s.find('т')
if m != -1:
    arr_word2.append(s[m])
else:
    arr_word2.append('*')
m = s.find('в')
if m != -1:
    arr_word2.append(s[m])
else:
    arr_word2.append('*')
m = s.find('о')
if m != -1:
    arr_word2.append(s[m])
else:
    arr_word2.append('*')

arr_str.append(("").join(arr_word2))

print((" ").join(arr_str))