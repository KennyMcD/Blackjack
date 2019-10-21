# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 11:17:17 2019

@author: Kenneth McDonnell
"""
import random
ACE = 11
K = 10
Q = 10
J = 10
MAX_CARDS = 52
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def getRank(self):
        return self.rank
    
    def getSuit(self):
        return self.suit

# Deck:
# cards = array of card objects
# cardsLeft = int of cards remaining in the deck (starts at 52)
class Deck:
    def __init__(self, cards, cardsLeft):
        self.cards = []
        self.cardsLeft = MAX_CARDS
    
    def appendSuit(self, suit):
        self.cards.append(Card(suit, "A"))   
        for i in range(2, 11):
            self.cards.append(Card(suit, i))          
        self.cards.append(Card(suit, "J"))
        self.cards.append(Card(suit, "Q"))
        self.cards.append(Card(suit, "K"))
        
    def createDeck(self):
        self.appendSuit("club")
        self.appendSuit("diamond")
        self.appendSuit("heart")
        self.appendSuit("spade")
        
    def shuffle(self):
        random.shuffle(self.cards)
        
    def dumpDeck(self):
        cards = 0
        for i in range(MAX_CARDS):
            print(str(self.cards[i].getRank()) + " " + str(self.cards[i].getSuit()) + '\n')
            cards += 1
        print(cards)
        

cards = []
deck = Deck(cards, MAX_CARDS)
deck.createDeck()
deck.shuffle()
deck.dumpDeck()

