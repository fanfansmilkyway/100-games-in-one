# coding=utf-8

from tkinter import *
import time
import pygame
import sys
import random
from playsound import playsound

print('马里奥成为了邪恶王国的首领,快来打倒他的城墙,拯救世界吧哈哈哈!')

class Game:
    def __init__ (self):
        tk = Tk()
        self.tk = tk
        self.shield_up = False
        self.tk.title('Game')
        self.tk.resizable(0, 0)
        self.tk.wm_attributes("-topmost", 1)
        self.canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
        self.canvas.configure(bg='white')
        self.canvas.pack()
        self.tk.update()

class Bullet:
    def __init__ (self, canvas, playsound):
        self.canvas = canvas
        self.playsound = playsound
        self.images = PhotoImage(file='python-game-pic/bullet(Game4).gif')
        self.image = self.canvas.create_image(450, 280, anchor='nw', image=self.images)
        self.canvas.bind_all('<KeyPress-Return>', self.fire)
        self.flying = False
        self.x = 0

    def fire(self, evt):
        if game.shield_up == False and self.flying == False:
            self.x = -10
            self.flying = True
            self.playsound('python-game-mp3/stickman_shooting(Game4).mp3', block=False)


    def draw(self):
        self.canvas.move(self.image, self.x, 0)
        pos = self.canvas.coords(self.image)
        self.rect = pygame.Rect(pos[0], pos[1], 10, 10)
        if pos[0] <= -500:
            self.x = 0
            self.playsound('python-game-mp3/stickman_reload(Game4).mp3' , block=False)
            self.canvas.move(self.image, 940, 0)
            self.flying = False


class Stickman:
    def __init__ (self, canvas):
        self.canvas = canvas
        self.images =  PhotoImage(file='python-game-pic/stickman1(shield-down)(Game4).gif')
        self.image = self.canvas.create_image(350, 200, image=self.images, anchor='nw')

    def draw(self):
        self.rect = pygame.Rect(410, 300, 250, 206)
    

class Shield:
    def __init__ (self, canvas):
        self.canvas = canvas
        self.images = [PhotoImage(file='python-game-pic/shield(down)(Game4).gif'),
            PhotoImage(file='python-game-pic/shield(up)(Game4).gif')
            ]
        self.image = self.canvas.create_image(360, 300, image=self.images[0], anchor='nw')
        game.canvas.bind_all('<KeyPress-space>',self.shield_up)
        game.canvas.bind_all('<KeyRelease-space>',self.shield_down)

    def shield_up(self, evt):
        game.canvas.itemconfig(self.image, image=self.images[1])
        game.shield_up = True

    def shield_down(self, evt):
        game.canvas.itemconfig(self.image, image=self.images[0])
        game.shield_up = False

    def draw(self):
        pos = self.canvas.coords(self.image)
        self.rect = pygame.Rect(pos[0] - 20, pos[1] - 20, 100, 100)


class Wall:
    def __init__ (self, canvas):
        self.canvas = canvas
        self.images = PhotoImage(file='python-game-pic/wall(Game4).gif')
        self.image = self.canvas.create_image(50, 70, image=self.images, anchor='nw')
    def draw(self):
        self.rect = pygame.Rect(50, 70, 100, 450)

class Boss:
    def __init__ (self, canvas):
        self.canvas = canvas
        self.images = PhotoImage(file='python-game-pic/boss(Game4).gif')
        self.image = self.canvas.create_image(50, 10, image=self.images, anchor='nw')

class Ghost:
    def __init__ (self, canvas, playsound):
        self.canvas = canvas
        self.playsound =  playsound
        self.images = PhotoImage(file='python-game-pic/ghost(Game4).gif')
        self.image = self.canvas.create_image(60, 10, image=self.images, anchor='nw')
        self.shield_crash_result = False
        self.x = 0
        self.y = 0

    def draw(self):
        whether_fire = random.randint(1, 300)
        pos = self.canvas.coords(self.image)
        self.rect = pygame.Rect(pos[0], pos[1], 20, 20)
        if whether_fire == 150:
            self.playsound('python-game-mp3/ghost_laugh(Game4).mp3' , block = False)
            self.x = 30
            self.y = 25
        if pos[0] + 20 >= 340 and game.shield_up == True:
            self.x = 0
            self.y = 0
            self.canvas.move(self.image, -270, -220)
            self.playsound('python-game-mp3/Shield_block(Game4).mp3' , block = False)

        self.canvas.move(self.image, self.x, self.y)
 

game = Game()
canvas = game.canvas


bullet = Bullet(canvas, playsound)
shield = Shield(canvas)
stickman = Stickman(canvas)
wall = Wall(canvas)
enermy = Boss(canvas)
ghost = Ghost(canvas, playsound)

wall_health = 100

while 1:
    stickman.draw()
    bullet.draw()
    wall.draw()
    ghost.draw()
    shield.draw()
    wall_crash_result = pygame.sprite.collide_rect(bullet, wall)
    stickman_crash_result = pygame.sprite.collide_rect(ghost, stickman)
    if wall_crash_result:
        wall_health -= 1
        print(wall_health)
    if wall_health <= 0:
        print('恭喜你!你打败了邪恶马里奥!!!')
        time.sleep(1)
        sys.exit(0)
    if stickman_crash_result:
        playsound('python-game-mp3/stickman_dead(Game4).mp3' , block = False)
        print('你被邪恶马里奥的幽灵手下杀死了!')
        time.sleep(1)
        sys.exit(0)
    game.tk.update_idletasks()
    game.tk.update()
    time.sleep(0.01)