from random import randint
import pygame
pygame.init()
pygame.font.init()

class TextArea():
    def __init__(self,x,y,w,h,color,text):
        self.rect = pygame.Rect(x,y,w,h)
        self.color = color
        pygame.draw.rect(win,color,self.rect)
        self.text = qfont.render(text,True, (0,0,0) )
        win.blit(self.text, (x,y))
    
    def set_text(self,new_text):
        pygame.draw.rect(win,self.color,self.rect)
        self.text = qfont.render(new_text,True, (0,0,0) )
        win.blit(self.text, (self.rect.x,self.rect.y))

win = pygame.display.set_mode( (500,500) )

win.fill( (0,100,46) )

qfont = pygame.font.Font(None,50)

quest = qfont.render("Вопрос:",True, (255,0,0) )
ans = qfont.render("Ответ:",True, (255,0,0) )

win.blit( quest, (50,50) )
win.blit( ans, (50,150) )

quest_table = TextArea(100,100,300,30,(0,255,0),"сколько тебе лет?")
ans_table = TextArea(100,200,300,30,(0,255,0),"9999")

pygame.display.update()

timer = pygame.time.Clock()

while True:
    timer.tick(40)
    for e in pygame.event.get():
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_q:
                quest_table.set_text("нажата кнопка q?")
            if e.key == pygame.K_a:
                ans_table.set_text("я не знаю....")

    pygame.display.update()



