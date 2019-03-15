from random import shuffle

class Card:
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    def __init__(self, suit, value):
        if suit not in Card.suits or value not in Card.values:
            raise ValueError(f"Please choose an existing suit/value!")
        self.suit = suit
        self.value = value
    def __repr__(self):
        return f"{self.value} of {self.suit}"


class Deck:
    cards = []
    def __init__(self):
        for suit in Card.suits:
            for value in Card.values:
                Deck.cards.append(Card(suit, value))

    def __repr__(self):
        return f"Deck of {self.count()} cards"

    def count(self):
        return len(Deck.cards)

    def _deal(self, amount):
        dealt = []
        if len(Deck.cards) == 0:
            raise ValueError("All cards have been dealt")
        for i in range(int(amount)):
            card = Deck.cards.pop()
            dealt.append(card)
        return dealt

    def shuffle(self):
        if len(self.cards) is not 52:
            raise ValueError("Only full decks can be shuffled")
        shuffle(self.cards)
        return self

    def deal_card(self):
        return self._deal(1)

    def deal_hand(self, amount):
        return self._deal(amount)

my_deck = Deck()
print(my_deck)
my_deck.shuffle()
hand = my_deck.deal_hand(5)
print(hand)
card = my_deck.deal_card()
print(card)
print(my_deck)
