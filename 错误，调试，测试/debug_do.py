def foo(s):
    n = int(s)
    assert n != 0, 'n is zero'  #表达式n != 0应该是True，否则，根据程序运行的逻辑，后面的代码肯定会出错。
    return 10 / n


foo('0')  #AssertionError: n is zero        Python    -O参数来关闭assert

# logging
import logging
logging.basicConfig(level=logging.INFO)

s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)



#pdb            -m pdb

import pdb

s = '0'
n = int(s)
pdb.set_trace() # 运行到这里会自动暂停
print(10 / n)