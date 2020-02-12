# used libraries
import random
import time

# Other modules
import Constants as VAR
import DeckClass as DC
import PlayerHand as PH
import ComputerHand as CH
import MainFunctions as MF
import HandFunctions as HF

# ---------------------------------------------GAME STARTS-----------------------
if __name__ == "__main__":

    while True:
# --------------------------------------------------------------------------------
        play_question = input("Welcome to Wizard! play? (Y/N)")

        if not play_question.lower().startswith("y"):
            print("your loss!")
            break
        else:
            players_nr = False
            while players_nr == False:
                try:
                    human_player = input("what's your name?: ")
                    nr_players = int(
                        input("how many CPU players you want to go against?(2-5)?")
                    )
                    if nr_players < 2 or nr_players > 5:
                        print("invalid number of players!")
                        continue
                    else:
                        print("let's go!")
                        time.sleep(1)
                        break
                except:
                    print("invalid number of players!")
                    continue
# --------------------------------------------------------------------
            player_list = []
            player_list.append([human_player, 0, 0, 0, ""])
            random.shuffle(VAR.computer_names)
            # Setting the numbers for queueing
            nr = 1
            while nr <= nr_players:
                player_list.append([VAR.computer_names[nr], 0, nr, nr, ""])
                player_list[nr][1] = 0
                player_list[nr][2] = nr
                player_list[nr][3] = nr
                player_list[nr][4] = ""
                nr += 1
            print("Players!:")
            for player in player_list:
                print(player[0])
                time.sleep(0.5)

            total_sessions = int(60 / len(player_list))
            print("Number of sessions in the game:", total_sessions)
            session_nr = 1
# ----------------------------------Deck initialize------------------------
            while session_nr <= total_sessions:
                deck = DC.DeckClass()
                deck.Shuffle()
                # last session does not look for dominant, all deck is distributed.
                if session_nr < total_sessions:
                    deck.dominant_colour = deck.FindDominant()
                deck.EvaluateDeck()
                MF.session_initialize_print(session_nr,total_sessions, deck.dominant_card)
# ----------------------------------Hands-------------------------------
                for player in player_list:
                    if player[0] == human_player:
                        player[4] = PH.Hand(player[0])
                    else:
                        player[4] = CH.ComputerHand(player[0])
                for player in player_list:
                    card_nr = 1
                    while card_nr <= session_nr:
                        player[4].add_card(deck.deck.pop(), card_nr)
                        card_nr += 1
# ------------------------------------------Bidding----------------------------
                bid_list = {}
                for player in player_list:
                    bid_list = player[4].place_bid(bid_list, session_nr, deck.deck_values)
                    time.sleep(0.5)
                MF.bid_list_print(bid_list,0)
# ------------------------------------Round-----------------------------------
                round_nr = 1
                while round_nr <= session_nr:
                    winner = ["None", "None", 0]
                    placed_card = ["None", "None", 0]
                    round_colour = ["None"]
                    MF.round_initialize_print(round_nr)
# --------------------------------Placing cards------------------------
                    for player in player_list:
                        placed_card = player[4].place_card(
                            deck.dominant_colour,
                            round_colour[0],
                            winner,
                            deck.deck_values,
                            bid_list,
                        )
                        round_colour[0] = MF.check_round_dominant(
                            round_colour[0], placed_card[1]
                        )
                        winner = MF.find_winner(
                            winner, placed_card, round_colour[0], deck.dominant_colour
                        )
                        time.sleep(1)

                    winner2 = winner[0]
                    bid_list[winner2][1] = bid_list[winner2][1] + 1

# ----------------------------Declaring winner----------------------------
                    MF.winner_print(winner[0],round_nr)
                    MF.bid_list_print(bid_list,1)

                    player_list = MF.round_reorder(player_list, winner[0])
                    round_nr += 1
# ------------------------------------------------------------------------
                MF.score_updater(player_list, bid_list)
                MF.results_print(session_nr,total_sessions,player_list,bid_list)
                player_list = MF.session_reorder(player_list)
                test = input("Press Enter to Continue ")
                if test == "exit":
                    break
                session_nr += 1
                continue
            MF.game_over_print
