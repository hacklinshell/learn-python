from io import StringIO

f = StringIO()
f.write('hello')        #5  返回写的成功字符数

f.write(' ')    #1

f.write('world') #5

print(f.getvalue()) #hello world


f = StringIO('水面细风生，\n菱歌慢慢声。\n客亭临小市，\n灯火夜妆明。')

while True:
    s = f.readline()
    if s == '':
        break
    print(s)


from io import BytesIO    

f = BytesIO()

f.write(b'hello')
f.write(b' ')
f.write(b'world!')
print(f.getvalue())


data = '人闲桂花落，夜静春山空。月出惊山鸟，时鸣春涧中。'.encode('utf-8')
f = BytesIO(data)
print(f.read())

#b'\xe4\xba\xba\xe9\x97\xb2\xe6\xa1\x82\xe8\x8a\xb1\xe8\x90\xbd\xef\xbc\x8c\xe5\xa4\x9c\xe9\x9d\x99\xe6\x98\xa5\xe5\xb1\xb1\xe7\xa9\xba\xe3\x80\x82\xe6\x9c\x88\xe5\x87\xba\xe6\x83\x8a\xe5\xb1\xb1\xe9\xb8\x9f\xef\xbc\x8c\xe6\x97\xb6\xe9\xb8\xa3\xe6\x98\xa5\xe6\xb6\xa7\xe4\xb8\xad\xe3\x80\x82'