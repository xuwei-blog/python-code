#100到999的水仙花数

sum = 0
for i in range(100,1000):
    a = i//100
    b = i//10%10
    c = i%10   #个位
   # print(str(a)+str(b)+str(c))

    if i == a**3 + b**3 + c**3:
        print(i)
