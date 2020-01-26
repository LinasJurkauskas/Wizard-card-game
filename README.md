# Wizard card game

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
* list 'cards' - all cards that are used in deck
* dict `cards_values`: card name : card game value , card bid likelyhood(%) of computer player
* list `CPU_names` - list of available CPU players to join in the game.

#### player_list - the master list of lists cointaining:
#1. player name
#2. player score
#3. player line number for session
4. player line number for round
5. player class object (hand for human, computer_hand for computer)

### Classes
#### 1. Deck_class - recreated each time a new session starts: 
 * Copies in the cards and card_values. 
 * Determines the session dominant card, enhances the card_values for dominant colour cards.
 * distributes the cards to players.

#### 2. Hand - A human player class. Recreated each time a new session starts:
 * Holds available cards for human player for current session.
 * placing the bid for current session function.
 * placing card for current round function.

#### Computer_Hand - recreated each time a new session starts:
 * Holds available cards for computer player for current session.
 * Evaluating cards &placing the bid for current session function.
 * Evaluating cards & placing card for current round function

### FUNCTIONS
#### 1. identify_winner()

