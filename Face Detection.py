import cv2
cam = cv2.VideoCapture(0)
detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
count=0            
while (True):
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.3, 5)
    
    for (x, y, w, h) in faces:
        count+=1
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.imwrite("TrainingImage/ " + str(count)+ ".jpg",gray[y:y + h, x:x + w])
        cv2.imshow('Frame', img)
               
        if cv2.waitKey(1) &  0xFF == ord('q'):
                    break
                
                    
cam.release()
cv2.destroyAllWindows()
   
