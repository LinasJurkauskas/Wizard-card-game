import WizardGame
import DeckClass
import random


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

# def cpu_action(name), min_val, max_val):
#     '''
#     Defines whether computer wants to win or lose the round
#     And if he is able to do that
#     '''
#     if bid_list[self.name][0] > bid_list[self.name][1]:
#         win = 1
#     else:
#         win = 0
    
#     if win = 1 and max_val 

def find_win_card(available_cards, winner_val):
    win_cards = []
    for card in available_cards:
        if card[1] > winner_val:
            win_cards.append(card)

    random.shuffle(win_cards)
    win_card = win_cards.pop()   
    return win_card

def find_max_loss_card(available_cards, winner_val):
    max_loss_card = []
    for card in available_cards:
        if len(max_loss_card) == 0 or (max_loss_card[1] < card[1] and card[1] < winner_val):
            max_loss_card = card
    
    return max_loss_card

def find_min_loss_card(available_cards):
    min_loss_card = []
    for card in available_cards:
        if len(min_loss_card) == 0 or (min_loss_card[1] > card[1]):
            min_loss_card = card
    
    return min_loss_card

def place_card(name,card):
    placed_card = []
    placed_card.append(name)
    placed_card.append(card[0])
    placed_card.append(card[1])

    return placed_card








# def get_min_max_cards(available_cards):
#     '''
#     gets min and max values available_cards
#     '''

#     min(x[1] for x in gen)

#     min_val = None
#     max_val = None
#     for card in cpu_round_cards:     
#         if min_val == None or min_val > card[1]:
#             min_val = card[1]
#         if max_val == None or max_val < card[1]:
#             max_val = card[1]

#     return (min_val, max_val)

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


    