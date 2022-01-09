def get_rounds(number):
    """

     :param number: int - current round number.
     :return: list - current round and the two that follow.
    """
    rounds = []
    rounds.append(number)
    rounds.append(number + 1)
    rounds.append(number + 2)
    
    return rounds


def concatenate_rounds(rounds_1, rounds_2):
    """

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """

    return rounds_1 + rounds_2


def list_contains_round(rounds, number):
    """

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return:  bool - was the round played?
    """

    return number in rounds


def card_average(hand):
    """

    :param hand: list - cards in hand.
    :return:  float - average value of the cards in the hand.
    """

    return sum(hand)/len(hand)
    


def approx_average_is_average(hand):
    """

    :param hand: list - cards in hand.
    :return: bool - if approximate average equals to the `true average`.
    """

    approx_avg1 = (hand[0] + hand[-1])/2
    approx_avg2 = hand[len(hand)//2]
    actual_avg = card_average(hand)
    
    return (actual_avg == approx_avg1) or (actual_avg == approx_avg2)


def average_even_is_average_odd(hand):
    """

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """
    odd_count = (len(hand) + 1)//2
    even_count = len(hand)//2

    # print(hand, odd_count, even_count)

    odd_avg = sum(hand[0::2])/odd_count
    even_avg = sum(hand[1::2])/even_count

    # print(odd_avg, even_avg)
    
    return odd_avg == even_avg


def maybe_double_last(hand):
    """

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """

    last_hand = hand[len(hand) - 1]
    if last_hand == 11:
        hand[len(hand) - 1] = last_hand*2

    return hand
