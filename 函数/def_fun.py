def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(-20))  #20


#空函数,用pass做占位符
def nop():
    pass


#数据类型检查用内置函数isinstance()实现


def my_abs_isin(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand tpye')
    if x >= 0:
        return x
    else:
        return -x


print(my_abs_isin('s'))  #参数错误会抛出错误
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
# File "<stdin>", line 3, in my_abs_isin
#TypeError: bad operand tpye

#返回多个值
#在游戏中经常需要从一个点移动到另一个点，给出坐标、位移和角度，就可以计算出新的新的坐标：

import math


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


x, y = move(100, 100, 60, math.pi / 6)
r = move(100, 100, 60, math.pi / 6)

print(x, y)  #151.96152422706632 70.0

print(r)        #(151.96152422706632, 70.0)   返回的是个元组   