import pygame, sys

width = 640
heigh = 480

#Actualizamos / dibujamos la pantalla
screen = pygame.display.set_mode((width, heigh))
screen.fill((246, 147, 48))
pygame.display.set_caption("Ciclo basico de Pygame")

pygame.init()

#Comprobamos eventos
gameOver = False
while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True
    
    #Refrescamos la pantalla
    pygame.display.flip()
            
pygame.quit()
sys.exit()