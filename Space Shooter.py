import pygame
pygame.init()

WIDTH=1900
HEIGHT=1000
screen= pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill("white")

bg=pygame.image.load("Lesson 4 - Space Shooter/Images/space.png")
bgscale=pygame.transform.scale(bg,(1900,1000))

ys=pygame.image.load("Lesson 4 - Space Shooter/Images/spaceship_yellow.png")
ysscale=pygame.transform.scale(ys,(175,130))
y=pygame.transform.rotate(ysscale,90)

rs=pygame.image.load("Lesson 4 - Space Shooter/Images/spaceship_red.png")
rsscale=pygame.transform.scale(rs,(175,130))
r=pygame.transform.rotate(rsscale,-90)

border=pygame.Rect(940,0,20,1000)
yrect=pygame.Rect(100,440,175,130)
rrect=pygame.Rect(1700,425,175,130)

def movey():
    if keys_pressed[pygame.K_w] and yrect.y>0:
        yrect.y=yrect.y-1
    if keys_pressed[pygame.K_a] and yrect.x>0:
        yrect.x=yrect.x-1
    if keys_pressed[pygame.K_s] and yrect.y<825:
        yrect.y=yrect.y+1
    if keys_pressed[pygame.K_d] and yrect.x<825:
        yrect.x=yrect.x+1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    keys_pressed = pygame.key.get_pressed()
    movey()
    screen.blit(bg,(0,0))
    screen.blit(y,yrect)
    screen.blit(r,rrect)
    pygame.draw.rect(screen,"black",border)
    pygame.display.update()