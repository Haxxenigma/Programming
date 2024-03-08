from random import randint
from math import gcd
from sys import exit

try:
    def find_coprime(n):
        while True:
            candidate = randint(2, n - 1)
            if (gcd(n, candidate) == 1):
                return candidate

    def gen_key():
        p = 71                  # prime number
        q = 37                  # prime number
        n = p * q
        phi = (p - 1) * (q - 1)
        e = find_coprime(phi)   # coprime with phi

        k = 1
        while True:
            candidate = (k * phi + 1) / e
            if (candidate % 1 == 0):
                d = int(candidate)
                break
            k += 1

        public_key = e, n
        private_key = d, n

        return public_key, private_key

    def encrypt(message, public_key):
        e, n = public_key
        ciphertext = []

        for letter in message:
            pos = alphabet.index(letter) + 1
            ciphertext.append(pow(pos, e, n))

        return ciphertext

    def decrypt(ciphertext, private_key):
        d, n = private_key
        message = []

        for letter in ciphertext:
            pos = pow(letter, d, n)
            message.append(alphabet[pos - 1])

        return ''.join(message)

    if __name__ == '__main__':
        alphabet = list('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя ,.!?')
        message = input('Enter your message: ')

        public_key, private_key = gen_key()
        print(f'\nPublic key: {public_key}; Private key: {private_key}')

        ciphertext = encrypt(message, public_key)
        print(f'Encrypted message: {ciphertext}')

        message = decrypt(ciphertext, private_key)
        print(f'Decrypted message: {message}')
except KeyboardInterrupt:
    print('\nExiting...')
    exit()