#import DeckClass
import random
import copy


def get_av_cards(cards,round_colour, dominant_colour,deck_values):
    '''
    creates a temporary list of all available cards in player hand
    list is later on used to define which card to place
    '''
    available_cards = []
    for card in cards:
        if round_colour == 'None':
            #1.1 no round dominant colour yet, all cards can be used:
            available_cards.append([card, deck_values[card][0]])
            #1.2 wizard and fool can be used all the time:
        elif card == 'Wizard' or card == 'Fool':
            available_cards.append([card, deck_values[card][0]])
        elif round_colour != 'None':
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
                    available_cards.append([card, deck_values[card][0]])
                else: #1.3.2.2 other colour cards can be added but they have no value
                    available_cards.append([card, 1])
            else:
                pass 
                    #card not added
    return available_cards


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

# def h_get_av_cards(cards,round_colour, dominant_colour):
#     '''
#     Used by human player
#     creates a temporary dictionary of all available cards in player hand
#     list is later on used to define which card to place
#     '''
#     i = 0
#     available_cards = {}
#     while i < len(cards):
#         if round_colour == 'None':
#             #1.1 no round dominant colour yet, all cards can be used:
#             available_cards[i] = cards[i]
#             #available_cards.append([card, WizardGame.deck.deck_values[card][0]])
#             #1.2 wizard and fool can be used all the time:
#         elif card == 'Wizard' or card == 'Fool':
#             available_cards[i] = cards[i]
#             #available_cards.append([card, WizardGame.deck.deck_values[card][0]])
#         elif round_colour != 'None':
#             #1.3 round dominant colour exists, if cpu has card in deck he is limited to only using round dominant colour.
#             nr_w_dominant_colour = 0
#             #1.3.1checks if cpu player has dominant colour
#             #for card2 in cards:
#             while i2 < len(cards):
#                 if round_colour in cards[i2]:
#                     nr_w_dominant_colour = 1
#             #1.3.2 if cpu has no round dominant all cards can be placed.Else only the round dominant ones
#             if nr_w_dominant_colour == 0 or round_colour in cards[i][0]:
#                 if round_colour in cards[i][0] or dominant_colour in cards[i][0]:
#                     #1.3.2.1 if card is session or round dominant, it retains its value
#                     #available_cards.append([card, WizardGame.deck.deck_values[card][0]])
#                     available_cards[i] = cards[i]
#                 else: #1.3.2.2 other colour cards can be added but they have no value
#                     available_cards.append([card, 1])
#             else:
#                 pass 
#                     #card not added
#     return available_cards



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


        #             if not int(player_move) in self.cards.keys():
    #                 print(self.cards)
    #                 print('invalid card, try again:')
    #             elif self.cards[player_move] == 'Wizard' or self.cards[player_move] == 'Fool':
    #                 card_valid = True
    #                 break
    # #------------------------------------Checks if user has no round colours in case he is using another colour-------------
    #             elif round_colour[0] != 'None' and self.cards[player_move].split(']')[0].replace('[','') != round_colour[0]:
    #                 for card in self.cards.values():
    #                     if round_colour[0] in card:
    #                         print('You must select the round colour card if you have one in your hand!')
    #                         card_valid = False
    #                         break
    #                     card_valid = True
    #             else:
    #                 card_valid = True
    #                 break
    #         except:
    #             print('invalid key provided!')
    #             continue 

                # placed_card[0] = self.name 
            # placed_card[1] = self.cards[player_move] 
            # placed_card[2] = deck.deck_values[self.cards[player_move]][0]