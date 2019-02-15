#在不改变原有功能代码的基础上,添加额外的功能,如用户验证等，称之为“装饰器”（Decorator）。


# wraps  装饰器中用

import functools

def log(func):        #log，是一个decorator，所以接受一个函数作为参数，并返回一个函数
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log                        #相当于执行了 now = log(now)  由于log()是一个decorator，返回一个函数，所以，原来的now()函数仍然存在，只是现在同名的now变量指向了新的函数，于是调用now()将执行新函数，即在log()函数中返回的wrapper()函数。
def now():
    print('2019-2-15')

 #调用now()函数，不仅会运行now()函数本身，还会在运行now()函数前打印一行日志：
now()      

#call now():
#2019-2-15


#   decorator本身需要传入参数       自定义log的文本：
def logger(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@logger('DEBUG')
def today():
    print('2019-2-15')

today()
print(today.__name__)