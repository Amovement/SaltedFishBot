# -*- coding: utf-8 -*-
# Author:       Amove

import win32gui
import win32con
import win32api
import time


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
    lParam = win32api.MAKELONG(x, y)
    count = 0
    while True:
        if count>=cnt:
            break
        time.sleep(0.2)
        win32api.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam)
        win32api.SendMessage(hwnd, win32con.WM_LBUTTONUP, 0, lParam)
        count+=1