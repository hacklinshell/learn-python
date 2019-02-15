#dict 字典

d = {'Michel': 95, 'bob': 75, 'meo': 20}
d['bob']  #75

#可以直接把数据放入dict
d['meo'] = 96
d['meo']  #96

#如果key不存在 就报错

#用in 判断  或者get方法

'struggle' in d  #False

d.get('struggle')  #  返回None  也可以指定返回值
d.get('struggle', -1)  # -1

#删除一个key用pop(key)

d.pop('bob')
d  #{'Michel': 95, 'meo': 96}

#请务必注意，dict内部存放的顺序和key放入的顺序是没有关系的。

#和list比较，dict有以下几个特点：

#1.查找和插入的速度极快，不会随着key的增加而变慢；
#2.需要占用大量的内存，内存浪费多。

#而list相反：

#1.查找和插入的时间随着元素的增加而增加；
#2.占用空间小，浪费内存很少。

#所以，dict是用空间来换取时间的一种方法。   dict的key必须是不可变对象。

#set  set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key

s = set([1, 2, 3])
s  #{1, 2, 3}

#重复元素在set中自动被过滤：
s = set([1, 1, 2, 2, 3, 3, 4])
s  #{1, 2, 3, 4}

#通过add(key)方法可以添加元素到set中

s.add(5)
s  #{1, 2, 3, 4, 5}

#通过remove(key)方法可以删除元素：

s.remove(2)
s  #{1, 3, 4, 5}

#set和dict的唯一区别仅在于没有存储对应的value，但是，set的原理和dict一样，所以，同样不可以放入可变对象，因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”

#再议不可变对象
#str是不变对象，而list是可变对象。


#对list进行操作，list内部的内容是会变化的，
a = ['b','v','a','f']
a.sort()
print(a)  #['a', 'b', 'f', 'v']


#对str进行操作.replace确实变出了'sbc'，但是变量a还是'abc'   replace方法创建了一个新字符串'sbc'并返回 a 变量本身的内容没变
a = 'abc'
a.replace('a','s')  #'sbc'
a       #'abc'