__author__ = '沅源'
# -*- coding:utf-8 -*-

class FlyBehavior(object):
    def fly(self):
        pass

class FlyWithWing(FlyBehavior):
    def fly(self):
        print('i am flying with wings')

class FlyNoWing(FlyBehavior):
    def fly(self):
        print("i can't fly")

class QuackBehavior(object):
    def quack(self):
        pass


class Quack(QuackBehavior):
    def quack(self):
        print('Quack')


class Squeak(QuackBehavior):
    def quack(self):
        print('Squeak')


class MuteQuack(QuackBehavior):
    def quack(self):
        print('MuteQuack')


class Duck(object):
    def __init__(self, flyParam, quackParam):
        self.flyBehavior = flyParam
        self.quackBehavior = quackParam
    def performFly(self):
        self.flyBehavior.fly()
    def performQuack(self):
        self.quackBehavior.quack()
    def swim(self):
        print('All ducks can swim..')
    def display(self):
        pass


class RedDuck(Duck):
    def __init__(self, flyParam=FlyWithWing(), quackParam=MuteQuack()):
        super(RedDuck,self).__init__(flyParam,quackParam)
    def display(self):
        print('I am a red duck')

class RubberDuck(Duck):
    def __init__(self, flyParam=FlyNoWing(), quackParam=Quack()):
        super(RubberDuck,self).__init__(flyParam,quackParam)
    def display(self):
        print('I am a rubber duck!')


duck = RedDuck()
duck.display()
duck.performFly()
duck.performQuack()

duck = RubberDuck()
duck.display()
duck.performFly()
duck.performQuack()