__author__ = 'LIUYuanYuan'
# -*- coding:utf-8 -*-


# 观察者模式定义了对象之间的一对多依赖，这样一来，当一个对象改变状态的时，它的所有依赖者都会
# 收到通知并自动更新

# 利用观察者模式，主题是具有状态的对象，并且可以控制这些状态。也就是说有一个具有状态的主题
# 观察者使用这些状态，虽然这些状态不属于他们，一个主题对多个观察者的关系

# 设计原则：为了交互对象之间的松耦合设计而努力


class Subject(object):
    def register_observer(self,o):
        pass

    def remove_observer(self,o):
        pass

    def notify_observer(self):
        pass


class Observer(object):
    def update(self, temp, humidity, pressure):
        pass


class DisplayElement(object):
    def display(self):
        pass


class WeatherData(Subject):

    def __init__(self):
        self.observers = []

    def register_observer(self,o):
        self.observers.append(o)

    def remove_observer(self,o):
        var = self.observers.index(o)
        if(var >= 0):
            self.observers.pop(var)
    def notify_observer(self):
        for i in self.observers