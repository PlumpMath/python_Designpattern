__author__ = '沅源'
# -*- coding:utf-8 -*-

#单例模式 http://blog.csdn.net/ghostfromheaven/article/details/7671853


#方法1，实现__new__方法  实现逻辑：将一个类的实例绑定到类变量_instance上，如果cls._instance为None说明此类还没有实例化，如果cls._instance
#为None，直接返回cls._instance

#super关键字的详细研究 http://blog.csdn.net/johnsonguo/article/details/585193

# class A:
#     def __init__(self):
#         print('Enter A')
#         print('Leave A')
#
# class B(A):
#     def __init__(self):
#         print('Enter B')
#         A.__init__(self)
#         print('Leave B')
#
# class C(A):
#     def __init__(self):
#         print('Enter C')
#         A.__init__(self)
#         print('Leave C')
#
# class D(A):
#     def __init__(self):
#         print('Enter D')
#         A.__init__(self)
#         print('Leave D')
#
# class E(B, C, D):
#     def __init__(self):
#         print("Enter E")
#         B.__init__(self)
#         C.__init__(self)
#         D.__init__(self)
#         print("Leave E")

# class A:
#     def __init__(self):
#         print('Enter A')
#         print('Leave A')
#
# class B(A):
#     def __init__(self):
#         print('Enter B')
#         super(B, self).__init__()
#         print('Leave B')
#
# class C(A):
#     def __init__(self):
#         print('Enter C')
#         super(C, self).__init__()
#         print('Leave C')
#
# class D(A):
#     def __init__(self):
#         print('Enter D')
#         super(D, self).__init__()
#         print('Leave D')
#
# class E(B, C, D):
#     def __init__(self):
#         print("Enter E")
#         super(E, self).__init__()
#         print("Leave E")
#
# E()

#类变量 _instance
# class Singleton(object):
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(cls, '_instance'):
#             orig = super(Singleton, cls)
#             cls._instance = orig.__new__(cls, *args, **kwargs)
#         return cls._instance

#共享属性，所谓单例就是所有引用拥有相同的状态和行为
#同一个类的所有实例天然拥有相同的行为
# class Borg(object):
#     _state = {}
#     def __new__(cls, *args, **kwargs):
#         ob = super(Borg, cls).__new__(cls, *args, **kwargs)
#         ob.__dict__ = cls._state
#         return ob


# 使用元类的方法
# 关于元类的知识 http://blog.jobbole.com/21351/
# 深入理解元类 http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000 /0014319106919344c4ef8b1e04c48778bb45796e0335839000
class Singleton2(type):

    def __init__(cls, name, bases, dict):
        print('init')
        super(Singleton2, cls).__init__(name, bases,dict)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        print('call')
        if cls._instance is None:
            cls._instance = super(Singleton2, cls).__call__(*args, **kwargs)
        return cls._instance

class Myclass3(object, metaclass= Singleton2):
    pass



# 使用装饰器


def singleton(cls, *args, **kwargs):

    instances = {}

    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return _singleton


@singleton
class my_class4(object):
    a = 1

    def __init__(self, x=0):
        self.x = x

one = my_class4()
two = my_class4()


