class Card:
    suits = {'s': '♠','h': '♥','c': '♣','d': '♦'}
    faces = {
        11: 'Jack',
        12: 'Queen',
        13: 'King',
        14: 'Ace'
    }
    def __init__(self, rank, suit):
        '''Called when you create a new card. For example `Card(10, 'h')`'''
        self.rank = rank + 2
        self.suit = suit
        self.chip = Card.getChip(self.rank)
    
    def __str__(self):
     return (f"[Rank: {self.rank}, Suit: {self.suit}, Chips: {self.chip}]")

    @staticmethod
    def getChip(rank):
        if rank == 14:
            return 11
        elif ((rank >= 11) and (rank <= 13)):
            return 10
        else:
            return rank