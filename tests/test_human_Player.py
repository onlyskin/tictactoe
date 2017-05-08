import pytest
import sys

from human_player import HumanPlayer
from board import Board
from console_ui import ConsoleUi

Ui = ConsoleUi()

def test_it_gets_3_first_time():
    sys.stdin = open('mock/get_human_move_stdin_1', 'r')

    b = Board()

    human_player = HumanPlayer('O')
    opponent = HumanPlayer('X')

    human_move = human_player.get_move(Ui, b, opponent)
    assert human_move == 3

def test_it_rejects_3_and_5_accepts_6(capsys):
    sys.stdin = open('mock/get_human_move_stdin_2', 'r')
    expected_stdout = open('mock/get_human_move_expected_stdout.txt', 'r').read()

    _input = [None, None, None, 'X', 'X', 'O', None, None, None]
    b = Board(_input)

    human_player = HumanPlayer('O')
    opponent = HumanPlayer('X')

    human_move = human_player.get_move(Ui, b, opponent)

    out, err = capsys.readouterr()
    assert out == expected_stdout

