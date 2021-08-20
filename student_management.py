import os
import re
filename = 'student.txt'
def main():
    while True:
        menu()
        choice = int(input('请选择'))
        if choice in [0, 1, 2, 3, 4, 5, 6, 7]:
            if choice == 0:
                answer = input('您确定要退出吗？y/n')
                if answer == 'y' or answer == 'Y':
                    print('谢谢您的使用')
                    break
                else:
                    continue
            elif choice == 1:
                insert()
            elif choice == 2:
                search()
            elif choice == 3:
                delete()
            elif choice == 4:
                modify()
            elif choice == 5:
                sort()
            elif choice == 6:
                total()
            elif choice == 7:
                show()
def menu():
    print('-------------------学生信息管理系统---------------------------')
    print('-----------------------功能菜单--------------------------')
    print('            1.录入学生信息')
    print('            2.查找学生信息')
    print('            3.删除学生信息')
    print('            4.修改学生信息')
    print('            5.排序')
    print('            6.统计学生总人数')
    print('            7.显示所有学生信息')
    print('            0.退出')
    print('------------------------------------------------------------')

def insert():
    student_list = []  # 存储学生信息
    while True:
        id = int(input('请输入ID:'))
        if not id:  # 空字符串布尔值为False （ex手贱打了空格，就重新输入）
            break
        name = input('请输入姓名:')
        if not name:
            break

        try:   # 异常处理
            english = int(input('请输入english成绩:'))
            java = int(input('请输入java成绩:'))
            python = int(input('请输入python成绩:'))
        except:
            print('输入无效，不是整数类型，请重新输入')
            continue
        student = {'id': id, 'name': name, 'english': english, 'java': java, 'python': python}
        student_list.append(student)  # 添加到列表中
        answer = input('是否继续添加y/n\n')  # 斜线n：换行
        if answer == 'y' or answer == 'Y':
            continue
        else:
            break
    # 调用save函数
    save(student_list)
    print('信息录入完毕')


def save(list1):
    try:
        stu_txt = open(filename, 'a', encoding='utf-8')  # 追加模式

    except:
        stu_txt = open(filename, 'w', encoding='utf-8')  # 只写
    for item in list1:
        stu_txt.write(str(item)+'\n')
    stu_txt.close()

def search():
    student_query = []
    while True:
        id = ''
        name = ''
        if os.path.exists(filename):
            mode = input('按ID查找按1，按姓名查找按2')
            if mode == '1':
                id = input('请输入学生ID:')
            elif mode == '2':
                name = input('请输入学生姓名:')
            else:
                print('您输入有误，请重新输入')
                search()
            with open(filename, 'r', encoding='utf-8') as rfile:
                student = rfile.readlines()
                for item in student:
                    d = dict(eval(item))
                    if id != '':
                        if d['id'] == int(id):
                            student_query.append(d)
                    elif name != '':
                        if d['name'] == name:
                            student_query.append(d)
            show_student(student_query)
            student_query.clear()  # 清空列表
            answer = input('是否继续查询y/n')
            if answer == 'y':
                continue
            else:
                break

        else:
            print('没有学生信息')
            return
def show_student(list1):
    if len(list1) == 0:
        print('没查到，无数据显示！')
        return
    # 定义标题显示格式
    format_title = '{:^6}\t{:^12}\t{:^10}\t{:^10}\t{:^10}\t{:^8}'
    print(format_title.format('id', '姓名', 'english成绩', 'python成绩', 'java成绩', '总成绩'))
    # 定义内容的显示格式
    format_data = '{:^6}\t{:^12}\t{:^10}\t{:^12}\t{:^12}\t{:^12}'
    for item in list1:
        print(format_data.format(item.get('id'),
                                 item.get('name'),
                                 item.get('english'),
                                 item.get('python'),
                                 item.get('java'),
                                 int(item.get('english'))+int(item.get('python'))+int(item.get('java'))
                                 ))

def delete():
    while True:
        student_id = input('请输入要删除学生的id：')
        if student_id != '':   # 有student_id输入就执行  空字符串不执行
            if os.path.exists(filename):  # 判断文件是否存在
                with open(filename, 'r', encoding='utf-8') as file:  # 上下文管理器
                    student_old = file.readlines()   # 读取数据放到列表里
            else:
                student_old = []  # 文件不存在 就定义空列表
            flag = False  # 标记是否删除 默认没有删除
            if student_old:    # 判断列表空不空  有内容就执行
                with open(filename, 'w', encoding='utf-8') as write:  # 只写的方式打开
                    d = {}
                    for item in student_old:
                        d = dict(eval(item))  # 将字符串转换成字典  eval代码
                        if d['id'] != int(student_id):  # 字典中的id 和 要删除的学生的id不相符的话
                            write.write(str(d)+'\n')  # 把d写进去  换行
                        else:
                            flag = True  # 表示已经删除
                    if flag:
                        print(f'id为{student_id}的学生信息已被删除')   # 格式化字符串
                    else:
                        print(f'没有找到ID为{student_id}的学生信息')
            else:
                print('无学生信息')
                break

            show()  # 删除之后要重新显示所有学生信息
            answer = input('是否继续删除y/n')
            if answer == 'y' or answer == 'Y':
                continue
            else:
                break

def modify():
    show()
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as read:
            student_old = read.readlines()
    else:
        return
    student_id = input('请输入要修改学员的ID：')
    with open(filename, 'w', encoding='utf-8') as write:
        for item in student_old:
            d = dict(eval(item))
            if d['id'] == int(student_id):
                print('找到学生信息，可以修改了')
                while True:
                    try:
                        d['name'] = int(input('请输入姓名：'))
                        d['english'] = int(input('请输入english：'))
                        d['python'] = int(input('请输入python：'))
                        d['java'] = int(input('请输入java：'))
                    except:
                        print('您输入的有误，请重新输入')
                    else:
                        break
                write.write(str(d)+'\n')
                print('修改成功')
            else:
                print('没找到')
                write.write(str(d)+'\n')
        answer = input('是否继续修改y/n')
        if answer == 'y':
            modify()

def sort():
    show()
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            student_list1 = rfile.readlines()
        student_new = []
        for item in student_list1:
            d = dict(eval(item))
            student_new.append(d)
    else:
        return
    asc_or_desc = input('0.升序；1.降序')
    if asc_or_desc == '0':
        asc_or_desc_bool = False
    elif asc_or_desc == '1':
        asc_or_desc_bool = True
    else:
        print('输入有误，请重新输入')
        sort()
    mode = input('请选择，0.总分排序，1.english成绩排序，2.python成绩排序，3.java成绩排序')
    if mode == '1':
        student_new.sort(key=lambda x: int(x['english']), reverse=asc_or_desc_bool)
    elif mode == '2':
        student_new.sort(key=lambda x: int(x['python']), reverse=asc_or_desc_bool)
    elif mode == '3':
        student_new.sort(key=lambda x: int(x['java']), reverse=asc_or_desc_bool)
    elif mode == '0':
        student_new.sort(key=lambda x: int(x['english'])+int(x['java'])+int(x['python']), reverse=asc_or_desc_bool)
    else:
        print('输入有误')
        sort()
    show_student(student_new)

def total():
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            students = rfile.readlines()
            if students:
                print(f'一共有{len(students)}名学生')
            else:
                print('还没有录入信息')



    else:
        print('暂未保存信息')
def show():
    student_list = []
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:

            students = rfile.readlines()
            for item in students:
                student_list.append(dict(eval(item)))
            if student_list:
                show_student(student_list)
    else:
        print('没有信息')




if __name__ == '__main__':
    main()