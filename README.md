# Image_Classification
In this example, a color detection using OpenCV and Python is performed to separate different colors.
The objective is to detect each color of the python logo, to be separated and denoised. That means, the blue, yellow and gray colors should be recognized. Check the (readme.pdf) file for more details.

<p align="center">
  <img src="https://github.com/SaysWis/Image_Classification/blob/main/Image_classification.jpg">
</p>

```
To try this example ...
1. Install python module : pip install opencv-python,
2. Define the upper and lower limits for your pixel values,
3. Make a call the cv2.inRange() function which  returns a mask, specifying which pixels lie into your upper and lower limits,
4. Once you have the mask, apply it to your image using cv2.bitwise_and() function,
5. Remove the internal and external noise using cv2.morphologyEx() function,
6. Add the three different processed images,
7. That's it.
```
