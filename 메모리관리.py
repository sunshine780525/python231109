# 메모리관리.py 

class MyClass:
    #초기화 ㅁ서드
    def __init__(self, value):
        self.value = value 
        print("Instance is created! value=", value)
    #소명자 ㅁ서드
    def __del__(self):
        print("Instance is deleted!")

#인스턴스 생성
d = MyClass(5)
#인스턴스 삭제(참조카운트 1->0)
#del d 

print('전체 코드 실행 종료')
