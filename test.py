import pygame
pygame.init()
pygame.font.init()

shrift = pygame.font.Font(None, 70 )
text = shrift.render("привет!",False, (0,0,255) )

win = pygame.display.set_mode((500,500))
win.blit(text, (0,0) )
x = 0
timer = pygame.time.Clock()

while True:
    for i in pygame.event.get():
        if i.type == 12:
            exit()
    x += 1
    text = shrift.render(str(x),False, (0,0,255) )
    win.fill( (255,255,255) )
    win.blit(text, (x,0) )
    timer.tick(60)
    pygame.display.update()