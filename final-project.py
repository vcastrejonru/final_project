import math
import random
import pygame
from PIL import Image

# notes for tomorrow:
    # try resizing so bg image keeps size ration but overall display resolution fits on screen
    # fix gif saving bugs
    #pixelated image resizes weird when pixel mode is active ?

image = pygame.image.load('illustration_3.jpg')
width, height = image.get_size()
resolution = (800, 800)
particle_img = pygame.image.load('leaf.png')

particle_img = pygame.transform.scale(particle_img, (25, 25))

def tint(image, color):
    tinted = image.copy()
    tint_surface = pygame.Surface(image.get_size())
    tint_surface.fill(color)

    tinted.blit(tint_surface, (0, 0), special_flags=pygame.BLEND_PREMULTIPLIED)

    return tinted

class Particle:
    def __init__(self):
        #particles porperties
        self.x = random.randint(0, width)
        self.y = random.randint(0, height)
        self.speed = random.randint(5, 10)
        size = random.randint(20, 50)
        #particle image
        base_image = pygame.transform.scale(particle_img, (size, size))
        #sampling the background for a color at spawn posiiton
        color = image.get_at((self.x, self.y))
        #this applies the color tint
        self.image = tint(base_image, color)
       
        self.start_x = self.x
        self.sway_angle = random.uniform(0, 6.28)

    def fall(self):
        self.sway_angle += 0.3
        self.x = self.start_x + math.sin(self.sway_angle) * 25

        self.y += self.speed #this will keep the  particle movign downard, its updating its position w the speed
        if self.y > height: #this is too see if the particle has fallen out of the sceen
            self.y = random.randint(-height, 0) #this resets the particle above the screen (avoids syncornized falling, thanks sam)
   
    def draw(self, screen):
        shadows = self.image.copy()
        shadows.fill((0, 0, 0, 100), special_flags=pygame.BLEND_RGBA_MULT)
        screen.blit(shadows, (self.x + 2, self.y + 3))
        screen.blit(self.image, (self.x, self.y))

particles = []
for i in range(50):
    particles.append(Particle())

def main():
    pygame.init()
    pygame.display.set_caption('Pixel Art Screen')
    clock = pygame.time.Clock()
    frames = []
    recording = True
    small_img = pygame.transform.scale(image, (width//8, height//8))
    pixelated_img = pygame.transform.scale(small_img, (width, height))
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
        if recording:
            frame = pygame.surfarray.array3d(screen)
            frame = frame.swapaxes(0, 1)
            frames.append(frame)
        if len(frames) > 300:
            recording = False
        
        dt = clock.tick(12) #dont delete
        pygame.display.flip()
    pygame.quit()

    images = [Image.fromarray(frame) for frame in frames]

    #images[0].save(
        #"pixel_art.gif",
        #save_all = True,
        #append_images = images[1:],
        #duration = 16,
        #loop = 0
   # )

if __name__ == "__main__":
    main()