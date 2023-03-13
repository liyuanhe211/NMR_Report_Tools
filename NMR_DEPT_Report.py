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
import pyperclip

print(
'''Read MestReNova DEPT peak able, give a DEPT report with + - labeled (Only compound type is listed). 
''')

digits = input("How many digits after decimal point (default 2): ")
if not digits:
    digits = 2
else:
    digits = int(digits)

print("Start to copy MestReNova DEPT peak table.\n")

clipboard_text = ""

while True:
    new_clipboard_text = pyperclip.paste()
    if new_clipboard_text != clipboard_text and new_clipboard_text.strip():
        clipboard_text = new_clipboard_text
        print("You copied:\n",clipboard_text)
        try:
            input_data = [x.split('\t') for x in clipboard_text.splitlines()]
            if 'ppm' not in input_data[0] or 'Intensity' not in input_data[0]:
                raise Exception()
            peaks = [line[input_data[0].index('ppm')] for line in input_data[1:]]
            intensities = [line[input_data[0].index('Intensity')] for line in input_data[1:]]
            type = [line[input_data[0].index('Type')] for line in input_data[1:]]
            annotation = [line[input_data[0].index('Flags')] for line in input_data[1:]]
            ret = ""
            for count,peak in enumerate(peaks):
                if type[count].strip()!='Compound' or 'None' not in annotation[count].strip():
                    print(type[count],annotation[count])
                    continue
                ret+=("{:."+str(digits)+"f}").format(float(peak))+' '+('(+)' if float(intensities[count])>0 else'(-)')+", "

            ret = ret.strip(', ') # + " ppm."
            print('--------------')
            print('Added to clipboard:')
            print(ret)
            print('--------------\n\n')
            pyperclip.copy(ret)
            clipboard_text = ret
        except Exception as e:
            print("\nDidn't get valid DEPT data on clipboard.")
            print('--------------\n\n')

    time.sleep(0.05)
