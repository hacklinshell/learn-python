from datetime import datetime

now = datetime.now()
print(now)  #2019-02-21 18:44:32.290580

dt = datetime(2019, 2, 12, 12, 20)  # 用指定日期时间创建datetime
print(dt)  #2019-02-12 12:20:00

#datetime转换为timestamp
dt.timestamp()  # 把datetime转换为timestamp
print(dt.timestamp())  #1549945200.0

#timestamp转换为datetime
t = 1549945200.0
print(datetime.fromtimestamp(t))  #2019-02-12 12:20:00

#timestamp也可以直接被转换到UTC标准时区的时间：
print(datetime.utcfromtimestamp(t))  #2019-02-12 04:20:00

#str转换为datetime

cday = datetime.strptime('2019-2-15 18:19:59', '%Y-%m-%d %H:%M:%S')

print(cday)

#collections
