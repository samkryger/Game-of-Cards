import random

from card import Card

class Deck(object):
    
    def __init__(self):
        self.create()

    def __str__(self):
        return '[' + ', '.join(str(card) for card in self.cards) + ']'
    
    def create(self):
        self.cards = []
        for i in range(4):
            for j in range(0,14):
                self.cards.append(Card(i, j))

    def sort(self):
        n = len(self.cards)
        for i in range(n): 
            pos = i 
            for j in range(i+1, n):
                a = self.cards[pos]
                b = self.cards[j]
                if (a.suitIndex > b.suitIndex or (a.suitIndex == b.suitIndex and a.faceIndex > b.faceIndex)):
                    pos = j
            self.cards[i], self.cards[pos] = self.cards[pos], self.cards[i] 
        
    def shuffle(self):
        n = len(self.cards)
        for i in range(n-1,0,-1): 
            j = random.randint(0,i+1) 
            self.cards[i],self.cards[j] = self.cards[j],self.cards[i]
