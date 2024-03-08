import random
import time


class Character:
    def __init__(self, name, max_xp, attack, defense, evasion, crit_dmg, crit_rate):
        self.name = name
        self.max_hp = max_xp
        self.hp = max_xp
        self.attack = attack
        self.defense = defense
        self.evasion = evasion
        self.crit_dmg = crit_dmg
        self.crit_rate = crit_rate
        self.level = 1
        self.experience = 0

    def attack_player(self, player):
        time.sleep(1)
        if random.randint(0, 100) > player.evasion:
            if random.randint(0, 100) > self.crit_rate:
                damage = self.attack * (1 + (self.crit_dmg / 100))
            else:
                damage = self.attack
            damage = damage + random.randrange(-5, 5)
            damage = max(0, damage - player.defense)
            player.hp -= damage
            print(f"[+] {self.name} атакует {player.name}, нанося {damage} урона!")
            if player.hp <= 0:
                print(f"\n{player.name} проиграл!")
        else:
            print(f"[-] {self.name} промахивается по {player.name}!")

    def is_alive(self):
        return self.hp > 0

    def gain_exp(self, experience):
        self.experience += experience
        if self.experience >= 100 * self.level:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.experience = 0
        self.max_hp += 20
        self.hp = self.max_hp
        self.attack += 15
        self.defense += 10
        self.evasion += 10
        self.crit_dmg += 20
        self.crit_rate += 10
        print(f"\n{self.name} поднялся на {self.level} уровень!")

    def display_stats(self):
        print("------------------------------------")
        print(f"Имя: {self.name}")
        print(f"Уровень {self.level}")
        print(f"Очки опыта={self.experience}/{100 * self.level}")
        print(f"Очки здоровья={self.hp}/{self.max_hp}")
        print(f"Сила атаки={self.attack}")
        print(f"Защита={self.defense}")
        print(f"Шанс уклонения={self.evasion}%")
        print(f"Критический урон={self.crit_dmg}%")
        print(f"Шанс критического попадания={self.crit_rate}%")
        print("------------------------------------")


def battle(player1, player2):
    print(f"\nБой между {player1.name} и {player2.name} начинается!")
    while player1.is_alive() and player2.is_alive():
        player1.attack_player(player2)
        player2.attack_player(player1)
    winner = player1 if player1.is_alive() else player2
    winner.gain_exp(50)
    print(f"{winner.name} побеждает битву и получает 50 очков опыта!")


def create_player(num):
    name = input(f"\nPlayer {num}: Введите свое имя: ")
    hp = int(input(f"Player {num}: Введите количество здоровья [100]: "))
    attack = int(input(f"Player {num}: Введите значение силы атаки [30]: "))
    defense = int(input(f"Player {num}: Введите значение защиты [20]: "))
    evasion = int(input(f"Player {num}: Введите значение шанса уклонения [30]: "))
    crit_dmg = int(input(f"Player {num}: Введите значение критического урона [75]: "))
    crit_rate = int(
        input(f"Player {num}: Введите значние шанса критического удара [50]: ")
    )

    return Character(name, hp, attack, defense, evasion, crit_dmg, crit_rate)


if __name__ == "__main__":
    player1 = create_player(1)
    player2 = create_player(2)

    player1.display_stats()
    player2.display_stats()

    battle(player1, player2)

    player1.display_stats()
    player2.display_stats()
