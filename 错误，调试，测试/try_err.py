
#  try来运行这段代码，如果执行出错，则后续代码不会继续执行 而是直接跳转至错误处理代码，即except语句块，执行完except后，如果有finally语句块，则执行finally语句块
try:
    print('try ... ')
    r = 10 / 0
    print('rease:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally....')
print('END')



#try ... 
#except: division by zero
#finally....
#END



def foo(s):
    return 10 / int(s)  #int(s) 返回0    10/0 错误

def bar(s):
    return foo(s) *2

def main():
    bar('0')

main()

# ZeroDivisionError: division by zero