a = 3.1415926
print(a,type(a))

a = 1.1
b = 2.2
print(a+b)

#计算机存储以二进制的形式  所以浮点数相加有误差

from decimal import Decimal
print(Decimal('1.1')+Decimal('2.2'))

