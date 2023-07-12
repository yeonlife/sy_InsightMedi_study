from tkinter import *
from tkinter import filedialog
from dicom_file_function import file_find, file_upload
import tkinter.messagebox as mbox
import os
import shutil

window = Tk()

# 파일 path 입력 Entry
entry_filepath = Entry(window, width = 100)
entry_filepath.pack(fill = "x", padx = 1, pady=1)    # fill="x": 윈도우 창 폭에 맞추기, padx/pady: 위젯 사이 여백 pixel 값

# button frame
fr_bt = Frame(window)
fr_bt.pack(fill="x", padx=1, pady=1)

# upload/find button
btn_upload = Button(fr_bt, text = "Upload", width=10, command = file_upload(entry_filepath))
btn_upload.pack(side="left", padx = 1, pady=1)
btn_find = Button(fr_bt, text = "Find", width=10, command = file_find(entry_filepath))
btn_find.pack(side="left", padx=1, pady=1)

window.title('dicom_viewer')
window.mainloop()