import math
import os
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import *
from tkinter.simpledialog import *
import struct

##함수 선언부
### 공통 함수부 ###
def loadImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    filename = askopenfilename(parent=window, filetypes=(("RAW파일","*.raw"),("모든파일","*.*")))
    # print(filename)

    # 파일크기 알아내기
    fSize = os.path.getsize(filename)  # Byte 단위
    inH = inW = int(math.sqrt(fSize))

    #메모리 확보
    # list comprehension
    inImage = [[0 for _ in range(inW)] for _ in range(inH)]
    # print(image)

    # 파일 -> 메모리 로딩
    rfp = open(filename, 'rb')
    for i in range(inH):
        for j in range(inW):
            inImage[i][j] = ord(rfp.read(1))  # ord : binary -> int 변환
            # read(한번에 읽을 byte 크기)

    rfp.close()
    equalImage()

def displayImage() :
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW

    if canvas != None :
        canvas.destroy()
    window.geometry(str(outH)+'x'+str(outW))  #outImage의 크기에 맞게 canvas 크기 조절
    canvas = Canvas(window, height=outH, width=outW)
    paper = PhotoImage(height=outH, width=outW)
    canvas.create_image((outH/2, outW/2), image=paper, state='normal')  #(outH/2, outW/2) : 중앙점 찾는거

    #메모리상에서 픽셀 값 다 저장해놓고 한번에 화면에 옮김 -> 시간 효율성 상승
    rgbString = ""
    for i in range(outH):
        tmpString = ""
        for j in range(outW):
            r = g = b = outImage[i][j]
            tmpString += "#%02x%02x%02x " % (r,g,b)
        rgbString +=  '{' + tmpString + '} '
    paper.put(rgbString)
    # 메모리 -> 화면 반복하니까 시간느림... 효율성 떨어짐
    # for i in range(outH):
    #     for j in range(outW):
    #         r = g = b = outImage[i][j]  # rgb -> gray scale 표현
    #         paper.put('#%02x%02x%02x' % (r,g,b) , (j,i))   #  # : 숫자  %02x : 16진수 표시
    canvas.pack()

def saveImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW

    saveFp = asksaveasfile(parent=window, mode='wb',
                           defaultextension="*.raw",
                           filetypes=(("RAW파일","*.raw"),("모든파일","*.*")))

    for i in range(outH):
        for j in range(outW):
            saveFp.write( struct.pack("B",outImage[i][j]))
    saveFp.close()
    messagebox.showinfo("성공", saveFp.name+'으로 저장')



### 영상 처리 함수부 ###
# equalImage -> 영상처리 함수의 기본 토대
def equalImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    # critical code :
    # 출력이미지의 크기를 결정 --> 알고리즘에 따라 달라짐  : 중요 설정
    outH = inH
    outW = inW

    # 메모리 확보
    # list comprehension
    outImage = [[0 for _ in range(outW)] for _ in range(outH)]

    ## 처리 알고리즘 부분 ##
    # inImage -> outImage 알고리즘 구현
    for i in range(inH):
        for j in range(inW):
            outImage[i][j] = inImage[i][j]

    displayImage()

def reverseImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    # critical code :
    # 출력이미지의 크기를 결정 --> 알고리즘에 따라 달라짐
    outH = inH
    outW = inW

    # 메모리 확보
    # list comprehension
    outImage = [[0 for _ in range(outW)] for _ in range(outH)]

    ## 처리 알고리즘 부분 ##
    # inImage -> outImage 알고리즘 구현
    #overflow , underflow 체크 !
    for i in range(inH):
        for j in range(inW):
            outImage[i][j] = 255 - inImage[i][j]

    displayImage()

def addImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    # critical code :
    # 출력이미지의 크기를 결정 --> 알고리즘에 따라 달라짐
    outH = inH
    outW = inW

    # 메모리 확보
    # list comprehension
    outImage = [[0 for _ in range(outW)] for _ in range(outH)]

    ## 처리 알고리즘 부분 ##
    # inImage -> outImage 알고리즘 구현
    value = askinteger("밝기 변경 값","-255 ~ 255 사이를 입력하세요", minvalue=-255, maxvalue=255)
    for i in range(inH):
        for j in range(inW):
            if (inImage[i][j] + value > 255):
                outImage[i][j] = 255
            elif (inImage[i][j] + value < 0 ):
                outImage[i][j] = 0
            else:
                outImage[i][j] = inImage[i][j] + value


    displayImage()

def bwImage_center():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    # critical code :
    # 출력이미지의 크기를 결정 --> 알고리즘에 따라 달라짐
    outH = inH
    outW = inW

    # 메모리 확보
    # list comprehension
    outImage = [[0 for _ in range(outW)] for _ in range(outH)]

    ## 처리 알고리즘 부분 ##
    # inImage -> outImage 알고리즘 구현
    for i in range(inH):
        for j in range(inW):
            if inImage[i][j] < 127:
                outImage[i][j] = 0
            else :
                outImage[i][j] = 255

    displayImage()

