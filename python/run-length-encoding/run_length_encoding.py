import re


def decode(string: str) -> str:
    output = ""
    sequences = re.split(r'([0-9]+[A-Za-z ]{1})', string)
    # for some reason there are some empty matches...throw those out
    for sequence in sequences:
        if sequence == '':
            sequences.remove(sequence)
    # build out sequences or add single chars 
    for sequence in sequences:
        if re.match(r'([0-9]+[A-Za-z ]{1})', sequence):
            for i in range(0, int(re.search(r'[0-9]+', sequence).group(0))):
                output += re.search(r'[A-Za-z ]+', sequence).group(0)
        else:
            output += sequence

    return output


def encode(string: str) -> str:
    output = ""
    count = 0
    for pos, char in enumerate(string):
        # handle final char in string
        if pos == len(string)-1:
            if count > 0 and char == string[pos]:
                output += str(count+1) + char
            else:
                output += char
        # handle every other char in string
        else:
            # catch chars not at end of sequence
            if char == string[pos + 1]:
                count += 1
            # catch final char in sequence
            elif char == string[pos-1]:
                count += 1
                output += str(count) + char
                count = 0
            # catch single chars
            else:
                output += char

    return output
