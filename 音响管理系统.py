# 1.增
def add_item():
    user_item = input('请输入item：')
    user_price = input('请输入price：')
    user_size = input('请输入size：')
    new_item = {'name':user_item,'price':user_price,'size':user_size}
    item_list.append(new_item)



# 2.删
def remove_item():
    name = input('请输入你要删除的音响name：')
    exist = False
    for item in item_list:
        if item['name'] ==name:
            exist= True
            item_list.remove(item)
        print('删除成功')
    if exist==False:
        print('未找到该设备')


# 3.改
def modify_item():
    name = input('请输入你要修改的音响name：')
    for item in item_list:
        exist = False
        if item['name'] ==name:
            exist = True
            name = input('请输入你要修改的音响name：')
            price = input('请输入你要修改的音响price：')
            size = input('请输入你要修改的音响size：')
            item['name']=name
            item['price']=price
            item['size']=size

    if exist:
        print('修改成功')
    else:
        print('未找到name')
# 4.查
def search_item():
    name = input('请输入你要查询的音响name：')
    exist= False
    for item in item_list:
        if item['name']==name:
            print('查询成功',item)
    if exist == False:
        print('查询失败，设备不存在')

# 5.展示

def show_all():
    for item in item_list:
        print(item)

item = {'name':'item1','price':'100','size':'big'}
item_list = [item]



def run():
    while True:
        print('欢迎来到音响系统')
        print('1.增加一台音响')
        print('2.删除一台音响')
        print('3.修改一台音响')
        print('4.查找一台音响')
        print('5.展示所有音响')
        user_choice = input('请输入功能序号:')
        if user_choice =='1':
            add_item()
        elif user_choice =='2':
            remove_item()
        elif user_choice =='3':
            modify_item()
        elif user_choice =='4':
            search_item()
        elif user_choice =='5':
            show_all()
        else:
            print('sorry,inputerror')

run()