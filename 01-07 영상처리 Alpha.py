import math
import os
from tkinter import *
from tkinter import messagebox
## 함수
def displayImage() :
    global canvas,paper,window,height,width,filename,image
    if canvas != None:
        canvas.destroy()

    canvas = Canvas(window, height=256, width=256)
    paper = PhotoImage(height=256, width=256)
    canvas.create_image((256 / 2, 256 / 2), image=paper, state='normal')

    for i in range(height) :
        for k in range(width) :
            r = g = b = image[i][k]
            paper.put('#%02x%02x%02x' % (r, g, b),(k, i) )

    canvas.pack()

def  reverseImage() :
    for i in range(height):
        for k in range(width):
            image[i][k] = 255 - image[i][k]

    displayImage()
def brightImage():
    for i in range(height):
        for k in range(width):
            if (image[i][k] + 50 > 255):
                image[i][k] = 255
            else:
                image[i][k] += 50
    displayImage()

def darkImage():
    for i in range(height):
        for k in range(width):
            if (image[i][k] - 100 < 0):
                image[i][k] = 0
            else:
                image[i][k] -= 100
    displayImage()

def BWImage():
    for i in range(height):
        for k in range(width):
            if (image[i][k] > 127):
                image[i][k] = 255
            else:
                image[i][k] = 0
    displayImage()

def BWavgImage():
    hap = 0
    for i in range(height):
        for k in range(width):
            hap += image[i][k]

    avg = hap / (height * width)

    for i in range(height):
        for k in range(width):
            if (image[i][k] < avg):
                image[i][k] = 255
            else:
                image[i][k] = 0
    displayImage()
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
def dim1(arr):
    arr_dim1 = []
    for i in range(height):
        for j in range(width):
            arr_dim1.append(image[i][j])
    return arr_dim1
def midImage() :
    for i in range(height) :
        for k in range(width) :
            if (image[i][k] < midValue) :
                image[i][k] = 0
            else :
                image[i][k] = 255
    displayImage()

def rotate90(a):
  n = len(a)

  result = [[0]* n for _ in range(n)]

  for i in range(n):
    for j in range(n):
      result[j][n-i-1] = a[i][j]
  return a

def rotate180(a):
  n = len(a)
  m = len(a[0])

  result = [[0]* n for _ in range(m)]

  for i in range(n):
    for j in range(m):
      result[n-i-1][n-j-1] = a[i][j]
  return result
def rotate270(a):
  n = len(a)
  m = len(a[0])

  result = [[0]* n for _ in range(m)]

  for i in range(n):
    for j in range(m):
      result[n-j-1][i] = a[i][j]
  return result
## 변수
window, canvas, paper = None, None, None
filename = ""
height, width = 0, 0
image = []

## 메인
window = Tk()
window.geometry('300x300')
window.title('영상처리 Alpha')

btnRevese = Button(window, text ='반전', command=reverseImage )
btnRevese.pack()
btnbright = Button(window, text ='밝게', command=brightImage )
btnbright.pack()
btndark = Button(window, text ='어둡게', command=darkImage )
btndark.pack()
btnBWmid = Button(window, text ='흑백', command=midImage )
btnBWmid.pack()
btnBWmid = Button(window, text ='90도', command=rotate90 )
btnBWmid.pack()
btnBWmid = Button(window, text ='흑백', command=midImage )
btnBWmid.pack()
btnBWmid = Button(window, text ='흑백', command=midImage )
btnBWmid.pack()

filename = 'Etc_Raw(squre)/new256.RAW'
# 파일 크기 알아내기
fSize = os.path.getsize(filename) # Byte 단위
height = width = int(math.sqrt(fSize))
# 메모리 확보 (영상 크기)
image = [ [0 for _ in range(width)] for _ in range(height)]
# 파일 --> 메모리 로딩
rfp = open(filename, 'rb')
for i in range(height) :
    for k in range(width) :
        image[i][k] = ord(rfp.read(1))

rfp.close()

##displayImage()

##reverseImage()
##brightImage()
##darkImage()
##BWImage()
##BWavgImage()
# imageAry = dim1(image)
# quickSort(imageAry)
# midValue = imageAry[len(imageAry)//2]
# print(midValue)
##rotate90(image)
##print(image)
##BWmidImage()

rotate90(image)
displayImage()
window.mainloop()



