'''
see ReadMe Functions part
'''

def session_reorder(player_list):
    for player in player_list:
        if player[2] == len(player_list)-1:
            player[2] = 0
        else:
            player[2] += 1
    player_list = sorted(player_list, key=lambda x: x[2], reverse=False)   
    return player_list


def round_reorder(player_list, winner):
    i = 0
    for player in player_list:
        if player[0] == winner:
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
    return player_list


def score_updater(player_list,bid_list):
    '''
    Rewards players with correct bids.
    Takes away points for players who missed their bids.
    '''
    for player in player_list:
        player_name = player[0]
        if bid_list[player_name][0] ==  bid_list[player_name][1]:
            player[1] = player[1] + (bid_list[player_name][0]*20)+20
        else:
            diff = (abs(bid_list[player_name][0] - bid_list[player_name][1]))*10
            player[1] = player[1] - diff
    return player_list


def find_winner(winner, placed_card, round_colour,dominant_colour):
    '''
    Checks if newly placed card is better than current winner card and replaces if so.
    '''
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
    elif dominant_colour in placed_card[1] and int(placed_card[2])> winner[2]:
        #user has session colour card that is higher than current winner score
        winner[0] = placed_card[0]
        winner[1] = placed_card[1]
        winner[2] = placed_card[2]
    elif round_colour in placed_card[1] and int(placed_card[2]) > winner[2]:
        #user has round colour card that is higher than current winner score
        winner[0] = placed_card[0]
        winner[1] = placed_card[1]
        winner[2] = placed_card[2]
    
    return winner

   
def check_round_dominant(round_colour,card):
    if round_colour == 'None' and card.find('[') != -1:
        round_colour = card.split(']')[0].replace('[','')
    else: 
        round_colour
    return round_colour
