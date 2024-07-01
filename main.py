import random

ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
ASCII_ = ascii_lowercase + ascii_uppercase + digits

MIN_KEY_LENGTH = 4
MAX_KEY_LENGTH = 8


def encrypt(text):
    """
    :param text:
    :return:
    """
    key_ = ""
    length = random.randint(MIN_KEY_LENGTH, MAX_KEY_LENGTH)
    for i in range(0, length):
        key_ += ASCII_[random.randint(0, len(ASCII_) - 1)]
    counter = 0
    encrypted_text_ = ""

    for y in range(0, len(text)):
        if counter >= len(key_):
            counter = 0
        encrypted_text_ += chr(ord(key_[counter]) + ord(text[y]))
        counter += 1
    return encrypted_text_, key_


def decrypt(encrypted_text_, key_):
    """
    :param encrypted_text_:
    :param key_:
    :return:
    """
    decrypted_text_ = ""
    counter = 0

    for y in range(0, len(encrypted_text_)):
        if counter >= len(key_):
            counter = 0
        decrypted_text_ += chr(abs(ord(encrypted_text_[y]) - ord(key_[counter])))
        counter += 1
    return decrypted_text_


encrypted_text, key = encrypt("Hello world!")

# encrypted_text = "«¥¥Õk½¨«Ò¯g"
# key = "KF99f"

decrypted_text = decrypt(encrypted_text, key)

print(encrypted_text)
print(key)
print(decrypted_text)
