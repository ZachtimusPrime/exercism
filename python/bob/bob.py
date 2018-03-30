import re

def hey(phrase: str) -> str:
    # remove any non-alphanumeric/punctuation char and strip leading/trailing whitespace
    phrase = re.sub(r'[^A-Za-z0-9\'.?! ]+', '', phrase).strip()

    if not re.match(r'.+', phrase):
        return "Fine. Be that way!"
    elif re.match(r'.{0,}[?][!]$', phrase) or re.match(r'[A-Z0-9 ]+[A-Z ]{1,}[?]$', phrase):
        return "Calm down, I know what I'm doing!"
    elif re.match(r'.{0,}[?]$', phrase):
        return "Sure."
    elif re.match(r'^[A-Z0-9 !]+[!]{0,}$', phrase) and not re.match(r'^[0-9 ]{0,}$', phrase):
        return "Whoa, chill out!"
    else:
        return "Whatever."
