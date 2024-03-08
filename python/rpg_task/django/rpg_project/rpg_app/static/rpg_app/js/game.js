class Player {
    constructor(name, maxXp, attack, defense, evasion, critDmg, critRate) {
        this.name = name;
        this.maxHp = maxXp;
        this.hp = maxXp;
        this.attack = attack;
        this.defense = defense;
        this.evasion = evasion;
        this.critDmg = critDmg;
        this.critRate = critRate;
        this.level = 1;
        this.experience = 0;
    }

    attackPlayer(player) {
        let damage;
        if (Math.random() > (player.evasion / 100)) {
            if (Math.random() > (this.critRate / 100)) {
                damage = this.attack * (1 + (this.critDmg / 100));
            } else {
                damage = this.attack;
            }
            damage = damage + Math.floor(Math.random() * 10) - 5;
            damage = Math.max(0, damage - player.defense);
            player.hp -= damage;
            console.log(`[+] ${this.name} атакует ${player.name}, нанося ${damage} урона!`);
            // if (player.hp <= 0) {
            //     console.log(`\n${player.name} проигрывает!`);
            // }
        } else {
            console.log(`[-] ${this.name} промахивается по ${player.name}!`);
        }
    }

    isAlive() {
        return this.hp > 0;
    }
}

$(document).ready(function () {
    const canvas = document.getElementById('rpg_canvas');
    const ctx = canvas.getContext('2d');

    const player1img = document.getElementById('player1');
    const player2img = document.getElementById('player2');
    const player3img = document.getElementById('player3');
    const player4img = document.getElementById('player4');
    const player5img = document.getElementById('player5');
    const player6img = document.getElementById('player6');
    const player1Win = document.getElementById('player1_win');
    const player2Win = document.getElementById('player2_win');
    const player1Loose = document.getElementById('player1_loose');
    const player2Loose = document.getElementById('player2_loose');

    ctx.drawImage(player1img, 10, 10);
    ctx.drawImage(player2img, 200, 10);

    function create_player(i) {
        const name = prompt(`Player ${i}: Введите свое имя: `, `Player ${i}`);
        const hp = parseInt(prompt(`Player ${i}: Введите количество здоровья: `, 100));
        const damage = parseInt(prompt(`Player ${i}: Введите значение силы атаки: `, 30));
        const defense = parseInt(prompt(`Player ${i}: Введите значение защиты: `, 10));
        const evasion = parseInt(prompt(`Player ${i}: Введите значение шанса уклонения: `, 15));
        const critDmg = parseInt(prompt(`Player ${i}: Введите значение критического урона: `, 75));
        const critRate = parseInt(prompt(`Player ${i}: Введите значние шанса критического удара: `, 15));

        return new Player(name, hp, damage, defense, evasion, critDmg, critRate);
    }

    const player1 = create_player(1);
    const player2 = create_player(2);

    let attacker = player1;

    function attack(attacker) {
        const defender = attacker === player1 ? player2 : player1;
        let xpos1, xpos2;
        let attack_img, defend_img;

        if (attacker === player1) {
            xpos1 = 140; xpos2 = 200;
            attack_img = player3img;
            defend_img = player6img;
        } else {
            xpos1 = 60; xpos2 = 10;
            attack_img = player4img;
            defend_img = player5img;
        }

        setTimeout(() => {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            ctx.drawImage(attack_img, xpos1, 10);
            ctx.drawImage(defend_img, xpos2, 10);
            attacker.attackPlayer(defender);

            setTimeout(() => {
                ctx.clearRect(0, 0, canvas.width, canvas.height);
                ctx.drawImage(player1img, 10, 10);
                ctx.drawImage(player2img, 200, 10);
                if (player1.isAlive() && player2.isAlive()) {
                    attack(attacker === player1 ? player2 : player1);
                } else {
                    if (player1.isAlive()) {
                        var winPosX = 10;
                        var loosePosX = 180;
                        var looseImg = player2Loose;
                        var winImg = player1Win;
                        var winner = player1;
                    } else {
                        var winPosX = 200;
                        var loosePosX = 10;
                        var looseImg = player1Loose;
                        var winImg = player2Win;
                        var winner = player2;
                    }
                    ctx.clearRect(0, 0, canvas.width, canvas.height);
                    ctx.drawImage(winImg, winPosX, 5);
                    ctx.drawImage(looseImg, loosePosX, 15);
                    console.log(`${winner.name} выигрывает битву!`);
                }
            }, 500);
        }, 1000);
    }

    attack(attacker);
});