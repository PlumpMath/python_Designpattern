__author__ = 'LIUYuanYuan'
# -*- coding:utf-8 -*-


# 观察者模式定义了对象之间的一对多依赖，这样一来，当一个对象改变状态的时，它的所有依赖者都会
# 收到通知并自动更新

# 利用观察者模式，主题是具有状态的对象，并且可以控制这些状态。也就是说有一个具有状态的主题
# 观察者使用这些状态，虽然这些状态不属于他们，一个主题对多个观察者的关系

# 设计原则：为了交互对象之间的松耦合设计而努力

# 设计逻辑：1.所有的观察着有一个公共的接口，这样可观察者可以通过接口通知观察着
#         2.所有的观察着必须在可观察者中注册（观察者初始化时候注册），这样主题才能通知到每一个观察着


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
        for i in self.observers:
            i.update(self.temp, self.humidity, self.pressure)

    def measurementsChanged(self):
        self.notify_observer()

    def setMeasurements(self, temp, humidity, pressure ):
        self.temp = temp
        self.humidity = humidity
        self.pressure = pressure
        self.measurementsChanged()

class CurrentConditionsDisplay(Observer, DisplayElement):
    def __init__(self, weatherdata):
        self.weatherData = weatherdata
        weatherdata.register_observer(self)

    def update(self, temp, humidity, pressure):
        self.temp = temp
        self.humidity = humidity
        self.pressure = pressure
        self.display()

    def display(self):
        print("current conditions:{} F degrees and {} humidity".format(self.temp, self.humidity))


if __name__ == '__main__':
    weatherdata = WeatherData()
    currentcondition = CurrentConditionsDisplay(weatherdata)

    weatherdata.setMeasurements(80, 65, 27.5)