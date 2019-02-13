## lsit list是一个可变的有序表

classmates = ["bob","colin","menken"]
print(classmates)   #['bob', 'colin', 'menken']
print(classmates[0]) #bob
print(classmates[1]) #colin
print(classmates[2]) #memken
print(classmates[-1]) #memken

len(classmates)     # 3
#list 中追加元素到末尾
classmates.append("egg")
print(classmates)        # ['bob', 'colin', 'menken', 'egg']
#插入指定位置
classmates.insert(2,'strugle')
print(classmates)          #['bob', 'colin', 'strugle', 'menken', 'egg'] 

#删除末尾的元素
classmates.pop()  # 'egg'
print(classmates)   #['bob', 'colin', 'strugle', 'menken']

#删除指定位置元素
classmates.pop(2) # 'strugle'
print(classmates) # ['bob', 'colin', 'menken']

#替换某个元素为别的元素，直接赋值到索引的位置
classmates[2] = 'neo'
print(classmates)   #['bob', 'colin', 'neo']

#list 里面的元素数据类型可以不同

L = ['HELLO',2,True]

#list 元素可以是另一个list

M = ['C','a',2,[1,'haha'],'test']
len(M)  # 5

#要拿到'haha'
M[3][1] #'haha'
print(M[3][1]) #haha

#如果list中一个元素没用  那么长度为0
S = []
len(S)  #0

#tuple  元组，  和list非常相似，但是tuple初始化后不能修改   指向永远不变

classmates = ('Michael', 'Bob', 'Tracy')
classmates  #('Michael', 'Bob', 'Tracy')
#定义一个tuple的时候，元素必须确定下来
#定义一个空的tuple
t = ()
t    #()

#定义只有一个元素的tuple  不能按照下面定义
t = (2)
t  # 2

# 因为()可以表示为小括号，就和tuple冲突了，默认按照小括号计算，所以t = 2 ，因此必须按照下面定义
t = (2,)
t #(2,)

# "可变的tuple"

t = ('a', 'b', ['A', 'B'])
t[2][0] = 'M'
t[2][2] = 'N'
t # ('a', 'b', ['M', 'B'])