import sys
import os
from tkinter import *


message = '''                           游戏目录

                游戏名称:           游戏难度(最高10,最低0):     好玩程度(最高10,最低0)

                1.猜数字游戏                7                          1
                2. 24点                    3                          4
                3.躲球                     5                          6
                4.邪恶马里奥                5                          5
                5.网球                     6                          6
        '''

print(message)
game = int(sys.stdin.readline())

if game == 1:   #猜数字游戏（1）
    os.system('python3 Game1_guess_number.py')
    
if game == 2:   #24点 (2)
    os.system('python3 Game2_24_points.py')

if game == 3:   #躲球 (3)
    os.system('python3 Game3_running_balls.py')

if game == 4:   #邪恶马里奥(4)
    os.system('python3 Game4_bad_mario.py')  
    
if game == 5:   #网球(5)
    os.system('python3 Game5_tennis.py')

mainloop()
        


