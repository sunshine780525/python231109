# demoloop
value=5
while value>0:
    print(value)
    value-=1

print('---for in루크---')
lst=[10,20,30]
print('방객수:',len(lst))
for item in lst:
        print(item)

d={'apple':100,'banana':200,'orange':300}
for item in d.items():
        print(item)

for k,v in d.items():
       print(k,v)

print('---구구단 출력---')
for x in [2,3,4,5,6]:
       print('---{0}단 출력---'.format(x))
       for y in [1,2,3,4,5,6,7,8,9]:
              print('{0}*{1}={2}'.format(x,y,x*y))

print('---continue구문---')
lst=[1,2,3,4,5,6,7,8,9,10]
for i in lst:
       if i>5:
              break
       print('item:{0}'.format(i))

print('---continue구문---')
lst=[1,2,3,4,5,6,7,8,9,10]
for i in lst:
       if i % 2 == 0:
              continue
       print('item:{0}'.format(i))     


print('---range---')
print(list(range(10)))
print(list(range(2000,2024)))
print(list(range(1,32)))

print('---리스트 내장--- ')
lst=list(range(1,11))
print(lst)
print([i**2 for i in lst if i>5])

d={100:'apple', 200:'kiwi'}
print([v.upper() for v in d.values()])

print('---필터링 함수---')
lst=[10,25,30]
def getBiggerthan20(i):
    return i>20

iterL =filter(None, lst)
for i in iterL:
       print(i)



