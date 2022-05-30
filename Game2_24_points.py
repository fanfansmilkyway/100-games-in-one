# coding=utf-8

import sys
import time
import random

print('欢迎参加24点游戏！')
print('规则自己摸索一下吧！')
other_player_points = 0
message_1 = '你的目前点数是%s.'
message_2 = '你抽到了%s.'
message_3 = '对手的第 %s 张牌是%s.'
message_4 = '对手的点数一共是 %s 点 '
messgae_5 = '你的点数是 %s，超过了24，你爆牌了！'
a = 0
player_card= 0
player_points = 0
cards = ['1','2','3','4','5','6','7','8','9','10','11','12','13']
c = 0
while True:
    player_card = int(random.choice(cards))
    time.sleep(1)
    print(' ')
    print('你是否要加牌？(否0/是1)')
    whether_add_card =int(sys.stdin.readline())
    if whether_add_card == 1 :
        time.sleep(0.2)
        print(message_2 %(player_card))
        player_points = player_points + player_card
        if player_points > 24:
            break
        time.sleep(0.4)
        print(message_1 % player_points)

    if whether_add_card == 0:
        other_player_card1 = int(random.choice(cards))
        other_player_card2 = int(random.choice(cards))
        other_player_card3 = int(random.choice(cards))
        c = c+1
        time.sleep(0.7)
        print(message_3 %(c,other_player_card1))
        c = c+1
        time.sleep(0.7)
        print(message_3 %(c,other_player_card2))
        c = c+1
        time.sleep(0.7)
        print(message_3 %(c,other_player_card3))
        other_player_points = other_player_card1 + other_player_card2 + other_player_card3
        print(' ')
        print(message_4 %(other_player_points))
        print(' ')
        time.sleep(1)
        break
if player_points > 24:
    time.sleep(0.5)
    print('你的点数是 %s，超过了24，你爆牌了！' % player_points)
    time.sleep(0.5)
    print(' ')
    print(' ')
    print('你输了！')
    time.sleep(1)
    print('bye~~~')
    time.sleep(0.5)
    sys.exit(0)
if other_player_points > 24:
    time.sleep(0.5)
    print('对手爆牌！')
    time.sleep(0.5)
    print(' ')
    print(' ')
    print('你赢了！！！')
    time.sleep(1)
    print('bye~~~')
    time.sleep(0.5)
    sys.exit(0)
if other_player_points > player_points:
    time.sleep(0.5)
    print("你的点数是 %s, 对手的点数是 %s, 他比你更大！" % (player_points, other_player_points))
    time.sleep(0.5)
    print(' ')
    print(' ')
    print('你输了')
    time.sleep(1)
    print('bye~~~')
    time.sleep(0.5)
    sys.exit(0)
if other_player_points < player_points:
    time.sleep(0.5)
    print("你的点数是 %s, 对手的点数是 %s, 你比他更大！!" % (player_points, other_player_points))
    time.sleep(0.5)
    print(' ')
    print(' ')
    print('你赢了！！！')
    time.sleep(1)
    print('bye~~~')
    time.sleep(0.5)
    sys.exit(0)
if other_player_points == player_points:
    time.sleep(0.5)
    print("你的点数是 %s, 对手的点数是 %s, 你们都一样" % (player_points, other_player_points))
    time.sleep(0.5)
    print(' ')
    print(' ')
    print('平手！')
    time.sleep(1)
    print('bye~~~')
    time.sleep(0.5)
    sys.exit(0)