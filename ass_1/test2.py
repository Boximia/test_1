import cv2
import numpy as np

img = cv2.imread('jarc.jpg', cv2.IMREAD_COLOR)

# 图像中心点坐标
height, width = img.shape[:2]
center = (width / 2, height / 2)

# 获取旋转矩阵
rotate_mat = cv2.getRotationMatrix2D(center, 60, 1.0)

# 旋转图像
rotated_img = cv2.warpAffine(img, rotate_mat, (width, height))

# 显示图像
cv2.imshow('rotated image', rotated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
