


#       https://www.cnblogs.com/feeland/p/4419121.html    继承和多态


class Animal(object):
    def run(self):
        print('Animal run')


class Dog(Animal):
    def run(self):
        print('Dog run')


class Cat(Animal):
    def run(self):
        print('Cat run')


def run_twice(animal):
    animal.run
    animal.run


a = Animal()
d = Dog()
c = Cat()

print('a is Animal?', isinstance(a, Animal))
print('a is Dog?', isinstance(a, Dog))
print('a is Cat?', isinstance(a, Cat))

print('d is Animal?', isinstance(d, Animal))
print('d is Dog?', isinstance(d, Dog))
print('d is Cat?', isinstance(d, Cat))

run_twice(c)
#a is Animal? True
#a is Dog? False
#a is Cat? False
#d is Animal? True
#d is Dog? True
#d is Cat? False


#若父类构造函数包含很多属性，子类仅需新增1、2个，会有不少冗余的代码
class Person(object):
    def __init__(self,name,sex):
        self.name = name
        self.sex = sex

class Child(Person):                          # Child 继承 Person
    def __init__(self,name,sex,mother,father):
        Person.__init__(self,name,sex)        # 子类对父类的构造方法的调用
        self.mother = mother
        self.father = father

May = Child("May","female","April","June")
print(May.name,May.sex,May.mother,May.father)       #May female April June