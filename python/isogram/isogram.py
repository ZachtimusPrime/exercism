def is_isogram(string) -> bool:
    char_set = set()
    for char in string.lower().replace("-","").replace(" ", ""):
        if char in char_set:
            return False
        char_set.add(char)
    return True
