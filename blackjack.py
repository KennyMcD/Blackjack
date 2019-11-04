# -*- coding: utf-8 -*-
"""
Next Century Project Submission

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

"""
Create card object with a suit and rank to be used for deck and hand

@author: Kenneth McDonnell
"""
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    # Purpose: return the rank of card
    # Input:   n/a
    # Return:  rank
    def getRank(self):
        return self.rank

    # Purpose: return suit of card
    # Input:   n/a
    # Return:  suit
    def getSuit(self):
        return self.suit

"""
Creates a deck object so players can draw; keeps track of cards remaining

@author Kenneth McDonnell
"""
class Deck:
    def __init__(self, cards, cardsLeft):
        self.cards = []
        self.cardsLeft = MAX_CARDS

    # Purpose: Appends set of 13 cards based on suit to cards array
    # Input:   suit
    # Return:  n/a
    def appendSuit(self, suit):
        for key in cardVal.keys():
            self.cards.append(Card(suit, key))

    # Purpose: Creates deck array by calling appendSuit for every suit
    # Input:   n/a
    # Return:  n/a
    def createDeck(self):
        self.appendSuit("♣")
        self.appendSuit("♦")
        self.appendSuit("♥")
        self.appendSuit("♠")

    # Purpose: Shuffle the deck in random order; uses random library
    # Input:   n/a
    # Return:  n/a
    def shuffle(self):
        random.shuffle(self.cards)

    # Purpose: Return card; remove it from deck
    # Input:   n/a
    # Return:  card object from top of deck
    def dealCard(self):
        self.cardsLeft -= 1
        return self.cards.pop()

    # Purpose: Prints contents of deck; used for testing/debugging
    # Input:   n/a
    # Return:  n/a
    def dumpDeck(self):
        cards = 0
        for i in range(self.cardsLeft):
            print(str(self.cards[i].getRank()) + " " + str(self.cards[i].getSuit()) + '\n')
            cards += 1
        print(cards)
"""
Hand object for each players; starts with 2 cards; allows player to draw cards

@author Kenneth McDonnell
"""
class Hand:
    def __init__(self, deck):
        self.deck = deck
        self.numCards = 0

    def setNumCards(self, cards):
        self.numCards = cards
        
    # Purpose: Adds one card to a player's hand
    # Input:   player's hand
    # Return:  updated player's hand with new card
    def draw(self, hand):
        self.numCards += 1
        hand.append(self.deck.dealCard())
        return hand

    # Purpose: Calculates value of player's current hand; handles aces
    # Input:   player's hand
    # Return:  value of player's hand
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

    # Purpose: Prints player's hand with string formatting
    # Input:   player's hand
    # Return:  n/a
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


"""
Player object; can hit or stay; checks for blackjack on initial hand

@author Kenneth McDonnell
"""
class Player:
        def __init__(self, hand, deck):
            self.hand = Hand(deck)
            self.currHand = []
            self.stay = False
            self.bust = False
            self.blackjack = False

        # Purpose: Adds one card to player's hand; accounts for busts
        # Input:   n/a
        # Return:  n/a
        def hit(self):
            self.hand.draw(self.currHand)
            handVal = self.hand.handValue(self.currHand)
            # Checks for blackjack
            if (handVal > 21):
                self.bust = True
            elif (handVal == 21):
                self.blackjack = True

        # Purpose: Draws two cards for player and checks for blackjack
        # Input:   n/a
        # Return:  n/a
        def startingHand(self):
            # Draw 2 cards
            self.hit()
            self.hit()
            # Blackjack check
            handVal = self.hand.handValue(self.currHand)
            if (handVal == 21):
                self.blackjack = True

        # Purpose: Get amount of cards in player's hand
        # Input:   n/a
        # Return:  length of player's hand array
        def handSize(self):
            return len(self.currHand)

        # Purpose: Set when player chooses to stay
        # Input:   n/a
        # Return:  n/a
        def setStay(self):
            self.stay = True

        # Purpose: Get whether player decides to stay
        # Input:   n/a
        # Return:  stay bool
        def getStay(self):
            return self.stay

        # Purpose: Get if player busts; set when hand value > 21
        # Input:   n/a
        # Return:  bust bool
        def getBust(self):
            return self.bust

        # Purpose: Get if player has blackjack; hand value = 21
        # Input:   n/a
        # Return:  blackjack bool
        def getBlackjack(self):
            return self.blackjack

        # Purpose: Print players current hand
        # Input:   n/a
        # Return:  returns current hand value
        def dumpPlayerHand(self):
            self.hand.dumpHand(self.currHand)
            handVal = self.hand.handValue(self.currHand)
            print(handVal)
            return handVal

"""
Dealer class which inherits player; Dealer is a player, although they show
their first card in hand.

@author Kenneth McDonnell
"""
class Dealer(Player):
    def __init__(self, hand, deck):
        self.hand = Hand(deck)
        self.currHand = []
        self.stay = False
        self.bust = False
        self.blackjack = False

    # Purpose: Show first card of dealers hand (like in real blackjack)
    # Input:   n/a
    # Return:  n/a
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

"""
Creates Game object which starts, runs, and ends game based on win conditions

@author Kenneth McDonnell
"""
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

    # Purpose: Runs the main menu and main game loop; checks for win conditions
    # Input:   n/a
    # Return:  n/a
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
                    print("Dealer Wins!")
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

def main():
    # Main
    game = Game()
    game.runGame()

if __name__ == "__main__":
    main()