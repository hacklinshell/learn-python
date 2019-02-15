#函数作为返回值

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax += n
        return ax
    return sum

f = lazy_sum(1,3,5,7,9)     
f       #           #调用lazy_sum()时，返回的并不是求和结果，而是求和函数：    <function lazy_sum.<locals>.sum at 0x00FDD6A8>
f()     #25 


#  闭包
#  在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中  这种称为“闭包（Closure）”的程序结构拥有极大的威力

#当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数：

f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
f1==f2  #False


#f1()，f2()和f3()  为什么返回9

def count():
    fs = []
    for i in range(1,4):
        def f():
            return i * i
        fs.append(f)
    return fs

f1,f2,f3 = count()

f1() #9
f2() #9
f3() #9

#全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。

def count1():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1,4):
        fs.append(f(i))
    return fs