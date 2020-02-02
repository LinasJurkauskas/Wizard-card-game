import WizardGame as Main
import HandFunctions as HF


#--------------------------------------------------------------------- PLAYER HAND------------------------------------------------
class Hand():
    def __init__(self,name):
        self.cards = {}
        self.bid = 0
        self.name = name

    def AddCard(self,card,card_nr):
        self.cards[card_nr] = card

    def PlaceBid(self):
        bidding = 1
        while bidding == 1:
            try:
                print('your cards:', self.cards)
                input_bid = int(input('Make a bid on how many rounds you expect to win: ')) 
                if input_bid > session_nr:
                    print("Can't bid more than there are rounds in this session!")
                else:
                        self.bid = int(input_bid)
                        bid_list[self.name] = [int(input_bid),0]
                        print(self.name, ' bids ', bid_list[self.name][0] )
                        break
            except:
                print('invalid number provided!')
                continue 

    def PlaceCard(self):
        placed_card = []
        print('--------------------------------------------------------')
        print('Dominant Colour of this session: ', Main.deck.dominant_colour)
        print('Dominant Colour of this round: ', Main.round_colour[0])
        print('Remaining cards in your hand:', self.cards)
        print('--------------------------------------------------------')
        card_valid = False
        while card_valid == False:
            try:
                player_move = int(input('Place a card (Key nr)'))
    #------------------------------------Input validation----------------------------------------------
                if not int(player_move) in self.cards.keys():
                    print(self.cards)
                    print('invalid card, try again:')
                elif self.cards[player_move] == 'Wizard' or self.cards[player_move] == 'Fool':
                    card_valid = True
                    break
    #------------------------------------Checks if user has no round colours in case he is using another colour-------------
                elif round_colour[0] != 'None' and self.cards[player_move].split(']')[0].replace('[','') != round_colour[0]:
                    for card in self.cards.values():
                        if round_colour[0] in card:
                            print('You must select the round colour card if you have one in your hand!')
                            card_valid = False
                            break
                        card_valid = True
                else:
                    card_valid = True
                    break
            except:
                print('invalid key provided!')
                continue 
#------------------------------------Placing the card-----------------------------------------------------------------------
        if card_valid == True: 
            HF.place_card(self.name, [self.cards[player_move], Main.deck.deck_values[self.cards[player_move]][0]])
            # placed_card[0] = self.name 
            # placed_card[1] = self.cards[player_move] 
            # placed_card[2] = deck.deck_values[self.cards[player_move]][0]
            print(self.name, ' places: ',self.cards[player_move])
            del self.cards[player_move]
            return placed_card