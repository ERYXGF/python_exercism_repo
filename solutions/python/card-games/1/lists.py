"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    return [number, number+1, number+2]
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """
    
def concatenate_rounds(rounds_1, rounds_2):
    return rounds_1 + rounds_2
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """

    pass


def list_contains_round(rounds, number):
    if number in rounds:
        return True
    else:
        return False
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """

    pass


def card_average(hand):
    return sum(hand)/len(hand)
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """

    pass


def approx_average_is_average(hand):
    average = sum(hand) / len(hand)
    extremes = (hand[0] + hand[-1]) / 2
    middle = hand[len(hand) // 2]
    return average == extremes or average == middle
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """

    pass


def average_even_is_average_odd(hand):
    even = 0
    odd = 0
    even_count = 0
    odd_count = 0
    for index, num in enumerate(hand):
        if index%2==0:
            even+=num
            even_count+=1
        else:
            odd+=num
            odd_count+=1
    even = even / even_count
    odd = odd / odd_count
    return even == odd
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """

    pass


def maybe_double_last(hand):
    if hand[-1] == 11:
        return hand[0:-1]+[22]
    return hand
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """

    pass
