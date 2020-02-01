import WizardGame

def SessionReorder(player_list):
    for player in player_list:
        if player[2] == len(player_list)-1:
            player[2] = 0
        else:
            player[2] += 1
    player_list = sorted(player_list, key=lambda x: x[2], reverse=False)   
    return player_list


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
    return player_list