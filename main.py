import inline as inline
import matplotlib
import spicy
from skimage.io import imread, imshow
import matplotlib.pyplot as plt

image = imread('D:\Images\ONEUS\ONEUS_200929_25.jpg', as_gray=False)
imshow(image)
print(image.shape)