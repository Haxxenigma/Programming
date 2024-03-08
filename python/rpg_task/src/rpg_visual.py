import pygame as pg
from lib.styles import *
from lib.battle import battle_render
from lib.input_box import InputBox
from lib.label import Label
from rpg_task2 import Character
import time
import sys


def main():
    running = True
    battle = False
    num, index = 1, 0
    size = 640, 360
    w, h = size

    screen = pg.display.set_mode(size)
    pg.display.set_caption("RPG Game")

    prompts = [
        "Введите свое имя:",
        "Введите количество здоровья [100]:",
        "Введите значение силы атаки [30]:",
        "Введите значение защиты [20]:",
        "Введите значение шанса уклонения [30]:",
        "Введите значение критического урона [75]:",
        "Введите значние шанса критического удара [50]:",
    ]

    input_w, input_h = 250, 32
    input_x = w / 2 - input_w / 2
    input_y = h / 2 - input_h / 2
    input_box = InputBox(input_x, input_y, input_w, input_h)

    label_y = input_y - 60
    label = Label(0, label_y, blue, True)

    title = Label(0, 50, blue, True)

    players_info = []
    player1_attacks = True
    player1 = None

    def init():
        for i in range(1, len(prompts)):
            players_info[i] = int(players_info[i])
        for i in range(len(prompts) + 1, len(prompts) * 2):
            players_info[i] = int(players_info[i])
        player1 = Character(*players_info[: len(prompts)])
        player2 = Character(*players_info[len(prompts) :])

        return player1, player2

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            num, index = input_box.handle_event(
                event, num, index, players_info, len(prompts)
            )
            if num > 2:
                running = False
                battle = True

        screen.fill((0, 0, 0))
        input_box.draw(screen)
        label.render(screen, f"Player {num}: {prompts[index]}")
        pg.display.flip()

    while battle:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                battle = False

        if not player1:
            player1, player2 = init()
            screen.fill((0, 0, 0))
            battle_render(screen, player1, player2)
            title.render(screen, "Битва начинается!")
            pg.display.flip()
            time.sleep(2)

        screen.fill((0, 0, 0))

        if player1_attacks:
            attacker = player1
            defender = player2
        else:
            attacker = player2
            defender = player1
        player1_attacks = not player1_attacks

        res = attacker.attack_player(defender)

        if res == "Miss!":
            color = red
        else:
            color = blue

        dmg_label = Label(defender.rect.left, 50, color)
        dmg_label.render(screen, str(res))
        battle_render(screen, player1, player2, attacker)
        pg.display.flip()

        time.sleep(1)

        screen.fill((0, 0, 0))
        battle_render(screen, player1, player2)
        pg.display.flip()
        time.sleep(1)

        if not player1.is_alive() or not player2.is_alive():
            while True:
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        sys.exit()
                screen.fill((0, 0, 0))
                winner = player1 if player1.is_alive() else player2
                title.render(screen, f"{winner} побеждает битву!")
                battle_render(screen, player1, player2, attacker, True)
                pg.display.flip()


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
