import random
import time
import sys
import copy
import Variables
import DeckClass
import PlayerHand

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
            if round_colour[0] == 'None' and self.cards[player_move].find('[') != -1:
                round_colour[0] = self.cards[player_move].split(']')[0].replace('[','')
            del self.cards[player_move] 

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
        cpu_round_cards = []
        for cpu_card1 in self.cards:
            if round_colour[0] == 'None':
                #1.1 no round dominant colour yet, all cards can be used:
                cpu_round_cards.append([cpu_card1, deck.deck_values[cpu_card1][0]])
                #1.2 wizard and fool can be used all the time:
            elif cpu_card1 == 'Wizard' or cpu_card1 == 'Fool':
                cpu_round_cards.append([cpu_card1, deck.deck_values[cpu_card1][0]])
            elif round_colour[0] != 'None':
                #1.3 round dominant colour exists, if cpu has card in deck he is limited to only using round dominant colour.
                cpu_w_dominant_colour = 0
                #1.3.1checks if cpu player has dominant colour
                for cpu_card2 in self.cards:
                    if round_colour[0] in cpu_card2:
                        cpu_w_dominant_colour = 1
                #1.3.2 if cpu has no round dominant all cards can be placed.Else only the round dominant ones
                if cpu_w_dominant_colour == 0 or round_colour[0] in cpu_card1:
                    if round_colour[0] in cpu_card1 or deck.dominant_colour in cpu_card1:
                        #1.3.2.1 if card is session or round dominant, it retains its value
                        cpu_round_cards.append([cpu_card1, deck.deck_values[cpu_card1][0]])
                    else: #1.3.2.2 other colour cards can be added but they have no value
                        cpu_round_cards.append([cpu_card1, 1])
                else:
                    pass    
        #2 Define max/min values
        cpu_cards_min_val = None
        cpu_cards_max_val = None
        for cpu_card3 in cpu_round_cards:     
            if cpu_cards_min_val == None or cpu_cards_min_val > cpu_card3[1]:
                cpu_cards_min_val = cpu_card3[1]
            if cpu_cards_max_val == None or cpu_cards_max_val < cpu_card3[1]:
                cpu_cards_max_val = cpu_card3[1]
        #3.defines if cpu wants to win
        if bid_list[self.name][0] > bid_list[self.name][1]:
            if cpu_cards_max_val > winner[2]:
                #3.1.1cpu wants to win and can win:
                for cpu_card1 in cpu_round_cards:
                    if cpu_card1[1] == cpu_cards_max_val:
                        #max value card is used:
                        placed_card[0] = self.name 
                        placed_card[1] = cpu_card1[0]
                        card_string  = cpu_card1[0]
                        placed_card[2] = deck.deck_values[card_string][0]
                        self.cards.remove(placed_card[1])
                        print(self.name, 'places:', placed_card[1])
                        break
            else:
                #3.1.2 cpu wants to win but he cannot:
                for cpu_card1 in cpu_round_cards:
                    if cpu_card1[1] == cpu_cards_min_val:
                        #min value card is used:
                        placed_card[0] = self.name 
                        placed_card[1] = cpu_card1[0]
                        card_string  = cpu_card1[0]
                        placed_card[2] = deck.deck_values[card_string][0]
                        self.cards.remove(placed_card[1])
                        print(self.name, 'places:', placed_card[1])
                        break                      
        else:
            #3.2 CPU wants to lose(interested to place highest possible card without taking the win).
            cpu_less_than_w_card_val = None
            for cpu_card1 in cpu_round_cards:
                if cpu_less_than_w_card_val == None:
                    cpu_less_than_w_card_val = cpu_card1[1]
                    placed_card[0] = self.name 
                    placed_card[1] = cpu_card1[0]
                    card_string  = cpu_card1[0]
                    placed_card[2] = deck.deck_values[card_string][0]
            #checks if next card is higher than the existing but still lower than the currenct winner card
                elif cpu_less_than_w_card_val < cpu_card1[1] and cpu_card1[1] < winner[2]:
                    cpu_less_than_w_card_val = cpu_card1[1]
                    placed_card[0] = self.name 
                    placed_card[1] = cpu_card1[0]
                    card_string  = cpu_card1[0]
                    placed_card[2] = deck.deck_values[card_string][0]
            print(self.name, 'places:', placed_card[1])
        #4. round dominant colour is determined if it was not before and the placed card is coloured.
        if round_colour[0] == 'None' and card_string.find('[') != -1:
            round_colour[0] = card_string.split(']')[0].replace('[','')  

