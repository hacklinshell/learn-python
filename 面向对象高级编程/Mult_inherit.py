#Python允许使用多重继承  采用MixIn就是一种常见的设计


class Animal(object):
    pass


#大类
class Manmal(Animal):
    pass


class Bird(Animal):
    pass


#功能
class RunnableMixIn(object):
    pass


class CarnivorousMixIn(object):
    pass


#MixIn 设计方式
class Dog(Manmal, RunnableMixIn, CarnivorousMixIn):
    pass
