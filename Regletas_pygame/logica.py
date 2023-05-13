import pygame
import math
class Regletas:
    # Cargar imágenes de regletas en una lista
    imagenes_regletas = [
        pygame.image.load("img/regleta_1.png"),
        pygame.image.load('img/regletas_1-2.png'),
        pygame.image.load('img/regletas_1-3.png'),
        pygame.image.load('img/regletas_1-4.png'),
        pygame.image.load('img/regletas_1-5.png'),
        pygame.image.load('img/regletas_1-6.png'),
        pygame.image.load('img/regletas_1-7.png'),
        pygame.image.load('img/regletas_1-8.png'),
        pygame.image.load('img/regletas_1-7.png'),
        pygame.image.load('img/regletas_1-10.png') 
    ]
    # Cargar imagen de la pregunta
    imagen_pregunta = pygame.image.load("img/regletas_pregunta.png")
    def __init__(self, ventana) -> None:
        # Inicializar ventana
        self.ventana = ventana

    def logica_juego(self, regletas):
        """
        Devuelve las imágenes de la regleta correspondiente a cada número y el número de regletas para cada uno.
        Args: 
            regletas (list): Lista de regletas, con el dividendo y el divisor.
        Returns: 
            tuple: Una tupla de imágenes de la regleta correspondiente al dividendo y al divisor, y el número de regletas para cada uno.
        """
        # Separar el dividendo y el divisor en numerador y denominador
        dividendo, divisor = regletas
        a, b = map(int, dividendo.split("/"))
        c, d = map(int, divisor.split("/"))

        # Devolver imágenes del divisor y del dividendo y el número de regletas para cada uno
        imagenes_dividendo = self.imagenes_regletas[b-1]
        imagenes_divisor = self.imagenes_regletas[d-1]
        return imagenes_dividendo, imagenes_divisor, a, c


    def mostrar_opciones(self, ventana):
        # Escalar y mostrar imagen de la pregunta
        imagen = pygame.transform.scale(self.imagen_pregunta, (40, 380))
        ventana.blit(imagen, (410, 140))

    def dibujar(self, ventana,entrada_regletas):
        # Obtener imágenes de las regletas y el número de regletas para cada uno
        divisor, dividendo, num, den = self.logica_juego(entrada_regletas)

        # Obtener ancho de las imágenes
        ancho_divisor = divisor.get_width()
        ancho_dividendo = dividendo.get_width()

        # Dibujar regletas en la ventana
        for i in range(num) :
            ventana.blit(divisor,(120+i*ancho_divisor,240))
        for i in range(den):
            ventana.blit(dividendo,(120+i*ancho_dividendo,320))

    def mostrar_todas_regletas(self, ventana):
        # Cargar imagen de la tabla de todas las regletas y escalarla
        regleta_todas = pygame.image.load("img/regletas_tabla.jpg")
        regleta_todass = pygame.transform.scale(regleta_todas, (300, 300))

        # Mostrar imagen en la ventana
        ventana.blit(regleta_todass, (40, 60))
