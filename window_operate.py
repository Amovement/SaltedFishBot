# -*- coding: utf-8 -*-
# Author:       Amove

import win32gui
import win32con
import win32api
import win32ui
import time
import win32com.client
from PIL import Image
from ctypes import windll
import cv2
import numpy as np
import sys
from PyQt5.QtWidgets import QApplication
import d3dshot
def get_window_handle(class_name=None, title=None):
    """
    通过类名和标题查找窗口句柄.

    Args:
        class_name(str|None):窗口的类名. 默认为None.
        title(str|None):窗口的标题. 默认为None.

    Returns:
        int: 返回找到的窗口句柄，如果没有找到则返回0.
    """
    return win32gui.FindWindow(class_name, title)


def set_top_window(hwnd):
    """
    窗口置顶
    """
    shell = win32com.client.Dispatch("WScript.Shell")
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(hwnd)


def hide_window(hwnd):
    """
    隐藏窗口

    Args:
        title(str|None):窗口的标题. 默认为None.

    Returns:
        None
    """
    if hwnd == 0:
        return False
    set_top_window(hwnd=hwnd)
    win32gui.ShowWindow(hwnd, win32con.SW_HIDE)
    return True


def show_window(hwnd):
    """
    显示窗口

    Args:
        title(str|None):窗口的标题. 默认为None.

    Returns:
        None
    """
    if hwnd == 0:
        return False
    win32gui.ShowWindow(hwnd, win32con.SW_SHOW)
    set_top_window(hwnd=hwnd)
    return True

# 后台点击操作
def perform_background_click(hwnd, x, y,cnt=1):
    lParam = win32api.MAKELONG(int(x), int(y))
    count = 0
    while True:
        if count>=cnt:
            break
        time.sleep(0.2)
        win32api.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam)
        win32api.SendMessage(hwnd, win32con.WM_LBUTTONUP, 0, lParam)
        count+=1
        
# 后台移动操作
def perform_background_move(hwnd, x, y,cnt=1):
    lParam = win32api.MAKELONG(int(x), int(y))
    lParam1 = win32api.MAKELONG(int(x)+100, int(y))
    count = 0
    while True:
        if count>=cnt:
            break
        time.sleep(0.2)
        win32api.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam)
        win32api.SendMessage(hwnd, win32con.WM_MOUSEMOVE, win32con.MK_LBUTTON, lParam1)
        win32api.SendMessage(hwnd, win32con.WM_LBUTTONUP, 0, 0)
        count+=1
        
#截图
def shot(hwnd,x,y):
    left, top, right, bot = win32gui.GetWindowRect(hwnd)
    width = right - left
    height = bot - top
    #返回句柄窗口的设备环境，覆盖整个窗口，包括非客户区，标题栏，菜单，边框
    hwndDC = win32gui.GetWindowDC(hwnd)
    #创建设备描述表
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    #创建内存设备描述表
    saveDC = mfcDC.CreateCompatibleDC()
    #创建位图对象准备保存图片
    saveBitMap = win32ui.CreateBitmap()
    #为bitmap开辟存储空间
    saveBitMap.CreateCompatibleBitmap(mfcDC,width,height)
    #将截图保存到saveBitMap中
    saveDC.SelectObject(saveBitMap)
    #保存bitmap到内存设备描述表
    saveDC.BitBlt((0,0), (width,height), mfcDC, (0,0), win32con.SRCCOPY)
    
    #如果要截图到打印设备：
    ###最后一个int参数：0-保存整个窗口，1-只保存客户区。如果PrintWindow成功函数返回值为1
    result = windll.user32.PrintWindow(hwnd,saveDC.GetSafeHdc(),0)
    print(result) 
    # #PrintWindow成功则输出1
    total_bytes = width*height*4
    buffer = bytearray(total_bytes)
    image =np.frombuffer(buffer, dtype=np.uint8).reshape(height, width, 4)
    cv2.imshow("Capture Test", image)
    cv2.waitKey()
    # #保存图像
    # ##方法一：windows api保存
    # ###保存bitmap到文件
    # saveBitMap.SaveBitmapFile(saveDC,"img_Winapi.bmp")
    
    # ##方法二(第一部分)：PIL保存
    # ###获取位图信息
    # bmpinfo = saveBitMap.GetInfo()
    # bmpstr = saveBitMap.GetBitmapBits(True)
    # ###生成图像
    # im_PIL = Image.frombuffer('RGB',(bmpinfo['bmWidth'],bmpinfo['bmHeight']),bmpstr,'raw','BGRX',0,1)
    # ##方法二（后续转第二部分）

    # #内存释放
    # win32gui.DeleteObject(saveBitMap.GetHandle())
    # saveDC.DeleteDC()
    # mfcDC.DeleteDC()
    # win32gui.ReleaseDC(hwnd,hwndDC)
    
    # ##方法二（第二部分）：PIL保存
    # ###PrintWindow成功,保存到文件,显示到屏幕
    # im_PIL.save("im_PIL.png") #保存
    # im_PIL.show() #显示
    
def  screen_fullshot():
    d = d3dshot.create(capture_output="numpy")
    d.display = d.displays[0]
    d.screenshot_to_disk()


 

     
def screen_fullshot1(x,y,w,h):
    app = QApplication(sys.argv)
    screen = QApplication.primaryScreen()
    if screen is None:
        print('screen is None')
        exit(0)
    originalPixmap = screen.grabWindow(QApplication.desktop().winId(),x,y,w,h)
    originalPixmap.save('444.jpg', 'png')