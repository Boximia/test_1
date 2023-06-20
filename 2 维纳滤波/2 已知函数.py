import cv2
import numpy as np

def add_gaussian_noise(image, mean, stddev):
    noise = np.random.normal(mean, stddev, image.shape).astype(np.uint8)
    noisy_image = cv2.add(image, noise)
    return noisy_image

def wiener_filter(image, kernel, snr):
    # 计算输入图像的傅里叶变换
    image_fft = np.fft.fft2(image)
    # 计算卷积核的傅里叶变换
    kernel_fft = np.fft.fft2(kernel, s=image.shape)

    # 计算维纳滤波器的频域表示
    wiener_filter_fft = np.conj(kernel_fft) / (np.abs(kernel_fft) ** 2 + 1/snr)

    # 对输入图像进行频域滤波
    filtered_image_fft = image_fft * wiener_filter_fft

    # 计算滤波结果的空域表示
    filtered_image = np.fft.ifft2(filtered_image_fft).real

    return filtered_image

# 读取输入图像
image = cv2.imread('test11.jpg', 0)

# 设计一个高斯模糊卷积核
kernel_size = 15
sigma = 2.0
kernel = cv2.getGaussianKernel(kernel_size, sigma)

# 添加高斯噪声到输入图像
mean = 0
stddev = 10
noisy_image = add_gaussian_noise(image, mean, stddev)

# 已知信噪比
known_snr = 30.0

# 应用维纳滤波
filtered_image = wiener_filter(noisy_image, kernel, known_snr)

# 显示结果
cv2.imshow('Noisy Image', noisy_image)
cv2.imshow('Filtered Image', filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
