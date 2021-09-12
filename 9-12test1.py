n = 2
def mul(x,y):
    global n
    n = x* y
    return n
s = mul(99,2)
print(s)
print(n)    # global申明之后 可以变量内容可以被覆盖
