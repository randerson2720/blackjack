import random
#This is a python blackjack game
#Author: Ryan Anderson

#create the deck
def create_deck():
    deck = []
    suits = ['hearts', 'diamonds', 'spades', 'clubs']
    values = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for suit in suits:
        for value in values:
            deck.append((suit,value))
    random.shuffle(deck)
    return deck

#deal the cards
def deal_cards(deck):
    hand = []
    for i in range(2):
        hand.append(deck.pop())
    return hand

#Get the cards values
def get_card_val(card):
    if card[1].isdigit():
        return int(card[1])
    elif card[1] == 'A':
        return 11
    else:
        return 10

#get the hand values
def get_hand_val(hand):
    value = 0
    num_aces = 0
    for card in hand:
        card_val = get_card_val(card)
        value += card_val
        if card[1] == 'A':
            num_aces += 1
    while value > 21 and num_aces:
        value -= 10
        num_aces -= 1
    return value

def show_cards(player_hand, dealer_hand, show_dealer_hand=False):
    print("Player's hand: ",player_hand)
    if show_dealer_hand:
        print("Dealer's hand: ", dealer_hand)
    else:
        print("Dealer's hand: ", [dealer_hand[0], 'XX'])

def player_turn(deck, player_hand, dealer_hand):
    while True:
        show_cards(player_hand, dealer_hand)
        choice = input("Do you want to hit or stand?").lower()
        if choice == 'hit':
            player_hand.append(deck.pop())
            if get_hand_val(player_hand) > 21:
                show_cards(player_hand, dealer_hand, True)
                print("Bust! You lose.")
                return False
        elif choice == 'stand':
            return True

def dealer_turn(deck,dealer_hand, player_hand):
    while get_hand_val(dealer_hand) < 17:
        dealer_hand.append(deck.pop())
    if get_hand_val(dealer_hand) > 21:
        show_cards(player_hand, dealer_hand, True)
        print("Dealer Bust! You win.")
        return False
    return True

def play_game():
    deck = create_deck()
    player_hand = deal_cards(deck)
    dealer_hand = deal_cards(deck)
    while True:
        show_cards(player_hand, dealer_hand)
        if get_hand_val(player_hand) == 21:
            print("Blackjack! You win.")
            return
        if not player_turn(deck,player_hand,dealer_hand):
            return
        if not dealer_turn(deck,dealer_hand,player_hand):
            return
        player_value = get_hand_val(player_hand)
        dealer_value = get_hand_val(dealer_hand)
        if player_value > dealer_value:
            print("You win!")
        elif player_value < dealer_value:
            print("You lose.")
        else:
            print("Push (tie)")
        return


play_game()





        


