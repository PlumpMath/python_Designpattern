__author__ = 'LIUYuanYuan'


# -*- coding:utf-8 -*-

# 模式特点：增加一个修饰类包裹原来的类，装饰过的对象可替代原始对象
# 原则：类应该对扩展开放，对修改关闭


class Beverage(object):
#     description = 'Unknown Beverage'
#
    def get_description(self):
        return self.description

    def cost(self):
        pass
#
# class CondimentDecorator(object):
#     def get_description(self):
#         pass



class CondimentDecorator(Beverage):
    def get_description(self):
        pass



class MilkyTea(Beverage):
    def __init__(self):
        self.description = "MilkyTea"

    def cost(self):
        return 1.99


class FruitJuice(Beverage):
    def __init__(self):
        self.description = "FruitJuice"

    def cost(self):
        return 1.80


class Coffee(Beverage):
    def __init__(self):
        self.description = "Coffee"

    def cost(self):
        return 2.00



class Pearl(object):

    def __init__(self, beverage):
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description()

    def cost(self):
        return 1.50 + self.beverage.cost()



class Pudding(object):

    def __init__(self, beverage):
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description()

    def cost(self):
        return 1.60 + self.beverage.cost()


class Milk(object):

    def __init__(self, beverage):
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description()

    def cost(self):
        return 2.10 + self.beverage.cost()


if __name__ == '__main__':

    b = FruitJuice()
    print('%s = $%s' % (b.get_description(), b.cost()))

    # b = FruitJuice()
    # print('%s = $%s' %(b.get_description(), b.cost()) )


    b = MilkyTea()
    b = Pearl(b)
    b = Pudding(b)
    print('%s = $%s' % (b.get_description(), b.cost()))

    b = Coffee()
    b = Pearl(b)
    b = Pudding(b)
    print('%s = $%s' % (b.get_description(), b.cost()))

    b = Coffee()
    b = Pearl(b)
    b = Milk(b)
    print('%s = $%s' % (b.get_description(), b.cost()))
