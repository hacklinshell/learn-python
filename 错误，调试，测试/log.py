#logging  非常容易地记录错误信息：


import logging


def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)
    
main()
print('END')


#ERROR:root:division by zero
#Traceback (most recent call last):
#  File "<stdin>", line 3, in main
#  File "<stdin>", line 2, in bar
#  File "<stdin>", line 2, in foo
#ZeroDivisionError: division by zero