from multiprocessing import Process     #multiprocessing模块就是跨平台版本的多进程模块

import os

def run_proc(name):
    print('Run child process %s (%s)' % (name,os.getpid()))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())

    p = Process(target=run_proc,args=('test',)) #传入一个执行函数和函数的参数，创建一个Process实例，

    print('Child process will start')

    p.start()   #用start()方法启动
    p.join()    #join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步

    print('child process end')



#Parent process 4448.
#Child process will start
#Run child process test (2672)
#child process end
