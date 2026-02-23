# ===================================================================
# Example : reading, displaying and interacting with an image

# Author : Amir Atapour Abarghouei, amir.atapour-abarghouei@durham.ac.uk

# Copyright (c) 2024 Amir Atapour Abarghouei

# License : LGPL - http://www.gnu.org/licenses/lgpl.html
# ===================================================================
import cv2
# ===================================================================

# mouse callback function - displays or sets image colour at the click
# location of the mouse

def colour_query_mouse_callback(event, x, y, flags, param):

    # records mouse events at postion (x,y) in the image window

    # left button click prints colour information at click location to stdout

    if event == cv2.EVENT_LBUTTONDOWN:
        # f-string is used here, which only works for python3 : https://realpython.com/python-f-strings/
        print(f"BGR colour at position ({x},{y}) = ({','.join(str(i) for i in image[y,x])})")

    # right button sets colour information at click location to white

    elif event == cv2.EVENT_RBUTTONDOWN:
        roi = image[y-50:y+50,x-50:x+50] # define a region of interest (ROI) around the click location
        windowNameROI = "ROI"
        cv2.imshow(windowNameROI, roi) # display the ROI in a named window


        #color = [255,255,255]  # change to white
        #color = [0,0,0]  # change to black
        #color = [0,0,225]  # change to red
        #color = [0,255,0]  # change to green
        #color = [255,0,0]  # change to blue
        #color = [220,220,220]  # change to light grey
        #color = [110,110,110]  # change to dark grey
        #color = [0,255,255]  # change to yellow
        colour = [255,0,255]  # change to purple
        image[y-2:y+3,x-2:x+3] = colour

def colour_query_mouse_callback_gray(event, x, y, flags, param):

    # records mouse events at postion (x,y) in the image window

    # left button click prints colour information at click location to stdout

    if event == cv2.EVENT_LBUTTONDOWN:
        # f-string is used here, which only works for python3 : https://realpython.com/python-f-strings/
        print(f"Grayscale value at position ({x},{y}) = {imageGray[y,x]}")

        topLeft = (x-50, y+50)
        bottomRight = (x+50, y-50)

        cv2.rectangle(imageGray, topLeft, bottomRight, (255,0,0), 2) # draw a red rectangle around the click location

# ===================================================================

# define display window name

windowName = "Displayed Image" # window name - for the displayed image
windowNameGray = "Displayed Image in Grayscale" # window name - for the displayed image in grayscale

# read an image from the specified file - the cv2.IMREAD_COLOR flag enables reading the image in colour

image = cv2.imread('./peppers.png', cv2.IMREAD_COLOR)
imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # convert the image to grayscale

# check that the image has been successfully loaded

if not image is None:

    # create a named window object

    cv2.namedWindow(windowName)
    cv2.namedWindow(windowNameGray)

    # set the mouse call back function that will be called every time
    # the mouse is clicked inside the associated window

    cv2.setMouseCallback(windowName,colour_query_mouse_callback)
    cv2.setMouseCallback(windowNameGray,colour_query_mouse_callback_gray)

    # set a loop control flag

    keep_processing = True

    while (keep_processing):

        # display this blurred image in a named window

        cv2.imshow(windowName, image)
        cv2.imshow(windowNameGray, imageGray)

        # start the event loop - essential

        # cv2.waitKey() is a keyboard binding function (argument is the time in milliseconds).
        # It waits for specified milliseconds for any keyboard event.
        # If you press any key in that time, the program continues.
        # If 0 is passed, it waits indefinitely for a key stroke.
        # (bitwise and with 0xFF to extract least significant byte of multi-byte response)

        key = cv2.waitKey(40) & 0xFF # wait 40ms (i.e. 1000ms / 25 fps = 40 ms)

        # It can also be set to detect specific key strokes by recording which key is pressed

        # e.g. if user presses "x" then exit

        if (key == ord('x')):
            keep_processing = False

else:
    print("No image file was loaded.")

# ... and now close all windows

cv2.destroyAllWindows()
# ===================================================================
