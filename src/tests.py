from collections import Counter
from morality import *


def start_game(player1=None, player2=None):
    game = Game()
    game.play(player1, player2)
    return game.get_registry()


def tests() -> None:
    top_players = start_game()
    assert top_players["Rat"] == 81
    assert top_players["Copycat"] == 74
    assert top_players["Grudger"] == 63
    assert top_players["Detective"] == 60
    assert top_players["Cheater"] == 48
    assert top_players["Cooperator"] == 46

    top_players = start_game(player1=Copycat(), player2=Detective())
    assert top_players["Copycat"] == 18
    assert top_players["Detective"] == 18

    top_players = start_game(player1=Grudger(), player2=Cooperator())
    assert top_players["Grudger"] == 20
    assert top_players["Cooperator"] == 20

    top_players = start_game(player1=Cheater(), player2=Detective())
    assert top_players["Cheater"] == 9
    assert top_players["Detective"] == -3

    top_players = start_game(player1=Cooperator(), player2=Detective())
    assert top_players["Cooperator"] == -1
    assert top_players["Detective"] == 27


if __name__ == "__main__":
    tests()
