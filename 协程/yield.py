def consumer():
    r = ''
    while True:
        n = yield r  #yield拿到消息，处理，又通过yield把结果传回
        if not n:
            return  #第一个send为空会执行
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'


def produce(c):
    c.send(None)  #c.send(None)启动生成器；  consumer 函数 执行到yield r后停止
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)  #c.send(n)切换到consumer执行
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()  #c.close()关闭consumer


c = consumer()
produce(c)

#  1.运行produce()后，开始执行到c.send(None)，跳入consumer函数并执行到n = yield r停止,此时r = ''；
#  2.然后开始produce()的第一次循环，从r = c.send(n)开始，跳入consumer函数，并把send的参数赋值给consumer()第一次循环的n,此时r = 1,n = 1.
#  3.因为consumer()第一次循环的n != '',因此直接print [CONSUMER] Consuming 1...,并赋200 OK给r
#  4.接着开始第二次循环，执行到n = yield r停止,即最后返回r给到produce()的r变量，因此produce会print [PRODUCER] Consumer return: 200 OK。



#[PRODUCER] Producing 1...
#[CONSUMER] Consuming 1...
#[PRODUCER] Consumer return: 200 OK
#[PRODUCER] Producing 2...
#[CONSUMER] Consuming 2...
#[PRODUCER] Consumer return: 200 OK
#[PRODUCER] Producing 3...
#[CONSUMER] Consuming 3...
#[PRODUCER] Consumer return: 200 OK
#[PRODUCER] Producing 4...
#[CONSUMER] Consuming 4...
#[PRODUCER] Consumer return: 200 OK
#[PRODUCER] Producing 5...
#[CONSUMER] Consuming 5...
#[PRODUCER] Consumer return: 200 OK




def jumping_range(N):
    index = 0
    while index < N:
        # 通过send()发送的信息将赋值给jump
        jump = yield index 
        print('jump %s' %jump)                 
        if jump is None:
            jump = 1
        index += jump

if __name__ == '__main__':
    itr = jumping_range(5)
    print(next(itr))    # index = 0   yield return 0   打印出0  暂停
    print(itr.send(2))  # jump = 2   打印出2     index =  2      2 < 5  打印出2 暂停
    print(next(itr))    #  没执行send 所以jump等于None jump = 1 index = 3 打印出3 暂停
    print(itr.send(-1)) # jump = -1     index = -1 + 3 = 2    打印出2 暂停