# Computer Vision

This project is a basic demonstration of using the OpenCV Python library to load and display images. The repository contains two folders: `Files` and `Images`. Below is a detailed description of each folder and the content within them.

## Repository Structure

- **Files**: Contains the `images.py` script, which is used to load an image from the `Images` folder using the OpenCV library.
- **Images**: Contains sample images that are loaded and displayed by the `images.py` script.

---

## Files Folder

The **Files** folder includes the main Python script `images.py` which does the following:
1. Loads an image from the `Images` folder using OpenCV's `cv2.imread()` function.
2. Displays the loaded image in a window using `cv2.imshow()`.
3. Waits for a key press to close the window using `cv2.waitKey(0)`.

### images.py

Here is a brief overview of the script:
- **Image Path**: The script reads an image from the `Images` folder (`../Images/image1.jpg`).
- **Display**: Once the image is loaded, it opens a window to display the image.
- **Close on Keypress**: After the image is displayed, the script waits for a key press to close the window and terminate the program.

To execute the script, you will need to install OpenCV if you don't have it already. You can install OpenCV using the following command:

```bash
pip install opencv-python
