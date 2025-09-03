import numpy as np
from scipy.ndimage import median_filter,gaussian_filter
import matplotlib.pyplot as plt
import cv2

def convolve(image,kernel):
    flip=np.flipud(np.fliplr(kernel))
    pad_h=np.size(kernel,0)
    pad_w=np.size(kernel,1)
    pad=np.pad(image,((pad_h,pad_h),(pad_w,pad_w)), mode='constant',constant_values=0)
    value=np.zeros_like(image,dtype=float)

    for i in range(np.size(image,0)):
        for j in range (np.size(image,1)):
            frame=pad[i:i+np.size(kernel,0),j:j+np.size(kernel,1)]
            value[i,j]=np.sum(frame*flip)
    return value

img = cv2.imread('image.png', cv2.IMREAD_GRAYSCALE)
fig, axes = plt.subplots(3, 2, figsize=(10, 12))

axes[0, 0].imshow(img, cmap = 'gray')
axes[0, 0].set_title('Original Image')
axes[0, 0].axis('off')

axes[0, 1].imshow(convolve(img, np.ones((5, 5)) / 25), cmap = 'gray')
axes[0, 1].set_title('Box Filter')
axes[0, 1].axis('off')

axes[1, 0].imshow(convolve(img, np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])), cmap = 'gray')
axes[1, 0].set_title('Horizontal Sobel Filter')
axes[1, 0].axis('off')

axes[1, 1].imshow(convolve(img, np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])), cmap = 'gray')
axes[1, 1].set_title('Vertical Sobel Filter')
axes[1, 1].axis('off')

img_gauss=gaussian_filter(img,sigma=5)
axes[2, 0].imshow(img_gauss, cmap = 'gray')
axes[2, 0].set_title('gaussian Image')
axes[2, 0].axis('off')

img_median=median_filter(img,size=3)
axes[2, 1].imshow(img_median, cmap = 'gray')
axes[2, 1].set_title('median Image')
axes[2, 1].axis('off')

plt.tight_layout()
plt.show()