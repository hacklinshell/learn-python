import time, threading

#current_thread()函数，它永远返回当前线程的实例
def loop():
    print('thread %s is runing' % threading.current_thread().name)

    n = 0
    while n < 5:
        n += 1
        print('thread %s --- %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s end ' % threading.current_thread().name)

#进程默认就会启动一个线程，我们把该线程称为主线程       MainThread
print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopTread')     #用LoopThread命名子线程
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)

#thread MainThread is running...
#thread LoopTread is runing
#thread LoopTread --- 1
#thread LoopTread --- 2
#thread LoopTread --- 3
#thread LoopTread --- 4
#thread LoopTread --- 5
#thread LoopTread end 
#thread MainThread ended.