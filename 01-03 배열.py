import random

#함수


#변수
ary1 = []


#메인
#배열의 초기화
for i in range(10): # (0,10,1),# for (int i = 0;i <10 ; i++)
    ary1.append(0)  #append 검색

print(ary1)
num = 2
for i in range(10):
    ary1[i] = num
    num+=2

print (ary1)

for i in range(10):
    ary1[i] = random.randint(0,1000)
#배열 처리
print(ary1)
#1. 배열의 값의 합계
sum_ary1 = sum(ary1)
print(sum_ary1)
#2. 배열 중 홀수만 합계
result = 0
for i in range(10):
    if ary1[i] % 2 != 0:
        result += ary1[i]
print(result)



'''
송준호 형님 풀이
#2. 배열 중 홀수만 합계
result = 0
result2 = []
for i in range(0,10,1) :
    if arr1[i]%2 != 0 :
        result += arr1[i]
        # result2.append(arr1[i])
print(arr1)
print(result)
'''
'''
교수님 풀이
1. 배열의 값의 합계 
hap = 0
for i in range(0,10,1):
    hap += ary1[i]
print(hap)
2. 배열 중 홀수만 합계
hap = 0
for i in range(0,10,1):
    if (ary1[i] % 2 != 0):
        hap += ary1[i]
    print(hap)
'''

