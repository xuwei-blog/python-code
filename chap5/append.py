list = [10,20,30,40,50]
list2 = [66]
list.append(100)
list.extend(list2)
print(list)
list.clear()
print(list)
del list
print(list)