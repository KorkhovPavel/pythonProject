import cv2


# Цветовые форматы
img = cv2.imread('../img/qrcode.png')
# img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
# img = cv2.cvtColor(img, cv2.COLOR_LAB2BGR)
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

r, g, b = cv2.split(img)
img = cv2.merge([b, g, r])
cv2.imshow('res', img)

cv2.waitKey(0)
