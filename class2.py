# class2.py
#1) 클래스 정의
class person:
    #클래스 멈버변수
    num_person = 0
    #초기화 메서드
    def __init__(self):
        self.name='default name'
    #출력메서드
    def print(self):
        print('my name is {0}'.format(self.name))

#2)인스턴스 생성
p1=person()
p2=person()
print('인스턴스 갯수:{0}'.format(person.num_person))
p1.name = '전우치'
p1.print()
p2.print()

#싫ㅇ시에 변수 추가
person.title='new title'
print(p1.title)
print(p2.title)
print(person.title)

#인스턴스 추가
p1.age=30
print(p1.age)
print(p2.age)


