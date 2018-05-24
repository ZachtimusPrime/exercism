hundreds_conv_dict = {
    "1": "C",
    "5": "D",
    "10": "M"
}

tens_conv_dict = {
    "1": "X",
    "5": "L",
    "10": "C" 
}

ones_conv_dict = {
    "1": "I",
    "5": "V",
    "10": "X" 
}

def convert_power_of_ten(number: int, power_conv_dict: dict):
    big_power = number / 5
    little_power = number % 5
    append = ""

    if big_power >= 1 and little_power < 4:
        append += power_conv_dict['5']
        for i in range(0, little_power):
            append += power_conv_dict['1']
    elif big_power > 1 and little_power == 4:
        append += "{}{}".format(power_conv_dict['1'], power_conv_dict['10'])
    elif little_power < 4:
        for i in range(0, little_power):
            append += power_conv_dict['1']
    else:
        append += "{}{}".format(power_conv_dict['1'], power_conv_dict['5'])

    return append

def numeral(number: int) -> str:
    
    thousands = int(number / 1000)
    hundreds = int((number % 1000) / 100)
    tens = int(((number % 1000) % 100) / 10)
    ones = int(((number % 1000) % 100) % 10)

    roman_numeral = ""

    for i in range(0,thousands):
        roman_numeral += "M"

    roman_numeral += convert_power_of_ten(hundreds, hundreds_conv_dict)
    roman_numeral += convert_power_of_ten(tens, tens_conv_dict)
    roman_numeral += convert_power_of_ten(ones, ones_conv_dict)
    
    return roman_numeral
