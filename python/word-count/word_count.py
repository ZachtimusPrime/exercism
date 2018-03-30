import re

def word_count(phrase: str) -> dict:
    # strip all non-alphanumeric chars from phrase (besides apostrophes in words)
    words = re.sub(r'[^A-Za-z0-9\']+', ' ', phrase).strip().lower()
    # remove any quotes around words and create word arr
    words = re.sub(r"'([A-Za-z0-9]+)'", r'\1', words).split(" ")

    word_dict = {}
    for word in words:
        if word not in word_dict.keys():
            word_dict[word] = 1
        else:
            word_dict[word] += 1
    return word_dict
