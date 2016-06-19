import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False

while not done:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True

  image = pygame.image.load("snake.png") 
  screen.blit(image, (136, 86))
        
  pygame.display.flip()
