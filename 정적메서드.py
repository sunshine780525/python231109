# 정적메서드.py
class MyCalc(object):
    #데코레이터(살이있는 주석)
    @staticmethod
    def my_add(x,y):
        return x+y
    #인스턴스메서드
    def mothoda(self):
        print('메서드 실행')


#클래스에서 직접 호출한다.
a = MyCalc.my_add(5,7)
print(a)

#인스턴스 생성
calc=MyCalc()
calc.methoda()


