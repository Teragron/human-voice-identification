# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 17:47:18 2021

@author: ahmet
"""

from PIL import Image
import os, os.path

mat_cs = "matrix/cs/cs{}.png"
mat_mert = "matrix/mert/mert{}.png"
mat_ortak = "matrix/ortak/ortak{}.png"
# mat_harry = "matrix/harry/harry{}.png"
# mat_kit = "matrix/kit/kit{}.png"
boyut = 224,224

DIR1 = 'matrix/cs'
DIR2 = 'matrix/mert'
DIR3 = "matrix/ortak"
# DIR3 = 'matrix/harry'
# DIR4 = 'matrix/kit'

l1 = len([name for name in os.listdir(DIR1) if os.path.isfile(os.path.join(DIR1, name))])
l2 = len([name for name in os.listdir(DIR2) if os.path.isfile(os.path.join(DIR2, name))])
l3 = len([name for name in os.listdir(DIR3) if os.path.isfile(os.path.join(DIR3, name))])
# l4 = len([name for name in os.listdir(DIR4) if os.path.isfile(os.path.join(DIR4, name))])

# image1 = Image.open("cs_trimmed1.png")
# new_image1 = image1.resize((boyut))
# new_image1.save("cs_resized.png")

for i in range(0,l1):
  image1 = Image.open(mat_cs.format(i))
  width1, height1 = image1.size
  print(width1, height1)
  print(int(i+1))
  new_image1 = image1.resize((boyut))
  new_image1.save(mat_cs.format(i))

print("---------------------------------------------------------------")
for j in range(0,l2):
  image2 = Image.open(mat_mert.format(j))
  width2, height2 = image2.size
  print(width2, height2)
  print(int(j+1))
  new_image2 = image2.resize((boyut))
  new_image2.save(mat_mert.format(j))
  
# print("---------------------------------------------------------------")

# for k in range(0,l3):
#   image3 = Image.open(mat_harry.format(k))
#   width3, height3 = image3.size
#   print(width3, height3)
#   print(int(k+1))
#   new_image3 = image3.resize((boyut))
#   new_image3.save(mat_harry.format(k))
  
# print("---------------------------------------------------------------")

# for l in range(0,l4):
#   image4 = Image.open(mat_kit.format(l))
#   width4, height4 = image4.size
#   print(width4, height4)
#   print(int(l+1))
#   new_image4 = image4.resize((boyut))
#   new_image4.save(mat_kit.format(l))