import HandFunctions as HF

# --------------------------------------------------------------------- PLAYER HAND------------------------------------------------
class Hand:
    def __init__(self, name):
        self.cards = {}
        self.bid = 0
        self.name = name

    def add_card(self, card, card_nr):
        self.cards[card_nr] = card

    def place_bid(self, bid_list, session_nr, deck_values):
        bidding = 1
        while bidding == 1:
            try:
                print("your cards:", self.cards)
                input_bid = int(
                    input("Make a bid on how many rounds you expect to win: ")
                )
                if input_bid > session_nr:
                    print("Can't bid more than there are rounds in this session!")
                else:
                    self.bid = int(input_bid)
                    bid_list[self.name] = [int(input_bid), 0]
                    print(self.name, " bids ", bid_list[self.name][0])
                    break
            except:
                print("invalid number provided!")
                continue
        return bid_list

    def place_card(self, dominant_colour, round_colour, winner, deck_values, bid_list):
        print("--------------------------------------------------------")
        print("Dominant Colour of this session: ", dominant_colour)
        print("Dominant Colour of this round: ", round_colour)
        print("Remaining cards in your hand:", self.cards)
        print("--------------------------------------------------------")
        card_valid = False
        while card_valid == False:
            try:
                player_move = int(input("Place a card (Key nr)"))
                # ------------------------------------Input validation----------------------------------------------
                if not int(player_move) in self.cards.keys():
                    print("invalid card, try again:")
                elif (
                    self.cards[player_move] == "Wizard"
                    or self.cards[player_move] == "Fool"
                ):
                    card_valid = True
                    break
                # ------------------------------------Checks if user has no round colours in case he is using another colour-------------
                elif (
                    round_colour != "None"
                    and self.cards[player_move].split("]")[0].replace("[", "")
                    != round_colour
                ):
                    for card in self.cards.values():
                        if round_colour in card:
                            print(
                                "You must select the round colour card if you have one in your hand!"
                            )
                            card_valid = False
                            break
                        card_valid = True
                else:
                    card_valid = True
                    break
            except:
                print("invalid key provided!")
                continue
        # ------------------------------------Placing the card-----------------------------------------------------------------------
        if card_valid == True:
            placed_card = HF.place_card(
                self.name,
                [self.cards[player_move], deck_values[self.cards[player_move]][0]],
            )

            print(self.name, " places: ", self.cards[player_move])
            del self.cards[player_move]
            return placed_card
