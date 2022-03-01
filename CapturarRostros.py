import cv2
import os

class CapturarRostros:
    def __init__(self,entrada,nombrePersona,url,urlIP):

     ruta='.\Datos'
     rutaPersona=ruta+'/'+nombrePersona

     if not os.path.exists(rutaPersona):
      os.makedirs(rutaPersona)

     if entrada=="1":
       captura =cv2.VideoCapture(1)
     if entrada=="2":
       captura =cv2.VideoCapture(0)
     if entrada=="4":
        captura =cv2.VideoCapture(urlIP)

     faceClassif=cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml')


     contador=0

     while True:
      ret, frame=captura.read()
    
      if ret==False:break
      gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
      auxFrame=frame.copy()
      faces=faceClassif.detectMultiScale(gray, 1.3, 5)

      for(x,y,w,h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0),2)
        rostro=auxFrame[y:y+h,x:x+w]
        rostro=cv2.resize(rostro,(150,150),interpolation=cv2.INTER_CUBIC)
        cv2.imwrite(rutaPersona+'/rostro_{}.jpg'.format(contador),rostro)
        contador=contador+1
      self.video=frame  
      cv2.imshow('frame',frame)
 
      if cv2.waitKey(1) & 0xFF==ord('q') or contador>=300:
        break

     captura.relase()
     cv2.destroyAllWindows()        