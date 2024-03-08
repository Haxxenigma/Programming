from random import randint
from sys import exit

try:
    def gen_key():
        p = 71                  # prime number; p > m
        g = 7                   # primitive root; g^(p-1) % p == 1 % p
        x = randint(2, p - 2)   # 1 < x < p - 1
        y = pow(g, x, p)

        public_key = p, g, y
        private_key = x

        return public_key, private_key

    def encrypt(message, public_key):
        p, g, y = public_key
        k = randint(2, p - 2)   # 1 < k < p - 1
        a = pow(g, k, p)
        b = []

        for letter in message:
            # pos = alphabet.index(letter) + 1
            # b.append(pos * y ** k % p)

            pos = alphabet.index(letter) + 1            # to be represented as letters instead of numbers
            cipherletter = alphabet[pos * y ** k % p]   # to be represented as letters instead of numbers
            b.append(cipherletter)                      # to be represented as letters instead of numbers

        b = ''.join(b)                                  # to be represented as letters instead of numbers
        return a, b

    def decrypt(ciphertext, private_key, p):
        a, b = ciphertext
        message = []

        for letter in b:
            # pos = letter * a ** (p - 1 - private_key) % p
            # message.append(alphabet[pos - 1])

            cipherpos = alphabet.index(letter)                  # to be represented as letters instead of numbers
            pos = cipherpos * a ** (p - 1 - private_key) % p    # to be represented as letters instead of numbers
            message.append(alphabet[pos - 1])                   # to be represented as letters instead of numbers

        return ''.join(message)

    if __name__ == '__main__':
        alphabet = list('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя ,.!?')
        message = input('Enter your message: ')

        public_key, private_key = gen_key()
        print(f'\nPublic key: {public_key}; Private key: {private_key}')

        ciphertext = encrypt(message, public_key)
        print(f'Encrypted message: {ciphertext}')

        message = decrypt(ciphertext, private_key, public_key[0])
        print(f'Decrypted message: {message}')
except KeyboardInterrupt:
    print('\nExiting...')
    exit()