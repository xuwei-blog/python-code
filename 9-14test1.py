txt = input('请输入一段英文文本:')   #  输入文本出现的次数
txt = txt.lower()
counts = {}

list1 = [chr(i) for i in range(97,123)]

for i in txt:
    if i in list1:
        counts[i]=counts.get(i,0)+1    # 原来没有这个字母就默认值0+1=1
                                       # 第二次出现 之前的累加次数+1  
       
items = list(counts.items())
# 以元组的形式输出


items.sort(key=lambda x:x[1],reverse = True)

for i in range(len(items)):
    word,count = items[i]
    print(word,count)


