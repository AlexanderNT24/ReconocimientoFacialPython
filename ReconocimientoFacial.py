import cv2
import os

class ReconocerRostros:
    def __init__(self,entrada,url,urlIP):
        absPath = os.path.abspath(__file__)

        path, nombreArchivo = os.path.split(absPath)
        ruta=path+'\Datos'
        personas=os.listdir(ruta)
        face_recognizer=cv2.face.EigenFaceRecognizer_create()
        print(personas)

        face_recognizer.read('modeloEigenFace.xml')

        if entrada=="1":
         captura =cv2.VideoCapture(1)
        if entrada=="2":
         captura =cv2.VideoCapture(0)
        if entrada=="4":
         captura =cv2.VideoCapture(urlIP)

        faceClassif=cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml')

        while True:
         ret, frame=captura.read()

         if ret==False:break
         gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
         auxFrame=gray.copy()

         faces=faceClassif.detectMultiScale(gray, 1.3, 5)

         for(x,y,w,h) in faces:
           rostro=auxFrame[y:y+h,x:x+w]
           rostro=cv2.resize(rostro,(150,150),interpolation=cv2.INTER_CUBIC)
           result=face_recognizer.predict(rostro)
           #cv2.putText(frame,'{}'.format(result),(x,y-5),1,1.3,(255,255,0),1,cv2.LINE_AA)
           if result[1]<5700:
             cv2.putText(frame,format(personas[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
             cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0),2)
           else:
             cv2.putText(frame,'Desconocido',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
             cv2.rectangle(frame, (x, y), (x + w, y + h), (0,0, 255),2)
        
         cv2.imshow('frame',frame)
 
         if cv2.waitKey(1) & 0xFF==ord('q'):
          break

        captura.relase()
        cv2.destroyAllWindows()        

