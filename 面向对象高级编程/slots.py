#Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性：

#__slots__
class Student(object):
    __slots__ = ('name','age')

class GraduateStudent(Student):
    pass

s = Student()

s.name = 'Struggle'
s.age = 12

#AttributeError: 'Student' object has no attribute 'score'
try:
    s.score = 99
except AttributeError as e:
    print('AttributeError:',e)


g = GraduateStudent()
g.score = 99
print('g.score =', g.score)