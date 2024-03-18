ru_alphabet = list("абвгдеёжзийклмнопрстуфхцчшщъыьэюя")
en_alphabet = list("abcdefghijklmnopqrstuvwxyz")


def transform(text: str, shift: int, lang: list):
    res = ""

    for letter in text:
        if letter.lower() in lang:
            letter_pos = lang.index(letter.lower())
            new_letter = lang[(letter_pos + shift) % len(lang)]

            if letter.isupper():
                new_letter = new_letter.upper()
        else:
            new_letter = letter

        res += new_letter

    return res


def main():
    mode = input("Encrypt[e] or decrypt[d] (default is 'e'): ")
    message = input("Enter your message: ").strip()
    shift = input("Enter shift/key (default is '3'): ").strip()
    lang = input("Select alphabet: 'ru' or 'en' (default is 'ru'): ")

    shift = 3 if shift == "" else int(shift)

    if lang.strip().lower() == "en":
        lang = en_alphabet
    else:
        lang = ru_alphabet

    if mode.lower() == "d":
        res = transform(message, -shift, lang)
        print(f"Decrypted message is: {res}")
    else:
        res = transform(message, shift, lang)
        print(f"Encrypted message is: {res}")

    # --------------------- guess mode ---------------------
    #
    # if mode.lower() == "d":
    #     for i in range(1, len(lang)):
    #         print(f"{i}: {transform(message, -i, lang)}")
    # else:
    #     for i in range(1, len(lang)):
    #         print(f"{i}: {transform(message, i, lang)}")


if __name__ == "__main__":
    main()
