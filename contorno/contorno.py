import cv2
print(cv2.__version__) # imprime la version

imagen = cv2.imread("contorno\contorno.jpg") # imread carga una imagen desde una ruta
grises = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY) # convierto la imagen a escala de grises para poder umbralizarla
tipo_umbral, imagen_umbral = cv2.threshold(grises, 100, 255, cv2.THRESH_BINARY) #  Si el valor del pixel es mayor al valor del umbral, se le asigna un valor (puede ser blanco), de otro modo se le asigna otro valor (puede ser negro).
# findContours obtiene el contorno
#Hay dos funciones APROX_NONE y APROX_SIMPLE, aprox_none agarra todo el contorno y el aprox_simple agarra solo los puntos que estan en los vertices de la figura. Siempre vamos a usar aprox_simple

contornos, jerarquia = cv2.findContours(imagen_umbral, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE) # devuelve contornos y jerarquia. 
#dibujo los contornos
cv2.drawContours(imagen, contornos, -1, (65, 105, 255), 3)# el segundo parametro son cual de los contornos tengo que contornear
cv2.imshow("imagen en grises", grises) # hace un display de la imagen
cv2.imshow("imagen original", imagen) # hace un display de la imagen
cv2.imshow("imagen umbralizada", imagen_umbral)
cv2.waitKey(0) # Es para indicarle que la imagen se mantenga estatica si le coloco otro numero espera un momento para cerrar si clickeo en cualquier tecla se detiene el programa
cv2.destroyAllWindows() # destruye todas las ventanas emergentes a la hora de tener varias ventanas abiertas
