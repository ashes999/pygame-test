import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
done = False

image = pygame.image.load("logo.png")

while not done:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True

  screen.blit(image, (70, 190))
        
  pygame.display.flip()
