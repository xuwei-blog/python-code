answer = input('请问你是会员吗？  y/n')
money = float(input('请输入您的购物金额：'))

if answer == 'y':
    if money>=200:
        print('您的购物金额为：',money*0.8)
    elif money>=100:
        print('您的购物金额为：',money*0.9)
    else:
        print('不打折')
else:
    if money >=200:
        print('您的购物金额为：',money*0.95)
    else:
        print('不打折')



