import pygame
import sys
import time
import re

# Importar clase boton y regletas
from boton import Boton
from logica import Regletas

# Importar colores
from colores import *


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

# Cargar archivo de sonido
sonido = pygame.mixer.Sound('felicitaciones.mp3')

# Crear los botones
boton_basico = Boton(50,200,imagen_boton_basico,0.5)
boton_avanzado = Boton(500,200,imagen_boton_avanzado,0.5)

# Crear texto pregunta 1
font = pygame.font.Font(None, 50)  # None indica la fuente predeterminada
font_opc = pygame.font.Font(None,34) 
texto_pregunta = font.render("Elija una regleta :)", True, PINK)
texto_opciones = font_opc.render("Regletas disponibles: ( 1/1 - 1/2 - 1/3 - 1/4 - 1/5 - 1/6 - 1/8 - 1/10 - 1/12 )", True, WHITE)
texto_opciones_2 = font_opc.render("y las variantes que se especifica en el manual", True, WHITE)
mensaje_error = font.render("Ingresaste caracteres invalidos", True, RED)
text_input = "" # variable que almacenará la entrada del usuario en el modo avanzado

patron = r"\d+/\d+"
regletas_identificadores= {1:"1/1",2:"1/2",3:"1/3",4:"1/4",5:"1/5",6:"1/6",7:"1/8",8:"1/10"}
regletas_imgs = Regletas(ventana)
circle_y = 140
juego_activo = False
Modo_de_juego = ""
entrada_regletas = []
game_over = False
opcion = 1
opciones_elegidas =[]
resultado=0
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
            elif evento.key == pygame.K_RETURN: # si el usuario presiona ENTER
                if re.match(patron, text_input):
                    print("El carácter cumple con el formato int/int")
                    entrada_regletas.append(text_input) # muestra la entrada del usuario en la consola
                else:
                    print("El carácter no cumple con el formato int/int")
                    ventana.blit(mensaje_error, (100, 400))
                    
                text_input = "" # vaciar la entrada de texto
                opciones_elegidas.append(opcion)
            elif evento .key == pygame.K_BACKSPACE: # si el usuario presiona retroceso
                text_input = text_input[:-1] # eliminar el último carácter

            else:
                text_input += evento.unicode # agregar el carácter ingresado a la entrada de texto
    # Poner imagen de fondo
    ventana.blit(background_image_modificado,(0,0))

    # Mostrar interfaz del juego principal
    if juego_activo and Modo_de_juego == "Basico":
        ventana.blit(texto_pregunta, (300, 90))
        regletas_imgs.mostrar_opciones(ventana)
        pygame.draw.rect(ventana,WHITE,(410,circle_y,40,46))
        if len(opciones_elegidas) >=2:
            Modo_de_juego = "Resultado"
            resultado = str(int(eval(regletas_identificadores[opciones_elegidas[0]])/eval(regletas_identificadores[opciones_elegidas[1]])))
        # print(opcion)
        
    elif juego_activo and Modo_de_juego == "Avanzado":
        ventana.blit(texto_opciones, (100, 100))
        ventana.blit(texto_opciones_2, (100, 130))
        input_text = font.render("Ingrese texto: " + text_input, True, BLUE)
        ventana.blit(input_text, (100, 180)) # posicionar el objeto de texto en la pantalla
        if len(entrada_regletas) >=2:
            Modo_de_juego="Resultado"
            resultado = str(eval(entrada_regletas[0])/eval(entrada_regletas[1]))
            
    elif juego_activo and Modo_de_juego == "Resultado":
        input_text = font.render("El resultado es:  " + resultado+" Manzanitas", True, BLUE)
        ventana.blit(input_text, (100, 180)) # posicionar el objeto de texto en la pantalla
        if len(opciones_elegidas) >= 2 and "" in entrada_regletas:
                entrada_regletas = regletas_identificadores[opciones_elegidas[0]],regletas_identificadores[opciones_elegidas[1]]
        regletas_imgs.dibujar(ventana,entrada_regletas)
        


    # Verificar si el menu esta activo
    if  (boton_avanzado.clicked or boton_basico.clicked):
        juego_activo = True
    if not juego_activo:
        ventana.fill(GREENISH_BLUE)
        boton_basico.dibujar(ventana)
        boton_avanzado.dibujar(ventana)
        
        if boton_avanzado.verificar_click():
            print("Modo Avanzado")
            Modo_de_juego="Avanzado"
        elif boton_basico.verificar_click():
            print("Modo basico")
            Modo_de_juego="Basico"
            


    # Actualizar pantalla
    pygame.display.flip()
    reloj.tick(30)