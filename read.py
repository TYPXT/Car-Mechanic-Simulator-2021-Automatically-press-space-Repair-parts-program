import cv2
import numpy as np
import pyautogui
import pygetwindow as gw
import keyboard
import time
import sys

def check_pixel_color(image, x, y, expected_color):
    # 读取图片

    # 检查指定位置的像素颜色
    pixel_color = image[y, x]
    if list(expected_color)[0]-2 <= list(pixel_color)[0] <= list(expected_color)[0]+2 and list(expected_color)[1]-15 <= list(pixel_color)[1] <= list(expected_color)[1]+15 and list(expected_color)[2]-30 <= list(pixel_color)[2] <= list(expected_color)[2]+30:
        return True
    else:
        return False

cursor = [0, 160, 255]  # 指定颜色（BGR格式）
green = [22, 246, 56]# [21,244,76]
startbtn = [79,189,255]
x_list = [12,32,53,74,95,116,137,157,178,199,220,241,262,282,303,324,345,366,386,407]
y_list = [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9]
y_list2 = [119,119,119,119,119,119,119,119,119,119,119,119,119,119,119,119,119,119,119,119]
#X,119
def position(image,xlist,ylist,color,one=False):
    position=[]
    if one==True:
        for x in range(len(xlist)):
            if check_pixel_color(image, xlist[x]-1, ylist[x], color):
                return x
    else:
        for x in range(len(xlist)):
            if check_pixel_color(image, xlist[x]-1, ylist[x], color):
                position.append(x)

            else:
                position.append(-1)
    return position

START=False

def start():
    START=True
    print('已启动')
    i=0
    while START:
        #获取截图
        target_window = gw.getWindowsWithTitle('Car Mechanic Simulator 2021')[0]
        window_rect = (target_window.left, target_window.top, target_window.width, target_window.height)
        screenshot = pyautogui.screenshot()
        screenshot = screenshot.crop((window_rect[0]+440, window_rect[1]+272, window_rect[0] + 433+425, window_rect[1] +272+132))
        image = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
        #显示截图
        cv2.imshow('Screen Capture', image)
        if cv2.waitKey(1) == ord('q'):
            cv2.destroyAllWindows()
            break
        if check_pixel_color(image, 13, 78, cursor) or check_pixel_color(image, 13, 78, startbtn):
            #自动开始
            i=0
            keyboard.press_and_release('space')
            time.sleep(0.2)
            continue
            #手动开始
            # i=0
            # time.sleep(0.5)
            # continue
        if check_pixel_color(image, 13, 78, [28,194,95]):
            #出现成功的提示需要等一小会再开始，防止过快开始获取到的绿色列表不准确
            i=0
            continue
        if position(image,x_list,y_list,cursor,True) in position(image,x_list,y_list2,green):
                if i==0:
                    time.sleep(0.3)
                    continue
                print("yes,CURSOR",position(image,x_list,y_list,cursor,True),position(image,x_list,y_list2,green))
                keyboard.press_and_release('space')
        i+=1
        
def stop():
    START=False
    print("已暂停，可再次启动，终止请关闭终端")

def exit():
    print("exit")
start_key = "e"
stop_key = "q"
keyboard.on_press_key(start_key, lambda _: start())
keyboard.on_press_key(stop_key, lambda _: stop())
while True:
    time.sleep(0.1)
    