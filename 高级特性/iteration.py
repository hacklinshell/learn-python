#给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration

#dict迭代：  dict迭代的是key
d = {'a': 1, 'b': 2, 'c': 3}

for k in d:
    print(k)

#迭代value
for value in d.values():
    print(value)

#同时迭代key和value
for k, v in d.items():
    print('%s == %d' % (k, v))
#   a == 1
#   b == 2
#   c == 3

#使用for循环时，只要作用于一个可迭代对象，for循环就可以正常运行
#判断一个对象是可迭代对象

#from collections import Iterable  错误  版本问题

from collections.abc import Iterable

isinstance('abc', Iterable)  # str是否可迭代  #True
isinstance([1, 2, 3], Iterable)  # list是否可迭代
isinstance(123, Iterable)  # 整数是否可迭代

#下标循环       enumerate函数可以把一个list变成索引-元素对

for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

#   0 A
#   1 B
#   2 C    

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x,y)
#   1 1
#   2 4
#   3 9