cards = ('S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'SJ', 'SQ', 'SK', 'SA')

def card_value(card):
    card_map = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    return card_map[card[1:]]

def check_straight(card1, card2, card3):
    values = sorted([card_value(card1), card_value(card2), card_value(card3)])
    if values[1] == values[0] + 1 and values[2] == values[1] + 1:
        return values[2]
    else:
        return 0

def check_3ofa_kind(card1, card2, card3):
    if card1 == card2 == card3:
        return card_value(card1)
    else:
        return 0

def check_royal_flush(card1, card2, card3):
    if check_straight(card1, card2, card3) == 14:
        return 14
    else:
        return 0

def play_cards(left1, left2, left3, right1, right2, right3):
    left_straight = check_straight(left1, left2, left3)
    right_straight = check_straight(right1, right2, right3)
    left_3ofa_kind = check_3ofa_kind(left1, left2, left3)
    right_3ofa_kind = check_3ofa_kind(right1, right2, right3)
    left_royal_flush = check_royal_flush(left1, left2, left3)
    right_royal_flush = check_royal_flush(right1, right2, right3)

    # check fir royal flush
    if left_royal_flush and not right_royal_flush:
        return -1
    if right_royal_flush and not left_royal_flush:
        return 1
    if left_royal_flush and right_royal_flush:
        return 0

    # check for straights
    if left_straight and right_straight:
        if left_straight > right_straight:
            return -1
        elif right_straight > left_straight:
            return 1
        else:
            return 0

    # check for 3 of a kind
    if left_3ofa_kind and right_3ofa_kind:
        if left_3ofa_kind > right_3ofa_kind:
            return -1
        elif right_3ofa_kind > left_3ofa_kind:
            return 1
        else:
            return 0

    # straight vs 3 of a kind
    if left_straight and right_3ofa_kind:
        return -1
    if right_straight and left_3ofa_kind:
        return 1
    return 0









