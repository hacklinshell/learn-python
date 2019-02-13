
print("hello")

print("test")
print("中文英文str")  #python3 字符串是Unicode编码

ord('A')  #65
ord('琳') #29747
chr(77)   #'M'
len('ABC') # 3
len('中文') # 2  
len('中文'.encode('utf-8')) #6
str = 'world'
print("hello,%s" % str )# hello,world
