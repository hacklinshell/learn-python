#__init__方法的第一个参数永远是self  创建的实例本身  各种属性绑定到self，因为self就指向创建的实例本身


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name,self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else: 
            return 'C'


bart = Student('Bart Simpson', 59)
print(bart.name, ":", bart.score)  #Bart Simpson : 59

bart.print_score()  #Bart Simpson: 59
print(bart.get_grade()) # C