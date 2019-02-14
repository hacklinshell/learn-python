#生成器 generator

#通过列表生成式，我们可以直接创建一个列表，列表容量肯定是有限的，占用很大的存储空间 。在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：

#把一个列表生成式的[]改成()，就创建了一个generator：

L = [x * x for x in range(10)]
L  #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

g = (x * x for x in range(10))
g  #<generator object <genexpr> at 0x035A9E70>
#通过next()函数获得generator的下一个返回值

for n in g:
    print(n)


#著名的斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到：
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'


#从第一个元素开始，推算出后续任意的元素，这种逻辑其实非常类似generator。    要把fib函数变成generator，只需要把print(b)改为yield b就可以了：
def fib1(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


#如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator：
# generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。


#定义一个generator，依次返回数字1，3，5：
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield (3)
    print('step 3')
    yield (5)


o = odd()
next(o)
next(o)
next(o)

"""
>>> next(o)
step 1
1
>>> next(o)
step 2
3
>>> next(o)
step 3
5
"""

for n in fib1(6):
    print(n)


# call generator manually: 拿不到generator的return语句的返回值。如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中：
g = fib1(5)
while 1:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break    

#杨辉三角
def triangles(n):
    L , index = [1], 0
    while index < n:
        yield L
        L = [1] + [L[i - 1] + L[i] for i in range(1, len(L))] + [1]  
        index += 1      
    
for x in triangles(5):
    print(x)

