#一个函数在内部调用自身本身，这个函数就是递归函数。


# 利用递归函数计算阶乘
#  n! = 1 x 2 x 3 x ... x n
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


fact(5)  #120


# 利用递归函数移动汉诺塔:   https://www.cnblogs.com/forever-snow/p/8316218.html    https://www.cnblogs.com/haidaojiege/p/7764012.html
def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
    else:
        move(n - 1, a, c, b)
        move(1, a, b, c)
        move(n - 1, b, a, c)


move(3, 'A', 'B', 'C')
#   move A --> C
#   move A --> B
#   move C --> B
#   move A --> C
#   move B --> A
#   move B --> C
#   move A --> C