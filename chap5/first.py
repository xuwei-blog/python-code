print('helloworld')
#可以输出数字
print(520)
print('helloworld')


#可以print表达式
print(3+1)

#读写的方式打开文件夹，无文件就会创建      必须要有指定盘符； file=fp 必须有     ；
fp = open('E:/text.txt','a+')   #  a+ 追加内容
print('helloworld',file=fp)
fp.close()

print('hello','world')            #在一行输出


