from abc import ABC, abstractmethod

class Player(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def evaluation(self):
        pass

    @abstractmethod
    def make_move(self):
        pass