# -*- coding: utf-8 -*-
__author__ = 'LiYuanhe'

import os
import shutil

import PyInstaller.__main__

version = "C13_2Digits_to_1Digit"
main_py_file = 'C13_2Digits_to_1Digit.py'
path = 'Pyinstaller_Packing'
work_path = os.path.join(path, f'temp_{version}')
output_path = os.path.join(path, version)
generated_exe_name = f"C13 2 Digits to 1 Digit.exe"
include_all_folder_contents = []
include_files = []
include_folders = []

PyInstaller.__main__.run([main_py_file,
                          "--name", generated_exe_name,
                          "--workpath", work_path,
                          "--distpath", output_path,
                          '--onefile',
                          '--clean'])


def copy_folder(src, dst):
    """

    :param src:
    :param dst: dst will *contain* src folder
    :return:
    """
    target = os.path.realpath(os.path.join(dst, filename_class(src).name))
    if os.path.isdir(target):
        # input('Confirm delete: '+target+" >>>")
        try:
            shutil.rmtree(target)
            print("Deleting:", target)
        except Exception:
            print("Delete Failed:", target)
            return None
    print("Copying:", src, 'to', dst)
    shutil.copytree(src, target)


generated_folder_name = output_path

for file in include_files:
    print(f"Copying {file} to {generated_folder_name}")
    shutil.copy(file, generated_folder_name)

for folder in include_folders:
    copy_folder(folder, generated_folder_name)

for folder in include_all_folder_contents:
    target = os.path.realpath(os.path.join(generated_folder_name, filename_class(folder).name))
    for current_object in os.listdir(folder):
        current_object = os.path.join(folder, current_object)
        if os.path.isfile(current_object):
            shutil.copy(current_object, generated_folder_name)
        else:
            copy_folder(current_object, generated_folder_name)

with open(os.path.join(generated_folder_name, 'Use this script to capture the error message if the program crashes.bat'), 'w') as crash_bat:
    crash_bat.write(f'"{generated_exe_name}"\npause\n')

# open_explorer_and_select(os.path.realpath(generated_folder_name))
