import os
from os import listdir
from os.path import isfile, join
import cv2
import numpy as np
import shutil
import pandas as pd

dir_name = os.getcwd() + '/images'
dir_name_empty = os.getcwd() + '/images_empty'
if not os.path.isdir(dir_name_empty):
    os.mkdir(dir_name_empty)
etalon_img_fname = 'litter_template_remove.jpg'
# data_etalon = open('litter_template_remove.jpg', 'rb').read()
data_etalon = cv2.imread(etalon_img_fname)
for f in listdir(dir_name):
    f_name = join(dir_name, f)
    if isfile(f_name):
        # data_cur = open(f_name, 'rb').read()
        data_cur = cv2.imread(f_name)
        if data_cur is None:
            continue
        if data_etalon.size != data_cur.size:
            continue
        difference = cv2.subtract(data_etalon, data_cur)
        if not np.any(difference):
            print("Moving file: " + f_name + " to " + dir_name_empty)
            shutil.move(f_name, join(dir_name_empty, f))
