import cv2
import numpy as np


def ordenarpuntos(puntos):
    m_puntos = list(np.concatenate(puntos[0], puntos[1], puntos[2], puntos[3]))
    y_order = sorted(m_puntos, key=lambda n_puntos:n_puntos[1])
    x1_order = y_order[:2]
    x1_order = sorted(x1_order, key=lambda x1_order:x1_order[0])
    x2_order = y_order[2:4]
    x2_order = sorted(x2_order, key=lambda x2_order:x2_order[0])
    x2_order = sorted(x2_order, key=lambda x2_order:x2_order[0])
    return [x1_order[0], x1_order[1], x2_order[0], x2_order[1]]


def alineamiento(imagen, ancho, alto):
    imagen_alineada = None
    grises = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY, )
    tipo_umbral, imagen_umbral = cv2.threshold(grises, 150, 255, cv2.THRESH_BINARY)
    contornos, jerarquia = cv2.findContours(imagen_umbral, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contornos = sorted(contornos, key=cv2.contourArea, reverse=True)[:1]
    cv2.drawContours(imagen, contornos, -1, (65, 105, 255), 3)
    cv2.imshow("umbral", imagen_umbral)