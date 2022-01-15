#
# ps9pr2.py (Problem Set 9, Problem 2)
#
# A Connect-Four Player class 
#  

from ps9pr1 import Board

# write your class below.

class Player:
    """ Represents a player of the Connect Four game
    """

# function 1

    def __init__(self, checker):
        """ Constructs a new player object by initializing two attributes,
            'checker', and 'num_moves'.
        """
        assert(checker == 'X' or checker == 'O')
        self.checker = checker
        self.num_moves = 0
        
# function 2

    def __repr__(self):
        """ Returns a string representing a Player object and indicates which 
            checker the player is using.
        """
        return 'Player ' + str(self.checker)

# function 3

    def opponent_checker(self):
        """ Returns a string representing the checker of the Player object’s 
            opponent.
        """
        if self.checker == 'X':
            return 'O'
        else:
            return 'X'

# function 4

    def next_move(self, b):
        """ Accepts a Board object 'b' as a parameter and returns the column 
            where the player wants to make the next move.
        """
        self.num_moves += 1
        
        while True:
            usr_input = input('Enter a column: ')
            col_num = int(usr_input)
            if col_num in range(b.width):
                if b.can_add_to(col_num) == True:
                    return col_num
            else:
                print('Try Again!')