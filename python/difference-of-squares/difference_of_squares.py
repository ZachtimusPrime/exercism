def square_of_sum(count: int) -> int:
    summation = 0
    for i in range(1, count + 1):
        summation += i
    return pow(summation, 2)


def sum_of_squares(count: int) -> int:
    square_summation = 0
    for i in range(1, count + 1):
        square_summation += pow(i, 2)
    return square_summation


def difference(count: int) -> int:
    x = square_of_sum(count)
    y = sum_of_squares(count)
    return abs(x-y)
