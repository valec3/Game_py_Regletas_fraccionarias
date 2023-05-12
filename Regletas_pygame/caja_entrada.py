import pygame,sys

# NO ESTA EN USO 
# NO ESTA EN USO 
# NO ESTA EN USO 
# NO ESTA EN USO 
# NO ESTA EN USO 
# NO ESTA EN USO 
# NO ESTA EN USO 
# NO ESTA EN USO 

pygame.init()
# Tamaño de la ventana
ventana_size = (900 , 600)

# Crear ventana
ventana = pygame.display.set_mode(ventana_size)

# Reloj para pausar y controlar FPS
reloj = pygame.time.Clock()
class TextInputBox:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = pygame.Color('gray20')
        self.text = ''
        self.font = pygame.font.Font(None, 32)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, 2)
        text_surface = self.font.render(self.text, True, pygame.Color('white'))
        surface.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode
                
input_box = TextInputBox(100, 100, 200, 50)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        else:
            input_box.handle_event(event)

    input_box.draw(ventana)
    pygame.display.flip()
