import pygame
pygame.init()

WIDTH=1900
HEIGHT=1000
screen= pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill("white")

bg=pygame.image.load("Lesson 4 - Space Shooter/Images/space.png")
bgscale=pygame.transform.scale(bg,(1900,1000))
ys=pygame.image.load("Lesson 4 - Space Shooter/Images/spaceship_yellow.png")
ysscale=pygame.transform.scale(ys,(175,103))
ysrotate=pygame.transform.rotate(ysscale,90)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.blit(bg,(0,0))
    screen.blit(ysrotate,(500,500))
    pygame.display.update()