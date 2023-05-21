# Copyright (c) 2023 Valec3
#
# Este archivo es parte del programa Regletas fraccionarias.
# Juego de regletas fraccionarias para niños
#
# Derechos de autor (c) 2023 Valec3
# Todos los derechos reservados.


import sys,pygame,time,re
from configuraciones import Configuraciones
from boton import Boton
from texto import Texto
import colores

class Regletas:
    """Clase general para gestionar el comportamiento del juego."""
    
    # Cargar imagen de la pregunta
    imagen_pregunta = pygame.image.load("img/regletas_tabla.png")
    
    def __init__(self) -> None:
        """Inicializa el juego y crea los recursos del juego."""
        pygame.init()
        
        self.clock = pygame.time.Clock() #Controlar FPS
        self.configuraciones = Configuraciones()
        
        self.ventana = pygame.display.set_mode(
            (self.configuraciones.ventana_width, self.configuraciones.ventana_height))
        self.rectangulo_ventana = self.ventana.get_rect()
        
        # Cargar imagenes de los botones
        self.imagen_btn_basico=pygame.image.load("img/boton_basico.png").convert_alpha()
        self.imagen_btn_avanzado=pygame.image.load("img/boton_avanzado.png").convert_alpha()
        
        self.imagenes_regletas = self.configuraciones.regletas
        # Crear los botones
        self.btn_basico = Boton(100,300,self.imagen_btn_basico,0.7)
        self.rectangulo_btn_bsc = self.imagen_btn_basico.get_rect()
        self.btn_avanzado = Boton(640,300,self.imagen_btn_avanzado,0.7)
        self.rectangulo_btn_avz = self.imagen_btn_avanzado.get_rect()
        
        # Texto
        self.texto_pregunta = Texto("Elija una tipo de regleta :)",42,colores.PINK,350,90)
        self.texto_opciones_l1 = Texto("Regletas disponibles: ( 1/1 - 1/2 - 1/3 - 1/4 - 1/5 - 1/6 - 1/8 - 1/10)",40,colores.WHITE,120,100)
        self.texto_opciones_l2 = Texto("Siga el formato especificado en el manual",40, colores.WHITE,120,140)
        self.texto_salir_rep = Texto("Salir con Q - Reiniciar con R", 32, colores.DARK_BLUE,10,10)
        self.text_input = "" # variable que almacenará la entrada del usuario en el modo avanzado
        
        # EXTRAS
        self.patron = self.configuraciones.patron
        self.sel_circulo=self.configuraciones.selector
        self.regletas_identificadores= {1:"1/1",2:"1/2",3:"1/3",4:"1/4",5:"1/5",6:"1/6",7:"1/8",8:"1/10"}
        self.entrada_regletas = []
        self.opcion = 1
        self.opciones_elegidas =[]
        self.resultado=0
        self.show_error = False
        self.start_time = 0
        
        # Iniciar el juego en un estado inactivo.
        self.game_active = False
        # Modo de juego
        self.modo_juego = ""
        pygame.display.set_caption("Regletas Fraccionarias")
        
        
    def dibujar_botones(self):
        """Dibujar los botones en pantalla."""
        self.btn_basico.dibujar(self.ventana)
        self.btn_avanzado.dibujar(self.ventana)
    
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
        try:
            a, b = map(int, dividendo.split("/"))
            c, d = map(int, divisor.split("/"))
        except SyntaxError:
            self.mostrar_error(3)
        cociente = int((a/b) / (c/d))
        if b > 10:
            b = 7
        elif d > 10:
            d = 7
        try:
            # Devolver imágenes del divisor y del dividendo y el número de regletas para cada uno
            imagenes_dividendo = self.imagenes_regletas[b-1]
            imagenes_divisor = self.imagenes_regletas[d-1]
            return imagenes_dividendo, imagenes_divisor, [a,b], [c,d], cociente
        except IndexError:
            self.game_active = False
        
    
    def mostrar_opciones(self, ventana):
        
        # Escalar y mostrar imagen de la pregunta
        imagen = pygame.transform.scale(self.imagen_pregunta, (400, 400))
        ventana.blit(imagen, (400, 140))

    def dibujar(self, ventana,entrada_regletas):
        # Obtener imágenes de las regletas y el número de regletas para cada uno
        divisor, dividendo, num, den,cociente = self.logica_juego(entrada_regletas)
        
        # Obtener ancho de las imágenes
        ancho_divisor = divisor.get_width()
        ancho_dividendo = dividendo.get_width()

        desbordamiento = False
        
        # Dibujar regletas en la ventana
        for i in range(num[0]) :
            ventana.blit(divisor,(120+i*ancho_divisor,240))
            if 120+i*ancho_divisor > 1200:
                desbordamiento = True
        for i in range(den[0]):
            ventana.blit(dividendo,(120+i*ancho_dividendo,320))
            if 120+i*ancho_dividendo > 1200:
                desbordamiento = True
        
        texto_why=Texto("¿Porque?",34,colores.CYAN,120,400)
        texto_why.draw(self.ventana)
        
        # Posicion de salida (EJE Y)
        x , y = 460 , 530
        
        if cociente < 1:
            texto_div = Texto(
                f"La regleta {den[0]}/{den[1]} es mayor que la regleta {num[0]}/{num[1]}. Asi que el resultado sera menor a cero.",
                30,
                colores.DARK_GREEN,
                120,430
                        )
            x , y =y ,x
            cociente = 1
            texto_div.draw(self.ventana)
        
        # Dibujar resultado visual
        for i in range(num[0]) :
            ventana.blit(divisor,(120+i*ancho_divisor,x))
        for i in range(cociente*den[0]):
            ventana.blit(dividendo,(120+i*ancho_dividendo,y))
            
        if num[1] == 7 or den[1] == 7:
            texto_nodis = Texto("Las representaciones para las regletas 1/7 y 1/9 no estan disponibles",30,colores.RED,120,600)
            texto_nodis.draw(self.ventana)
        
        if desbordamiento:
            texto_advertencia = Texto("! EL NUMERO DE REGLETAS INGRESADO ESTA EXCEDIENDO EL LIMITE DE PANTALLA !",
                                    34,
                                    colores.RED,
                                    120,680
                                    )
            texto_advertencia.draw(self.ventana)
            

    def run_game(self):
        """Inicia el bucle principal del juego."""
        while True:
            
            self._revisar_eventos()
            
            self._actualizar_ventana()
            self.clock.tick(60) #FPS
            
    def _revisar_eventos(self):
        """Respond to keypresses and mouse events."""
        for evento in pygame.event.get():
            # Verificar si se ha cerrado la pantalla
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Detección de teclado - PULSASIONES
            if evento.type == pygame.KEYDOWN:
                self._revisar_eventos_keydown(evento)
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
                
    def _revisar_eventos_keydown(self, evento):
        
        """Responde a teclas presionadas."""
        if evento.key == pygame.K_q or evento.key == pygame.K_ESCAPE:#Salir del juego
            sys.exit()
        elif evento.key == pygame.K_r:
            self.game_active = False
        elif evento.key == pygame.K_RETURN:
            if self.text_input == "1":
                self.text_input = "1/1"
            if re.match(self.patron, self.text_input): #Verificar si la entrada del usuario es correcta
                print("El carácter cumple con el formato int/int")
                self.entrada_regletas.append(self.text_input) # muestra la entrada del usuario en la consola
            else:
                print("El carácter no cumple con el formato int/int")
            self.text_input = "" # vaciar la entrada de texto
            self.opciones_elegidas.append(self.opcion)
        elif evento.key == pygame.K_BACKSPACE: # si el usuario presiona retroceso
            if len(self.text_input) >=1:
                self.text_input = self.text_input[:-1] # eliminar el último carácter
        else:
            if self.modo_juego == "A":
                self.text_input += evento.unicode # agregar el carácter ingresado a la entrada de texto
        self.mover_selector(evento)
        
    def _check_play_button(self, mouse_pos):
        """Inicia un nuevo juego cuando se hace click en algun boton."""
        if self.game_active == False:
            if self.btn_basico.rect.collidepoint(mouse_pos):
                self.game_active = True
                self.modo_juego = "B"
            elif  self.btn_avanzado.rect.collidepoint(mouse_pos):
                self.game_active =True
                self.modo_juego = "A"
            
    def mover_selector(self,evento):
        if evento.key == pygame.K_UP:
            # Acción cuando se presiona la tecla arriba
            self.sel_circulo[1] -= 50
            self.opcion -=1
            if self.sel_circulo[1] < 140 and self.opcion < 1:
                self.sel_circulo[1] = 140
                self.opcion = 1
        elif evento.key == pygame.K_DOWN:
            # Acción cuando se presiona la tecla abajo
            self.sel_circulo[1] += 50
            self.opcion +=1
            if self.sel_circulo[1] > 490 and self.opcion > 8:
                self.sel_circulo[1] = 490
                self.opcion = 8
                
    def iniciar_modo(self):
        
        # Mostrar interfaz del juego principal
        if  self.modo_juego == "B":
            self.texto_pregunta.draw(self.ventana)
            self.mostrar_opciones(self.ventana)
            pygame.draw.rect(self.ventana,colores.GREEN,(self.sel_circulo[0],self.sel_circulo[1],400,50))
            texto_elecciones = Texto(f"Numero de regletas elegidas: {len(self.opciones_elegidas)}",40,colores.GREEN,120,600)
            texto_elecciones.draw(self.ventana)
            if len(self.opciones_elegidas) >=2:
                self.modo_juego = "Resultado"
                self.resultado = str(eval(
                    self.regletas_identificadores[self.opciones_elegidas[0]])/eval(self.regletas_identificadores[self.opciones_elegidas[1]]
                    ))
            
        elif self.modo_juego == "A":
            self.texto_opciones_l1.draw(self.ventana)
            self.texto_opciones_l2.draw(self.ventana)
            input_text = Texto("Ingrese su regleta (a/b): "+self.text_input,44,colores.WHITE,140,220)
            input_text.draw(self.ventana) # posicionar el objeto de texto en la pantalla
            if len(self.entrada_regletas) >=2:
                self.modo_juego="Resultado"
                self.resultado = str(eval(self.entrada_regletas[0])/eval(self.entrada_regletas[1]))
                
        elif self.modo_juego == "Resultado":
            input_text = Texto("El resultado de dividir estas regletas es: "+self.resultado,40,colores.LIGHT_YELLOW,120,160)
            input_text.draw(self.ventana) # posicionar el objeto de texto en la pantalla
            
            if len(self.opciones_elegidas) >= 2 and len(self.entrada_regletas) < 2:
                    self.entrada_regletas = self.regletas_identificadores[self.opciones_elegidas[0]],self.regletas_identificadores[self.opciones_elegidas[1]]
            self.dibujar(self.ventana,self.entrada_regletas)
            
    def mostrar_error(self, duracion):
        self.show_error = True
        self.start_time = time.time()

        while time.time() - self.start_time < duracion:
            self.ventana.fill(colores.BLACK)
            texto_error=Texto("ERROR INESPERADO",40,colores.RED,400,400)
            texto_error.draw(self.ventana)            
        self.show_error = False
        
    def _actualizar_ventana(self):
            """Actualizar imagenes en la ventana y mostrar ventana actual."""
            # Redibuja el fondo durante cada pasada por el bucle.
            self.ventana.blit(self.configuraciones.bg_imagen,(0,0))
            self.texto_salir_rep.draw(self.ventana)
            
            # Dibujar la pantalla del modo
            self.iniciar_modo()
            #Dibujar el boton si el juego esta inactivo.
            if not self.game_active:
                self.modo_juego=""
                self.entrada_regletas=[]
                self.opciones_elegidas = []
                self.ventana.blit(self.configuraciones.bg_botons,(0,0))
                self.dibujar_botones()
                
            if self.show_error:
                self.mostrar_error( 3)
                
            #Actualizar pantalla
            pygame.display.flip()
                

# Correr juego 
if __name__ == "__main__":
    Regletas_fraccionarias = Regletas()
    Regletas_fraccionarias.run_game()