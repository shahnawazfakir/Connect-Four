#
# ps9pr3.py  (Problem Set 9, Problem 3)
#
# Playing the game 
#   

from ps9pr1 import Board
from ps9pr2 import Player
import random
    
def connect_four(p1, p2):
    """ Plays a game of Connect Four between the two specified players,
        and returns the Board object as it looks at the end of the game.
        inputs: p1 and p2 are objects representing Connect Four
          players (objects of the class Player or a subclass of Player).
          One player should use 'X' checkers and the other player should
          use 'O' checkers.
    """
    # Make sure one player is 'X' and one player is 'O'.
    if p1.checker not in 'XO' or p2.checker not in 'XO' \
       or p1.checker == p2.checker:
        print('need one X player and one O player.')
        return None

    print('Welcome to Connect Four!')
    print()
    b = Board(6, 7)
    print(b)
    
    while True:
        if process_move(p1, b) == True:
            return b

        if process_move(p2, b) == True:
            return b

# function 1

def process_move(p, b):
    """ Takes in two parameters, a Player object p for the player whose move 
        is being processed, and a Board object b for the board on which the 
        game is being played. Performs several tasks such as printing whose
        turn it is, obtaining player's next move, applying the move on the 
        board, and checks to see if the move results in a win or tie.
    """
    print(str(p) + "'s turn")
    p_next_move = p.next_move(b)
    b.add_checker(p.checker, p_next_move)
    print()
    print(b)
    
    if b.is_win_for(p.checker) == True:
        print()
        print(str(p), 'wins in', p.num_moves, 'moves.')
        print('Congratulations!')
        return True
    elif b.is_full() == True:
        print()
        print("It's a tie!")
        return True
    else:
        print()
        return False

# function 2

class RandomPlayer(Player):
    
    def next_move(self, b):
        """ Takes in a Board object 'b' as a parameter and chooses a column at 
            random from the columns in the board 'b' that are not full yet, and 
            returns the index of that randomly selected column.
        """
        self.num_moves += 1
        availabel_cols = [col for col in range(b.width) if b.can_add_to(col) == True]
        return random.choice(availabel_cols)