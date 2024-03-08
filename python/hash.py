from bin_operations import bin_sum, bin_mult, bin_div
from random import randint

bin_mode = True
alphabet = list(
    "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя ,.!?"
)


def calculate_hash(message):
    p = 17  # prime number
    q = 5  # prime number
    n = p * q  # p * q
    h = 3  # randint(1, 100)  # initialization vector

    if bin_mode:
        h = bin(h)

    for i, letter in enumerate(message):
        pos = alphabet.index(letter) + 1
        if bin_mode:
            sum = bin_sum(h, bin(pos))
            sqr = bin_mult(sum, sum)
            _, h = bin_div(sqr, bin(n))
        else:
            h = pow((h + pos), 2, n)
        print(f"h({i+1}): ", h)

    return h


def main():
    message = "достойно похвалы"  # input('Enter your message: ')

    message_hash = calculate_hash(message)
    print(f"Hash of the message: {message_hash}")


if __name__ == "__main__":
    main()
