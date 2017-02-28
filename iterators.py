#!/usr/bin/python3

import sys
#iterator


list = [10,20,30,40]
it = iter(list)

# for x in it:
#     if list[len(list)-1] == x:
#         print(x)
#     else:
#         print (x, end='')
#
# for x in list:
#     if list[len(list)-1] == x:
#         print(x)
#     else:
#         print (x, end='')

while True:
    try:
        print (next(it))
    except StopIteration:
        sys.exit()
