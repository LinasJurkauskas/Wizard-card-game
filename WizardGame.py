# used libraries
import random
import time
#import sys
#import copy
#-- Other modules
import Variables
import DeckClass
import PlayerHand as PH
import ComputerHand
import OrderFunctions as OF
import HandFunctions as HF
   
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
                    time.sleep(1)
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
            time.sleep(1)
            print('--------------------------------------------------------------------------------')
            print('Session ', session_nr,'out of ',total_sessions, ' begins!')
            print('This Session dominates: ',deck.dominant_card)
            print('--------------------------------------------------------------------------------')
    #----------------------------------Hands----------------------------------------------------------
            for player in player_list:
                if player[0] == human_player:
                    player[4] = PH.Hand(player[0])
                else:
                    player[4] = ComputerHand.ComputerHand(player[0])     
            for player in player_list:
                card_nr = 1
                while card_nr <= session_nr:
                    player[4].AddCard(deck.deck.pop(),card_nr)
                    card_nr += 1
    #------------------------------------------Bidding----------------------------------------------------------
            bid_list = {}
            for player in player_list:
                bid_list = player[4].place_bid(bid_list, session_nr, deck.deck_values)
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
                time.sleep(1)
#------------------------------------------Placing cards----------------------------------------              
                for player in player_list:
                    placed_card = player[4].place_card(deck.dominant_colour, round_colour[0], winner, deck.deck_values, bid_list)
                    #print(placed_card)
                    round_colour[0] = OF.check_round_dominant(round_colour[0],placed_card[1])
                    #print(round_colour)
                    winner = OF.find_winner(winner, placed_card, round_colour[0], deck.dominant_colour)
                    #print(winner)
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
                player_list = OF.round_reorder(player_list, winner[0])
                round_nr += 1
#------------------------------------------------------------------------------------
            OF.score_updater(player_list, bid_list)
            #time.sleep(2)    
            print('Results: (sessions ,',session_nr,'/',total_sessions, ')')
            for player in player_list:
                print(player[0], 'score: ', player[1],'bids/wins: ', bid_list[player[0]])
            player_list = OF.session_reorder(player_list)
            #next session!  
            session_nr += 1  
            continue

        print('--------------------------------------------------------------------------------')
        print('-----------------------------Game over------------------------------------------')
        print('--------------------------------------------------------------------------------')


        



   


  
  
  
