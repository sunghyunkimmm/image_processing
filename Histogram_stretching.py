import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("image/noise_img.jpg")

#print(gray_img.shape) --> (683,1024)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def search_value_idx(hist, bias = 0):
    for i in range(hist.shape[0]):
        idx = np.abs(bias - i)
        if hist[idx] > 0: return idx
    return -1

def stretching(image):

    bsize, ranges = [64], [0,256]
    hist = cv2.calcHist([image], [0], None, bsize, ranges)

    bin_width = ranges[1]/bsize[0]
    high =search_value_idx(hist, bsize[0]-1) * bin_width
    low = search_value_idx(hist, 0) * bin_width

    idx = np.arange(0, 256)
    idx = (idx - low) * 255/(high - low)
    idx[0:int(low)] = 0
    idx[int(high+1)] = 255

    processed_img = cv2.LUT(image, idx.astype('uint8'))

    return processed_img

processed_img = stretching(gray_img)


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

