#pool

#如果要启动大量的子进程，可以用进程池的方式批量创建子进程

from multiprocessing import Pool
import os, time, random


def long_time_task(name):
    print('Run task %s (%s)' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f second' % (name, end - start))

if __name__ == '__main__':
    print('Parent process %s' % os.getpid())

    p = Pool(4)

    for i in range(5):
        p.apply_async(long_time_task,args=(i,))

    print('waiting for all subprocesses done ...')

    p.close()           #调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了。
    p.join()            #对Pool对象调用join()方法会等待所有子进程执行完毕，

    print('All  subprocesses done')
    
#Parent process 17376
#waiting for all subprocesses done ...
#Run task 2 (20640)
#Task 2 runs 0.84 second
#Run task 3 (12492)
#Task 3 runs 0.66 second
#Run task 4 (12492)
#Task 4 runs 0.43 second
#Run task 1 (15316)
#Task 1 runs 1.21 second
#Run task 0 (1852)
#Task 0 runs 2.53 second
#All  subprocesses done