# [Wizard card game](https://en.wikipedia.org/wiki/Wizard_(card_game)).

## General Game mechanics

* deck has 60 cards. 13 of each colour (52) + 8 special cards(4 wizards & 4 fools)
* wizard card is most powerful. The first player to place wizard card always wins the round.
* fool card is the least powerful. The first player to place fool card always looses the round.
* regular card works based on their numerical value (i.e. red fighter 3 < red captain 7)
* The game is divided in sessions (called rounds in original documentation). 
* First session gives each player one card in hand -> 1 round. 
* Next session gives two cards and so forth until all the deck is distributed among players.
* Before the start of each session players are asked how many rounds they expect to win.
* `Key to win the game is to correctly predict how many rounds you can win in session.`
* During round each player must place 1 card of their hand (complying with the card placing rules). 
* `Highest value card wins the round.`
More info can be found [here](https://en.wikipedia.org/wiki/Wizard_(card_game)).

## Code mechanics
* 1 human player.
* Human player can choose between 2-5 computer opponents.

### Variables:
* list `cards` - all cards that are used in deck
* dict `cards_values`: card name : card game value , card bid likelyhood(%) of computer player
* list `CPU_names` - list of available CPU players to join in the game.

* list `player_list` - contains: player name,player score, player queue line for session, player queue line for round, player current hand class object (hand for human, computer_hand for computer)

### Classes
#### 1. Deck_class - recreated each time a new session starts: 
 * Copies in the cards and card_values. 
 * Determines the session dominant card, enhances the card_values for dominant colour cards.
 * distributes the cards to players.
 ##### 1.1 Find_dominant function
 * once deck is shuffled, random card is selected (popped) out of deck.
 * if it's a colour card it determines the session dominant colour. If it's not colour, there is no dominant card.
 * the popped card is out of the game for that session.
 ##### 1.2 Evaluate deck
* for cards in deck with dominant colour, the deck_values are adjusted(need to be calibrated further)
* 20 basis points so that dominant card would overrule any other colour card if allowed
* +0.25 % chance that cpu would bid to win on this card during bidding session. 
##### 1.3 deal
* function used to pop cards out of deck and return to player hand(s)

#### 2. Hand - A human player class. Recreated each time a new session starts:
 * Holds available cards for human player for current session.
 * placing the bid for current session function.
 * placing card for current round function.
##### 2.1 add_card
* human adds cards to his hand from the deck (function connected to the 1.3 deal)
##### 2.2 place_bid
* player is given a question how many bids he wants to make in a session
* answer within game rules is inserted into bid_list
##### 2.3 place_card
* User is asked to select card from his deck, which is then validated and if accepted placed.

#### 3. Computer_Hand - recreated each time a new session starts:
 * Holds available cards for computer player for current session.
 * Evaluating cards &placing the bid for current session function.
 * Evaluating cards & placing card for current round function
##### 3.1 place_bid 
 * CPU evalutes all his cards and based on its value and % chance determines if he wants to bid on it.
##### 3.2 place_card
* defines what cards cpu can place in the round.
* defines min/max values of his cpu_round_cards.
* defines if CPU wants to win/lose, can cpu win/lose and takes the action (based on its score in the bid_list and the current winner score)
* round dominant colour determined.




