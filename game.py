import pygame
pygame.init()

screenWidth=720
screenHeight=720
run=True

bl=(255,105,180)
white=(255,255, 255)
x=50
y=50
width=50
height=50
speed=40
isJump= False
jumpCount=10

win=pygame.display.set_mode((screenHeight, screenWidth))
pygame.display.set_caption("New", "My")

while run:
#for (this) event
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
    key=pygame.key.get_pressed()

    if key[pygame.K_LEFT] and x>0:
        x-=speed
    if key[pygame.K_RIGHT] and x<screenWidth-width-100:
        x+=speed
    if not isJump:
        if key[pygame.K_UP] :
            isJump=True
    else:
        if jumpCount >=-10:
            if jumpCount>0:
                y-=(jumpCount**2)*0.5
            else:
                y+=(jumpCount**2)*0.5
            jumpCount-=1
        else:
            jumpCount=10
            isJump=False

    if key[pygame.K_DOWN] and y<screenHeight-height-100:
        y+=speed

    win.fill((0, 120, 255))
    pygame.draw.rect(win, white,(x,y, width, height))
    #pygame.draw.circle(win, bl, (20,15), 15)
    #Lets disable for now circluar object

    pygame.display.update()

pygame.quit()
