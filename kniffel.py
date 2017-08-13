def get_user_hand():

    """Get the user's hand from input. Input as 'dice1, dice2, ...'."""

    pass


def calc_payoff(user_hand, hand):

    """
    Calculate the payoff (i.e. the hand's point score * the probability of
    getting such a hand).
    """

    pass


def calc_hand_prob(user_hand, hand):

    """
    Calculate probability of rolling 'hand' given the dice present in
    'user_hand'.
    """

    pass


possible_hands = ["ones", "twos", "threes", "fours", "fives", "sixes",
                   "3same", "4same", "full", "sstreet", "lstreet", "kniffel"]

user_hand = get_user_hand()

payoff_dict = {}
for hand in possible_hands:
    payoff_dict[hand] = calc_payoff(user_hand, hand)

print payoff_dict
