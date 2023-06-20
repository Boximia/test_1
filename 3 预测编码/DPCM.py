import numpy as np
import matplotlib.pyplot as plt
from skimage import io
from skimage.metrics import peak_signal_noise_ratio as psnr
from skimage.metrics import structural_similarity as ssim

def dpcm_encode(image, quantization_bits):
    # 将图像转换为灰度图
    gray_image = image.mean(axis=2)

    # 对灰度图进行差分编码
    diff = np.diff(gray_image, axis=1)

    # 对差分图像进行量化
    quantization_levels = 2 ** quantization_bits
    quantized_diff = np.round(diff * (quantization_levels - 1)) / (quantization_levels - 1)

    return quantized_diff

def dpcm_decode(quantized_diff, quantization_bits):
    quantization_levels = 2 ** quantization_bits

    # 对量化后的差分图像进行解码
    diff = quantized_diff * (quantization_levels - 1)

    # 恢复原始图像
    decoded_image = np.zeros((diff.shape[0], diff.shape[1] + 1))
    decoded_image[:, 0] = diff[:, 0]
    for i in range(1, diff.shape[1]):
        decoded_image[:, i] = decoded_image[:, i-1] + diff[:, i]

    # 转换为uint8类型
    decoded_image = np.clip(decoded_image, 0, 255).astype(np.uint8)

    return decoded_image

# 读取图像
image = io.imread('test11.jpg')

# 设置量化器的位数
quantization_bits_list = [1, 2, 4, 8]

# 对每个量化器进行编码和解码，并计算PSNR和SSIM值
for quantization_bits in quantization_bits_list:
    # 编码
    encoded_diff = dpcm_encode(image, quantization_bits)

    # 解码
    decoded_image = dpcm_decode(encoded_diff, quantization_bits)

    # 计算PSNR和SSIM值
    # psnr_value = psnr(image, decoded_image)
    # ssim_value = ssim(image, decoded_image, data_range=decoded_image.max() - decoded_image.min())

    # 显示解码后的图像及其PSNR和SSIM值
    plt.figure()
    plt.imshow(decoded_image, cmap='gray')
    # plt.title(f'Quantization bits: {quantization_bits}\nPSNR: {psnr_value:.2f}, SSIM: {ssim_value:.2f}')
    plt.axis('off')

plt.show()
