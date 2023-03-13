# -*- coding: utf-8 -*-

"""
有些老师觉得13C-NMR只应有一位有效数字，但机械转化为一位有效数字时会有看起来重复的信号（报告形如”81.3, 49.9, 49.9, 18.0“）
此时又有些老师认为不应该出现重复的数字表示不同的峰，要在重复数字之后标明重复峰的具体值（形如”81.3, 49.9 (49.96), 49.9 (49.98), 18.0“）
我认为这纯粹是浪费时间多此一举。经过重复实验，碳谱本来就能精确到0.01 ppm。
但为了满足这些人的需求，写这脚本实现从小数点后两位到小数点后一位的转化

使用方法：
将英文逗号分割的数字复制进剪切板，如：54.38, 54.11, 53.84, 53.57, 53.30, 44.48, 44.46, 38.57, 36.62, 28.47, 25.37, 12.82
直接粘贴，就是对的：54.4, 54.1, 53.8, 53.6, 53.3, 44.5 (44.48), 44.5 (44.46), 38.6, 36.6, 28.5, 25.4, 12.8

"""

__author__ = 'LiYuanhe'

import pyperclip
import time


def is_float(input_str):
    # 确定字符串可以转换为float
    try:
        float(input_str)
        return True
    except ValueError:
        return False


formatted = lambda x: "{:.1f}".format(float(x))

clipboard_text = ""

print("Copy comma-separated floating point numbers to the clipboard\n"
      "    e.g. 54.38, 54.11, 53.84, 53.57, 53.30, 44.48, 44.46, 38.57, 36.62, 28.47, 25.37, 12.82\n"
      "Then paste to get:\n"
      "    54.4, 54.1, 53.8, 53.6, 53.3, 44.5 (44.48), 44.5 (44.46), 38.6, 36.6, 28.5, 25.4, 12.8\n"
      "\n"
      "Monitor start...\n")

while True:
    new_clipboard_text = pyperclip.paste()
    if new_clipboard_text != clipboard_text and new_clipboard_text:
        clipboard_text = new_clipboard_text
        comma_split = [x.strip() for x in clipboard_text.split(',')]
        if all([is_float(x) for x in comma_split]):
            comma_split = [float(x) for x in comma_split]
            ret = []
            for count, i in enumerate(comma_split):
                new_number = None
                if count > 0:
                    if formatted(i) == formatted(comma_split[count - 1]):
                        new_number = formatted(i) + " ({:.2f})".format(i)
                        new_number
                if count < len(comma_split) - 2:
                    if formatted(i) == formatted(comma_split[count + 1]):
                        new_number = formatted(i) + " ({:.2f})".format(i)
                if new_number is None:
                    new_number = formatted(i)
                ret.append(new_number)
            ret = ", ".join(ret)
            print(ret)
            print("----------------------")
            pyperclip.copy(ret)
            clipboard_text = ret
        else:
            print("Illegal input, the input should be floating point number splitted by comma and spaces.")
            print("----------------------")

    # Wait for a short amount of time before checking the clipboard again
    time.sleep(0.05)
