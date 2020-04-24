import cv2


def canny(image):
    return cv2.Canny(image, 100, 200)


def binary(image):
    threshold = 100
    _, img_thresh = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY)
    return img_thresh
