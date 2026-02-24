# ===================================================================

# Example : save an image from file (and invert it)

# Author : Amir Atapour Abarghouei, amir.atapour-abarghouei@durham.ac.uk

# Copyright (c) 2024 Amir Atapour Abarghouei

# based on : https://github.com/tobybreckon/python-examples-ip/blob/master/skeleton.py
# License : LGPL - http://www.gnu.org/licenses/lgpl.html

# ===================================================================

import cv2

# ===================================================================

# read an image from the specified file (in colour)

img = cv2.imread('peppers.png', cv2.IMREAD_COLOR)

# check it has loaded

if not img is None:

    print("Processing and saving image.")

    # performing logical inversion - see OpenCV Manual entry for bitwise_not()

    inverted = cv2.bitwise_not(img)

    # write inverted image to file

    #cv2.imwrite("inverted-peppers.png", inverted)

    #cv2.imwrite("inverted-peppers.bmp", inverted)
    #cv2.imwrite("inverted-peppers.tiff", inverted)

    cv2.imwrite("inverted-peppers-quality5.jpg", inverted, (cv2.IMWRITE_JPEG_QUALITY, 5))
    cv2.imwrite("inverted-peppers-quality95.jpg", inverted, (cv2.IMWRITE_JPEG_QUALITY, 95))

    cv2.imwrite("inverted-peppers-compression9.png", inverted, (cv2.IMWRITE_PNG_COMPRESSION, 9))
    cv2.imwrite("inverted-peppers-compression0.png", inverted, (cv2.IMWRITE_PNG_COMPRESSION, 0))

    cv2.imwrite("inverted.jpg", inverted)
    cv2.imwrite("inverted.png", inverted)

else:
    print("No image file was loaded.")

# ===================================================================

inverted = cv2.imread('inverted.jpg', cv2.IMREAD_COLOR)
inverted_png = cv2.imread('inverted.png', cv2.IMREAD_COLOR)

inverted_back = cv2.bitwise_not(inverted)
cv2.imwrite("inverted_back.jpg", inverted_back)

inverted_back_png = cv2.bitwise_not(inverted_png)
cv2.imwrite("inverted_back.png", inverted_back_png)

diff_jpg = cv2.absdiff(inverted_back, img)
diff_png = cv2.absdiff(inverted_back_png, img)

diff_jpg = diff_jpg * 255 / diff_jpg.max()
diff_png = diff_png * 255 / diff_png.max()

cv2.imshow("diff (jpg)", diff_jpg)
cv2.imshow("diff (png)", diff_png)

cv2.waitKey(0)

