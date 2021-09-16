value = input("请输入第一个元素：>")
num = 1
list1 = []
list1.append(value)
while value != '':
    num+=1
    value = input("请再次输入元素，返回空结束：>")
    list1.append(value)


for i in range(len(list1)):
    if ',' == list1[i]:
        list1[i] = list1[i].replace(',','.')

file = open('a.csv','w',encoding='utf-8')
file.write(','.join(list1)+'\n')
file.seek(0)
file.close
print('csv 保存完成')


file2 = open('a.csv','r+',encoding='utf-8')

data = file2.read().strip('\n').split(',')
for i in range(len(data)):
    if '.' == data[i]:
        data[i] = data[i].replace('.',',')
print(data)
file2.close
        
