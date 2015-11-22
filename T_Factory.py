__author__ = '沅源'
# -*- coding:utf-8 -*-


#工厂模式特点就是顶一个创建对象的接口，让子类决定实例化哪一个类。这使得一个类的实例化过程延迟到其子类中
#模式的目的：将可能涉及到很多类的对象创建过程封装带一个单独的方法中。通过给定的上下文输出指定的对象类型

#什么时候使用：使用工厂模式的最佳时机就是需要使用到单个实体的多个变体时，比如，你有一个按钮类，这个按钮类有
#很多变体，例如图片按钮，输入框按钮或者是flash按钮等，那么在不同的场合你会需要不同的按钮，这时候就可以通过
#一个工厂来创建不同的按钮

class Button(object):
    html = ''
    def get_html(self):
        return self.html

class Image(Button):
    html = '<img alt='' />'

class Input(Button):
    html = '<input type="text" />'

class Flash(Button):
    html = ""

class ButtonFactory():
    def create_button(self, typ):
        targetclass = typ.capitalize()
        print(targetclass)
        return globals()[targetclass]()

#globals()将以字典的方式返回所有的全局变量，因此targetclass = type.captitalize()将通过
#传入的type字符串得到类名（Image, Input, Flash），而global()[targetclass]将通过类名取到类的类，
#而globals()[targetclass]()将创建此类的对象

button_obj = ButtonFactory()
button = ['image', 'input', 'flash']
for b in button:
    print(button_obj.create_button(b).get_html())