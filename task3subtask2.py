import numpy as np
import cv2
import matplotlib.pyplot as plt
import copy
img=cv2.imread('shapes.jpg')
out=img.copy()

Red=np.array([0,0,255])
Black=np.array([0,0,0])
Blue=np.array([255,0,0])

lower_red=np.array([0,0,200])
upper_red=np.array([50,50,255])
mask_red=np.all((img>=lower_red)&(img<=upper_red),axis=2).astype(np.uint8)*255
out[mask_red>0]=Blue

lower_black=np.array([0,0,0])
upper_black=np.array([50,50,50])
mask_black=np.all((img>=lower_black)&(img<=upper_black),axis=2).astype(np.uint8)*255
out[mask_black>0]=Red

lower_blue=np.array([200,0,0])
upper_blue=np.array([255,50,50])
mask_blue=np.all((img>=lower_blue)&(img<=upper_blue),axis=2).astype(np.uint8)*255
out[mask_blue>0]=Black

fig, axes = plt.subplots(1, 2)
axes[0].imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
axes[0].set_title('Original Image')
axes[0].axis('off')
axes[1].imshow(cv2.cvtColor(out,cv2.COLOR_BGR2RGB))
axes[1].set_title('Processed Image')
axes[1].axis('off')
plt.show()
