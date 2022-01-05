import cv2


capturaVideo = cv2.VideoCapture(0) # El valor cero es para buscar camaras que esten trabajando en la pc si es mas de 0 son camaras externas
if not capturaVideo.isOpened():
    print("No se encontro una camara")
    exit()
while True:
    status, frame = capturaVideo.read() # el read arroja dos valores
    cv2.imshow("En vivo", frame)
    if cv2.waitKey(1) == ord("q"): # presionando la q se sale la camara
        break
capturaVideo.release()
cv2.destroyAllWindows()