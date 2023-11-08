# func3.py
# 불변인데 ㅎ마수 내부에서 읽기쓰기
# 전역변수
g=1

def testscope(a):

    global g
    g=2
    return a+g

print(testscope(1))
print('전역변수 g:',g)

print(globals())

def times(a=10,b=20):
    return a*b

print(times())
print(times(5))
print(times(5,6))

def connecturi(server,port):
    strurl = 'http://'+server+':'+port
    return strurl

print(connecturi('multi.com','80'))
print(connecturi(port='8080',server='multi.com'))

def union(*ar):
    result=[]
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result

print(union('ham','egg'))
print(union('ham','egg','spam'))

#정의되지 않은 인자(dict)
def useruribuilder(server, port, **user):
    strurl='http://'+server+':'+port+'/?'
    for key in user.keys():
        strurl+=key+'='+user[key]+'&'
    return strurl

print(useruribuilder('multi.com','80',id='kim',passwd='1234'))
print(useruribuilder('multi.com','80',id='kim',passwd='1234',name='mike',age='30'))


g=lambda x,y:x*y
print(g(3,4))
print(g(5,6))

print((lambda x:x*x)(3))
print(globals())

lst=[10,25,30]
iterL=filter(lambda x:x>20,lst)
for item in iterL:
    print(item)

    
