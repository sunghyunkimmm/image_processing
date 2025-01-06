import cv2
import numpy as np
import matplotlib.pyplot as plt
from Histogram_stretching import stretching
from equalization import equalization

img = cv2.imread("image/noise_img.jpg")

#print(gray_img.shape) --> (683,1024)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

stretched_img = stretching(gray_img)
equalized_img = equalization(gray_img)


fig, axes = plt.subplots(2, 2, figsize=(12, 8))
axes = axes.ravel()


#Generate Histogram
stretched_hist,stretched_bins = np.histogram(stretched_img.ravel(),256,[0,256])
equalized_hist,equalized_bins = np.histogram(equalized_img.ravel(),256,[0,256])

# original image
axes[0].imshow(stretched_img, cmap="gray")
axes[0].set_title("stretched_image")
axes[0].axis("off")

# processed image
axes[1].imshow(equalized_img, cmap="gray")
axes[1].set_title("equalized_image")
axes[1].axis("off")


axes[2].plot(stretched_bins[:-1], stretched_hist, color="blue")
axes[2].set_title("stretched_image")
axes[2].set_xlim([0, 256])


axes[3].plot(equalized_bins[:-1], equalized_hist, color="green")
axes[3].set_title("equalized_image")
axes[3].set_xlim([0, 256])

plt.tight_layout()
plt.show()