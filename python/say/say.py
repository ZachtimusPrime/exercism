from num2words import num2words

def say(number: int) -> str:

    if number < 0 or number > 999999999999:
        raise ValueError("Must enter a number between 0 and 999,999,999,999")

    return num2words(number, lang='en').replace('thousand,','thousand').replace('million,','million').replace('billion,','billion')
