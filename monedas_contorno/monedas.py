import cv2
import numpy as np

VALOR_GAUSS = 3
VALOR_KERNEL = 3
original = cv2.imread("monedas_contorno\monedas.jpg")
grises = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
tipo_umbral, umbral = cv2.threshold(grises, 100, 255, cv2.THRESH_BINARY)
desenfoque = cv2.GaussianBlur(grises, (VALOR_GAUSS, VALOR_KERNEL), 0) # desenfoque gaussiano sirve para poder desenfocar y de esta forma las imagenes que son borrosas aumentan la calidad si es que tiene ruido la imagen
canny = cv2.Canny(desenfoque, 60,100) # reduce el ruido definitivamente
kernel = np.ones((VALOR_KERNEL, VALOR_KERNEL), np.uint8) #lo uso porque necesito base 8
cierre = cv2.morphologyEx(canny, cv2.MORPH_CLOSE, kernel) #aplico clausura porque el ruido esta adentro
contornos, jerarquia = cv2.findContours(cierre.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # CV_RETR_EXTERNAL da contornos "externos", por lo que si tiene (digamos) un contorno que encierra a otro (como círculos concéntricos), sólo se da el más externo.
print(f"Monedas encontradas {len(contornos)}")
cv2.drawContours(original, contornos, -1, (65, 105, 255), 3)
cv2.imshow("grises", grises)
cv2.imshow("desenfoque", desenfoque)
cv2.imshow("canny", canny)
cv2.imshow("cierre", cierre)
cv2.imshow("resultado", original)
cv2.waitKey(0)
cv2.destroyAllWindows()