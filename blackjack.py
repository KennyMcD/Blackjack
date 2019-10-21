# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 11:17:17 2019

@author: kenny
"""

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank= rank
        print(str(suit) + " " + str(rank))