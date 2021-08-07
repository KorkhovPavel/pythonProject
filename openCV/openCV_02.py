import cv2
import numpy as np

# img
img = cv2.imread('img/331541.jpg')

# изменение размера
# img = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2))
# размытие
# img = cv2.GaussianBlur(img, (9, 9), 0)
# из цветного в серый
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# выделение контуров
img = cv2.Canny(img, 200, 200)
# обводка контуров
karnel = np.ones((1,1), np.uint8)
img = cv2.dilate(img, karnel, iterations=1)
# уменьшение толщины контура обводки
img = cv2.erode(img, karnel, iterations=1)

cv2.imshow('res', img)
# print(img.shape)
cv2.waitKey(0)

# # video

# cap = cv2.VideoCapture('video/video_2021-08-04_19-14-00.mp4')

# # камера
# # cap = cv2.VideoCapture(0)
# # cap.set(3,500)
# # cap.set(4,400)

# while True:
#     success, img = cap.read()
#     cv2.imshow('res', img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
