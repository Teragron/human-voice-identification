# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 00:26:24 2021

@author: ahmet
"""

from fastai.vision.all import *

path = Path("matrix/")
fnames = get_image_files(path)
print(f"Total Images: {len(fnames)}")
def label_func(x): return x.parent.name
dls = ImageDataLoaders.from_path_func(path, fnames, label_func, bs=32)

dls.valid.show_batch(max_n=6, nrows=1)