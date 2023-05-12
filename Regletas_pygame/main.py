import pygame
import sys
# Importar colores
from colores import *

# Importar clase boton
from boton import Boton

from logica import Regletas

# Iniciar libreria pygame
pygame.init()

# Tamaño de la ventana
ventana_size = (900 , 600)

# Crear ventana
ventana = pygame.display.set_mode(ventana_size)

# Reloj para pausar y controlar FPS
reloj = pygame.time.Clock()

# Cargar la imagen del fondo
background_image = pygame.image.load('img/background.jpg').convert()
background_image_modificado = pygame.transform.scale(background_image,(900,600))

# Cargar imagenes de los botones
imagen_boton_basico=pygame.image.load("img/boton_basico.png").convert_alpha()
imagen_boton_avanzado=pygame.image.load("img/boton_avanzado.png").convert_alpha()

# Crear los botones
boton_basico = Boton(100,200,imagen_boton_basico,0.5)
boton_avanzado = Boton(450,200,imagen_boton_avanzado,0.5)

# Crear texto pregunta 1
font = pygame.font.Font(None, 32)  # None indica la fuente predeterminada
text = font.render("Elija una regleta :)", True, PINK)
text_x = 350
text_y = 100


regletas_imgs = Regletas(ventana)
circle_y = 140
juego_activo = False
Modo_de_juego = ""
game_over = False
opcion = 1
# Bucle del juego
while not game_over:
    for evento in pygame.event.get():
        # Verificar si se ha cerrado la pantalla
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Detección de teclado - PULSASIONES
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_UP:
                # Acción cuando se presiona la tecla arriba
                circle_y -= 48
                opcion -=1
                if circle_y < 140 and opcion < 1:
                    circle_y = 140
                    opcion = 1
            elif evento.key == pygame.K_DOWN:
                # Acción cuando se presiona la tecla abajo
                circle_y += 48
                opcion +=1
                if circle_y > 474 and opcion > 8:
                    circle_y = 474
                    opcion = 8
    # Poner imagen de fondo
    ventana.blit(background_image_modificado,(0,0))

    # Mostrar interfaz del juego principal
    if juego_activo:
        ventana.blit(text, (text_x, text_y))
        regletas_imgs.mostrar_opciones(ventana)

        pygame.draw.rect(ventana,WHITE,(410,circle_y,40,46))
        print(pygame.mouse.get_pos())
        print(opcion)

    # Verificar si el menu esta activo
    if  (boton_avanzado.clicked or boton_basico.clicked):
        juego_activo = True
    if not juego_activo:
        ventana.fill(GREENISH_BLUE)
        boton_basico.dibujar(ventana)
        boton_avanzado.dibujar(ventana)
        if boton_basico.verificar_click():
            print("Modo basico")
        elif boton_avanzado.verificar_click():
            print("Modo avanzado")
        # print(boton_avanzado.clicked,boton_basico.clicked)
    
        
    # Actualizar pantalla
    pygame.display.flip()
    reloj.tick(30)