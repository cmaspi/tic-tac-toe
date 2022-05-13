from typing import Tuple
from typing import Union
from board import Board

class player(object):
    def __init__(self, marker : str):
        assert marker.__len__() == 1, "The marker should be a single character"
        assert marker != ' ', "The marker cannot be a space character"
        self.marker = marker
    
class human(player):
    def get_move(self, board : Board):
        """
        Takes the move from the user, check if it's valid. Then
        marks on the board
        """
        invalid = True
        while invalid:
            invalid = False
            x,y = map(int, input("Enter your move : ").split())
            if x < 0 or x > 2 or y < 0 or y > 2:
                print("Enter a valid index: {0-2} {0-2}")
                invalid = True
            if board.state[x][y] != ' ':
                print("The position is already occupied")
                invalid = True
        board.state[x][y] = self.marker

class ai(player):
    def minimax(self, board : Board, p_marker : str, o_marker : str) -> Union[int, Tuple[int,int]] :
        """
        find the best move using minimax algorithm and marks
        it on the board. It also returns the score of that move.
        """

        move = (-1, -1)

        if sum([1 if board.state[i][j]==' ' else 0 for i in range(3) for j in range(3)]) == 9:
            return 0, (1, 1)
        
        score = board.evaluate(p_marker)

        if score == 1 or score == -1:
            return score * sum([1 if board.state[i][j] == ' ' else 0 for i in range(3) for j in range(3)]), move
        
        if not board.movesLeft():
            return 0, move
        
        best = -10

        for i in range(3):
            for j in range(3):
                if board.state[i][j] == ' ':
                    board.state[i][j] = p_marker
                    score, _ = self.minimax(board, o_marker, p_marker)
                    score = -score
                    if best < score:
                        best = score
                        move = (i, j)
                    board.state[i][j] = ' '

        return best, move

    def get_move(self, board : Board, o_marker : str) -> None:
        _, (x,y) = self.minimax(board, self.marker, o_marker)
        board.state[x][y] = self.marker
    

        


            
        

        
        

