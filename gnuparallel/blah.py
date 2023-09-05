#!/usr/bin/env python3

from __future__ import print_function, division

import sys
import time
import datetime

if __name__ == '__main__':
    now = datetime.datetime.now()
    print(now.strftime('%H:%M:%S'))

    time.sleep(int(sys.argv[1]))

    now = datetime.datetime.now()
    print(now.strftime('%H:%M:%S'))
