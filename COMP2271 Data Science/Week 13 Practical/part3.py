import cv2
from matplotlib.pylab import gamma

img = cv2.imread('peppers.png', cv2.IMREAD_COLOR)

img = img / max(img.flatten())

img_gamma_third = img ** (1/3)

img_gamma_three = img ** 3

cv2.imshow("Original", img)
cv2.imshow("Gamma = 1/3", img_gamma_third)
cv2.imshow("Gamma = 3", img_gamma_three)
cv2.waitKey(0)