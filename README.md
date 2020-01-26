# Wizard card game
Python projects
a learning python github to test skills and build rookie projects.
#Game flow: https://en.wikipedia.org/wiki/Wizard_(card_game)
#deck has 60 cards. 13 of each colour (52) + 8 special cards(4 wizards & 4 fools)
#wizard card is most powerful. The first player to place wizard card always wins the round.
#fool card is the least powerful. The first player to place fool card always looses the round.
#regular card works based on their numerical value (i.e. red fighter 3 < red captain 7)

#There is 1 human player and 2-5 CPU players.
#The game is divided in sessions. Each session increases the number of cards in hand and therefore rounds.
#Before the start of each session players are asked how many rounds they expect to win.
#First session has players 1 card in hand -> 1 round. Next session 2 and so forth until all the deck is distributed among players.
#Key to win the game is to correctly predict how many rounds you can win in session.
#During round each player must place 1 card of their hand (complying with the card placing rules). Highest value card wins the round.
#After each session the score is calculated and updated.
#highest total score at the end of the game wins!
#--------------------------------------------------------------------------------------------------------------------------------------------
#Starting variables:
#cards - Full list of all cards that are used in deck
#cards_values - a dictionary of cards with [card game value, card bid likelyhood(%) for cpu]
#cards & card_values are copied into the deck class each session, where their card game values may be modified depending on the session dominant card.
#CPU_names - list of available CPU players to join in the game.
#
#player_list - the master list of lists cointaining:
#1. player name
#2. player score
#3. player line number for session
4. player line number for round
5. player class object (had for human, computer_hand for computer)

#Classes
#1. Deck_class - recreated each time a new session starts: 
 1.1 Copies in the cards and card_values. 
 1.2 Determines the session dominant card, enhances the card_values for dominant colour cards.
 1.3 distributes the cards to players.

 2. Hand - A human player class. Recreated each time a new session starts:
 2.1 Holds available cards for human player for current session.
 2.2 placing the bid for current session function.
 2.3 placing card for current round function.

 3. Computer_Hand - recreated each time a new session starts:
 3.1 Holds available cards for computer player for current session.
 3.2 Evaluating cards &placing the bid for current session function.
 3.3 Evaluating cards & placing card for current round function

#FUNCTIONS
#identify_winner()
#global player_list
#testing
