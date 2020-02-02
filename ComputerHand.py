import random


class ComputerHand():
    def __init__(self,name):
        self.cards = []
        self.bid = 0
        self.name = name

    def AddCard(self,card, card_nr):
        self.cards.append(card)
    
    def place_bid(self, bid_list, session_nr, deck_values):      
        cp_bid = 0
        for card in self.cards:
            if random.random() < deck_values[card][1]:
                cp_bid += 1
        bid_list[self.name] = [cp_bid,0]
        print(self.name, ' bids ', cp_bid)
        return bid_list

    def place_card(self,  dominant_colour, round_colour, winner, deck_values,bid_list):
        import HandFunctions as HF
        available_cards = HF.get_av_cards(self.cards, round_colour, dominant_colour, deck_values)
        max_val = max(card[1] for card in available_cards)

        if bid_list[self.name][0] > bid_list[self.name][1]:
            if max_val > winner[2]:
                #3.1.1cpu wants to win and can win:
                card = HF.find_win_card(available_cards,winner[2])
                placed_card = HF.place_card(self.name,card)
                self.cards.remove(placed_card[1])
            else:
                #3.1.2 cpu wants to win but he cannot:
                card = HF.find_min_loss_card(available_cards)
                placed_card = HF.place_card(self.name,card)
                self.cards.remove(placed_card[1])                          
        else:
            #3.2 CPU wants to lose:
            card = HF.find_max_loss_card(available_cards,winner[2])
            placed_card = HF.place_card(self.name,card)
            self.cards.remove(placed_card[1]) 

        print(self.name, 'places:', placed_card[1])
        return placed_card

