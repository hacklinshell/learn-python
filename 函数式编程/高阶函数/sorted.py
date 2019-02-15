#排序

#sorted()函数就可以对list进行排序

sorted([36, 5, -12, 9, -21])  #[-21, -12, 5, 9, 36]

#可以接收一个key函数来实现自定义的排序

sorted([36, 5, -12, 9, -21], key=abs)  #[5, 9, -12, -21, 36]

#字符串排序，是按照ASCII的大小比较的，由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面

sorted(['bob', 'about', 'Zoo', 'Credit'])  #['Credit', 'Zoo', 'about', 'bob']

#忽略大小写，按照字母序排序
sorted(['bob', 'about', 'Zoo', 'Credit'],
       key=str.lower)  #['about', 'bob', 'Credit', 'Zoo']

#进行反向排序，不必改动key函数，可以传入第三个参数reverse=True：
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower,
       reverse=True)  #['Zoo', 'Credit', 'bob', 'about']

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

sorted(
    L, key=lambda s: s[0]
)  #按名字排序  #[('Adam', 92), ('Bart', 66), ('Bob', 75), ('Lisa', 88)]

from operator import itemgetter     

L = [('Bob', 75), ('Adam', 92), ('eBart', 66), ('sLisa', 88)]
sorted(
    L, key=itemgetter(              #itemgetter(0)  获取对象的第1个域 值 
        0))  #L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
