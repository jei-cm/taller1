from colorImage import *


class ColorImage:
    x1 = ColorImage(input('Ingrese la direccion:'), input('Ingrese nombre de la imagen:'))  # Pedir dirección de imagen
    x1.displayProperties()  # primer metodo:alto y ancho de la imagen
    x1.makeGray()  # Segundo metodo: imagen en grises
    x1.colorizeRGB('red')  # Tercer metodo: Hacer rojiza la imagen
    x1.makeHue()  # Cuarto metodo: versión de tonos/colores resaltados
