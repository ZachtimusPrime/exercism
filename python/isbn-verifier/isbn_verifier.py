import re

def verify(isbn: str) -> bool:
    isbn = isbn.upper().replace("-","")
    isbn_value = 0
    if re.match('^[0-9]{9}[X0-9]{1}$',isbn):
        modifier = 10
        for char in isbn:
            if char == "X":
                isbn_value += 10 * modifier
            else:
                isbn_value += int(char) * modifier
            modifier -= 1
        if isbn_value % 11 == 0:
            return True
        else: 
            return False
    else:
        return False
