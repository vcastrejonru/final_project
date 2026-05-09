import random
import pygame

# Can i add a feature to let the user choose a file from their documents???? 

# Add particle system
    # Look into sprites for diff particles shapes
    # + math for light sway of leaves falling
    # make the sprites choose random color based on the image

class Particle():

    def __init__(self, pos=(1, 0), size=(10), life=1000):
        self.pos = pos
        self.size = size
        self.color = pygame.Color(self.random_color())
        self.age = 0
        self.life = life
        self.dead = False
        self.alpha = 255
        self.surface = self.update_surface()

    def random_color(self):

        x = random.randint(0, self.image.get_width())
        y = random.randint(0, self.image.get_height()) 

    def update(self, dt):
        self.age += dt
        if self.age > self.life:
             self.dead = True
        self.alpha = 255 * (1 - (self.age / self.life))

    def update_surface(self):
        
        #sprites?
    def draw(self, surface):
        if self.dead:
            return
        self.surface.set_alpha(self.alpha)
        surface.blit(self.surface, self.pos)



def main():
    pygame.init()
    pygame.display.set_caption('Pixel Art Screen')
    clock = pygame.time.Clock()
    dt = 0
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
        dt = clock.tick(12)
    pygame.quit()

if __name__ == "__main__":
    main()