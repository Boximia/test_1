# -- coding: utf-8 --
import cv2
import matplotlib.pyplot as plt
import numpy as np
from math import log10
img=cv2.imread("gwl.jpg",0)

# 获取图像高度和宽度
height = img.shape[0]
width = img.shape[1]

#创建一幅图像， uint8是专门用于存储各种图像的（包括RGB，灰度图像等），范围是从0–255
result = np.zeros((height, width), np.uint8)
result1 = np.zeros((height, width), np.uint8)
# 图像灰度反转
for i in range(height):
    for j in range(width):
        if (img[i, j])+50>255:
            gray = 255
        else:
            gray = (img[i, j])+50
        result[i, j] = np.uint8(gray)

# 显示图形
plt.figure(num='comparison')
titles = ['gray Image', 'brightness increased']
images = [img, result]
for i in range(2):
    plt.subplot(1, 2, i + 1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()
