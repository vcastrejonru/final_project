import os
import random
import pygame


def main():
    pygame.init()
    pygame.display.set_caption('Pixel Art Screen')
    clock = pygame.time.Clock()
    dt = 0
    image = pygame.image.load('illustartion_RMV.jpg')
    width, height = image.get_size()
    resolution = (width, height)
    screen = pygame.display.set_mode(resolution)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        #image = pygame.transform.scale(width//3, height//3)
        #image = pygame.transform.scale(width, height)
        black = pygame.Color(0, 0, 0)
        screen.blit(image)
        pygame.display.flip()
        dt = clock.tick(12)
    pygame.quit()

if __name__ == "__main__":
    main()