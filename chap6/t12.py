list1 = [{'1':'a','2':'b','3':['c','cc']},{'1':'aa','2':'bb','3':['cc','cc']},{'1':'aaa','2':'bbb','3':['ccc','ccc']}]
#uname = input("请输入名字：")
for item in list1:  #遍历列表   item是字典

    actor_list1 = item['3'] #演员的列表
    for actor in actor_list1:
        print(actor)

