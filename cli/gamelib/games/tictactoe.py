from .game import Game


class TicTacToe(Game):
    def __init__(self) -> None:
        # set the name of the game (class+timestamp)
        # set game counter to 0
        # set number of players?
        self._name = "tictactoe"    # unique game name (used for parsing)
        self._session = None        # unique session number to retain game state
        self._game_counter = 0
        self._player_num = None
        self._trace = False         # variable that changes log info to allow for recoverability
        self._board = [None]

    def setup(self):
        ''''''
        pass

    def is_over(self) -> bool:
        pass

    def display(self):
        pass

    def advance(self):
        pass

    def log_state(self):
        pass

    def __repr__(self) -> str:
        pass

    def __str__(self) -> str:
        pass