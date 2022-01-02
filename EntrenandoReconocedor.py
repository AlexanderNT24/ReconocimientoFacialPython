import cv2
import os
import numpy as np

class EntrenarRostros:
    def __init__(self):
        ruta='D:\FiltrosPythonYOpenCV\ReconocimientoFacial\Datos'

        listaPersonas=os.listdir(ruta)

        etiquetas=[]

        faceData=[]

        etiqueta=0

        for nombrePersona in listaPersonas:
          rutaPersonas=ruta+'/'+nombrePersona
    
          for fileName in os.listdir(rutaPersonas):
            etiquetas.append(etiqueta)
            faceData.append(cv2.imread(rutaPersonas+'/'+fileName,0))
            imagen=cv2.imread(rutaPersonas+'/'+fileName,0)
          etiqueta=etiqueta+1

        print(etiquetas)

        face_recognizer=cv2.face.EigenFaceRecognizer_create()

        face_recognizer.train(faceData,np.array(etiquetas))

        face_recognizer.write('modeloEigenFace.xml')


