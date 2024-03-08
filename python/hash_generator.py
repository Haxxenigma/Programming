import hashlib
import bcrypt

choose = input("Choose: \n [1] MD5 \n [2] SHA-256 \n [3] bcrypt \n Enter: ")
match choose:
    case "1":
        text = input("Enter text to hash: ")
        hash_object = hashlib.md5()
        hash_object.update(text.encode("utf-8"))
        md5_hash = hash_object.hexdigest()
        print("Hash value MD5:", md5_hash)
        result = md5_hash
    case "2":
        text = input("Enter text to hash: ")
        hash_object = hashlib.sha256()
        hash_object.update(text.encode("utf-8"))
        sha256_hash = hash_object.hexdigest()
        print("Hash value SHA-256:", sha256_hash)
        result = sha256_hash
    case "3":
        text = input("enter text to hash: ")
        salt = bcrypt.gensalt()
        bcrypt_hash = bcrypt.hashpw(text.encode("utf-8"), salt)
        print("hash value bcrypt:", bcrypt_hash.decode("utf-8"))
        result = bcrypt_hash.decode("utf-8")
    case _:
        print(f"Sorry, I couldn't understand {choose!r}")
        result = False


if result != False:
    if input("\nEnter a hash value to match against the received value: ") == result:
        print("Fully matches!")
    else:
        print("Doesn't match!")
