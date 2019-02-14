#函数除了正常定义的必选参数外，还可以使用默认参数、可变参数和关键字参数，


#x2
def power1(x):
    return x * x


#x3 x4 x5
def power2(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


power2(5, 2)  #25

#默认参数   n是默认参数


def power3(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


power3(5)  #25
power3(5, 2)  #25

#可变参数


# a2 + b2 +c2
def calc(*numbers):
    sum = 0
    for num in numbers:
        sum = sum + num * num
    return sum


#calc 可以传入任意个参数
calc(1, 2, 3, 4)  #30
calc(1, 2)  #5
calc()  # 0

#传入一个list或tuple  在list或tuple前面加一个*号,把list或tuple的元素变成可变参数传进去
nums = [1, 2, 3, 4]
calc(*nums)  #30

#关键字参数
#可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。


#函数person除了必选参数name和age外，还接受关键字参数kw。在调用该函数时，可以只传入必选参数：
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


person('colin', 90)  #name: colin age: 90 other: {}

#也可以传入任意个数的关键字参数
person(
    'Bob', 35, city='Beijing')  #name: Bob age: 35 other: {'city': 'Beijing'}

person(
    'Adam', 45, gender='M', job='Engineer'
)  #name: Adam age: 45 other: {'gender': 'M', 'job': 'Engineer'}

#先组装出一个dict,把该dict转换为关键字参数传进去
extra = {'city': 'Beijing', 'job': 'Engineer'}
person(
    'Jack', 24,
    **extra)  #name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}

#命名关键字参数
#限制关键字参数的名字       和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。


def person1(name, age, *, city, job):
    print(name, age, city, job)


person1('Jack', 24, city='Beijing', job='Engineer')  #Jack 24 Beijing Engineer

#如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：


def person2(name, age, *args, city, job):
    print(name, age, args, city, job)


def print_scores(**kw):
    print('      Name    Score')
    print('------------------')
    for name, score in kw.items():
        print('%10s      %d' % (name, score))
    print()


stu = {'Ame': 20, 'Pbe': 30, 'ESE': 90}
print_scores(**stu)

#
#      Name    Score
#------------------
#       Ame      20
#       Pbe      30
#       ESE      90


def print_info(name, *, gender, city='Beijing', age):
    print('Personal Info')
    print('---------------')
    print('   Name: %s' % name)
    print(' Gender: %s' % gender)
    print('   City: %s' % city)
    print('    Age: %s' % age)
    print()


print_info('Bob', gender='male', age=20)

#Personal Info
#---------------
#   Name: Bob
# Gender: male
#   City: Beijing
#    Age: 20

print_info('Lisa', gender='female', city='Shanghai', age=18)

#Personal Info
#---------------
#   Name: Lisa
# Gender: female
#   City: Shanghai
#    Age: 18