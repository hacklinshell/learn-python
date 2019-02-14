#列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式

#生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]可以用list(range(1, 11))：

list(range(1, 11))  #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#生成[1x1, 2x2, 3x3, ..., 10x10]  #把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来
[x * x for x in range(1, 11)]  #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#for循环后面还可以加上if判断，
[x * x for x in range(1, 11) if x % 2 == 0]  #[4, 16, 36, 64, 100]

#两层循环，可以生成全排列
[m + n for m in 'ABC'
 for n in 'XYZ']  #['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']

#for循环其实可以同时使用两个甚至多个变量，
d = {'x': 'A', 'y': 'B', 'z': 'C'}
for k, v in d.items():
    print(k, '=', v)
#   x = A
#   y = B
#   z = C

#把一个list中所有的字符串变成小写：
L = ['Hello', 'World', 'IBM', 'Apple']
[s.lower() for s in L]  #['hello', 'world', 'ibm', 'apple']