#TASK 1: DEFINING CARD VALUES
def value_of_card(card):
    if card in ['J','K','Q']:
        return(10)
    if card in ['A']:
        return(1)
    else:
        return int(card)
#TASK 2: DETERMINING WHICH CARD HAS A HIGHER VALUE    
def higher_card(card_one, card_two):
    def card_value(card):
        if card in ['J','K','Q']:
            return(10)
        if card in ['A']:
            return(1)
        else:
            return int(card)

    first_value=value_of_card(card_one)
    second_value=value_of_card(card_two)

    if first_value>second_value:
        return card_one
    if first_value<second_value:
        return card_two
    elif first_value==second_value:
        return(card_one,card_two)
#TASK 3: DETERMINING THE ACES VALUE
def value_of_ace(card_one,card_two):
    def card_value(card):
        if card in ['J','K','Q']:
            return 10
        if card =='A':
            return 1
        else:
            return int(card)

     #if theres already an ace make it equal one

    if card_one=='A' or card_two=='A':
        return 1
        
    starting_cards=card_value(card_one)+card_value(card_two)
        
    if starting_cards+11<=21:
        return 11
    else:
        return 1
#TASK 4: DETERMINING WHEN THERE IS A BLACKJACK
def is_blackjack(card_one, card_two):
    ten_cards = ['10', 'J', 'Q', 'K']
    return (
        (card_one == 'A' and card_two in ten_cards) or
        (card_two == 'A' and card_one in ten_cards)
    )
#TASK 5: DETERMINING IF PAIRS CAN BE SPLIT
def can_split_pairs(card_one, card_two):
    def value_of_cards(card):
        if card in ['10','K','J','Q']:
            return 10
        if card=='A':
            return 1
        else:
            return int(card)
    #define cards with value of 10
    value_ten_cards=['10','K','J','Q']
    if card_one in value_ten_cards and card_two in value_ten_cards:
        return True
    if card_one==card_two:
        return True
    else:
        return False
#TASK 6: DETERMINING WHEN A PLAYER CAN DOUBLE DOWN
def can_double_down(card_one, card_two):
    def value_of_cards(card):
        if card in ['10','K','J','Q']:
            return 10
        if card=='A':
            return 1
        else:
            return int(card)
    starting_cards=value_of_cards(card_one)+value_of_cards(card_two)
    if starting_cards in [9,10,11]:
        return True
    else:
        return False
        
    
    

