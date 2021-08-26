class Car(object):
    def __init__(self,type,no):
        self.type=type
        self.no=no
    def start(self):
        pass
    def stop(self):
        pass

class Taxi(Car):
    def __init__(self,type,no,company):
        super().__init__(type,no)
        self.company=company
    def start(self):
        print('乘客您好！')
        print(f'我是{self.company}出租车公司的，车牌是{self.no},请问您去哪')
    def stop(self):
        print('目的的到了，请您付款下车，欢迎再次乘坐')

class FamilyCar(Car):
    def __init__(self,type,no,name):
        super().__init__(type,no)
        self.name=name
    def start(self):
        print(f'我是{self.name}，我的汽车我做主')
    def stop(self):
        print('目的地到了，我们去玩吧')


if __name__ == '__main__':
    taxi = Taxi('上海大众','金A88888','长城')
    taxi.start()
    taxi.stop()
    print('-'*30)
    familyCar=FamilyCar('广汽丰田','金B888888','武大郎')
    familyCar.start()
    familyCar.stop()
