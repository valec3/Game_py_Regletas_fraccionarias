import pygame
class Boton:
    """
    Clase que representa un botón en la pantalla.
    """

    def __init__(self, x: int, y: int, imagen: pygame.Surface,escala:int) -> None:
        """
        Constructor de la clase Boton.

        :param x: La posición en x del botón en la pantalla.
        :type x: int
        :param y: La posición en y del botón en la pantalla.
        :type y: int
        :param imagen: La imagen del botón.
        :type imagen: pygame.Surface
        """
        ancho = imagen.get_width()
        alto = imagen.get_height()
        self.imagen = pygame.transform.scale(imagen,(int(ancho*escala),int(alto*escala)))
        self.rect = imagen.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
    def verificar_click(self):
        """
        Metodo para verificar si se hizo click en el boton

        Returns:
            type bool: Estado actual del boton
        """
        # Obtiene la posición actual del mouse.
        posicion_mouse = pygame.mouse.get_pos()
        
        # Si la posición del mouse está dentro del rectángulo del botón, verifica si se ha hecho clic en él.
        if self.rect.collidepoint(posicion_mouse):
            # Si se hace clic en el botón, cambia su estado a True.
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
            # Si se suelta el botón del mouse, cambia su estado a False.
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
                
        # Devuelve el estado actual del botón.
        return self.clicked
    def dibujar(self, ventana: pygame.Surface) -> None:
        """
        Dibuja el botón en la ventana especificada.

        :param ventana: La superficie donde se dibujará el botón.
        :type ventana: pygame.Surface
        """
        ventana.blit(self.imagen, (self.rect.x, self.rect.y))
