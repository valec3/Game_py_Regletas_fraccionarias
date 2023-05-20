# Importar colores
import colores 
import pygame

class Configuraciones:
    """Una clase para almacenar todos los ajustes del juego."""
    # Cargar imágenes de regletas en una lista
    regletas = [
        pygame.image.load("img/regleta_1.png"),
        pygame.image.load('img/regleta_1-2.png'),
        pygame.image.load('img/regleta_1-3.png'),
        pygame.image.load('img/regleta_1-4.png'),
        pygame.image.load('img/regleta_1-5.png'),
        pygame.image.load('img/regleta_1-6.png'),
        pygame.image.load('img/regleta_nd.png'),
        pygame.image.load('img/regleta_1-8.png'),
        pygame.image.load('img/regleta_nd.png'),
        pygame.image.load('img/regleta_1-10.png') 
    ]
    bg_image_load = pygame.image.load('img/background.jpg')
    def __init__(self):
        """Inicializar los ajustes del juego."""
        # Screen settings
        self.ventana_width = 1200
        self.ventana_height = 800
        self.bg_imagen = pygame.transform.scale(self.bg_image_load,(1200,800))
        self.bg_botons = colores.WHITE
        self.patron = r'^([1-9]|1\d|20)/(1|2|3|4|5|6|7|8|9|10)$'
        self.selector= [300,140]