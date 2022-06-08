# game sets up constraints, parameters, and other critical functionality
from game_factory import Game_Factory

gf = Game_Factory()

# game will hold an instace of what board game is being played
game = gf.select()

# setup game parameters
game.setup(players=2,log=None,strat=None)

# setup game loop
while(not game.is_over):
    game.display()
    game.advance()
    game.log_state()