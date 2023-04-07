import cv2
import numpy as np

# 读取图片
img = cv2.imread('jarc.jpg',cv2.IMREAD_UNCHANGED)

# 定义平移矩阵，向右平移100像素，向下平移50像素
M = np.float32([[1, 0, 100], [0, 1, 50]])

# 执行平移操作
shifted = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))

# 显示图片
cv2.imshow('shifted image', shifted)
cv2.waitKey(0)
cv2.destroyAllWindows()
