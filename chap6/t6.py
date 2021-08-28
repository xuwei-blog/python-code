

s = '天涯共此时'


print(s.encode(encoding='GBK'))
f = b'\xec\xcc'
print(f.decode(encoding='GBK'))