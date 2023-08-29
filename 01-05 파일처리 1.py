##파일을 2가지
#텍스트 파일
#바이너리 파일   --> 이미지 파일 중 raw 파일.
import os.path
import math

filename = 'Etc_Raw(squre)\LENA256.RAW'
#파일 크기 알아내기
fsize = os.path.getsize(filename) #Byte 단위
height = width = int(math.sqrt(fsize))
print(height,'x',width)
#메모리 확보(영상 크기)
image = [[0 for _ in range(width)] for _ in range(height)]
# 파일 --> 메모리 로딩
rfp = open(filename,'rb')
for i in range(height):
    for k in range(width):
        image[i][k] = ord(rfp.read(1))
rfp.close()

##일부만 확인
for i in range(100,105,1):
    for k in range(100,105,1):
        print("%3d" % image[i][k], end=' ')
    print()
print()

#반전
image = [[0 for _ in range(width)] for _ in range(height)]
# 파일 --> 메모리 로딩
rfp = open(filename,'rb')
for i in range(height):
    for k in range(width):
        image[i][k] = ord(rfp.read(1))
rfp.close()

## 반전 처리
for i in range(height) :
    for k in range(width) :
        image[i][k] = 255 - image[i][k]

for i in range(100, 105, 1):
    for k in range(100, 105, 1):
        print("%3d " % image[i][k], end='')
    print()
print()