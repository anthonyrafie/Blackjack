import random


class Card:
    def __init__(self, face, suit, value):
        self.face = face
        self.suit = suit
        self.value = value


def play():
    # Creating deck
    deck = []
    faces = {
        "King": 10,
        "Queen": 10,
        "Jack": 10,
        "Ten": 10,
        "Nine": 9,
        "Eight": 8,
        "Seven": 7,
        "Six": 6,
        "Five": 5,
        "Four": 4,
        "Three": 3,
        "Two": 2,
        "Ace": 11
    }
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    for face in faces:
        for suit in suits:
            deck.append(Card(face, suit, faces[face]))

    # Dealing user's hand
    user_hand = []
    user_score = 0
    print("Your hand: \n")
    for i in range(2):
        random_card = deck.pop(random.randint(0, len(deck) - 1))
        user_hand.append(random_card)
        user_score += random_card.value
        print(random_card.face + " of " + random_card.suit)
    print("\nYour current score: " + str(user_score))
    print("\n///////////////////////////\n")

    # Dealing dealer's hand
    dealer_hand = []
    dealer_score = 0
    print("Dealer's Hand: \n")
    for i in range(2):
        random_card = deck.pop(random.randint(0, len(deck) - 1))
        dealer_hand.append(random_card)
        dealer_score += random_card.value
    print(dealer_hand[1].face + " of " + dealer_hand[1].suit + "\nHidden card")
    print("\n///////////////////////////\n")

    # If user has Blackjack, automatically sets their next move to n
    if user_score == 21:
        user_next_move = "n"
    # Asking user if they want another card
    else:    
        user_next_move = input("Draw another card? (y/n) ")

        # Checking if they entered an invalid response
        while user_next_move != "y" and user_next_move != "n":
            user_next_move = input("Invalid answer. Draw another card? (y/n) ")
        
        print("\n///////////////////////////\n")

    while True:
        # If they answer yes, draw a card and ask again
        if user_next_move == "y":
            random_card = deck.pop(random.randint(0, len(deck) - 1))
            user_hand.append(random_card)
            user_score += random_card.value
            print("Your hand: \n")
            ace_indices = []
            for i in range(len(user_hand)):
                print(user_hand[i].face + " of " + user_hand[i].suit)
                if user_hand[i].face == "Ace" and user_hand[i].value == 11:
                    ace_indices.append(i)

            # Checking if user has lost
            while user_score > 21:
                # Checking if there are aces that can be evaluated as 1 instead of 11
                if ace_indices != []:
                    user_hand[ace_indices.pop()].value = 1
                    user_score -= 10
                else:
                    print("\nYour current score: " + str(user_score))
                    print("\n///////////////////////////\n")
                    print("You lose. You'll get 'em next time!")
                    return None
            print("\nYour current score: " + str(user_score))
            print("\n///////////////////////////\n")

            # If user has Blackjack, automatically sets their next move to n
            if user_score == 21:
                user_next_move = "n"
                continue
            
            # Asking again if they want another card
            user_next_move = input("Draw another card? (y/n) ")

            # Checking again if they entered an invalid response
            while user_next_move != "y" and user_next_move != "n":
                user_next_move = input("Invalid answer. Draw another card? (y/n) ")
            
            print("\n///////////////////////////\n")

            continue

        # If they answer no, let the dealer play and compare both scores
        else:
            # Revealing dealer's full hand
            print("Dealer's hand: \n")
            for card in dealer_hand:
                print(card.face + " of " + card.suit)
            print("\nDealer's current score: " + str(dealer_score))
            print("\n///////////////////////////\n")
            
            # Dealer draws cards until they have a score of at least 17
            while dealer_score < 17:
                random_card = deck.pop(random.randint(0, len(deck) - 1))
                dealer_hand.append(random_card)
                dealer_score += random_card.value
                print("Dealer's hand: \n")
                ace_indices = []
                for i in range(len(dealer_hand)):
                    print(dealer_hand[i].face + " of " + dealer_hand[i].suit)
                    if dealer_hand[i].face == "Ace" and dealer_hand[i].value == 11:
                        ace_indices.append(i)

                # Checking if dealer has lost
                while dealer_score > 21:
                    # Checking if there are aces that can be evaluated as 1 instead of 11
                    if ace_indices != []:
                        dealer_hand[ace_indices.pop()].value = 1
                        dealer_score -= 10
                    else:
                        print("\nDealer's current score: " + str(dealer_score))
                        print("\n///////////////////////////\n")
                        print("Dealer loses. You win!")
                        return None
                print("\nDealer's current score: " + str(dealer_score))
                print("\n///////////////////////////\n")
            
            break

    # Checking who won
    if user_score > dealer_score:
        if user_score == 21:
            print("Blackjack! You win!")
            return None
        else:
            print("You win!")
            return None
    elif user_score == dealer_score:
        if user_score == 21 and dealer_score == 21:
            print("Double Blackjack, it's a tie!")
            return None
        else:
            print("It's a tie!")
            return None
    else:
        print("You lose. You'll get 'em next time!")
        return None


play()