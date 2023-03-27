#Importar librería cv2
import cv2

#Leer imagen
img = cv2.imread('2B60000.jpg')
#Cambiar img a escala de grises

#img2 = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

#Analiza 81 pixeles grises
"""
for fila in range (9):
    for columna in range (9):
        print("Color", "fila:", + fila, "columna", + columna, "=", str(img2[fila,columna]))

#Mostrar imagen
cv2.imshow('imagenGris',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
print(img[0][0])
print(img[95][79])
