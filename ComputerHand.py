import random


class ComputerHand():
    def __init__(self,name):
        self.cards = []
        self.bid = 0
        self.name = name

    def AddCard(self,card, card_nr):
        self.cards.append(card)
    
    def PlaceBid(self):
        import WizardGame as Main        
        cp_bid = 0
        for card in self.cards:
            if random.random() < Main.deck.deck_values[card][1]:
                cp_bid += 1
        Main.bid_list[self.name] = [cp_bid,0]
        print(self.name, ' bids ', cp_bid)

    def PlaceCard(self): 
        import WizardGame as Main
        import HandFunctions as HF
        available_cards = HF.get_av_cards(self.cards, Main.round_colour[0], Main.deck.dominant_colour)
        max_val = max(card[1] for card in available_cards)

        if Main.bid_list[self.name][0] > Main.bid_list[self.name][1]:
            if max_val > Main.winner[2]:
                #3.1.1cpu wants to win and can win:
                card = HF.find_win_card(available_cards,Main.winner[2])
                placed_card = HF.place_card(self.name,card)
                self.cards.remove(placed_card[1])
            else:
                #3.1.2 cpu wants to win but he cannot:
                card = HF.find_min_loss_card(available_cards)
                placed_card = HF.place_card(self.name,card)
                self.cards.remove(placed_card[1])                          
        else:
            #3.2 CPU wants to lose:
            card = HF.find_max_loss_card(available_cards,Main.winner[2])
            placed_card = HF.place_card(self.name,card)
            self.cards.remove(placed_card[1]) 

        print(self.name, 'places:', placed_card[1])
        return placed_card

