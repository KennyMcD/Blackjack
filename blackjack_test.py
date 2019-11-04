# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 13:58:28 2019

@author: kenny
"""
import blackjack
import unittest

class TestFunctions(unittest.TestCase):
    def test_ace(self):
        # Creating card objects for ace check
        ace = blackjack.Card("♣", 'A')
        king = blackjack.Card("♣", 'K')
        queen = blackjack.Card("♣", 'Q')
        
        # Creating the player's hand
        playerHand = [ace, king, queen]
        hand = blackjack.Hand([])
        hand.setNumCards(3)
        
        # Hand value should be 21, this shows ace's
        # will switch from 11 to 1
        val = hand.handValue(playerHand)
        actual = val
        expected = 21
        
        # Check if hand is equal to 21
        self.assertEqual(expected, actual, "Failed ace test")

    def test_two_ace(self):
        # Creating card objects for ace check
        aceOne = blackjack.Card("♣", 'A')
        aceTwo = blackjack.Card("♣", 'A')
        queen = blackjack.Card("♣", 'Q')
        nine = blackjack.Card("♣", '9')
        
        # Creating the player's hand
        playerHand = [aceOne, aceTwo, queen, nine]
        hand = blackjack.Hand([])
        hand.setNumCards(4)
        
        # Hand value should be 21, this shows ace's
        # will switch from 11 to 1
        val = hand.handValue(playerHand)
        actual = val
        expected = 21
        
        # Check if hand is equal to 21
        self.assertEqual(expected, actual, "Failed two ace test")
        
if __name__ == "__main__":
    unittest.main() 