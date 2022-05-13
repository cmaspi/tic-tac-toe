from board import Board
from player import human, ai, player

class Game():
    def __init__(self, player1 : player, player2 : player) -> None:
        self.player1 = player1
        self.player2 = player2
    
    def begin_game(self):
        """
        Begins the game
        """
        restart = True
        while restart:
            board = Board()
            gameover = False
            moves = 0
            while not gameover:
                current = self.player2 if moves % 2 else self.player1
                opposite = self.player1 if moves % 2 else self.player2
                board.print()
                if isinstance(current, ai):
                    current.get_move(board, opposite.marker)
                else:
                    current.get_move(board)
                
                score = board.evaluate(current.marker)
                if score == 1:
                    board.print()
                    print(f'{current.marker} wins')
                    gameover = True
                if not board.movesLeft() and not gameover:
                    board.print()
                    print("TIE!")
                    gameover = True
                moves += 1

            print("To quit the game press q, any other key to restart")
            restart = True if input() != 'q' else False




