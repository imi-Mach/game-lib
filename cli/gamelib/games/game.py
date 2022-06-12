from abc import ABC, abstractmethod

class Game(ABC):
    '''
    Every game in the library implements the "Game" class.
    In other words, each game (regardless of logic) must
    have these methods to satisfy the game loop.
    '''

    @abstractmethod
    def __init__(self) -> None:
        '''
        Upon construction each Game should declare and initialize any
        identification, counter, seed, or state variables and should
        log these varibles for recoverability.
        '''
        pass

    @abstractmethod
    def setup(self):
        '''
        Setup phase resets a game to the initialized state, but does not
        remove any history of the session. This means the game should be
        independent of the previous but not overwriting the previous game's
        data.
        '''
        pass

    @abstractmethod
    def is_over(self) -> bool:
        '''
        To exit the game loop, the game must check for game termination condition.
        if the game is over, then the game should set a flag and return false.
        '''
        pass

    @abstractmethod
    def display(self):
        '''
        Display is meant to expose the state of the board from all player's perspective.
        '''
        pass

    @abstractmethod
    def advance(self):
        '''
        Advance allows the next board state to occur. Time is discrete. If the game is 
        turnbased, then the advance may only call upon a single player. If the game has
        several plays making a choice, then the advance can be modeled with a datastructure.
        '''
        pass

    @abstractmethod
    def log_state(self):
        '''
        The recoverability of a game is dependent on its ability to log details. Log state
        writes the result of subsequent advances.
        '''
        pass

    @abstractmethod
    def __repr__(self) -> str:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass