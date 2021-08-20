import cv2

# поиск лиц фото
# img = cv2.imread('../img/f3.jpg')
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
# faces = cv2.CascadeClassifier('faces.xml')
#
# res = faces.detectMultiScale(gray, scaleFactor=3, minNeighbors=4)
#
# for (x,y,w,h) in res:
#     cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),thickness=2)
#
# cv2.imshow('res', img)
#
# cv2.waitKey(0)

# поиск лиц видео
cap = cv2.VideoCapture(0)
cap.set(3, 500)
cap.set(4, 400)

while True:
    success, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = cv2.CascadeClassifier('faces.xml')
    res = faces.detectMultiScale(gray, scaleFactor=3, minNeighbors=2)
    for (x, y, w, h) in res:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), thickness=2)
    cv2.imshow('res', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
