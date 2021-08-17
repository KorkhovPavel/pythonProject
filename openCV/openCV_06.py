import cv2
import numpy  as np
# открывает картинку и создаем полотно = размерам картинки
photo = cv2.imread('../img/566599.jpg')
img = np.zeros(photo.shape[:2],dtype='uint8')
# создание полотна
# img = np.zeros((350,350),dtype='uint8')
# создание круга
circle = cv2.circle(img.copy(),(0,0),50, 255, -1)
# создание квадрата
rectangle = cv2.rectangle(img.copy(),(200,200),(500,500), 255, -1)
# вывод где есть совпадения
# img = cv2.bitwise_and(circle,rectangle)
# вывод все
# img = cv2.bitwise_or(circle,rectangle)
# вывод все кроме совпадения
# img = cv2.bitwise_xor(circle,rectangle)
# инверсия
# img = cv2.bitwise_not(circle)
# применение к картинке
img = cv2.bitwise_or(photo,photo,mask=rectangle)
cv2.imshow('res', img)

cv2.waitKey(0)