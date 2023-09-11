# -*- coding: utf-8 -*-
# Author:       Amove
# vision 1.1 zero 修改支持高分辨

from window_operate import *
from gaming_func import *
from notice_func import *
import sys,time,os
import threading
import d3dshot

if __name__ == '__main__':
    # 初始化
    hwnd = get_window_handle(title="咸鱼之王")
    #获取窗口 大小w，h
    rect = win32gui.GetWindowRect(hwnd)
    x,y=rect[0],rect[1]
    w,h=rect[2] - x,rect[3] - y

    if hwnd == 0:
        print("游戏未启动，退出...")
        time.sleep(3)
        os._exit(1)
    print_help()
    print("Start...tap help for more details.")

    # 领取离线奖励的线程
    thread1 = threading.Thread(target=shoucai_rountin_long, args=(hwnd,))
    thread1.start()

    # 爬塔的线程
    thread2 = threading.Thread(target=fuben_tower_rountin, args=(hwnd,))
    thread2.start()

    time.sleep(1)
    # 主函数
    while True:
        print_notice()
        cmd_input = input()

        if cmd_input == "1":
            show_window(hwnd)
        elif  cmd_input == "2":
            hide_window(hwnd)
        elif  cmd_input == "help":
            print_help()
        elif  cmd_input == "shoucai":     
            shoucai(hwnd,h,w)
        elif  cmd_input == "tower":
            fuben_tower(hwnd,h,w)
        elif  cmd_input == "daily":
            daily_test(hwnd,h,w)
        elif cmd_input =="shot":
            show_window(hwnd)
            screen_fullshot1(x,y,w,h)
            # d = d3dshot.create(capture_output="numpy")
            # d.display = d.displays[0]
            # d.screenshot_to_disk()
            # shot(hwnd,h,w)
        elif  cmd_input == "exit":
            print("Bye!")
            os._exit(1)