import cv2
import numpy as np

ruido = cv2.CascadeClassifier(r"C:\Users\novasrodrigo\Desktop\Reconocimiento de imagenes\reconocimiento_facial\archivos\haarcascade_frontalface_default.xml")
camara = cv2.VideoCapture(0)
while True:
    status, frame = camara.read() # el read arroja dos valores
    grises = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cara = ruido.detectMultiScale(grises, 1.2, 7)
    for(x,y,e1,e2) in cara: # e1 y e2 son las esquinas
        cv2.rectangle(frame, (x,y), (x+e1, y+e2), (255,0,0),2)
    cv2.imshow("En vivo", frame)
    if cv2.waitKey(1) == ord("q"): # presionando la q se sale la camara
        break


