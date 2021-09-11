s1 = 'bag'
s2 = 'ont'
d = {}
for c in (65,97):
    for i in range(26):
        d[chr(i+c)] = chr((i+13)%26+c)

print(''.join(d.get(c) for c in s1 ))
print(''.join(d.get(c) for c in s2 ))
