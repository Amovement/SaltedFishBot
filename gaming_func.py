# -*- coding: utf-8 -*-
# Author:       Amove

import time
import datetime
from window_operate import *
import threading

# 创建互斥锁
mutex = threading.Lock()

def shoucai(hwnd):
    perform_background_click(hwnd,43,345) # 收益按钮
    time.sleep(0.5)
    perform_background_click(hwnd,303,676,7) # 升级按钮
    time.sleep(0.5)
    perform_background_click(hwnd,154,669) # 领奖励按钮

def shoucai_rountin(hwnd):
    print("收菜线程已上线...",datetime.datetime.now())
    while True:
        print("收菜线程心跳...",datetime.datetime.now())
        time.sleep(60*60*2) # 两小时
        with mutex:  # 获取互斥锁
            shoucai(hwnd)

def fuben_tower(hwnd):
    perform_background_click(hwnd,413,795) # 副本按钮
    time.sleep(1)
    perform_background_click(hwnd,225,233) # tower 按钮
    time.sleep(1)
    
    for i in range(0,10):
        perform_background_click(hwnd,238,788) # 挑战按钮
        time.sleep(0.5)
        perform_background_click(hwnd,51,717,3) # 跳过按钮
        time.sleep(0.5)

    perform_background_click(hwnd,45,796) # 退出按钮
    time.sleep(1)
    perform_background_click(hwnd,230,792,2) # 战斗按钮
    time.sleep(1)

def fuben_tower_rountin(hwnd):
    print("咸将塔线程已上线...",datetime.datetime.now())
    while True:
        print("咸将塔线程心跳...",datetime.datetime.now())
        time.sleep(60*60*2) # 两小时
        with mutex:  # 获取互斥锁
            fuben_tower(hwnd)

