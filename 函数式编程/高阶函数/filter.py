#filter()函数用于过滤序列。


#filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。

#在一个list中，删掉偶数，只保留奇数，可以这么写：

def is_odd(n):
    return n % 2 == 1

list(filter(is_odd,[1,2,4,5,6,7,8,15])) #[1, 5, 7, 15]

#把一个序列中的空字符串删掉

def not_empty(s):
    return s and s.strip()      #移除字符串头尾指定的字符（默认为空格或换行符）或字符序列        # 去除首尾空格

list(filter(not_empty,['A','','b',None]))   #['A', 'b']



#1000以内的素数打印         埃氏筛法
def main():
    for n in primes():
        if n < 1000:
            print(n)
        else:
            break

def _odd_iter():        #  一个从3开始的奇数序列：偶数肯定不是素数  生成器  一个无限序列
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):      #筛选函数
    return lambda x: x % n > 0      #埃氏筛法

def primes():       #定义一个生成器，不断返回下一个素数
    yield 2         #先返回第一个素数2
    it = _odd_iter()     # 初始序列
    while True:
        n = next(it)    # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it)  ## 构造新序列

if __name__ == '__main__':
    main()