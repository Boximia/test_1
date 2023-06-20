import cv2
import numpy as np

def otsu_thresholding(image):
    # 将图像转换为灰度图
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # 使用大津法计算阈值
    _, threshold = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    return threshold

def iterative_thresholding(image, initial_threshold=127, max_iterations=100):
    # 将图像转换为灰度图
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # 迭代计算阈值
    threshold = initial_threshold
    for _ in range(max_iterations):
        # 分割图像
        _, binary_image = cv2.threshold(gray_image, threshold, 255, cv2.THRESH_BINARY)
        
        # 计算当前阈值下的前景和背景的平均灰度值
        foreground_mean = np.mean(gray_image[binary_image == 255])
        background_mean = np.mean(gray_image[binary_image == 0])
        
        # 更新阈值为前景和背景平均灰度值的均值
        new_threshold = int((foreground_mean + background_mean) / 2)
        
        # 如果新阈值与旧阈值相等，则停止迭代
        if new_threshold == threshold:
            break
        
        threshold = new_threshold
    
    return binary_image

# 读取图像
image = cv2.imread('test11.jpg')

# 使用大津法进行阈值分割
otsu_result = otsu_thresholding(image)

# 使用迭代法进行阈值分割
iterative_result = iterative_thresholding(image)

# 显示结果
cv2.imshow('Original Image', image)
cv2.imshow('Otsu Thresholding', otsu_result)
cv2.imshow('Iterative Thresholding', iterative_result)
cv2.waitKey(0)
cv2.destroyAllWindows()
