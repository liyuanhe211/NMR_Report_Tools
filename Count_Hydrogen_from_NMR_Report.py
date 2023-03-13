# -*- coding: utf-8 -*-
__author__ = 'LiYuanhe'

import sys
import os
import math
import copy
import shutil
import re
import time
import random

if __name__ == '__main__':
    while True:
        a=input("Copy NMR report here:")
        re_ret = re.findall(r'(\d+)H\)',a)
        print(sum([int(x) for x in re_ret]))