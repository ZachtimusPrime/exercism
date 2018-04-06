def is_armstrong(number: int) -> bool:
    summation = 0
    for i in str(number):
        summation += pow(int(i), len(str(number)))
    if number == summation:
        return True
    return False