def bwImage_mean():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    # critical code :
    # 출력이미지의 크기를 결정 --> 알고리즘에 따라 달라짐
    outH = inH
    outW = inW

    # 메모리 확보
    # list comprehension
    outImage = [[0 for _ in range(outW)] for _ in range(outH)]

    ## 처리 알고리즘 부분 ##
    # inImage -> outImage 알고리즘 구현
    sum = 0
    for i in range(inH):
        for j in range(inW):
            sum += inImage[i][j]

    avg = sum//(inH * inW)
    for i in range(inH):
        for j in range(inW):
            if inImage[i][j] > avg:
                outImage[i][j] = 255
            else :
                outImage[i][j] = 0


    displayImage()

def rotate90():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    # critical code :
    # 출력이미지의 크기를 결정 --> 알고리즘에 따라 달라짐
    outH = inH
    outW = inW

    # 메모리 확보
    # list comprehension
    outImage = [[0 for _ in range(outW)] for _ in range(outH)]

    ## 처리 알고리즘 부분 ##
    # inImage -> outImage 알고리즘 구현
    for i in range(inH):
        for j in range(inW):
            outImage[j][outH - i - 1]= inImage[i][j]

    displayImage()

def rotate180():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    # critical code :
    # 출력이미지의 크기를 결정 --> 알고리즘에 따라 달라짐
    outH = inH
    outW = inW

    # 메모리 확보
    # list comprehension
    outImage = [[0 for _ in range(outW)] for _ in range(outH)]

    ## 처리 알고리즘 부분 ##
    # inImage -> outImage 알고리즘 구현
    for i in range(inH):
        for j in range(inW):
            outImage[outH - i -1][outW - j - 1]= inImage[i][j]

    displayImage()

def rotate270():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    # critical code :
    # 출력이미지의 크기를 결정 --> 알고리즘에 따라 달라짐
    outH = inH
    outW = inW

    # 메모리 확보
    # list comprehension
    outImage = [[0 for _ in range(outW)] for _ in range(outH)]

    ## 처리 알고리즘 부분 ##
    # inImage -> outImage 알고리즘 구현
    for i in range(inH):
        for j in range(inW):
            outImage[outH - j - 1][i]= inImage[i][j]

    displayImage()

def x_symmetry():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    # critical code :
    # 출력이미지의 크기를 결정 --> 알고리즘에 따라 달라짐
    outH = inH
    outW = inW

    # 메모리 확보
    # list comprehension
    outImage = [[0 for _ in range(outW)] for _ in range(outH)]

    ## 처리 알고리즘 부분 ##
    # inImage -> outImage 알고리즘 구현
    for i in range(inH):
        for j in range(inW):
            outImage[i][outW - j - 1]= inImage[i][j]

    displayImage()

def y_symmetry():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    # critical code :
    # 출력이미지의 크기를 결정 --> 알고리즘에 따라 달라짐
    outH = inH
    outW = inW

    # 메모리 확보
    # list comprehension
    outImage = [[0 for _ in range(outW)] for _ in range(outH)]

    ## 처리 알고리즘 부분 ##
    # inImage -> outImage 알고리즘 구현
    for i in range(inH):
        for j in range(inW):
            outImage[outH - i - 1][j]= inImage[i][j]

    displayImage()

#### 기하학 처리  ###
def moveImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    # critical code :
    # 출력이미지의 크기를 결정 --> 알고리즘에 따라 달라짐  : 중요 설정
    outH = inH
    outW = inW

    # 메모리 확보
    # list comprehension
    outImage = [[0 for _ in range(outW)] for _ in range(outH)]

    ## 처리 알고리즘 부분 ##
    # inImage -> outImage 알고리즘 구현
    # 가로,세로 이동할 칸수 입력받음
    xVal = askinteger("X값", "")
    yVal = askinteger("Y값", "")

    for i in range(inH):
        for j in range(inW):
            if (0 <= i+xVal < outH) and (0 <= j+yVal < outW):
                outImage[i+xVal][j+yVal] = inImage[i][j]

    displayImage()

def zoomOutImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW

    # critical code :
    # 축소 배율 입력받음
    scale = askinteger("축소배율","")
    # 출력이미지의 크기를 결정 --> 알고리즘에 따라 달라짐  : 중요 설정
    outH = inH // scale
    outW = inW // scale

    # 메모리 확보
    # list comprehension
    outImage = [[0 for _ in range(outW)] for _ in range(outH)]

    ## 처리 알고리즘 부분 ##
    # inImage -> outImage 알고리즘 구현
    for i in range(inH):
        for j in range(inW):
            outImage[i//scale][j//scale] = inImage[i][j]

    displayImage()

def zoominImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW

    # critical code :
    # 확대 배율 입력받음
    scale = askinteger("확대배율","")
    # 출력이미지의 크기를 결정 --> 알고리즘에 따라 달라짐  : 중요 설정
    outH = inH * scale
    outW = inW * scale

    # 메모리 확보
    # list comprehension
    outImage = [[0 for _ in range(outW)] for _ in range(outH)]

    ## 처리 알고리즘 부분 ##
    # inImage -> outImage 알고리즘 구현

    # for i in range(inH):
    #     for j in range(inW):
    #         outImage[i * scale][j * scale] = inImage[i][j]

    # 그냥 확대하면 빈공간이 생김 -> 0으로 자동으로 채워짐
    # backwarding 방법으로 해결 -> 확대 된 곳에 채워질 픽셀값을 역으로 어떤 곳에서 가져올지 생각해서 채움
    for i in range(outH):
        for j in range(outW):
            outImage[i][j] = inImage[i // scale][j // scale]


    displayImage()

def rotateImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    # critical code :
    # 출력이미지의 크기를 결정 --> 알고리즘에 따라 달라짐  : 중요 설정
    # 회전각도(반 시계방향으로 생각)  -> 컴퓨터는 라디안값을 줘야함
    angle = askinteger("각도","0~360")
    radian = angle * math.pi / 180.0

    #중심점 값
    cx = inH // 2
    cy = inW // 2



    outH = inH
    outW = inW

    # 메모리 확보
    # list comprehension
    outImage = [[0 for _ in range(outW)] for _ in range(outH)]

    ## 처리 알고리즘 부분 ##
    ## 문제점
    ## 1. 깨짐 ( hole 생김 ) , 2. 중앙을 기준으로 회전하지 않음
    # inImage -> outImage 알고리즘 구현

    # for i in range(inH):
    #     for j in range(inW):
    #         newI = int(math.cos(radian)*(i-cx) - math.sin(radian)*(j-cy)) + cx
    #         newJ = int(math.sin(radian)*(i-cy) + math.cos(radian)*(j-cy)) + cy
    #
    #         if (0 <= newI < outH) and (0 <= newJ < outW):
    #             outImage[newI][newJ] = inImage[i][j]

    for i in range(outH):
        for j in range(outW):
            oldI = int(math.cos(radian)*(i-cx) + math.sin(radian)*(j-cy)) + cx
            oldJ = int(math.sin(radian)*(i-cy) - math.cos(radian)*(j-cy)) + cy

            if (0 <= oldI < inH) and (0 <= oldJ < inW):
                outImage[i][j] = inImage[oldI][oldJ]

    displayImage()

##전역 변수부
window , canvas, paper = None, None, None  #이미지 디스플레이 표현용 변수
filename = ""   #파일 path 변수
inImage, outImage = None, None   #input, output 이미지 저장할 변수
inH, inW, outH, outW = 0,0,0,0   #input, output 이미지 height, width

##메인 코드부

window = Tk()
#일반적으로 아무것도 안하면 창크기가 위젯크기에 맞춰짐
window.geometry('300x300')  #창 크기 고정
window.title("GrayScale Image Processing (RC1)")  # 창 제목 부여

#메뉴 만들기 -> 버튼대체
mainMenu = Menu(window)  #메뉴 틀
window.config(menu=mainMenu)

#파일 메뉴
fileMenu = Menu(mainMenu)  #상위 메뉴 (파일)
mainMenu.add_cascade(label="파일", menu=fileMenu)
fileMenu.add_command(label="열기", command=loadImage)
fileMenu.add_command(label="저장", command=saveImage)
fileMenu.add_separator()  #메뉴 구분선
fileMenu.add_command(label="종료", command=None)

#영상처리 메뉴
image1Menu = Menu(mainMenu) #상위 메뉴 (영상처리)
mainMenu.add_cascade(label="영상처리1", menu=image1Menu)
image1Menu.add_command(label="동일영상", command=equalImage)
image1Menu.add_command(label="반전", command=reverseImage)
image1Menu.add_command(label="밝게/어둡게", command=addImage)
image1Menu.add_command(label="흑백1(중심)", command=bwImage_center)
image1Menu.add_command(label="흑백1(평균)", command=bwImage_mean)
image1Menu.add_command(label="회전90", command=rotate90)
image1Menu.add_command(label="회전180", command=rotate180)
image1Menu.add_command(label="회전270", command=rotate270)
image1Menu.add_command(label="좌우반전", command=x_symmetry)
image1Menu.add_command(label="상하반전", command=y_symmetry)


image2Menu = Menu(mainMenu)
mainMenu.add_cascade(label="화소점처리", menu=image2Menu)
image2Menu.add_command(label="동일영상", command=equalImage)
image2Menu.add_command(label="반전", command=reverseImage)
image2Menu.add_command(label="밝게/어둡게", command=addImage)

image3Menu = Menu(mainMenu)
mainMenu.add_cascade(label="기하학처리", menu=image3Menu)
image3Menu.add_command(label="이동", command=moveImage)
image3Menu.add_command(label="회전", command=rotateImage)
image3Menu.add_command(label="축소", command=zoomOutImage)
image3Menu.add_command(label="확대", command=zoominImage)


window.mainloop()