# -*- coding: utf-8 -*-
# Author:       Amove

from window_operate import *
from gaming_func import *
from notice_func import *
import sys,time,os
import threading


if __name__ == '__main__':
    # 初始化
    hwnd = get_window_handle(title="咸鱼之王")
    if hwnd == 0:
        print("游戏未启动，退出...")
        time.sleep(3)
        os._exit(1)
    print_help()
    print("Start...tap help for more details.")

    # 领取离线奖励的线程
    thread1 = threading.Thread(target=shoucai_rountin, args=(hwnd,))
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
            shoucai(hwnd)
        elif  cmd_input == "tower":
            fuben_tower(hwnd)
        elif  cmd_input == "exit":
            print("Bye!")
            os._exit(1)