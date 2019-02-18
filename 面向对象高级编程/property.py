#用装饰器函数把 get/set 方法“装饰”成属性调用：


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score

    @property
    def score(self):
        return self.__score

    @score.setter                       #setter 是property的装饰后的副产品
    def score(self, score):
        if score < 0 or score > 100:
            raise ValueError('invaild score')
        self.__score = score


s = Student('coa', 90)
s.score = 80
print(s.score)
