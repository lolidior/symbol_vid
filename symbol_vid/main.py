import numpy as np
import cv2

cap = cv2.VideoCapture(0)
alphabet = " `.,-':<>;+!*/?%"
while True:
    ret,frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    x = 256//len(alphabet)
    new = np.zeros((frame.shape[0],frame.shape[1]))
    for i in range(0,new.shape[0],7):
        for j in range(0,new.shape[1],7):
            cv2.putText(new,alphabet[frame[i][j]//x], (j,i),cv2.FONT_HERSHEY_SIMPLEX,0.25,(255,255,255))
    cv2.imshow("lol", new)
    np_frame = np.asarray(frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
print (np_frame)
cap.release()
cv2.destroyAllWindows()