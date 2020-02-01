import Variables
import random
import copy

class DeckClass():

    def __init__(self):
        '''
        See ReadMe Classes - 1.
        '''
        self.dominant_colour = ''
        self.dominant_card = ''
        self.deck = []
        self.deck_values = {}
        self.deck_values = copy.deepcopy(Variables.cards_values)
        for card in Variables.cards:
            self.deck.append(card)

    def Shuffle(self):
        random.shuffle(self.deck)

    def FindDominant(self):
        self.dominant_card = str(self.deck.pop())
        if self.dominant_card.find('[') == -1:
            self.dominant_colour = 'None'
        else:
            colour_list = self.dominant_card.split(']')
            self.dominant_colour = colour_list[0].replace('[','')
        return self.dominant_colour

    def EvaluateDeck(self):
        for value in self.deck_values:
            if value.find(self.dominant_colour) == -1:
                pass
            else:
                self.deck_values[value][0] = self.deck_values[value][0] + 20
                self.deck_values[value][1] = self.deck_values[value][1] + 0.25

    def Deal(self):
        single_card = self.deck.pop()
        return single_card