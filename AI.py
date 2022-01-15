# AI Player for use in Connect Four

import random  
from game import *

class AIPlayer(Player):

    def __init__(self, checker, tiebreak, lookahead):
        """ Constructs a new AIPlayer object by initializing three attributes,
            'checker', 'tiebreak', 'lookahead'.
        """
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)

        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead

    def __repr__(self):
        """ Returns a string representing an AIPlayer object.
        """
        return ('Player ' +  str(self.checker) + ' (' + str(self.tiebreak) + ', ' + str(self.lookahead) + ')')

    def max_score_column(self, scores):
        """ Takes a list 'scores' containing a score for each column of the board, 
            and returns the index of the column with the maximum score. If 
            one or more columns are tied for the maximum score, the method applies 
            AIPlayer‘s tiebreaking strategy to break the tie.
        """
        max_scores_list = []
        
        for c_score in range(len(scores)):
            if scores[c_score] == max(scores):
                max_scores_list += [c_score]
        if self.tiebreak == 'LEFT':
            return max_scores_list[0]
        elif self.tiebreak == 'RIGHT':
            return max_scores_list[-1]
        elif self.tiebreak == 'RANDOM':
            return random.choice(max_scores_list)

    def scores_for(self, b):
        """ Takes a Board object 'b' and determines the called AIPlayer‘s scores 
        for the columns in 'b'. Also creates an opponent and determines it's 
        scores. Returns a list of scores after computing the necessary scores 
        for each column. 
        """
        scores = [50] * b.width
        
        for col in range(b.width):
            if b.can_add_to(col) == False:
                scores[col] = -1
            elif b.is_win_for(self.checker) == True:
                scores[col] = 100
            elif b.is_win_for(self.opponent_checker()) == True:
                scores[col] = 0
            elif self.lookahead == 0:
                scores[col] = 50
            else:
                b.add_checker(self.checker, col)
                opponent = AIPlayer(self.opponent_checker(), self.tiebreak, (self.lookahead - 1))
                opponent_scores = opponent.scores_for(b)
                
                if max(opponent_scores) == 100:
                    scores[col] = 0
                elif max(opponent_scores) == 50:
                    scores[col] = 50
                elif max(opponent_scores) == 0:
                    scores[col] = 100
                b.remove_checker(col)
        
        return scores

    def next_move(self, b):
        """ Computes and returns the best possible move for AIPlayer. Keeps track of
            the number of moves made by AIPlayer.
        """
        self.num_moves += 1
        ai_next_move = self.max_score_column(self.scores_for(b))
        return ai_next_move