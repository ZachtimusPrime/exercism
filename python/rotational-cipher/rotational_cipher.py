import string

alpha = {}
index = 0
for char in string.ascii_lowercase:
    alpha[char] = index
    index += 1
alpha_index = dict(zip(alpha.values(), alpha.keys()))


def rotate(text: str, key: int) -> str:
    cipher_text = ""
    for char in text:
        if char in string.ascii_letters and char.isupper():
            cipher_text += alpha_index[(alpha[char.lower()] + key) % 26].upper()
        elif char in string.ascii_letters:
            cipher_text += alpha_index[(alpha[char] + key) % 26]
        else:
            cipher_text += char
    return cipher_text
