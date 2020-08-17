import cv2
import os


class ColorImage:
    def __init__(self, dir, name):
        self.dir = dir  # dirección de la imagen
        self.name = name  # nombre de la imagen
        self.path_file = os.path.join(dir, name)  # Enlazamiento del nombre y dirección de la imagen
        self.image = cv2.imread(self.path_file)  # Guardar y abrir la imagen
        cv2.imshow("Imagen", self.image)  # Mostrar la imagen
        cv2.waitKey(0)  # Mantener la imagen abierta

    def displayProperties(self):
        print(self.image.shape)  # Mostrar ancho y alto de la imagen

    def makeGray(self):
        self.image_gray = cv2.cvtColor(self.image, cv2.COLOR_RGB2GRAY)  # cambiar de BGR a grises y guardar
        cv2.imshow("Imagen en grises", self.image_gray)  # mostrar imagen en grises
        cv2.waitKey(0)  # mantener abierta la imagen

    def colorizeRGB(self, color):
        self.image_c = self.image.copy()  # para que se modifique la copia y no afecte el metodo makeHue
        # self.color = input('Digite un color entre blue, green, red para colorizar la imagen:')

        if color == 'blue':  # condicional si se desea la imagen azulada
            self.image_c[:, :, 1] = 0  # canal g a 0
            self.image_c[:, :, 2] = 0  # canal r a 0

        if color == 'green':  # condicional si se desea la imagen verdoza
            self.image_c[:, :, 0] = 0  # canal b a 0
            self.image_c[:, :, 2] = 0  # canal r a 0

        if color == 'red':  # condicional si se desea la imagen rojiza
            self.image_c[:, :, 0] = 0  # canal b a 0
            self.image_c[:, :, 1] = 0  # canal g a 0

        cv2.imshow("Imagen colorizada", self.image_c)  # mostrar imagen colorizada
        cv2.waitKey(0)  # mantener abierta la imagen

    def makeHue(self):
        self.image_hue = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)  # Transformar de BGR a HSV y guardar
        self.image_hue[:, :, 1] = 255  # convertir el canal S a 255
        self.image_hue[:, :, 2] = 255  # convertir el canal V a 255
        self.image_hue_ = cv2.cvtColor(self.image_hue, cv2.COLOR_HSV2BGR)  # transformar la imagen HSV a BGR
        cv2.imshow('Imagen  hue', self.image_hue_)  # mostrar imagen en Hue
        cv2.waitKey(0)  # mantener abierta la imagen
