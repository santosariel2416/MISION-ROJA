# Jesus Ariel Santos 24-EISN-2-034

import pygame
import sys

def iniciar_juego():

    # Iniciar pygame
    pygame.init()

    # Tamaño de ventana
    Ancho = 1000
    Alto = 700

    pantalla = pygame.display.set_mode((Ancho, Alto))
    pygame.display.set_caption("Mision Roja")

    # tiempo para los FPS
    tiempo = pygame.time.Clock()

    # Variable de control
    corriendo = True

    # Bucle principal
    while corriendo:

        tiempo.tick(60)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False

        # Fondo rojo oscuro
        pantalla.fill((60, 0, 0))

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    iniciar_juego()
