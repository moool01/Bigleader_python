import random
## 함수
def display():
    for i in range(ROW):
        for k in range(COL):
            print("%3d" % image2[i][k], end=' ')
        print()
    print()

##quick sort
def quickSort(ary):

    n = len(ary)
    if n<= 1:
        return ary
    pivot = ary[n//2]
    leftAry , rightAry = [],[]

    for num in ary:
        if num <pivot:
            leftAry.append(num)
        elif num >pivot:
            rightAry.append(num)
    return quickSort(leftAry) + [pivot]+ quickSort(rightAry)
##변수
image1 = [ [0,0,0,0,0],
          [0,0,0,0,0],
          [0,0,0,0,0],
          [0,0,0,0,0],
          [0,0,0,0,0],
          ]
print(image1)
COL,ROW = 5,5
##메인
##메모리 할당
image2 = []
tmpAry = []
for i in range(ROW):
    for k in range(COL):
        tmpAry.append(0)
    image2.append(tmpAry)
    tmpAry=[]
print(image2)
print(tmpAry)

##파일 --> 메모리로 로딩(Loading)
for i in range(ROW):
    for k in range(COL):
        pixel= random.randint(0,255)
        image2[i][k] = pixel
#디스플레이 (화면 출력)
display()
##영상 처리
#(1) 영상을 50 밝게 처리하자.
for i in range(ROW):
    for k in range(COL):
        image2[i][k] += 50

display()

##255이상일떄 거르는방법
for i in range(ROW):
    for k in range(COL):
        if (image2[i][k]+50 > 255):
            image2[i][k] =255
        else:
            image2[i][k] +=50
display()
'''
## 100어둡게
for i in range(ROW):
    for k in range(COL):
        if (image2[i][k]-100 < 0):
            image2[i][k] =0
        else:
            image2[i][k] -=100
display()

## 완전 흑백 처리
for i in range(ROW):
    for k in range(COL):
        if (image2[i][k] > 127):
            image2[i][k] =255
        else:
            image2[i][k] = 0
display() 

#평균값 구하기
hap = 0
for i in range(ROW):
    for k in range(COL):
        hap += image2[i][k]
        
avg = hap /(ROW*COL)

for i in range(ROW):
    for k in range(COL):
        if (image2[i][k] < avg):
            image2[i][k] =255
        else:
            image2[i][k] = 0

#중앙값 사용
for i in range(ROW):
    for k in range(COL):
        image2.sort()
mid = image

#반전 하기
for i in range(ROW):
    for k in range(COL):
        image2[i][k] = 255 -image2[i][k]
display()
'''
image = sum(image2, [])
print(image)
image = quickSort(image)
print(image)

##중앙값

for i in range(ROW):
    for k in range(COL):
        if (image2[i][k] > image[(len(image)+1)//2]):
            image2[i][k] =255
        else:
            image2[i][k] = 0
display()
## 함수 선언 부분 ##

