import cv2
import numpy as np

# 读取图片
img = cv2.imread('jarc.jpg', cv2.IMREAD_UNCHANGED)

# 水平镜像
h_flipped = cv2.flip(img, 1)

# 垂直镜像
v_flipped = cv2.flip(img, 0)

# 水平垂直镜像
hv_flipped = cv2.flip(img, -1)

# 显示图片
cv2.imshow('horizontal flipped image', h_flipped)
cv2.imshow('vertical flipped image', v_flipped)
cv2.imshow('horizontal and vertical flipped image', hv_flipped)
cv2.waitKey(0)
cv2.destroyAllWindows()
