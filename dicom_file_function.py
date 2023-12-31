from tkinter import *
from tkinter import filedialog
import PIL
from PIL import Image, ImageTk
import pydicom
import os
import shutil
import numpy as np
import tkinter.messagebox as mbox
from pydicom.pixel_data_handlers.util import apply_modality_lut, apply_voi_lut

dcm_ext = r"*.dcm *.DCM"
mp4_ext = r"*.mp4"

def file_find(entry_filepath):
    file = filedialog.askopenfilenames(filetypes = (("DCM file", dcm_ext), ("mp4 file", mp4_ext), ("all file", "*.*")), initialdir=r"C:\Users")
    entry_filepath.delete(0,'end')
    entry_filepath.insert('end', file[0])

def file_upload(entry_filepath):
    if len(entry_filepath.get()) == 0:
        mbox.showinfo("warning", "select file, please")
        return
    else:
        file_name = os.path.basename(entry_filepath.get())
        dest_path = os.path.join("D:\\", file_name)
        shutil.copy(entry_filepath.get(), dest_path)
        entry_filepath.delete(0,'end')
        return