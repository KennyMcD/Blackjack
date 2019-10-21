# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 11:17:17 2019

@author: Kenneth McDonnell
"""
import random
cardVal = {
        'A': 11,  
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'J': 10,
        'Q': 10,
        'K': 10
    }
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
    
    # Create a set of 13 cards based on the suit
    def appendSuit(self, suit):
        for key in cardVal.keys():
            self.cards.append(Card(suit, key)) 
    
    # Create 4 sets of each suit for the deck
    def createDeck(self):
        self.appendSuit("club")
        self.appendSuit("diamond")
        self.appendSuit("heart")
        self.appendSuit("spade")
        
    # Shuffle the deck
    def shuffle(self):
        random.shuffle(self.cards)
        
    # Return the top card of the deck
    def getCard(self):
        self.cardsLeft -= 1
        return self.cards.pop()
       
    # Prints contents of deck
    def dumpDeck(self):
        cards = 0
        for i in range(self.cardsLeft):
            print(str(self.cards[i].getRank()) + " " + str(self.cards[i].getSuit()) + '\n')
            cards += 1
        print(cards)
        
# Takes the deck and makes an array of 2 or more cards
class Hand:
    def __init__(self, deck):
        self.deck = deck
        self.numCards = 0
    # returns an array of at least 2 cards
    def draw(self, hand):
        self.numCards += 1
        hand.append(self.deck.getCard())
        
    # Start hand by drawing twice and adding ranks of cards
    def handValue(self, hand):
        handVal = 0
        for i in range(self.numCards):
            handVal += cardVal[hand[i].getRank()]
        print(handVal)
        return handVal
    
    def dumpHand(self, hand):
        for i in range(self.numCards):
            print(str(hand[i].getRank()) + " " + str(hand[i].getSuit()) + '\n')
        

        
cards = []
deck = Deck(cards, MAX_CARDS)
deck.createDeck()
deck.shuffle()
#deck.getCard()
#deck.dumpDeck()
playerHand = []
hand = Hand(deck)
hand.draw(playerHand)
hand.draw(playerHand)
hand.handValue(playerHand)
hand.dumpHand(playerHand)
#deck.dumpDeck()
print("Welcome to Blackjack!")
choice = input("1) Start \n2) Rules\n3) Exit\n")
if choice == 1:
    #start game
    print("start")
elif choice == 2:
    print("rules")
elif choice == 3:
    exit