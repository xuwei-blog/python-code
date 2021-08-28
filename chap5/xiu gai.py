'''list = [10,20,30,40,50,66,214,34,5]
list.sort()
print(list)
list.sort(reverse=False)
print(list)
list.sort(reverse=True)
print(list)



items = ['Fruits','books','Others']
prices = [96,  78,85]
d = {   item.upper():price    for item,price in zip(items,prices)   }
print(d)


p = (10,[20,30],9)
print(p)
print(type(p))
print(p[0],type(p[0]))
print(p[1])
print(p[2])
'''

s = {1,2,3}
s.update((4,3,7))
s.update(('python'))
print(s)