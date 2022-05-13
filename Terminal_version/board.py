from typing import List
import sys

class Board():
    def __init__(self) -> None:
        self.state = [[" " for _ in range(3)] for _ in range(3)]

    def print(self):
        """
        prints the current state of the board
        """
        print("\t0\t1\t2\n")
        for i in range(3):
            print(f'{i}\t', end = "")
            print("{}   |   {}   |   {}".format(*self.state[i]))
            if i!=2:
                print("\t",end = "")
                print("-"*17)
        print()
        sys.stdout.flush()
    
    def movesLeft(self) -> bool:
        """
        Returns True if there are still moves left on the
        board, False otherwise.
        """
        for row in self.state:
            for val in row:
                if val == ' ':
                    return True
        return False

    def evaluate(self, player : str) -> int:
        """
        Evaluates the board for win or tie or match in progress
        """

        def check(values : List) -> bool:
            """
            Checks whether the given values are all the same.
            Also all the positions shoudl be non-empty
            """
            if values[0] == ' ':
                return False # empty position

            all_same = all([ values[0] == i for i in values ])

            return all_same

        comb_dispatch = {0 : (0,0), 1 : (1,0), 2 : (2,0),\
                        3 : (0,0), 4 : (0,1), 5 : (0,2),\
                        6 : (0,0), 7 : (0,2)}

        combs = [ self.state[0], self.state[1], self.state[2],\
                    [i[0] for i in self.state],\
                    [i[1] for i in self.state],\
                    [i[2] for i in self.state],\
                    [self.state[i][i] for i in range(3)],\
                    [self.state[i][2-i] for i in range(3)]]

        bool_comb = [check(i) for i in combs]

        score = 0
        idx = -1
        for i in range(len(combs)):
            if bool_comb[i]:
                idx = i
                break
        if idx != -1:
            y, x = comb_dispatch[idx]
            score = 1 if self.state[y][x] == player else -1
        return score
        