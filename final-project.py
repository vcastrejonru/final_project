import math
import random
import pygame

# Can i add a feature to let the user choose a file from their documents???? 

# Add particle system
    # Look into sprites for diff particles shapes
    # + math for light sway of leaves falling
    # make the sprites choose random color based on the image

image = pygame.image.load('illustartion_RMV.jpg')
width, height = image.get_size()
particle_img = pygame.image.load('leaf.png')

particle_img = pygame.transform.scale(particle_img, (25, 25))


class Particle:
    def __init__(self):
        self.x = random.randint(0, width)
        self.y = random.randint(0, height)
        self.speed = random.randint(5, 15)

        size = random.randint(20, 50)
        self.image = pygame.transform.scale(particle_img, (size, size))

        self.start_x = self.x
        self.angle = random.uniform(0, 6.28)
    

    def fall(self):
        self.angle += 0.3
        self.x = self.start_x + math.sin(self.angle) * 25

        self.y += self.speed #this will keep the  particle movign downard, its updating its position w the speed
        if self.y > height: #this is too see if the particle has fallen out of the sceen
            self.y = random.randint(-height, 0) #this resets the particle above the screen (avoids syncornized falling, thanks sam)
    
    def draw(self, screen):
        screen.blit(particle_img, (self.x, self.y))

particles = []
for i in range(50):
    particles.append(Particle())


def main():
    pygame.init()
    pygame.display.set_caption('Pixel Art Screen')
    clock = pygame.time.Clock()
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
        
        for particle in particles:
            particle.fall()
            particle.draw(screen)
        
        dt = clock.tick(12) #dont delete
        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()