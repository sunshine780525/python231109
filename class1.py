# class1.py
#1) 클래스 정의
class person:
    #초기화 메서드
    def __init__(self):
        self.name='default name'
    #출력메서드
    def print(self):
        print('my name is {0}'.format(self.name))

#2)인스턴스 생성
p1=person()

#3) 메서드
p1.print()
