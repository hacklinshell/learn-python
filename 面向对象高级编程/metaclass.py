#动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的。

#type()函数允许我们动态创建出类来，

#  metaclass是创建类，所以必须从`type`类型派生
def fn(self, name='world'): # 先定义函数
    print('Hello, %s.' % name)

Hello = type('Hello', (object,), dict(hello=fn)) # 创建Hello class  

h = Hello()
print('call h.hello():')
h.hello()
print('type(Hello) =', type(Hello))
print('type(h) =', type(h))


class ListMetaclas(type):
    def __new__(
            cls, name, bases, attrs
    ):  #__new__()方法接收到的参数依次是： cls 当前准备创建的类的对象； name 类的名字；bases  类继承的父类集合； attrs 类的方法集合
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


# 指示使用ListMetaclass来定制类


class Myclass(list, metaclass=ListMetaclas):        #指示使用ListMetaclass来定制类，传入关键字参数metaclass
    pass

L = Myclass()

L.add(1)
L.add(2)
L.add(3)
L.add('END')
print(L)        #[1, 2, 3, 'END']
