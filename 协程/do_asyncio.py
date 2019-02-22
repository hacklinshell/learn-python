import asyncio
import threading

#Coroutine  协程            corporate routine的缩写，直接翻译为协同的例程，一般我们都简称为协程 协程称为  轻量级的线程即微线程。


@asyncio.coroutine      #@asyncio.coroutine把一个generator标记为coroutine类型
def hello():
    print('hello world (%s)' % threading.current_thread())
    r = yield from asyncio.sleep(1)
    print('hello again (%s)' % threading.current_thread())

#新的async await 语法
async def hello1():
    print('hello world')
    r = await asyncio.sleep(1)
    print('hello again')



#获取eventloop
loop = asyncio.get_event_loop()
tasks = [hello(),hello()]
#执行coroutine
loop.run_until_complete(asyncio.wait(tasks))
loop.close()


#hello world (<_MainThread(MainThread, started 15780)>)
#hello world (<_MainThread(MainThread, started 15780)>)
#(暂停约1秒)
#hello again (<_MainThread(MainThread, started 15780)>)
#hello again (<_MainThread(MainThread, started 15780)>)