import cv2

# Load the image from file
image_path = r'F:\Github\Computer Vision\Files\img.jpg'
image = cv2.imread(image_path)

# Check if image was loaded successfully
if image is None:
    print(f"Error: Unable to load image from path {image_path}. Check if the path is correct.")
else:
    # Display the image in a window
    cv2.imshow('Loaded Image', image)

    # Wait for a key press and close the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()