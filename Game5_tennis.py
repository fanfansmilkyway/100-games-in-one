from tkinter import *
import time
import random
import pygame
from playsound import playsound

print('按上下左右键移动, 按回车键(enter)击球')

class Game:
    def __init__ (self):
        tk = Tk()
        self.tk = tk
        self.shield_up = False
        self.tk.title('Game')
        self.tk.resizable(0, 0)
        self.tk.wm_attributes("-topmost", 1)
        self.canvas = Canvas(tk, width=800, height=400, bd=0,highlightthickness=0)
        self.canvas.configure(bg='white')
        self.canvas.pack()
        self.tk.update()

class Stickman:
    def __init__ (self, canvas):
        self.canvas = canvas
        self.images = PhotoImage(file='python-game-pic/stickman(Game5).gif')
        self.image = self.canvas.create_image(550, 100, anchor='nw', image=self.images)
        game.canvas.bind_all('<KeyPress-Left>', self.forward)
        game.canvas.bind_all('<KeyPress-Right>', self.backward)
        game.canvas.bind_all('<KeyPress-Down>', self.left)
        game.canvas.bind_all('<KeyPress-Up>', self.right)
        game.canvas.bind_all('<KeyRelease-Left>', self.stop)
        game.canvas.bind_all('<KeyRelease-Right>', self.stop)
        game.canvas.bind_all('<KeyRelease-Down>', self.stop)
        game.canvas.bind_all('<KeyRelease-Up>', self.stop)
        self.x = 0
        self.fx = 0
        self.y = 0
        self.fy = 0

    def forward(self, evt):
        self.x = 0
        self.fx = 3
        self.y = 0
        self.fy = 0
    def backward(self, evt):
        self.x = 3
        self.fx = 0
        self.y = 0
        self.fy = 0
    def left(self, evt):
        self.x = 0
        self.fx = 0
        self.y = 3
        self.fy = 0
    def right(self, evt):
        self.x = 0
        self.fx = 0
        self.y = 0
        self.fy = 3
    def stop(self, evt):
        self.x = 0
        self.fx = 0
        self.y = 0
        self.fy = 0

    def draw(self):
        pos = self.canvas.coords(self.image)
        wall_pos = wall.canvas.coords(wall.image)
        self.rect = pygame.Rect(pos[0]-30, pos[1]-30, 70, 110)
        if pos[0] + 70 >= wall_pos[0]:
            self.x = 0
        if pos[1] <= 0:
            self.fy = 0
        if pos[0] <= 200:
            self.fx = 0
        if pos[1] + 110 >= 400:
            self.y = 0
        self.canvas.move(self.image, self.x - self.fx, self.y - self.fy)

class Ball:
    def __init__(self, canvas, playsound, color):
        self.canvas = canvas
        self.playsound = playsound
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 550, 100)
        self.x = random.randint(-8, -4)
        self.y = random.randint(-3, 3)
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_times = 0
        game.canvas.bind_all('<KeyPress-space>', self.hit)

    def hit(self, evt):
        if self.stickman_crash_result:
            self.x = -8
            self.y = -self.y + random.randint(-5, 5)
            self.playsound('python-game-mp3/tennis_hit(Game5).mp3', block = False)
            self.hit_times += 1
        
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        self.rect = pygame.Rect(pos[0], pos[1], 10, 10)
        self.stickman_crash_result = False
        if pos[1] <= 0:
            self.y = 3
            self.playsound('python-game-mp3/tennis_wall(Game5).mp3', block = False)
        if pos[1] + 15 >= self.canvas_height:
            self.y = -3
            self.playsound('python-game-mp3/tennis_wall(Game5).mp3', block = False)
        if pos[0] <= 0:
            self.x = 4
            self.playsound('python-game-mp3/tennis_wall(Game5).mp3', block = False)
        if pos[0] + 15 >= self.canvas_width:
            self.x = -4
            self.playsound('python-game-mp3/tennis_wall(Game5).mp3', block = False)

class Wall:
    def __init__ (self, canvas):
        self.canvas = canvas
        self.images = PhotoImage(file='python-game-pic/wall(Game5).gif')
        self.image = self.canvas.create_image(780, -30, anchor='nw', image=self.images)
    def draw(self):
        pos = self.canvas.coords(self.image)
        self.rect = pygame.Rect(pos[0], pos[1], 30, 460)
        self.canvas.move(self.image, -0.05, 0)

game = Game()
canvas = game.canvas
tk = game.tk
stickman = Stickman(canvas)
ball = Ball(canvas, playsound, 'lime')
wall = Wall(canvas)

while 1:
    stickman.draw()
    ball.draw()
    wall.draw()
    ball.stickman_crash_result = pygame.sprite.collide_rect(stickman, ball)
    ball_wall_crash_result = pygame.sprite.collide_rect(ball, wall)
    if ball_wall_crash_result:
        break
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)

playsound('python-game-mp3/lose_game(Game5).mp3', block = True)
print('你失误了')
print('   ')
print('你一共连续击球了 %s 次' %(ball.hit_times))
