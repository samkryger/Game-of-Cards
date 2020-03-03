class Card(object):
    suits = ["♠","♥","♦","♣"]
    faces = ['A','1','2','3','4','5','6','7','8','9','10','J','Q','K']
    
    def __init__(self, suit, face):
        self.suitIndex = suit
        self.faceIndex = face

    def __str__(self):
        face = Card.faces[self.faceIndex]
        suit = Card.suits[self.suitIndex]
        return face + suit
