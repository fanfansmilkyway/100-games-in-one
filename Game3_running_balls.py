# coding=utf-8

from tkinter import *
import pygame
import random
import time
import sys

print('按上下左右键控制你的火柴人')
time_start = time.time()

class Game:
    def __init__ (self):
        tk = Tk()
        self.tk = tk
        self.tk.title("Game")
        self.tk.resizable(0, 0)
        self.tk.wm_attributes("-topmost", 1)
        self.canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
        self.canvas.pack()
        self.tk.update()

class Ball:
    def __init__(self, canvas, color):
        self.move_x = random.randint(50, 450)
        self.move_y = random.randint(50,180)
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, self.move_x, self.move_y)
        starts_x = [-5, -4, -2, 2, 4, 5]
        random.shuffle(starts_x)
        self.x = starts_x[0]
        starts_y = [-5, -4, -2, 0, 2, 3]
        random.shuffle(starts_y)
        self.y = starts_y[0]
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        self.rect = pygame.Rect(pos[0], pos[1], 15, 15)
        if pos[1] <= 0:
            self.y = 3
        if pos[1] + 30 >= self.canvas_height:
            self.y = -3
        if pos[0] <= 0:
            self.x = 4
        if pos[0] + 27 >= self.canvas_width:
            self.x = -4

class Stickman:
    def __init__ (self,canvas):
        self.canvas = canvas
        self.image = PhotoImage(file='python-game-pic/stickman1(Game3).gif')
        self.id = self.canvas.create_image(200, 270, anchor=NW, image=self.image)
        self.canvas.pack()
        self.canvas.bind_all('<KeyPress-Up>', self.forward)
        self.canvas.bind_all('<KeyPress-Down>', self.backward)
        self.canvas.bind_all('<KeyPress-Left>', self.left)
        self.canvas.bind_all('<KeyPress-Right>', self.right)
        self.x = 0
        self.y = 0
        self.fx = 0
        self.fy = 0
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
    def forward(self, evt):
        self.x = 0
        self.y = 0
        self.fx = 0
        self.fy = 3
    def backward(self, evt):
        self.x = 0
        self.y = 3
        self.fx = 0
        self.fy = 0
    def left(self, evt):
        self.x = 0
        self.y = 0
        self.fx = 3
        self.fy = 0
    def right(self, evt):
        self.x = 3
        self.y = 0
        self.fx = 0
        self.fy = 0
    def draw(self):
        pos = self.canvas.coords(self.id)
        self.rect = pygame.Rect(pos[0], pos[1], 27, 30)
        if pos[1] <= 0:
            self.fy = 0
        if pos[1] + 30 >= self.canvas_height:
            self.y = 0
        if pos[0] <= 0:
            self.fx = 0
        if pos[0] + 27 >= self.canvas_width:
            self.x = 0
        self.canvas.move(self.id, self.x - self.fx, self.y - self.fy)

        
game = Game()
canvas = game.canvas
tk = game.tk

ball1 = Ball(canvas, 'red')
ball2 = Ball(canvas, 'blue')
ball3 = Ball(canvas, 'purple')
stickman = Stickman(canvas)

while 1:
    ball1.draw()
    ball2.draw()
    ball3.draw()
    stickman.draw()
    tk.update_idletasks()
    tk.update()

    crash_result_ball1 = pygame.sprite.collide_rect(ball1, stickman)
    crash_result_ball2 = pygame.sprite.collide_rect(ball2, stickman)
    crash_result_ball3 = pygame.sprite.collide_rect(ball3, stickman)

    if crash_result_ball1 == 1 or crash_result_ball2 == 1 or crash_result_ball3 == 1:
        break
    time.sleep(0.01)

time_end = time.time()
survival_time = format(time_end - time_start, '.2f')
print('你一共生存了%s秒' %(survival_time))
time.sleep(0.3)
print('bye~~~')