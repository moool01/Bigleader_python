print('Hello~ World')

num = 100
if(num > 100):
    print("100보다 크다")
elif (num <100):
    print('100보다 작다')
else:
    print('100이다')

hap = 0
for i in range(1,101,1):
    hap += i
print("1번",hap)


hap2 = 0
i = 1
while (i < 101):
    hap2 += i
    i += 1
print("2번",hap2)

##함수 선언부

def addNumber(a,b):
    addHap = 0
    for i in range(a,b+1,1):
        addHap += i
    return addHap
##전역 변수부
hap = 0

##메인 코드부
hap = addNumber(1,100)
print("3번" ,hap)
