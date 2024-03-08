def text_to_hex(text):
    hex_value = " ".join(hex(ord(char))[2:] for char in text)
    return hex_value


def hex_to_text(hex_value):
    hex_value = hex_value.replace(" ", "")
    text = bytearray.fromhex(hex_value).decode()
    return text


def url_encode(text):
    encoded_text = ""
    for char in text:
        if char.isalnum() or char in ["-", "_", ".", "~"]:
            encoded_text += char
        else:
            encoded_text += "%" + hex(ord(char))[2:].upper()
    return encoded_text


def url_decode(text):
    decoded_text = ""
    i = 0
    while i < len(text):
        if text[i] == "%":
            decoded_text += chr(int(text[i + 1 : i + 3], 16))
            i += 3
        else:
            decoded_text += text[i]
            i += 1
    return decoded_text


def base64_encode(text):
    charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

    def byte_to_binary(byte):
        binary = bin(byte)[2:].rjust(8, "0")
        return binary

    byte = text.encode("utf-8")
    binary = [byte_to_binary(b) for b in byte]
    binary = "".join(binary)

    while len(binary) % 6 != 0:
        binary += "0"
    groups = [binary[i : i + 6] for i in range(0, len(binary), 6)]
    base64_chars = [charset[int(group, 2)] for group in groups]
    padding = (3 - len(byte) % 3) % 3
    base64_chars += ["="] * padding
    base64_text = "".join(base64_chars)
    return base64_text


def base64_decode(base64_text):
    charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    padding_char = "="

    def base64_char_to_bits(char):
        bits = charset.index(char)
        bits = bin(bits)[2:].rjust(6, "0")
        return bits

    if padding_char in base64_text:
        base64_text = base64_text[: base64_text.index(padding_char)]
    binary = [base64_char_to_bits(char) for char in base64_text]
    binary = "".join(binary)
    groups = [binary[i : i + 8] for i in range(0, len(binary), 8)]
    text_chars = [chr(int(group, 2)) for group in groups]
    text = "".join(text_chars)
    return text


choose = input(
    "Choose: \n [1] text to hex \n [2] hex to text \n [3] url encode \n [4] url decode \n [5] base64 encode \n [6] base64 decode \n Enter: "
)

match choose:
    case "1":
        input_text = input("Enter your text: ")
        hex_value = text_to_hex(input_text)
        print(f"Output: {hex_value}")
    case "2":
        input_hex = input("Enter your hex value: ")
        text = hex_to_text(input_hex)
        print(f"Output: {text}")
    case "3":
        input_text = input("Enter your text: ")
        url_encoded = url_encode(input_text)
        print(f"Output: {url_encoded}")
    case "4":
        input_url_encoded = input("Enter you URL encoded text: ")
        url_decoded = url_decode(input_url_encoded)
        print(f"Output: {url_decoded}")
    case "5":
        input_text = input("Enter your text: ")
        base64_encoded = base64_encode(input_text)
        print(f"Output: {base64_encoded}")
    case "6":
        input_base64_encoded = input("Enter your Base64 encoded text: ")
        base64_decoded = base64_decode(input_base64_encoded)
        print(f"Output: {base64_decoded}")
    case _:
        print(f"Sorry, I couldn't understand {choose!r}")
