import cv2
import numpy as np

# Load your image
image_path = 'images/assets/testimage.png'
image = cv2.imread(image_path)

# Check if image is loaded properly
if image is None:
    print("Error: Image not found. Check the file path.")
else:
    # Convert to HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Adjusted range for red color to catch close shades and exclude pinks
    # Increase the lower bounds of saturation and value to exclude lighter shades
    lower_red1 = np.array([0, 120, 100])  # Adjusted
    upper_red1 = np.array([10, 255, 255])
    mask_red1 = cv2.inRange(hsv, lower_red1, upper_red1)

    lower_red2 = np.array([170, 120, 100])  # Adjusted
    upper_red2 = np.array([180, 255, 255])
    mask_red2 = cv2.inRange(hsv, lower_red2, upper_red2)

    # Combine the masks for red
    mask_red = cv2.bitwise_or(mask_red1, mask_red2)

    # Adjusted single range for green to catch close shades effectively
    lower_green = np.array([35, 100, 100])
    upper_green = np.array([85, 255, 255])  # Broadened range
    mask_green = cv2.inRange(hsv, lower_green, upper_green)

    # Process for red objects
    contours_red, _ = cv2.findContours(mask_red, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours_red:
        if cv2.contourArea(cnt) > 500:
            cv2.drawContours(image, [cnt], -1, (0, 255, 0), 2)

    # Process for green objects
    contours_green, _ = cv2.findContours(mask_green, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours_green:
        if cv2.contourArea(cnt) > 500:
            cv2.drawContours(image, [cnt], -1, (0, 0, 255), 2)

    # Display the image
    cv2.imshow('Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
