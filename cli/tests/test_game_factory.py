from collections import deque
import pytest
import mock

from gamelib.game_factory import Game_Factory
from gamelib.games.tictactoe import TicTacToe

def multi_input(inputs):
    def next_input(_):
        return inputs.popleft()
    return next_input

@pytest.fixture
def game_factory():
    return Game_Factory()

def test_select_tic_tac_toe(monkeypatch, game_factory):
    monkeypatch.setattr('builtins.input', lambda _: "0")
    game = game_factory.select()
    assert isinstance(game, TicTacToe)

def test_select_quit(monkeypatch, game_factory):
    monkeypatch.setattr('builtins.input', lambda _: "quit")
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        game_factory.select()
        
    assert pytest_wrapped_e.type == SystemExit

def test_select_invalid_numeric(monkeypatch, game_factory):

    input_set = deque(["-1","quit"])
    monkeypatch.setattr('builtins.input', multi_input(input_set))

    with pytest.raises(SystemExit) as pytest_wrapped_e:
        game = game_factory.select()
        assert game is None

    assert pytest_wrapped_e.type == SystemExit

def test_select_invalid_string(monkeypatch, game_factory):
    
    input_set = deque(["thisIsAnInvalidOption","quit"])
    monkeypatch.setattr('builtins.input', multi_input(input_set))
    
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        game = game_factory.select()
        assert game is None

    assert pytest_wrapped_e.type == SystemExit