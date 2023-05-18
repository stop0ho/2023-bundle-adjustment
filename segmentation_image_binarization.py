import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('img/sample9.jpg', 0)

hist, bin_edges = np.histogram(image, bins=256)

plt.figure(figsize=(14, 5))
plt.subplot(121)
plt.imshow(image, cmap='gray')
plt.title('original image', fontsize=15)
plt.xticks([])
plt.yticks([])

plt.subplot(122), plt.plot(hist), plt.title('Histogram', fontsize=15)

weight1 = np.cumsum(hist)
weight2 = np.cumsum(hist[::-1])[::-1]

bin_mids = (bin_edges[:-1] + bin_edges[1:]) / 2.

mean1 = np.cumsum(hist * bin_mids) / weight1
mean2 = (np.cumsum((hist * bin_mids)[::-1]) / weight2[::-1])[::-1]

inter_class_variance = weight1[:-1] * \
    weight2[1:] * (mean1[:-1] - mean2[1:]) ** 2
index_of_max_val = np.argmax(inter_class_variance)

threshold = bin_mids[:-1][index_of_max_val]

print("Otsu's algorithm implementation thresholding result: ", threshold)


# Plotting weight and between-class variance
plt.figure(figsize=(14, 5))
plt.subplot(121)
plt.plot(weight1)
plt.plot(weight2)
plt.title('Weight profiles', fontsize=15)
plt.xlabel('pixel values'), plt.ylabel('weight')

plt.subplot(122)
plt.plot(inter_class_variance)
plt.title('Between-class variance', fontsize=15)
plt.xlabel('pixel values'), plt.ylabel('variance')

otsu_threshold, image_result = cv2.threshold(
    image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
print(otsu_threshold)


maxValue = 255
th, dst = cv2.threshold(image, otsu_threshold, maxValue, cv2.THRESH_BINARY)

plt.figure(figsize=(14, 5))
plt.subplot(121)
plt.imshow(image, cmap='gray')
plt.title('original image', fontsize=15)
plt.xticks([]), plt.yticks([])

plt.subplot(122)
plt.imshow(dst, cmap='gray')
plt.title('filtered image', fontsize=15)
plt.xticks([]), plt.yticks([])

plt.show()
