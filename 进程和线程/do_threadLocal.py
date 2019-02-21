import threading


#一个ThreadLocal变量虽然是全局变量，但每个线程都只能读写自己线程的独立副本，互不干扰。ThreadLocal解决了参数在一个线程中各个函数之间互相传递的问题。
loca_school = threading.local()     #全局变量local_school是一个ThreadLocal对象 


def process_student():

    std = loca_school.student       # Thread对它都可以读写student属性       每个属性如local_school.student都是线程的局部变量 可以任意读写而互不干扰，也不用管理锁的问题，ThreadLocal内部会处理。
    print('hello , %s (in %s )' % (std,threading.current_thread().name))

def prcess_thread(name):
    loca_school.student = name          #全局变量local_school是一个dict，不但可以用local_school.student，还可以绑定其他变量，如local_school.teacher等等。
    process_student()


t1 = threading.Thread(target=prcess_thread,args=('Alice',),name='thread-1')
t2 = threading.Thread(target=prcess_thread,args=('BOB',),name='thread-2')

t1.start()
t2.start()
t1.join()
t2.join()

#hello , Alice (in thread-1 )
#hello , BOB (in thread-2 )