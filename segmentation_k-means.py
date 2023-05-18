import numpy as np
import os
import cv2
import matplotlib.pyplot as plt


class k_means:
    def __init__(self):
        original_image = cv2.imread("img/sample9.jpg")
        self.img = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)
        self.vectorized = self.img.reshape((-1, 3))
        self.vectorized = np.float32(self.vectorized)

    def process(self, K):
        criteria = (cv2.TERM_CRITERIA_EPS +
                    cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)

        attempts = 10
        ret, label, center = cv2.kmeans(self.vectorized, K, None, criteria, attempts,
                                        cv2.KMEANS_PP_CENTERS)

        center = np.uint8(center)
        res = center[label.flatten()]
        self.result_image = res.reshape((self.img.shape))

        figure_size = 15
        plt.figure(figsize=(figure_size, figure_size))
        plt.subplot(1, 2, 1), plt.imshow(self.img)
        plt.title('Original Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(1, 2, 2), plt.imshow(self.result_image)
        plt.title('Segmented Image when K = %i' %
                  K), plt.xticks([]), plt.yticks([])
        plt.show()


img = cv2.imread('img/sample9.jpg')
Z = img.reshape((-1, 3))
# convert to np.float32
Z = np.float32(Z)
# define criteria, number of clusters(K) and apply kmeans()
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 16
ret, label, center = cv2.kmeans(
    Z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
# Now convert back into uint8, and make original image
center = np.uint8(center)
res = center[label.flatten()]
res2 = res.reshape((img.shape))

cv2.imshow('res2', res2)
cv2.waitKey(0)
cv2.destroyAllWindows()
