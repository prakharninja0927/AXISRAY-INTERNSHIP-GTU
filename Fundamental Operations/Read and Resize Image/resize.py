import cv2 as cv

# reading an image
img = cv.imread('../Resources/Photos/cat.jpg')
cv.imshow('Cat', img)

print('Properties of Original image')
print(f'height: {img.shape[0]}, width: {img.shape[1]}, color channels: {img.shape[2]}')


# defining resizing function
def resize(img, scale=0.75):
    height = int(img.shape[0] * scale)
    width = int(img.shape[1] * scale)
    dimensions = (width, height)

    return cv.resize(src=img,dsize=dimensions,interpolation=cv.INTER_AREA)

resized_image = resize(img)
cv.imshow('Resized Image',resized_image)
print('\n\nProperties of Resized image')
print(f'height: {resized_image.shape[0]}, width: {resized_image.shape[1]}, '
      f'color channels: {resized_image.shape[2]}')

cv.waitKey(0)
