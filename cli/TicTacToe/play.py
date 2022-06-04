# game sets up constraints, parameters, and other critical functionality
import game_factory

# game will hold an instace of what board game is being played
game = None

# optimization: add a game selector method to the game_factory to clean up code from the "play" file

# function used when mapping a list of index, game pairs to a string list
def selector(tup):
    num, name = tup
    return "[" + str(num) + "] " + name

option = None
games_enum = enumerate(game_factory.get_games())
options = ", ".join(map(selector,games_enum))
selection = dict(games_enum)

# optimization: make method for handling player choices when quiting is an option
while(not game):
    print("Pick a game, here are the options:")
    print(options)
    option = input("Pick a number or type \"quit\":> ")
    if option == "quit":
        exit()
    game = game_factory.pick(selection[option])


# setup game parameters
game.setup(players=2,log=None,strat=None)

# setup game loop
while(not game.is_over):
    game.display()
    game.make_move()
    game.log_state()