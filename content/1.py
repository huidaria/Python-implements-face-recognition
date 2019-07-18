import cv2
faceCascade = cv2.CascadeClassifier(r'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
ok = True
while ok:
    ok, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(32, 32),
    )
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 5)
    cv2.imshow('video', img)
    k = cv2.waitKey(1)
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()