import json

d = dict(name='bob', age=20, score=80)

json.dumps(d)  #dumps 返回一个str，内容就是标准的JSON。

#'{"name": "bob", "age": 20, "score": 80}'


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def __str__(self):
        return 'Student object (%s, %s, %s)' % (self.name, self.age, self.score)

s = Student('Bob',12,50)
std_data = json.dumps(s,default= lambda obj:obj.__dict__)

print('Dump student:',std_data)         #Dump student: {"name": "Bob", "age": 12, "score": 50}


rebuild = json.loads(std_data, object_hook=lambda d: Student(d['name'], d['age'], d['score']))
print(rebuild)      #Student object (Bob, 12, 50)

