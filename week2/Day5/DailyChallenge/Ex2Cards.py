# Exercise 2: Create a deck of cards class

# The Deck of cards class should NOT inherit from a Card class.

# The requirements are as follows:

#     The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)
import random
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    def __str__(self):
        return f'{self.value} of {self.suit}'
    def __repr__(self):
        return f"Card('{self.suit}', '{self.value}')"
    
#     The Deck class :
#         should have a shuffle method which makes sure the deck of cards has all 52 cards and then rearranges them randomly.
#         should have a method called deal which deals a single card from the deck. After a card is dealt, it should be removed from the deck.
class Deck:
    def __init__(self):
        self.cards = []
        self.suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        self.values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self._build_deck()
        self.shuffle()

    def _build_deck(self):
        for suit in self.suits:
            for value in self.values:
                self.cards.append(Card(suit,value))

    def __str__(self):
        return f'Deck of {len(self.cards)} cards'
    
    def shuffle(self):
        if len(self.cards) == 52:
            random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            raise ValueError('All cards have been dealt.')


if __name__ == '__main__':
    instance = Deck()
    # rint(instance.cards)
    print(instance.deal())