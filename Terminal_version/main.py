from player import human, ai
from game import Game

p1 = ai('X')
p2 = human('O')

game = Game(p1, p2)
game.begin_game()

