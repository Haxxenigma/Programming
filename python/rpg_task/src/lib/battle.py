import pygame as pg
from lib.styles import *
from random import choice


def battle_render(screen, player1, player2, attacker=None, battle_ends=False):
    players = [player1, player2]
    images = ["imgs/player1.png", "imgs/player2.png"]
    # move_cords = [(640 / 4) - (60 / 2), 640 - (640 / 4) - (60 / 2)]
    x1, x2 = 110, 430
    move_cords = [x1, x2]

    if attacker == player1:
        random_img = ["imgs/player3.png", "imgs/player3_bonus.png"]
        images = [choice(random_img), "imgs/player6.png"]
        move_cords = [330, x2]
    elif attacker == player2:
        random_img = ["imgs/player4.png", "imgs/player4_bonus.png"]
        images = ["imgs/player5.png", choice(random_img)]
        move_cords = [x1, 210]

    if battle_ends:
        if attacker == player1:
            images = ["imgs/player_winner1.png", "imgs/player_looser2.png"]
            move_cords = [x1, x2]
        elif attacker == player2:
            images = ["imgs/player_looser1.png", "imgs/player_winner2.png"]
            move_cords = [x1, x2]

    for i, player in enumerate(players):
        player.display_init(images[i], move_cords[i])
        if attacker:
            player.move(images[i], move_cords[i])
        player.display(screen)
