import random
import pygame

# Can i add a feature to let the user choose a file from their documents???? 

# Add particle system
    # Look into sprites for diff particles shapes
    # + math for light sway of leaves falling
    # make the sprites choose random color based on the image



      


def main():
    pygame.init()
    pygame.display.set_caption('Pixel Art Screen')
    #clock = pygame.time.Clock()
    #dt = 0
    #particle_img = pygame.image.load('leaf.png')
   # particle_img = pygame.transform.scale(particle_img, (15, 15))
   # particles = []
    image = pygame.image.load('illustartion_RMV.jpg')
    width, height = image.get_size()
    resolution = (width, height)
    small_img = pygame.transform.scale(image, (width//8, height//8))
    pixelated_img = pygame.transform.scale(small_img, resolution)
    screen = pygame.display.set_mode(resolution)
    running = True
    show_pixelated = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    show_pixelated = False
                if event.button == 3:
                    show_pixelated = True
        if show_pixelated:
            screen.blit(pixelated_img, (0, 0))
        else:
            screen.blit(image, (0, 0))
        pygame.display.flip()
        #dt = clock.tick(12)
    pygame.quit()

if __name__ == "__main__":
    main()