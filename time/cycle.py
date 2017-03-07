from datetime import datetime
from time import sleep
import unittest

def cycle(val, int):

    dsoc_mock = val
    time_start = datetime.now()
    time_diff = 0

    while dsoc_mock != 0:

        time_now = datetime.now()
        time_diff = (time_now - time_start).seconds
        print('dsoc_mock is: {0} and loop is running for {1}sec'.format(dsoc_mock, time_diff))
        if time_diff % 2 == 0:
            dsoc_mock -= 1
        # self.assertEqual(dsoc_mock, 2)
        sleep(int)

    print('dsoc_mock is: {} and loop stopped'.format(dsoc_mock))

if __name__ == '__main__':
    cycle(8, 4)
    # unittest.main()
