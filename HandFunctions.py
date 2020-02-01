import WizardGame
import DeckClass


def get_av_cards(cards,round_colour, dominant_colour):
    '''
    creates a temporary list of all available cards in player hand
    list is later on used to define which card to place
    '''
    available_cards = []
    for card in cards:
        if round_colour == 'None':
            #1.1 no round dominant colour yet, all cards can be used:
            available_cards.append([card, WizardGame.deck.deck_values[card][0]])
            #1.2 wizard and fool can be used all the time:
        elif card == 'Wizard' or card == 'Fool':
            available_cards.append([card, WizardGame.deck.deck_values[card][0]])
        elif round_colour[0] != 'None':
            #1.3 round dominant colour exists, if cpu has card in deck he is limited to only using round dominant colour.
            nr_w_dominant_colour = 0
            #1.3.1checks if cpu player has dominant colour
            for card2 in cards:
                if round_colour in card2:
                    nr_w_dominant_colour = 1
            #1.3.2 if cpu has no round dominant all cards can be placed.Else only the round dominant ones
            if nr_w_dominant_colour == 0 or round_colour in card:
                if round_colour in card or dominant_colour in card:
                    #1.3.2.1 if card is session or round dominant, it retains its value
                    available_cards.append([card, WizardGame.deck.deck_values[card][0]])
                else: #1.3.2.2 other colour cards can be added but they have no value
                    available_cards.append([card, 1])
            else:
                pass 
                    #card not added
    return available_cards

                      
      # cpu_round_cards = []
        # for cpu_card1 in self.cards:
        #     if round_colour[0] == 'None':
        #         #1.1 no round dominant colour yet, all cards can be used:
        #         cpu_round_cards.append([cpu_card1, deck.deck_values[cpu_card1][0]])
        #         #1.2 wizard and fool can be used all the time:
        #     elif cpu_card1 == 'Wizard' or cpu_card1 == 'Fool':
        #         cpu_round_cards.append([cpu_card1, deck.deck_values[cpu_card1][0]])
        #     elif round_colour[0] != 'None':
        #         #1.3 round dominant colour exists, if cpu has card in deck he is limited to only using round dominant colour.
        #         cpu_w_dominant_colour = 0
        #         #1.3.1checks if cpu player has dominant colour
        #         for cpu_card2 in self.cards:
        #             if round_colour[0] in cpu_card2:
        #                 cpu_w_dominant_colour = 1
        #         #1.3.2 if cpu has no round dominant all cards can be placed.Else only the round dominant ones
        #         if cpu_w_dominant_colour == 0 or round_colour[0] in cpu_card1:
        #             if round_colour[0] in cpu_card1 or deck.dominant_colour in cpu_card1:
        #                 #1.3.2.1 if card is session or round dominant, it retains its value
        #                 cpu_round_cards.append([cpu_card1, deck.deck_values[cpu_card1][0]])
        #             else: #1.3.2.2 other colour cards can be added but they have no value
        #                 cpu_round_cards.append([cpu_card1, 1])
        #         else:
        #             pass  


    