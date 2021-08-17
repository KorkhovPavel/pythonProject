import cv2
import numpy as np

photo = np.zeros((450, 450, 3), np.uint8)

# цвет
photo[:] = 155, 120, 120
# квадрат
# cv2.rectangle(photo, (10, 40), (100, 100), (255, 0, 0), thickness=7)
# # линия
# cv2.line(photo, (0, photo.shape[0] // 2), (photo.shape[1], photo.shape[0] // 2), (255, 0, 0), thickness=7)
# # круг
# cv2.circle(photo, (photo.shape[1] // 2, photo.shape[0] // 2), 50, (255, 0, 0), thickness=7)
# # текст
# cv2.putText(photo, 'hello', (150, 150), cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 255, 0), thickness=2)

cv2.imshow('res', photo)

cv2.waitKey(0)
