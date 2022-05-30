# coding=utf-8

import random
import time
import sys

num = random.randint(1,1000)
times = 0
print("欢迎参加猜数字游戏！")
print('规则：猜一个1到1000的数，才对了则游戏胜利并结束')
time.sleep(1)
print(' ')
print('游戏开始！！！')

while True:
    print(' ')
    print('请猜一个从1到1000的数字')
    guess = input()
    if isinstance(guess, int) == False:
        time.sleep(0.5)
        print(' ')
        print('请输入正整数!')
        continue
    message = '你猜对了！！！恭喜🎉！你一共用了 %s 次'
    i = int(guess)
    if i == num:
        for a in range(0,4):
            print(' ')
        print(message %(times))
        break
    if i < num:
        time.sleep(0.5)
        print(' ')
        print('你猜小了，再试一遍吧')
        times = times + 1
    if i > num:
        time.sleep(0.5)
        print(' ')
        print('你猜大了，再试一遍吧')
        times = times + 1
    if abs(i - num)< 50:
        time.sleep(0.55)
        print(' ')
        print('很接近了！！')
        
time.sleep(1)
for b in range(0,2):
    print(' ')
print("游戏结束！！！")