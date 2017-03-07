#!/usr/bin/python

from datetime import datetime
from time import sleep

def l_cycle(per, int):
    period = per
    time_start = datetime.now()
    time_diff = 0
    while time_diff != period:
        time_now = datetime.now()
        time_diff = (time_now - time_start).seconds
        print('lopp is running {}secs'.format(time_diff))
        sleep(int)
    print('loop run for {}secs'.format(time_diff))


if __name__ == '__main__':
    l_cycle(10, 2)
