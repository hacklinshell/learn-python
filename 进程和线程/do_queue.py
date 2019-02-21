from multiprocessing import Process, Queue
import os, time, random


def write(q):
    print('process to write %s' % os.getpid())
    for value in ['a', 'b', 'c']:
        print('write %s' % value)
        q.put(value)
        time.sleep(random.random())


def read(q):
    print('process to read %s ' % os.getpid())
    while True:
        value = q.get(True)
        print('get %s from queue' % value)


if __name__ == '__main__':
    
    q = Queue()
    pw = Process(target=write, args=(q, ))
    pr = Process(target=read, args=(q, ))

    pw.start()
    pr.start()
    pw.join()

    pr.terminate()


#windows 环境下可能只有 write进程

#process to write 17817
#write a
#process to read 17818 
#get a from queue
#write b
#get b from queue
#write c
#get c from queue
