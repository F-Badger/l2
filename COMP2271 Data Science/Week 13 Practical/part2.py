import cv2

img =  cv2.imread('peppers.png', cv2.IMREAD_COLOR)

du_logo = cv2.imread("DULogo.png", cv2.IMREAD_COLOR)

mask = cv2.imread("DULogoMask.png", cv2.IMREAD_COLOR)

mask_height, mask_width = mask.shape[:2]

just_logo = cv2.bitwise_xor(du_logo, mask)

img[0:mask_height, 0:mask_width] = cv2.bitwise_and(img[0:mask_height, 0:mask_width], mask)
img[0:mask_height, 0:mask_width] = cv2.bitwise_xor(img[0:mask_height, 0:mask_width], just_logo)

cv2.imshow("Image with logo", img)
cv2.waitKey(0)