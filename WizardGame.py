# used libraries
import random
import time
import sys
import copy
#-- Other modules
import Variables
import DeckClass
import PlayerHand
import OrderFunctions
import HandFunctions

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
        print('--------------------------------------------------------')
        print('Dominant Colour of this session: ', deck.dominant_colour)
        print('Dominant Colour of this round: ', round_colour[0])
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
            placed_card[0] = self.name 
            placed_card[1] = self.cards[player_move] 
            placed_card[2] = deck.deck_values[self.cards[player_move]][0]
            print(self.name, ' places: ',self.cards[player_move])
            return placed_card

#--------------------------------------------------------------------- COMPUTER HAND----------------------------------------
class ComputerHand():
    def __init__(self,name):
        self.cards = []
        self.bid = 0
        self.name = name

    def AddCard(self,card, card_nr):
        self.cards.append(card)
    
    def PlaceBid(self):
        cp_bid = 0
        for card in self.cards:
            if random.random() < deck.deck_values[card][1]:
                cp_bid += 1
        bid_list[self.name] = [cp_bid,0]
        print(self.name, ' bids ', cp_bid)

    def PlaceCard(self): 
        available_cards = HandFunctions.get_av_cards(self.cards, round_colour[0], deck.dominant_colour)
        max_val = max(card[1] for card in available_cards)

        if bid_list[self.name][0] > bid_list[self.name][1]:
            if max_val > winner[2]:
                #3.1.1cpu wants to win and can win:
                card = HandFunctions.find_win_card(available_cards,winner[2])
                placed_card = HandFunctions.place_card(self.name,card)
                self.cards.remove(placed_card[1])
            else:
                #3.1.2 cpu wants to win but he cannot:
                card = HandFunctions.find_min_loss_card(available_cards)
                placed_card = HandFunctions.place_card(self.name,card)
                self.cards.remove(placed_card[1])                          
        else:
            #3.2 CPU wants to lose:
            card = HandFunctions.find_max_loss_card(available_cards,winner[2])
            placed_card = HandFunctions.place_card(self.name,card)
            self.cards.remove(placed_card[1]) 

        print(self.name, 'places:', placed_card[1])
        return placed_card



   
#--------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------GAME STARTS------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------

while True:
#--------------------------------------------------------------------------------------------------------------------------------
    play_question = input('Welcome to Wizard! play? (Y/N)')

    if not play_question.lower().startswith('y'):
        print('your loss!')
        break
    else:
        players_nr = False
        while players_nr == False:
            try:
                human_player = input("what's your name?: ")
                nr_players = int(input('how many CPU players you want to go against?(2-5)?'))
                if nr_players < 2 or nr_players > 5:
                    print('invalid number of players!')
                    continue
                else:
                    print("let's go!")
                    #time.sleep(2)
                    break
            except:
                print('invalid number of players!')
                continue
#-------------------------------------------------------------------------------------------------------------------
        player_list = [] 
        player_list.append([human_player,0,0,0,''])
        random.shuffle(Variables.computer_names)
        #Setting the numbers for queueing
        nr = 1
        while nr <= nr_players:
            player_list.append([Variables.computer_names[nr], 0, nr, nr, ''])
            player_list[nr][1] = 0
            player_list[nr][2] = nr
            player_list[nr][3] = nr
            player_list[nr][4] = ''
            nr += 1
        print('Players!:')
        for player in player_list:
            print(player[0])

        #time.sleep(1)
        total_sessions = int(60/len(player_list))
        print('Number of sessions in the game:', total_sessions)
        session_nr = 1     
#----------------------------------Deck initialize----------------------------------------------------------
        while session_nr <= total_sessions:
            deck = DeckClass.DeckClass() 
            deck.Shuffle()
            #last session does not look for dominant, all deck is distributed.
            if session_nr < total_sessions: 
                deck.dominant_colour = deck.FindDominant()
            deck.EvaluateDeck()
            print('--------------------------------------------------------------------------------')
            print('Session ', session_nr,'out of ',total_sessions, ' begins!')
            #time.sleep(2)
            print('This Session dominates: ',deck.dominant_card)
            print('--------------------------------------------------------------------------------')
    #----------------------------------Hands----------------------------------------------------------
            for player in player_list:
                if player[0] == human_player:
                    player[4] = Hand(player[0])
                else:
                    player[4] = ComputerHand(player[0])       
            for player in player_list:
                #print(player)
                card_nr = 1
                while card_nr <= session_nr:
                    #print(deck.deck.pop())
                    #print(player[4].cards)
                    #player[4].cards[card_nr] = deck.deck.pop()
                    player[4].AddCard(deck.deck.pop(),card_nr)
                    #player[4].AddCard(deck.Deal())
                    card_nr += 1
                    #print(player[4].cards)
    #------------------------------------------Bidding----------------------------------------------------------
            bid_list = {}
            for player in player_list:
                player[4].PlaceBid()
                #time.sleep(1)

            print(bid_list)
            #time.sleep(1)
            print('--------------------------------------------------------------------------------')    
    #------------------------------------------Round----------------------------------------------------------
            round_nr = 1
            while round_nr <= session_nr:
                winner = ['None', 'None', 0]
                placed_card = ['None', 'None', 0]
                round_colour = ['None'] 
                print('Round ', str(round_nr), ' begins!')
                print('--------------------------------------------------------------------------------')
               # time.sleep(2)
#------------------------------------------Placing cards----------------------------------------                
                for player in player_list:
                    placed_card = player[4].PlaceCard()
                    round_colour[0] = OrderFunctions.check_round_dominant(round_colour[0],placed_card[1])
                    winner = OrderFunctions.find_winner(winner, placed_card, round_colour[0], deck.dominant_colour)
                    #time.sleep(1)
                
                winner2 = winner[0]
                bid_list[winner2][1] = bid_list[winner2][1] +1

#------------------------------------------Declaring winner-------------------------------------------------------
                print('--------------------------------------------------------------------------------')
                print(winner[0], 'wins round number ',str(round_nr),'!, score: ', winner[2])
                print('--------------------------------------------------------------------------------')
                print('Score of this session:')
                print(bid_list)
                #time.sleep(2)
                
                #reorder sequence based on winner
                player_list = OrderFunctions.round_reorder(player_list, winner[0])
                round_nr += 1
#------------------------------------------------------------------------------------
            #player_list = OrderFunctions.score_updater(player_list)
            #total_score_updater()
            OrderFunctions.score_updater(player_list, bid_list)
            #time.sleep(2)    
            print('Results: (sessions ,',session_nr,'/',total_sessions, ')')
            for player in player_list:
                print(player[0], 'score: ', player[1],'bids/wins: ', bid_list[player[0]])
            player_list = OrderFunctions.session_reorder(player_list)
            #next session!  
            session_nr += 1  
            continue

        print('--------------------------------------------------------------------------------')
        print('-----------------------------Game over------------------------------------------')
        print('--------------------------------------------------------------------------------')


        



   


  
  
  
