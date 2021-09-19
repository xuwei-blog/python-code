import time as t

print(t.time())   # 当前时间的时间戳
print()
print(t.gmtime(1000))    # 时间戳起始时间
print()
print(t.gmtime(t.time()))  # 当前时间
print()
print(t.ctime())     #  可读的时间
print()
print(t.localtime())   #当前时间
