# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 11:17:17 2019

@author: Kenneth McDonnell
"""
import random
# Dictionary for card values
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

# A card has a rank and a suit
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def getRank(self):
        return self.rank
    
    def getSuit(self):
        return self.suit

# Deck:
# Cards: array of card objects
# CardsLeft: int of cards remaining in the deck (starts at 52)
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
        self.appendSuit("♣")
        self.appendSuit("♦")
        self.appendSuit("♥")
        self.appendSuit("♠")
        
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
        
# A hand is made from a deck
class Hand:
    def __init__(self, deck):
        self.deck = deck
        self.numCards = 0
    # returns an array of at least 2 cards
    def draw(self, hand):
        self.numCards += 1
        hand.append(self.deck.getCard())
        
        return hand
    
    # Counts the value of the current player's hand
    def handValue(self, hand):
        handVal = 0
        ace = 0
        for i in range(self.numCards):
            handVal += cardVal[hand[i].getRank()]
            if (hand[i].getRank() == 'A'):
                ace += 1        
        # Handles aces; also handles if 2 or more aces are drawn
        while (handVal > 21 and ace > 0):
            handVal -= 10
            ace -= 1
        return handVal
   
    def dumpHand(self, hand):
        print("Hand")
        
        for i in range(self.numCards):
            r = str(hand[i].getRank())
            s = str(hand[i].getSuit())
            print("┌─────────┐")
            print("│"+"{0:2s}".format(r)+"       │")
            print("│         │")
            print("│         │")
            print("│    "+s+"    │")
            print("│         │")
            print("│         │")
            print("│       "+"{0:2s}".format(r)+"│")
            print("└─────────┘")
            #print(str(hand[i].getRank()) + " " + str(hand[i].getSuit()) + '\n')
        
# A player has a hand and a hand is from a deck
class Player:
        def __init__(self, hand, deck):
            self.hand = Hand(deck)
            self.currHand = []
            self.stay = False
            self.bust = False
            self.blackjack = False
        # Player draws one card, if hand value > 21 player busts
        def hit(self):
            self.hand.draw(self.currHand)
            handVal = self.hand.handValue(self.currHand)
           
            
            if (handVal > 21):
                self.bust = True
            elif (handVal == 21):
                self.blackjack = True
              
        # Starts the player by drawing 2 cards and checking for blackjack
        def startingHand(self):
            # Draw 2 cards
            self.hit()
            self.hit()
            #self.hand.dumpHand(self.currHand)
            # Blackjack check
            #self.hand.dumpHand(self.currHand)    
            handVal = self.hand.handValue(self.currHand)
            #print(handVal)
            if (handVal == 21):
                self.blackjack = True
        # Simple sets and gets     
        def handSize(self):
            return len(self.currHand)
        
        def setStay(self):
            self.stay = True
            
        def getStay(self):
            return self.stay
        
        def getBust(self):
            return self.bust
        
        def getBlackjack(self):
            return self.blackjack
        
        def dumpPlayerHand(self):
            self.hand.dumpHand(self.currHand) 
            handVal = self.hand.handValue(self.currHand)
            print(handVal)  
            return handVal
        
# A dealer is a player that shows their first card
class Dealer(Player):
    def __init__(self, hand, deck):
        self.hand = Hand(deck)
        self.currHand = []
        self.stay = False
        self.bust = False
        self.blackjack = False
    
    def peekFirst(self):
        r = str(self.currHand[0].getRank())
        s = str(self.currHand[0].getSuit())
        print("┌─────────┐")
        print("│"+"{0:2s}".format(r)+"       │")
        print("│         │")
        print("│         │")
        print("│    "+s+"    │")
        print("│         │")
        print("│         │")
        print("│       "+"{0:2s}".format(r)+"│")
        print("└─────────┘")
        

class Game():
    def __init__(self):
        self.cards = []
        self.deck = Deck(self.cards, MAX_CARDS)
        self.deck.createDeck()
        self.deck.shuffle()
        self.playerHand = Hand(self.deck)
        self.player = Player(self.playerHand, self.deck)   
        self.dealerHand = Hand(self.deck)
        self.dealer = Dealer(self.dealerHand, self.deck)   
        
    def runGame(self):
        # Running the game
        print("Welcome to Blackjack!")
        choice = input("1) Start \n2) Exit\n")
        
        if choice == '1':
            playagain = True
            while (playagain == True):
                # Start game
                # Dealer Draw
                print("Dealer's Peek")
                self.dealer.startingHand()
                self.dealer.peekFirst() # Print dealer's first card
                print('\n')
                # Player turn
                print("Human's turn")
                self.player.startingHand()
                # Allows the player to stay or hit until they bust or get blackjack
                while (self.player.getStay() != True):
                    self.player.dumpPlayerHand()
                    # Loop menu for human player
                    play = input("1) Hit\n2) Stay\n")
                    # Hit
                    if (play == '1'):
                        self.player.hit()
                        if (self.player.getBust() == True):
                            print("Human Bust")
                            self.player.setStay()
                        elif (self.player.getBlackjack() == True):
                            print("Human Blackjack")
                            self.player.setStay()
                    # Stay
                    elif (play == '2'):
                        self.player.setStay()
                playerVal = self.player.dumpPlayerHand() # Print player's hand
            
                # Dealer turn
                print("\nDealer's turn")
                dealerVal = self.dealer.dumpPlayerHand() # Reveal dealer's hand
                # Checking if player gets blackjack on starting hand
                if (self.player.handSize() == 2 and self.player.getBlackjack() == True and self.dealer.getBlackjack() == False):
                    print("Human wins!")
                    # Checking if dealer gets blackjack on starting hand
                elif (self.dealer.getBlackjack() == True and self.player.getBlackjack() == False):
                    print("Dealer Wins!")
                # Both players have blackjack on their starting hands
                elif (self.player.handSize() == 2 and self.player.getBlackjack() == True and self.dealer.getBlackjack() == True):
                    print("Tie game!")
                else:
                    # Dealer hits when hand value is less than 17
                    while (dealerVal < 17):
                        self.dealer.hit()
                        dealerVal = self.dealer.dumpPlayerHand()
                        print("\n")
                    self.dealer.setStay()
                    # Cases for if either player has blackjack or busts
                
                    # Dealer busts, player stayed or has blackjack
                    if (self.dealer.getBust() == True and self.player.getBust() == False):
                        print("Dealer Bust") 
                        print("Human Wins!")
                    # Player busts, dealer stayed or has blackjack
                    elif (self.dealer.getBust() == False and self.player.getBust() == True):
                        print("Human Bust") 
                        print("Dealer Wins!")
                    # Dealer has blackjack and the player doesn't or busts
                    elif (self.dealer.getBlackjack() == True and self.player.getBlackjack() == False):
                        print("Dealer Blackjack")
                        print("Dealer Wins!")
                    # Both players bust; dealer wins
                    elif (self.dealer.getBust() == True and self.player.getBust() == True):  
                        print("Dealer Wins!")
                    # Both players reach blackjack after hitting        
                    elif (self.dealer.getBlackjack() == True and self.player.getBlackjack() == True):
                        print("Tie Game!")
                    else:   
                        # Comparing hand values if no player busts or gets blackjack
                        if (dealerVal < playerVal):
                            print("Player Wins!")
                        elif (dealerVal > playerVal):
                            print("Dealer Wins!")
                        elif (dealerVal == playerVal):
                            print("Tie Game!")
                        
                pa = input("Play again?(y/n) ")
                # Restart the game; instantiate new objects
                if (pa == 'y'):
                    playagain = True
                    # Creates deck          
                    cards = []
                    self.deck = Deck(cards, MAX_CARDS)
                    self.deck.createDeck()
                    self.deck.shuffle()
        
                    # Creates human player
                    playerHand = Hand(self.deck)
                    self.player = Player(playerHand, self.deck)
        
                    # Creates dealer player
                    dealerHand = Hand(self.deck)
                    self.dealer = Dealer(dealerHand, self.deck)
                # End game
                else:
                    playagain = False
                    print("Goodbye")        
        else:
            print("See you next time!")
        
       
game = Game()
game.runGame()
'''
# Creates deck          
cards = []
deck = Deck(cards, MAX_CARDS)
deck.createDeck()
deck.shuffle()
#deck.getCard()
#deck.dumpDeck()

# Creates human player
playerHand = Hand(deck)
player = Player(playerHand, deck)

# Creates dealer player
dealerHand = Hand(deck)
dealer = Dealer(dealerHand, deck)

# Running the game

        
        
        
print("Welcome to Blackjack!")
choice = input("1) Start \n2) Exit\n")

if choice == '1':
    playagain = True
    while (playagain == True):
        # Start game
        # Dealer Draw
        print("Dealer's Peek")
        dealer.startingHand()
        dealer.peekFirst() # Print dealer's first card
        print('\n')
        # Player turn
        print("Human's turn")
        player.startingHand()
        # Allows the player to stay or hit until they bust or get blackjack
        while (player.getStay() != True):
            player.dumpPlayerHand()
            # Loop menu for human player
            play = input("1) Hit\n2) Stay\n")
            # Hit
            if (play == '1'):
                player.hit()
                if (player.getBust() == True):
                    print("Human Bust")
                    player.setStay()
                elif (player.getBlackjack() == True):
                    print("Human Blackjack")
                    player.setStay()
            # Stay
            elif (play == '2'):
                player.setStay()
        playerVal = player.dumpPlayerHand() # Print player's hand
    
        # Dealer turn
        print("\nDealer's turn")
        dealerVal = dealer.dumpPlayerHand() # Reveal dealer's hand
        # Checking if player gets blackjack on starting hand
        if (player.handSize() == 2 and player.getBlackjack() == True and dealer.getBlackjack() == False):
            print("Human wins!")
            # Checking if dealer gets blackjack on starting hand
        elif (dealer.getBlackjack() == True and player.getBlackjack() == False):
            print("Dealer wins!")
        # Both players have blackjack on their starting hands
        elif (player.handSize() == 2 and player.getBlackjack() == True and dealer.getBlackjack() == True):
            print("Tie game!")
        # Dealer hits when hand value is less than 17
        while (dealerVal < 17):
            dealer.hit()
            dealerVal = dealer.dumpPlayerHand()
            print("\n")
        dealer.setStay()
        # Cases for if either player has blackjack or busts
    
        # Dealer busts, player stayed or has blackjack
        if (dealer.getBust() == True and player.getBust() == False):
            print("Dealer Bust") 
            print("Human Wins!")
        # Player busts, dealer stayed or has blackjack
        elif (dealer.getBust() == False and player.getBust() == True):
            print("Human Bust") 
            print("Dealer Wins!")
        # Dealer has blackjack and the player doesn't or busts
        elif (dealer.getBlackjack() == True and player.getBlackjack() == False):
            print("Dealer Blackjack")
            print("Dealer Wins!")
        # Both players bust; dealer wins
        elif (dealer.getBust() == True and player.getBust() == True):  
            print("Dealer Wins!")
        # Both players reach blackjack after hitting        
        elif (dealer.getBlackjack() == True and player.getBlackjack() == True):
            print("Tie Game!")
        else:   
            # Comparing hand values if no player busts or gets blackjack
            if (dealerVal < playerVal):
                print("Player Wins!")
            elif (dealerVal > playerVal):
                print("Dealer Wins!")
            elif (dealerVal == playerVal):
                print("Tie Game!")
                
        pa = input("Play again?(y/n) ")
        # Restart the game; instantiate new objects
        if (pa == 'y'):
            playagain = True
            # Creates deck          
            cards = []
            deck = Deck(cards, MAX_CARDS)
            deck.createDeck()
            deck.shuffle()

            # Creates human player
            playerHand = Hand(deck)
            player = Player(playerHand, deck)

            # Creates dealer player
            dealerHand = Hand(deck)
            dealer = Dealer(dealerHand, deck)
        # End game
        else:
            playagain = False
            print("Goodbye")        
else:
    print("See you next time!")
'''