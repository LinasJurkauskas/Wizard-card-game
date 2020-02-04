import random
import copy


def get_av_cards(cards, round_colour, dominant_colour, deck_values):
    """
    creates a temporary list of all available cards in player hand
    list is later on used to define which card to place
    """
    available_cards = []
    for card in cards:
        if round_colour == "None":
            # 1.1 no round dominant colour yet, all cards can be used:
            available_cards.append([card, deck_values[card][0]])
            # 1.2 wizard and fool can be used all the time:
        elif card == "Wizard" or card == "Fool":
            available_cards.append([card, deck_values[card][0]])
        elif round_colour != "None":
            # 1.3 round dominant colour exists, if cpu has card in deck he is limited to only using round dominant colour.
            nr_w_dominant_colour = 0
            # 1.3.1checks if cpu player has dominant colour
            for card2 in cards:
                if round_colour in card2:
                    nr_w_dominant_colour = 1
            # 1.3.2 if cpu has no round dominant all cards can be placed.Else only the round dominant ones
            if nr_w_dominant_colour == 0 or round_colour in card:
                if round_colour in card or dominant_colour in card:
                    # 1.3.2.1 if card is session or round dominant, it retains its value
                    available_cards.append([card, deck_values[card][0]])
                else:  # 1.3.2.2 other colour cards can be added but they have no value
                    available_cards.append([card, 1])
            else:
                pass
                # card not added
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
        if len(max_loss_card) == 0 or (
            max_loss_card[1] < card[1] and card[1] < winner_val
        ):
            max_loss_card = card

    return max_loss_card


def find_min_loss_card(available_cards):
    min_loss_card = []
    for card in available_cards:
        if len(min_loss_card) == 0 or (min_loss_card[1] > card[1]):
            min_loss_card = card

    return min_loss_card


def place_card(name, card):
    placed_card = []
    placed_card.append(name)
    placed_card.append(card[0])
    placed_card.append(card[1])

    return placed_card
