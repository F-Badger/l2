# ===================================================================
# Example : reading, displaying and smoothing an image

# Author : Amir Atapour Abarghouei, amir.atapour-abarghouei@durham.ac.uk

# Copyright (c) 2024 Amir Atapour Abarghouei

# License : LGPL - http://www.gnu.org/licenses/lgpl.html
# ===================================================================
import cv2
# ===================================================================

# define display window name

windowName = "Original Image" # window name - for the original image
windowName2 = "5x5 Mask" # window name 2 - for the smoothed image
windowName3 = "15x15 Mask" # window name 3 - for the smoothed image
windowName4 = "3x3 Mask"
windowName5 = "Flip"
windowName6 = "Canny"
windowName7 = "Resize 50%"
windowName8 = "Resize 200%"
windowName9 = "Resize 150%, Inter_nearest"
windowName10 = "Resize 150%, Inter_linear"

# read an image from the specified file - the cv2.IMREAD_COLOR flag enables reading the image in colour

image = cv2.imread('./peppers.png', cv2.IMREAD_COLOR)

# check that the image has been successfully loaded

if not image is None:

    # performing smoothing on the image using a 5x5 smoothing mark (see manual entry for GaussianBlur())

    blur = cv2.GaussianBlur(image,(5,5),0)
    blur2 = cv2.GaussianBlur(image,(15,15),0)
    blur3 = cv2.GaussianBlur(image,(3,3),0)

    flip = cv2.flip(image, 1) # flip the image horizontally``

    grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # convert the image to grayscale

    canny = cv2.Canny(grey, 10, 200) # perform Canny edge detection on the grayscale image

    resize1 = cv2.resize(image, (0,0), fx=0.5, fy=0.5) # resize the image to 50% of its original size
    resize2 = cv2.resize(image, (0,0), fx=2, fy=2) # resize the image to 200% of its original size
    resize3 = cv2.resize(image, (0,0), fx=1.5, fy=1.5, interpolation=cv2.INTER_NEAREST) # resize the image to 150% of its original size using nearest neighbour
    resize4 = cv2.resize(image, (0,0), fx=1.5, fy=1.5, interpolation=cv2.INTER_LINEAR) # resize the image to 150% of its original size using linear interpolation

    # display the original image and this blurred image in named windows

    cv2.imshow(windowName, image)
    cv2.imshow(windowName2, blur)
    cv2.imshow(windowName3, blur2)
    cv2.imshow(windowName4, blur3)

    cv2.imshow(windowName5, flip)

    cv2.imshow(windowName6, canny)

    cv2.imshow(windowName7, resize1)
    cv2.imshow(windowName8, resize2)
    cv2.imshow(windowName9, resize3)
    cv2.imshow(windowName10, resize4)

    # start the event loop - essential

    # cv2.waitKey() is a keyboard binding function (argument is the time in milliseconds).
    # It waits for specified milliseconds foxr any keyboard event.
    # If you press any key in that time, the program continues.
    # If 0 is passed, it waits indefinitely for a key stroke.

    key = cv2.waitKey(0) # wait

    # It can also be set to detect specific key strokes by recording which key is pressed

    # e.g. if user presses "x" then exit and close all windows

    if (key == ord('x')):
        cv2.destroyAllWindows()
else:
    print("No image file was loaded.")
# ===================================================================
