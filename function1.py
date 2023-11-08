# function1.py
#1) 함수 정의
def setValue(newValue):
    #지역변수
    x=newValue
    print('지역변수',x)

#2)호출
retValue=setValue(5)
print(retValue)

def swap(x,y):
    return y,x

retValue=swap(3,4)
print(retValue[0], retValue[1])

def intersect(prelist, postlist):
    result=[]
    for x in prelist:
        if x in postlist and x not in result:
            result.append(x)
    return result

#호출
print(intersect('HAM','SPAM'))
