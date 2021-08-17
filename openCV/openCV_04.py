import cv2
import numpy as np

# cap = cv2.VideoCapture('video/video_2021-08-07_23-29-38.mp4')

# # видео с эфектами
# while True:
#     success, img = cap.read()
#
#     # изменение размера
#     # img = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2))
#     # размытие
#     img = cv2.GaussianBlur(img, (1, 1), 0)
#     # из цветного в серый
#     img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     # выделение контуров
#     img = cv2.Canny(img, 200, 200)
#     # обводка контуров
#     karnel = np.ones((1, 1), np.uint8)
#     img = cv2.dilate(img, karnel, iterations=1)
#     # уменьшение толщины контура обводки
#     img = cv2.erode(img, karnel, iterations=1)
#
#     cv2.imshow('res', img)
#     if cv2.waitKey(10) & 0xFF == ord('q'):
#         break


img = cv2.imread('../img/2021.08.16_09_16_33_qrcode.png')
new_img = np.zeros(img.shape, np.uint8)
new_img[:] = 155, 120, 120

# отзеркаливание
# img = cv2.flip(img, 1)


def rotate(img_p, angel):
    """
    поворот картинки
    :param img_p:
    :param angel:
    :return:
    """
    h, w = img_p.shape[:2]
    point = (h // 2, w // 2)

    m = cv2.getRotationMatrix2D(point, angel, 1)
    return cv2.warpAffine(img_p, m, (h, w))


def indent(img_p, x, y):
    """
    создает рамки
    :param img_p:
    :param x:
    :param y:
    :return:
    """
    mat = np.float32([[1, 0, x], [0, 1, y]])
    return cv2.warpAffine(img_p, mat, (img_p.shape[1], img_p.shape[0]))


# контуры изображения
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.GaussianBlur(img, (5, 5), 0)
img = cv2.Canny(img, 100, 140)
c, h = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

print(c)
# контуры изображения  переносим на новую картинку

cv2.drawContours(new_img, c, -1, (0, 0, 0), thickness=1)

cv2.imwrite('Image.jpg', new_img)

cv2.imshow('res', new_img)

cv2.waitKey(0)
