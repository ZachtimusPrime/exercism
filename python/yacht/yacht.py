from collections import Counter

# Score categories
# Change the values as you see fit
YACHT = 'YACHT'
ONES = 'ONES'
TWOS = 'TWOS'
THREES = 'THREES'
FOURS = 'FOURS'
FIVES = 'FIVES'
SIXES = 'SIXES'
FULL_HOUSE = 'FULL_HOUSE'
FOUR_OF_A_KIND = 'FOUR_OF_A_KIND'
LITTLE_STRAIGHT = 'LITTLE_STRAIGHT'
BIG_STRAIGHT = 'BIG_STRAIGHT'
CHOICE = 'CHOICE'


def score_yacht(dice: [int]) -> int:
    for i in dice:
        if i != dice[0]:
            return 0
    return 50

def score_digit(dice: [int], digit: int) -> int:
    score = 0
    for i in dice:
        if i == digit:
            score += digit
    return score

def score_full_house(dice: [int]) -> int:
    unique = set()
    for i in dice:
        if i not in unique:
            unique.add(i)
    if len(unique) != 2:
        return 0
    else:
        return sum(dice)

def score_four_of_a_kind(dice: [int]) -> int:
    occurences = Counter(dice)
    for k, v in occurences.items():
        if v >= 4:
            return k*4
    return 0

def score_little_straight(dice: [int]) -> int:
    if Counter([1,2,3,4,5]) == Counter(dice):
        return 30
    return 0

def score_big_straight(dice: [int]) -> int:
    if Counter([2,3,4,5,6]) == Counter(dice):
        return 30
    return 0

def score_choice(dice: [int]) -> int:
    return sum(dice)

def score(dice: [int], category: str) -> int:

    solutions = {
        YACHT: score_yacht(dice),
        ONES: score_digit(dice,1),
        TWOS: score_digit(dice,2),
        THREES: score_digit(dice,3),
        FOURS: score_digit(dice,4),
        FIVES: score_digit(dice,5),
        SIXES: score_digit(dice,6),
        FULL_HOUSE: score_full_house(dice),
        FOUR_OF_A_KIND: score_four_of_a_kind(dice),
        LITTLE_STRAIGHT: score_little_straight(dice),
        BIG_STRAIGHT: score_big_straight(dice),
        CHOICE: score_choice(dice)
    }

    return solutions[category]
