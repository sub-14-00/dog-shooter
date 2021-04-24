from pygame import *
from random import randint
import json

font.init()

class Button:
    def __init__(self,x,y,text,color=(204,186,186),h=50):
        self.text =text
        self.color = color
        letters = len(text)
        w = 60+letters*7
        self.x = x
        self.y = y
        self.rect = Rect(x,y,w,h)
        self.font = font.SysFont("Impact",20)
        self.textlabel = self.font.render(text,0,(0,0,0))
        
    def show(self):
        draw.rect(win, self.color, self.rect) #рисуем кнопку
        draw.rect(win, (0,0,0), self.rect,5) #обвводим
        win.blit(self.textlabel, (self.x+15, self.y+10) )
    
    def check_click(self,pos):
        return self.rect.collidepoint(pos)

class Basic(sprite.Sprite):

    def __init__(self,x,y,width,height,speed,image_name):
        super().__init__()

        self.image = image.load(image_name)
        self.image = transform.scale(self.image, (width,height))

        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.speed = speed

    def resetxy(self):
        self.rect.x = self.x
        self.rect.y = self.y

    def reset(self):
        win.blit( self.image, (self.x,self.y) )

class Hero(Basic):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a]:
            self.x -= self.speed
        if keys[K_d]:
            self.x += self.speed
        if keys[K_F5]:
            save_data()
        if keys[K_F9]:
            load_data()
        self.resetxy()
        self.reset()
    
    def fire(self):
        if len(bullets) < 5:
            b = Bullet(x=self.x, y=self.y,
            width=5, height=5, speed = 2, 
            image_name="bullet.png")
            bullets.add(b)
            shoot_sound.play()
        
class Bullet(Basic):
    def update(self):
        if self.y < 0:
            bullets.remove(self)
        self.y -= self.speed
        self.resetxy()
        self.reset()

class Enemy(Basic):
    def update(self):
        self.y += self.speed
        if self.y > h:
            self.y = 0
        self.resetxy()
        self.reset()
        if sprite.collide_rect(self,myay):
            exit()

def save_data():
    data_tmp = {"x":myay.x,"y":myay.y}
    with open("baza.json","w",encoding="utf-8") as file:
        json.dump(data_tmp,file,ensure_ascii=False)
    print("данные сохранены!",data_tmp)

def load_data():
    global data_tmp
    with open("baza.json","r",encoding="utf-8") as file:
        data_tmp = json.load(file)
    myay.x = data_tmp["x"]
    myay.y = data_tmp["y"]

myay = Hero(0,0,50,100,2,"hero.png")

w = 500
h = 500

win = display.set_mode( (w,h) )

bg = image.load("background.jpg")
bg = transform.scale(bg, (w,h) )

load_data()

run = True

enemys = sprite.Group()
bullets = sprite.Group()
def spawn_enemy():
    x = randint(0,w-50)
    new_enemy = Enemy(x,0,50,50,2,"enemy.png")
    enemys.add(new_enemy)

clock = time.Clock()
seconds = 0
old_seconds = 0

mixer.init()
mixer.music.load("bg.mp3")
mixer.music.play()

shoot_sound = mixer.Sound("shot_sound.ogg")

pause_b = Button(x=100,y=100,text="пауза")
play_b = Button(x=100,y=100,text="пуск")
gamemode = "игра"

while run:
    clock.tick(60)

    if gamemode == "игра":
        seconds += 1/60
        if int(seconds) != old_seconds:
            spawn_enemy()
            old_seconds += 1

        sprite.groupcollide(enemys,bullets,True,True)
        win.blit(bg, (0,0))
        pause_b.show()
        myay.update()
        enemys.update()
        bullets.update()
    if gamemode == "пауза":
        win.fill((0,0,0))
        play_b.show()
    display.update()

    for e in event.get():
        if e.type == QUIT:
            save_data()
            run = False
        if e.type == KEYUP:
            if e.key == K_SPACE:
                myay.fire()
        if e.type == MOUSEBUTTONDOWN:
            if e.button == 1:
                if gamemode == "игра":
                    if pause_b.check_click(e.pos):
                        gamemode = "пауза"
                elif gamemode == "пауза":
                    if play_b.check_click(e.pos):
                        gamemode = "игра"
            