#from board.logic.Card import Card
from .Card import Card
import numpy as np
import random

class Deck:
    deck = np.array([])

    def __init__(self):
        self.deck = []
        suits = ['s','h','c','d']
        for suit in suits:
            for x in range(13):
                self.deck.append(Card(x, suit))

    def __str__(self):
        return '\n'.join(str(card) for card in self.deck)
    
    def shuffle(self):
        random.shuffle(self.deck)

    def showHands(self):
        return '\n'.join(str(self.deck[x]) for x in range(8))
    
    def selectCards(self):
        return

startCards = Deck()

startCards.shuffle()
print(startCards.showHands())