

"""Define the data structures for a generic deck of cards. Explain how you
would subclass the data structures to implement blackjack.
"""

from random import shuffle

class Deck():
    def __init__(self):
        values = ['A', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        suits= ['♠', '♥', '♦', '♣']
        self.cards = set((suit, value) for value in values for suit in suits)

    def shuffle(self):
        return shuffle(list(self.cards))


