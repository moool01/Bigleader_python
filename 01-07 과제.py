import math
import os
from tkinter import *
from tkinter import messagebox

## 함수 선언 ##
def displayImage() :
    global window, canvas, paper, height, width, filename
    if canvas != None :
        canvas.destroy()

    canvas = Canvas(window, height=512, width=512)
    paper = PhotoImage(height=512, width=512)
    canvas.create_image((256 / 2, 256 / 2), image=paper, state='normal')

    for i in range(height) :
        for k in range(width) :
            r = g = b = image[i][k]
            paper.put('#%02x%02x%02x' % (r, g, b), (k, i))

    canvas.pack()

def dim1(arr):
    arr_dim1 = []
    for i in range(height):
        for k in range(width):
            arr_dim1.append(image[i][k])
    return arr_dim1

def qSort(arr, start, end) :
	if end <= start :
		return

	low = start
	high = end

	pivot = arr[(low + high) // 2]
	while low <= high :
		while arr[low] < pivot :
			low += 1
		while arr[high] > pivot :
			high -= 1
		if low <= high :
			arr[low], arr[high] = arr[high], arr[low]
			low, high = low + 1, high - 1

	mid = low

	qSort(arr, start, mid-1)
	qSort(arr, mid, end)

def quickSort(ary) :
	qSort(ary, 0, len(ary)-1)

def reverseImage() :
    for i in range(height):
        for k in range(width):
            image[i][k] = 255 - image[i][k]

    displayImage()

def brightImage() :
    for i in range(height) :
        for k in range(width) :
            if (image[i][k] + 50 > 255) :
                image[i][k] = 255
            else :
                image[i][k] += 50
    displayImage()

def darkImage() :
    for i in range(height) :
        for k in range(width) :
            if (image[i][k] - 100 < 0) :
                image[i][k] = 0
            else :
                image[i][k] -= 100
    displayImage()

def midImage() :
    for i in range(height) :
        for k in range(width) :
            if (image[i][k] < midValue) :
                image[i][k] = 0
            else :
                image[i][k] = 255
    displayImage()

def wb127Image() :
    for i in range(height) :
        for k in range(width) :
            if (image[i][k] < 127) :
                image[i][k] = 255
            else :
                image[i][k] -= 0
    displayImage()

def wbMeanImage() :
    hap = 0
    for i in range(height) :
        for k in range(width) :
            hap += image[i][k]
    avg = hap / (height * width)

    for i in range(height) :
        for k in range(width) :
            if (image[i][k] < avg) :
                image[i][k] = 255
            else :
                image[i][k] = 0
    displayImage()

def rotate_90():
    global image
    new_ary = [[0 for _ in range(width)] for _ in range(height)]
    for i in range(height):
        for k in range(width):
            new_ary[k][height-i-1] = image[i][k]
    image = new_ary
    displayImage()

def rotate_180() :
	global image
	n = height
	new_ary = [[0 for _ in range(width)] for _ in range(height)]

	for i in range(0, n):
		for k in range(0, n):
			new_ary[i][k] = image[n - i - 1][n - k - 1]
			#new_ary[n - i - 1][n - k - 1] = image[i][k]
	image = new_ary
	displayImage()

def rotate_270() :
	global image
	n = height
	new_ary = [[0 for _ in range(width)] for _ in range(height)]

	for i in range(0, n):
		for k in range(0, n):
			new_ary[n - k - 1][i] = image[i][k]
			#new_ary[n - i - 1][n - k - 1] = image[i][k]
	image = new_ary
	displayImage()

def TopBottom() :
	global image
	n = height
	new_ary = [[0 for _ in range(width)] for _ in range(height)]

	for i in range(0, n):
		for k in range(0, n):
			new_ary[i][k] = image[n - i - 1][k]
			#new_ary[n - i - 1][n - k - 1] = image[i][k]
	image = new_ary
	displayImage()

def LeftRight() :
	global image
	n = height
	new_ary = [[0 for _ in range(width)] for _ in range(height)]

	for i in range(0, n):
		for k in range(0, n):
			new_ary[i][k] = image[ i ][n- k -1]
			#new_ary[n - i - 1][n - k - 1] = image[i][k]
	image = new_ary
	displayImage()



## 변수 선언 ##
window, canvas, paper = None, None, None
filename = ""
height, width = 0, 0
image = []


## 메인 코드 ##
window = Tk()
window.geometry('700x700')
window.title('영상처리 과제')

# 버튼
btnRevese = Button(window, text ='반전', command=reverseImage )
btnRevese.pack()
btnbright = Button(window, text = '밝게', command=brightImage)
btnbright.pack()
btndark = Button(window, text ='어둡게', command=darkImage )
btndark.pack()

btnwb127 = Button(window, text = '흑백(127)', command = wb127Image)
btnwb127.pack()
btnwbMean = Button(window, text = '흑백(평균)', command = wbMeanImage)
btnwbMean.pack()
btnMid = Button(window, text ='중앙', command=midImage)
btnMid.pack()

btnRotate90 = Button(window, text ='90도 회전', command=rotate_90)
btnRotate90.pack()
btnRotate180 = Button(window, text ='180도 회전', command=rotate_180)
btnRotate180.pack()
btnRotate270 = Button(window, text ='270도 회전', command=rotate_270)
btnRotate270.pack()

btnTB = Button(window, text ='상하반전', command=TopBottom)
btnTB.pack()
btnLR = Button(window, text ='좌우반전', command=LeftRight)
btnLR.pack()



# 파일 불러오기
filename = 'Etc_Raw(squre)/new256.RAW'
# 파일 크기 알아내기
fSize = os.path.getsize(filename)
height = width = int(math.sqrt(fSize))
# 메모리 확보 (영상 크기)
image = [ [0 for _ in range(width)] for _ in range(height)]
# 파일 --> 메모리 로딩
rfp = open(filename, 'rb')
for i in range(height) :
    for k in range(width) :
        image[i][k] = ord(rfp.read(1))

rfp.close()

# 1차원으로 만들기
imageAry = dim1(image)
# quick 정렬
quickSort(imageAry)
# 중앙값 찾기
midValue = imageAry[len(imageAry)//2]
# 이미지 출력
displayImage()

window.mainloop()
