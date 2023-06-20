# -- coding: utf-8 --
import cv2
import matplotlib.pyplot as plt
import numpy as np
img=cv2.imread("gwl.jpg",0)

img=np.double(img)
result=img**2
result= np.uint8(result*255/np.max(result))
print(result)

plt.figure(num='comparison')
titles = ['gray Image', 'r=2']
images = [img, result]
for i in range(2):
    plt.subplot(1, 2, i + 1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()




