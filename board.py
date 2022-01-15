# A Connect Four Board class

class Board:
    """ a data type for a Connect Four board with arbitrary dimensions
    """   
    def __init__(self, height, width):
        """ Constructs a new Board object by initializing three attributes,
            'height', 'width', and 'slots'
        """
        self.height = height
        self.width = width
        self.slots = [[' '] * self.width for row in range(self.height)]

    def __repr__(self):
        """ Returns a string that represents a Board object.
        """
        s = ''         

        for row in range(self.height):
            s += '|'

            for col in range(self.width):
                s += self.slots[row][col] + '|'

            s += '\n'
        
        for col in range((self.width * 2) + 1):
            s += '-'
        
        s += '\n '
        
        for col in range(self.width):
            s += str(col % 10) + ' '
        return s

    def add_checker(self, checker, col):
        """ adds the specified checker (either 'X' or 'O') to the
            column with the specified index col in the called Board.
            inputs: checker is either 'X' or 'O'
                    col is a valid column index
        """
        assert(checker == 'X' or checker == 'O')
        assert(col >= 0 and col < self.width)
        
        row = 0
        while self.slots[row][col] == ' ':
            row += 1
            if row == (self.height - 1):
                break
        if self.slots[row][col] != ' ':
            row -= 1
            
        self.slots[row][col] = checker
    
    def reset(self):
        """ This function loops over all slots of the board and sets 
            them to a space character.
        """
        for row in range(self.height):
            for col in range(self.width):
                self.slots[row][col] = ' '
    
    def add_checkers(self, colnums):
        """ takes a string of column numbers and places alternating
            checkers in those columns of the called Board object,
            starting with 'X'.
            input: colnums is a string of valid column numbers
        """
        checker = 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'

    def can_add_to(self, col):
        """ Checks different cases to determine if it is valid to place 
            a checker in the column 'col' on the calling Board object
            Returns True if the checker is valid. Otherwise, returns False.
        """
        if col < 0:
            return False
        elif col >= self.width:
            return False
        elif self.slots[0][col] != ' ':
            return False
        else:
            return True
        
    def is_full(self):
        """ Returns True if the called Board object is completely full of 
            checkers, and returns False otherwise.
        """
        for col in range(self.width):
            if self.can_add_to(col) == True:
                return False
        return True

    def remove_checker(self, col):
        """ Removes the top checker from column 'col' of the called Board 
            object. If the column is empty then it will not change.
        """
        for row in range(self.height):
            if self.slots[row][col] != ' ':
                self.slots[row][col] = ' '
                break
    
    def is_horizontal_win(self, checker):
        """ Checks for a horizontal win for the specified checker.
        """
        for row in range(self.height):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                self.slots[row][col + 1] == checker and \
                self.slots[row][col + 2] == checker and \
                self.slots[row][col + 3] == checker:
                    return True

        return False

    def is_vertical_win(self, checker):
        """ Checks for a vertical win for the specified checker.
        """
        for row in range(self.height - 3):
            for col in range(self.width):
                if self.slots[row][col] == checker and \
                self.slots[row + 1][col] == checker and \
                self.slots[row + 2][col] == checker and \
                self.slots[row + 3][col] == checker:
                    return True
        
        return False
    
    def is_down_diagonal_win(self, checker):
        """ Checks for a diagonal win downwards for the specified checker.
        """
        for row in range(self.height - 3):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                self.slots[row + 1][col + 1] == checker and \
                self.slots[row + 2][col + 2] == checker and \
                self.slots[row + 3][col + 3] == checker:
                    return True
        return False
    
    def is_up_diagonal_win(self, checker):
        """ Checks for a diagonal win upwards for the specified checker.
        """
        for row in range(3, self.height):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                self.slots[row - 1][col + 1] == checker and \
                self.slots[row - 2][col + 2] == checker and \
                self.slots[row - 3][col + 3] == checker:
                    return True
        return False


    def is_win_for(self, checker):
        """ Accepts a parameter checker that is either 'X' or 'O'. Returns 
            True if there are four consecutive slots containing a checker 
            on the board. Otherwise, it returns False.
        """
        assert(checker == 'X' or checker == 'O')
        
        if self.is_horizontal_win(checker) == True:
            return True
        elif self.is_vertical_win(checker) == True:
            return True
        elif self.is_down_diagonal_win(checker) == True:
            return True
        elif self.is_up_diagonal_win(checker) == True:
            return True
        else:
            return False