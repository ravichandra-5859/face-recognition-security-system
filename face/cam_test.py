import cv2
camera0=cv2.VideoCapture(0)


while True:
    ret,frame1=camera0.read()
    cv2.imshow('frame',frame1)
    if cv2.waitKey(27) & 0xFF==ord('q'):
        break
cv2.release()
cv2.destroyAllWindows()
