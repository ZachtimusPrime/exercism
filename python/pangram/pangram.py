import re

def is_pangram(sentence: str) -> bool:
    alphabet_set = set()
    for char in sentence.lower():
        if re.match('[a-z]', char):
            alphabet_set.add(char)
    if len(alphabet_set) == 26:
        return True
    else:
        return False
