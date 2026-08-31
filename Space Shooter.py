import pygame
pygame.init()

WIDTH=900
HEIGHT=600
screen= pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill("white")

ybullet=[]
rbullet=[]

bg=pygame.image.load("Lesson 4 - Space Shooter/Images/space.png")
bgscale=pygame.transform.scale(bg,(900,600))

ys=pygame.image.load("Lesson 4 - Space Shooter/Images/spaceship_yellow.png")
ysscale=pygame.transform.scale(ys,(50,50))
y=pygame.transform.rotate(ysscale,90)

rs=pygame.image.load("Lesson 4 - Space Shooter/Images/spaceship_red.png")
rsscale=pygame.transform.scale(rs,(50,50))
r=pygame.transform.rotate(rsscale,-90)

bsound=pygame.mixer.Sound("Lesson 4 - Space Shooter/Images/Gun+Silencer.mp3")

border=pygame.Rect(440,0,20,1000)
yrect=pygame.Rect(100,440,50,50)
rrect=pygame.Rect(800,300,50,50)

font1=pygame.font.SysFont("Impact",100)
yscore=5
rscore=5

def movey():
    if keys_pressed[pygame.K_w] and yrect.y>0:
        yrect.y=yrect.y-1
    if keys_pressed[pygame.K_a] and yrect.x>0:
        yrect.x=yrect.x-1
    if keys_pressed[pygame.K_s] and yrect.y<550:
        yrect.y=yrect.y+1
    if keys_pressed[pygame.K_d] and yrect.x<390:
        yrect.x=yrect.x+1

def mover():
    if keys_pressed[pygame.K_UP] and rrect.y>0:
        rrect.y=rrect.y-1
    if keys_pressed[pygame.K_DOWN] and rrect.y<550:
        rrect.y=rrect.y+1
    if keys_pressed[pygame.K_LEFT] and rrect.x>460:
        rrect.x=rrect.x-1
    if keys_pressed[pygame.K_RIGHT] and rrect.x<850:
        rrect.x=rrect.x+1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LCTRL:
                bullet=pygame.Rect(yrect.x+40,yrect.y+21,30,6)
                ybullet.append(bullet)
                bsound.play()
            if event.key == pygame.K_RCTRL:
                bullet=pygame.Rect(rrect.x-20,rrect.y+22,30,6)
                rbullet.append(bullet)
                bsound.play()
    keys_pressed = pygame.key.get_pressed()
    movey()
    mover()
    screen.blit(bg,(0,0))
    screen.blit(y,yrect)
    screen.blit(r,rrect)
    pygame.draw.rect(screen,"black",border)
    for i in ybullet:
        pygame.draw.rect(screen,"yellow",i)
        i.x+=1
    for i in rbullet:
        pygame.draw.rect(screen,"red",i)
        i.x-=1

    rhealth=font1.render("Lives: "+ str(rscore),True,"red")
    screen.blit(rhealth,(820,10))
    pygame.display.update()