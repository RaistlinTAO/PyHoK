# -*- coding: utf-8 -*-


import logging
import os
from time import sleep

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
    os.system('adb -s vsq4eyaq8lfy8hd6 shell input tap {} {}'.format(x, y))


def do_money_work():
    #logging.debug('***Start***')
    tap_screen(1650, 877)
    sleep(1)
    tap_screen(2099, 1077)
    sleep(1)
    tap_screen(1960, 1000)
    sleep(1)


if __name__ == '__main__':
    for i in range(repeat_times):
        logging.info('Initial Count: #{}'.format(i + 1))
        do_money_work()
