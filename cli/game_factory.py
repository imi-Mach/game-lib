from games.game import Game
from games.tictactoe import TicTacToe

# def tic_tac_toe(players=2,log=None,strat=None):
#     pass


class Game_Factory():

    def __init__(self) -> None:
        self.__game_dict = {
            "TICTACTOE": TicTacToe
            }


    def select(self, given=None) -> Game:
        game = None

        if given in self.__game_dict:
            game = self.__game_dict[given]()
        else:

            # function used when mapping a list of index, game pairs to a string list
            def selector(tup):
                num, name = tup
                return "[" + str(num) + "] " + name

            # option defines a string representing games by number choices
            option = None

            # enumerate games by numbers
            games_enum = enumerate(self.__game_dict)
            selection = dict(games_enum)

            games_enum = enumerate(self.__game_dict)
            options = ", ".join(map(selector, games_enum))

            # make map between number and game
            games_enum = enumerate(self.__game_dict)
            selection = dict(games_enum)

            # optimization: make method for handling player choices when quiting is an option
            while(not game):
                print("Pick a game, here are the options:")
                print(options)
                option = input("Pick a number or type \"quit\":> ")
                if not option.isnumeric():
                    if option == "quit":
                        exit()
                elif int(option) in selection:
                    game = self.__game_dict[selection[int(option)]]()
                    break
                print("\nInvalid option, please try again.\n")
        
        return game

