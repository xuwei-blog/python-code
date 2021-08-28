'''
for i in range(3):
    pwd=input('请输入密码：')  #不能用int   because后续密码是字符串
    if pwd =='8888':
        print('密码正确')
        break
    else:
        print('密码错误')
'''

a=0
while a<3:
    pwd = input('请输入密码：')  # 不能用int   because后续密码是字符串
    if pwd == '8888':
        print('密码正确')
        break
    else:
        print('密码错误')
    a=a+1