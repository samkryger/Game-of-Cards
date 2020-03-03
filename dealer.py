from deck import Deck
from card import Card
import random

class Dealer(object):
    
    def __init__(self):
        self.combineDecks()
        
    def __str__(self):
        return '[' + ', '.join(str(card) for card in self.megaDeck) + ']'
    
    def combineDecks(self):
        self.megaDeck = []
        for i in range(4):
            for i in range(4):
                for j in range(0,14):
                    self.megaDeck.append(Card(i, j))
    
    def shuffle(self):
        n = len(self.megaDeck)
        for i in range(n-1,0,-1): 
            j = random.randint(0,i+1) 
            self.megaDeck[i],self.megaDeck[j] = self.megaDeck[j],self.megaDeck[i]
            
    def deal(self):
        self.dealtCards = []
        self.cardDealt = self.megaDeck[0]
        print(f'''Card Dealt: {self.cardDealt}''')
        self.dealtCards.append(self.megaDeck[0])
        self.megaDeck.pop(0)
    
    def recycle(self):
        for i in range(len(self.dealtCards)):
            self.megaDeck.append(self.dealtCards[i])
        self.shuffle()
