import cv2 as cv
import numpy as np


def reScale(image, scale_width):
    (image_height, image_width) = image.shape[:2]
    new_height = int(scale_width / image_width * image_height)
    return cv.resize(src=image, dsize=(scale_width, new_height))


img = cv.imread('../Resources/Images/virat.jpg')
watermark = reScale(cv.imread('../Resources/Images/watermark.png'), 400)

cv.imshow('Image', img)


(watermark_height, watermark_width) = watermark.shape[:2]
(img_height, img_width) = img.shape[:2]

img = cv.cvtColor(src=img,code= cv.COLOR_BGR2BGRA)
watermark = cv.cvtColor(src=watermark,code= cv.COLOR_BGR2BGRA)

# define overly
overly = np.zeros((img_height, img_width, 4), dtype=np.uint8)
overly[0:watermark_height, img_width-watermark_width:img_width] = watermark


# put watermark on image
watermarked_img = cv.addWeighted(src1=overly, alpha=1.0, src2=img, beta=1.0, gamma=0)

cv.imshow('Overly', overly)
cv.imshow('Watermarked Image', watermarked_img)

cv.waitKey(0)
