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

from pathlib import Path

path = r"C:\Users\LiYuanhe\Desktop\LYH-16-42-B-Pure"
path = Path(path)

for i in path.glob(r"**\*"):
    if i.is_file():
        try:
            i_content = open(str(i)).read()
        except:
            continue
        with open(str(i),'w') as output_file:
            output_file.write(i_content.replace('LYH-16-42-B-Pure',"LYH-17-42-B-Pure"))