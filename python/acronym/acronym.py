def abbreviate(words: str) -> str:
    word_list = words.replace("-", " ").split(" ")

    acronym = ""
    for word in word_list:
        acronym += word[0].upper()
    return acronym
