import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("image/noise_img.jpg")

#print(gray_img.shape) --> (683,1024)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)



# Can make histogram for equalization with using dictionary

# value = {}
#
# for i in range(256):
#     value[i] = 0
#
# for i in range(h):
#     for j in range(w):
#         value[gray_img[i][j]]+=1

def equalization(image):

        h, w = image.shape
        bins, ranges = [256], [0,256]
        hist = cv2.calcHist([image], [0], None, bins, ranges)


        # Calculate the accumulated sum
        accum_sum = np.zeros(hist.shape, np.float32)
        accum_sum[0] = hist[0]

        for i in range(1,hist.shape[0]):
            accum_sum[i] = accum_sum[i-1] + hist[i]


        # Normalize by the total number of pixels
        Normalized_pixel = (accum_sum/(h*w))*255

        # Apply the equalization using Look Up Table
        processed_img = cv2.LUT(image, Normalized_pixel.astype("uint8"))

        return processed_img

processed_img = equalization(gray_img)

#Generate Histogram
original_hist,original_bins = np.histogram(gray_img.ravel(),256,[0,256])
processed_hist,processed_bins = np.histogram(processed_img.ravel(),256,[0,256])



fig, axes = plt.subplots(2, 2, figsize=(12, 8))
axes = axes.ravel()

# original image
axes[0].imshow(gray_img, cmap="gray")
axes[0].set_title("Original Grayscale Image")
axes[0].axis("off")

# processed image
axes[1].imshow(processed_img, cmap="gray")
axes[1].set_title("Processed Image")
axes[1].axis("off")


axes[2].plot(original_bins[:-1], original_hist, color="blue")
axes[2].set_title("Original Histogram")
axes[2].set_xlim([0, 256])


axes[3].plot(processed_bins[:-1], processed_hist, color="green")
axes[3].set_title("Processed Histogram")
axes[3].set_xlim([0, 256])

plt.tight_layout()
plt.show()
