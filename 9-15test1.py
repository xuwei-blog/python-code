file = open('text1.txt','rt')
list1 = file.read().strip('\n').split(',')

print(list1)
file.close
