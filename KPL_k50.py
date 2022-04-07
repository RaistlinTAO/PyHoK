# -*- coding: utf-8 -*-


import logging
import os
from time import sleep

# 屏幕分辨率
device_x, device_y = 1520, 720
#2400 1080

# 通关模式：1=重新挑战 -> 挑战界面，2=重新挑战-> 更换阵容
game_mode = 2

# 各步骤等待间隔
step_wait = [3, 16, 35, 5, 3]

# 刷金币次数
repeat_times = 60000

# 日志输出
logging.basicConfig(format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.DEBUG)


def tap_screen(x, y):
    os.system('adb -s 8e610fd shell input tap {} {}'.format(x, y))


def do_money_work():
    #logging.debug('***Start***')
    #红包入口
    #tap_screen(998, 1945)
    tap_screen(998, 2087)
    sleep(1)
    #开红包
    tap_screen(540, 1386)
    sleep(0.5)
    #???
    tap_screen(550, 1530)
    sleep(0.5)
    #关闭红包页面
    tap_screen(780, 880)
    sleep(1)
    #????
    tap_screen(540, 1630)
    sleep(0.5)

if __name__ == '__main__':
    for i in range(repeat_times):
        logging.info('Initial Count: #{}'.format(i + 1))
        do_money_work()
