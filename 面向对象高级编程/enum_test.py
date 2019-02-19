from enum import Enum
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug',
                       'Sep', 'Oct', 'Nov', 'Dec'))

#for name, member in Month.__members__.items():
#    print(name, '=>', member, ',', member.value)        #value属性则是自动赋给成员的int常量，默认从1开始计数。



#Jan => Month.Jan , 1
#Feb => Month.Feb , 2
#Mar => Month.Mar , 3
#Apr => Month.Apr , 4
#May => Month.May , 5
#Jun => Month.Jun , 6
#Jul => Month.Jul , 7
#Aug => Month.Aug , 8
#Sep => Month.Sep , 9
#Oct => Month.Oct , 10
#Nov => Month.Nov , 11
#Dec => Month.Dec , 12


from enum import Enum, unique

@unique     #@unique装饰器可以帮助我们检查保证没有重复值。
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


day1 = Weekday.Mon
print(day1) #Weekday.Mon
print(Weekday.Tue)  #Weekday.Tue
print('Weekday[\'Tue\'] =', Weekday['Tue']) #Weekday['Tue'] = Weekday.Tue
print(Weekday(1))   #Weekday.Mon
print('day1 == Weekday.Tue ?', day1 == Weekday.Tue) #print('day1 == Weekday.Tue ?', day1 == Weekday.Tue)