# function2.py
print('---불변형식---')
a=1.2
print(id(a))
a=2,3
print(id(a))

print('---가변형식---')
lst=[1,2,3]
print(id(lst))
lst.append(4)
print(id(lst))

print('---입+출---')
wordlist=['j','a','m']

def change(x):
    x1=x[:]
    x1[0]='h'
    print('함수내부:',x1)

change(wordlist)
print('함수 호출후:',wordlist)

print('---지역,전역변수---')
x=5
def func1(a):
    return a+x

print(func1(1))

def func2(a):
    x=10
    return a+x

print(func2(1))
