#让内部属性不被外部访问，可以把属性的名称前加上两个下划线__  实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问


class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

    def set_name(self, name):
        self.__name = name

    def set_score(self, score):
        self.__score = score


bart = Student('Bart Simpson', 59)
print('bart.get_name() =', bart.get_name())
bart.set_score(60)
print('bart.get_score() =', bart.get_score())

#bart.get_name() = Bart Simpson
#bart.get_score() = 60