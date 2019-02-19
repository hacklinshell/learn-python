#定制类


#__str__
class Student(object):
    def __init__(self, name):
        self.__name = name

    def __str__(self):  #使用__srt__() 方法 返回一个定制的字符串
        return 'Student object (name: %s)' % self.__name

    __repr__ = __str__  #__repr__()  显示调用是调用的__repr__()    __str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串


print(Student('Michel'))  #Student object (name: Michel)

#__iter__()  返回一个迭代对象，可以用for ... in 循环


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100:
            raise StopIteration()
        return self.a


for x in Fib():
    print(x)

#1
#1
#2
#3
#5
#8
#13
#21
#34
#55
#89

#__getitem__()  获取下标操作


class Fib1(object):
    def __getitem__(self,n):
        if isinstance(n,int):   #  n是个索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a

        if isinstance(n,slice): # n是个切片
            start = n.start
            stop = n.stop
            
            if start is None:
                start = 0
            
            a,b = 1,1
            L = []
            for x in range(stop):
                if x > start:
                    L.append(a)
                a,b = b,a + b
            return L

f=Fib1()
f[4]    #5
f[5]    #8
f[0:5]  #f[0:5]


#__getattr__() 


class Studen1(object):
    def __init__(self):
        self.name = 'bob'
    def __getattr__(self,attr):
        if attr == 'score':
            return 99
        if attr == 'age':
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)

s = Studen1()

print(s.name)   #bob
print(s.score)  #99
print(s.age()) # 25
print(s.grade) #AttributeError: 'Student' object has no attribute 'grade'

##__call__  直接对实例进行调用
class Studen2(object):
    def __init__(self,name):
        self.name = name

    def __call__(self):
        print('Studuen2 name is %s' % self.name)
    

s = Studen2('boa')
s()     #Studuen2 name is boa


