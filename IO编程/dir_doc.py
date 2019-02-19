import os
os.name  #'nt'  Windows系统

os.environ
os.environ.get('PATH')


##查看当前目录的绝对路径
os.path.abspath('.')        #'D:\\work\\python'

os.path.join()  #合成路径
os.path.split() #拆分路径
os.rename() #重命名
os.remove() #删除