def IdentifyWinner():
        if  winner[0] == 'None':
            #first card in round, by default becomes winner.
            winner[0] = placed_card[0]
            winner[1] = placed_card[1]
            winner[2] = placed_card[2]
        elif placed_card[2] == 50 and winner[2] != 50: 
            #user has wizard card and it has not been placed in this round yet.
            winner[0] = placed_card[0]
            winner[1] = placed_card[1]
            winner[2] = placed_card[2]
        elif int(placed_card[2])  == 0 and int(placed_card[2]) == winner[2]:
            #user has fool card but it already has been placed.New placer becomes winner.
            winner[0] = placed_card[0]
            winner[1] = placed_card[1]
            winner[2] = placed_card[2]
        elif deck.dominant_colour in placed_card[1] and int(placed_card[2])> winner[2]:
            #user has session colour card that is higher than current winner score
            winner[0] = placed_card[0]
            winner[1] = placed_card[1]
            winner[2] = placed_card[2]
        elif round_colour[0] in placed_card[1] and int(placed_card[2]) > winner[2]:
            #user has round colour card that is higher than current winner score
            winner[0] = placed_card[0]
            winner[1] = placed_card[1]
            winner[2] = placed_card[2]

def SessionPlayersReorder():
    global player_list
    for player in player_list:
        if player[2] == len(player_list)-1:
            player[2] = 0
        else:
            player[2] += 1
    player_list = sorted(player_list, key=lambda x: x[2], reverse=False)     

def total_score_updater():
    for player in player_list:
        player_name = player[0]
        if bid_list[player_name][0] ==  bid_list[player_name][1]:
            #player bid correctly, rewarded.
            player[1] = player[1] + (bid_list[player_name][0]*20)+20
        else:
            #player bid incorrectly, points taken away.
            diff = (abs(bid_list[player_name][0] - bid_list[player_name][1]))*10
            player[1] = player[1] - diff

def RoundWinnerReorder():
    global player_list
    i = 0
    for player in player_list:
        if player[0] == winner[0]:
            player[3] = 0
            break
        else:
            i += 1
    n = 0
    for player in player_list[i:]:
        player[3] = n
        n += 1

    for player in player_list[:i]:
        player[3] = n
        n += 1
    player_list = sorted(player_list, key=lambda x: x[3], reverse=False)
   
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
                    time.sleep(2)
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

        time.sleep(1)
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
            time.sleep(2)
            print('This Session dominates: ',deck.dominant_card)
            print('--------------------------------------------------------------------------------')
    #----------------------------------Hands----------------------------------------------------------
            for player in player_list:
                if player[0] == human_player:
                    print(player[0])
                    player[4] = PlayerHand.Hand(player[0])
                    #player[4] = PlayerHand.Hand(player[0])
                    #print(player[4])
                else:
                    player[4] = ComputerHand(player[0])   
                    print(player[4])      
            for player in player_list:
                print(player)
                card_nr = 1
                while card_nr <= session_nr:
                    #print(deck.deck.pop())
                    #print(player[4].cards)
                    #player[4].cards[card_nr] = deck.deck.pop()
                    player[4].AddCard(deck.pop(),card_nr)
                    #player[4].AddCard(deck.Deal())
                    card_nr += 1
                    #print(player[4].cards)
    #------------------------------------------Bidding----------------------------------------------------------
            bid_list = {}
            for player in player_list:
                player[4].PlaceBid()
                time.sleep(1)

            print(bid_list)
            time.sleep(1)
            print('--------------------------------------------------------------------------------')    
    #------------------------------------------Round----------------------------------------------------------
            round_nr = 1
            while round_nr <= session_nr:
                winner = ['None', 'None', 0]
                placed_card = ['None', 'None', 0]
                round_colour = ['None'] 
                print('Round ', str(round_nr), ' begins!')
                print('--------------------------------------------------------------------------------')
                time.sleep(2)
#------------------------------------------Placing cards----------------------------------------                
                for player in player_list:
                    player[4].PlaceCard()
                    IdentifyWinner()
                    time.sleep(1)
                
                winner2 = winner[0]
                bid_list[winner2][1] = bid_list[winner2][1] +1

#------------------------------------------Declaring winner-------------------------------------------------------
                print('--------------------------------------------------------------------------------')
                print(winner[0], 'wins round number ',str(round_nr),'!, score: ', winner[2])
                print('--------------------------------------------------------------------------------')
                print('Score of this session:')
                print(bid_list)
                time.sleep(2)
                
                #reorder sequence based on winner
                RoundWinnerReorder()
                round_nr += 1
#------------------------------------------------------------------------------------
            total_score_updater()
            time.sleep(2)    
            print('Results: (sessions ,',session_nr,'/',total_sessions, ')')
            for player in player_list:
                print(player[0], 'score: ', player[1],'bids/wins: ', bid_list[player[0]])
            SessionPlayersReorder()
            #next session!  
            session_nr += 1  
            continue

        print('--------------------------------------------------------------------------------')
        print('-----------------------------Game over------------------------------------------')
        print('--------------------------------------------------------------------------------')


        



   


  
  
  
