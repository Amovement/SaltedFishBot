# -*- coding: utf-8 -*-
# Author:       Amove
# vision 1.1 zero 修改支持高分辨

import time
import datetime
from window_operate import *
import threading

# 创建互斥锁
mutex = threading.Lock()
def fuben_tower_rountin(hwnd):
    print("咸将塔线程已上线...",datetime.datetime.now())
    while True:
        print("咸将塔线程心跳...",datetime.datetime.now())
        time.sleep(60*60*3) # 三小时
        with mutex:  # 获取互斥锁
            fuben_tower(hwnd)
            
def shoucai_rountin_long(hwnd):
    print("收菜线程已上线...",datetime.datetime.now())
    while True:
        print("收菜线程心跳...",datetime.datetime.now())
        time.sleep(60*60*10) # 两小时
        with mutex:  # 获取互斥锁
            shoucai(hwnd)
            
#为了黑市活动设置短时间的
def shoucai_rountin_short(hwnd):
    print("收菜线程已上线...",datetime.datetime.now())
    while True:
        print("收菜线程心跳...",datetime.datetime.now())
        time.sleep(60*60*2) # 两小时
        with mutex:  # 获取互斥锁
            shoucai(hwnd)
            
                        
def shoucai(hwnd,h,w):
    time.sleep(1.5)
    # perform_background_move(hwnd,0.35*w,0.86*h,3)  #划开锁屏（无法保证在首页）
    time.sleep(2)
    # 43/450 345/844
    perform_background_click(hwnd,0.0856*w,0.408*h,) # 收益按钮
    time.sleep(0.7)
    # 303/450 676/844
    perform_background_click(hwnd,0.67*w,0.8*h,5) # 升级按钮
    time.sleep(0.7)
    # 154/450 669/844
    perform_background_click(hwnd,0.34*w,0.792*h) # 领奖励按钮
    time.sleep(1.5)


            
def fuben_tower(hwnd,h,w):
    time.sleep(1.5)
    # perform_background_move(hwnd,0.35*w,0.86*w,3)  #划开锁屏（无法保证在首页）
    time.sleep(0.7)
    #413/450 795/844
    perform_background_click(hwnd,0.917*w,0.942*h) # 副本按钮
    time.sleep(2)
    #225/450 233/844
    perform_background_click(hwnd,0.3*w,0.276*h) # tower 按钮
    time.sleep(2)
    
    for i in range(0,10):
        #238/450 788/844
        perform_background_click(hwnd,0.529*w,0.934*h) # 挑战按钮
        time.sleep(1)
         #51/450 717/844
        perform_background_click(hwnd,0.11*w,0.849*h,3) # 跳过按钮
        time.sleep(4)

    time.sleep(1.5)
     #39/450 807/844
    perform_background_click(hwnd,0.0867*w,0.956*h,2) # 退出按钮
    time.sleep(1)
     #230/450 792/844
    perform_background_click(hwnd,0.511*w,0.938*h,2) # 返回案板首页
    time.sleep(5)

def daily_test(hwnd,h,w):
    show_window(hwnd)
    time.sleep(1.5)
    # perform_background_move(hwnd,0.35*w,0.86*w,3)  #划开锁屏（无法保证在首页）
    # time.sleep(1.5)
    #413/450 795/844
    perform_background_click(hwnd,0.917*w,0.942*h) # 副本按钮
    time.sleep(1)
    #225/450 233/844
    perform_background_click(hwnd,0.3*w,0.476*h) # 咸王考验按钮
    time.sleep(1)

    perform_background_click(hwnd,0.511*w,0.908*h,1) # 点击挑战按钮
    time.sleep(1)
    perform_background_click(hwnd,0.11*w,0.849*h,2) # 跳过按钮
    time.sleep(1)
    perform_background_click(hwnd,0.511*w,0.758*h,) # 点击确认
    time.sleep(1)
    perform_background_click(hwnd,0.0867*w,0.956*h,2) # 退出按钮
    time.sleep(1)
     #230/450 792/844
    perform_background_click(hwnd,0.511*w,0.938*h,2) # 返回案板首页
    time.sleep(5)

