import string
import re

pos_dict = {}
count = 0
for char in string.ascii_lowercase:
    pos_dict[char] = count
    count += 1

reverse_alphabet = list(reversed(string.ascii_lowercase))

def encode(plain_text: str) -> str:
    ciphertext = ""
    for char in plain_text.lower():
        if char in reverse_alphabet:
            ciphertext += reverse_alphabet[pos_dict[char]]
        elif re.search(r'[0-9]', char):
            ciphertext += char
    
    # format ciphertext with a space every 5 chars
    formatted_ciphertext = re.sub(r'([a-z0-9]{,5})', r'\1 ', ciphertext).strip()

    return formatted_ciphertext

def decode(ciphered_text: str) -> str:
    cleartext = ""
    for char in ciphered_text.replace(" ",""):
        if char in reverse_alphabet:
            cleartext += reverse_alphabet[pos_dict[char]]
        elif re.search(r'[0-9]', char):
            cleartext += char

    return cleartext
