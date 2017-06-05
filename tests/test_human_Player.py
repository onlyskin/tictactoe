from StringIO import StringIO

import pytest

from human_player import HumanPlayer
from board import Board
from console_ui import ConsoleUi

def get_input_function(input_list):
    return lambda: input_list.pop(0)

def test_it_gets_3_first_time():
    ui = ConsoleUi(StringIO(), get_input_function(['3']))
    b = Board()
    human_player = HumanPlayer('O', ui)
    opponent = HumanPlayer('X', ui)

    human_move = human_player.get_move(b, opponent)
    assert human_move == 3

def test_it_rejects_3_and_5_accepts_6():
    ui = ConsoleUi(StringIO(), get_input_function(['3', '5', '6']))
    _input = [[None, None, None], ['X', 'X', 'O'], [None, None, None]]
    b = Board(_input)
    human_player = HumanPlayer('O', ui)
    opponent = HumanPlayer('X', ui)

    human_move = human_player.get_move(b, opponent)
    expected_output = open('fixtures/get_human_move_expected_output.txt', 'r').read()

    assert ui._out_stream.getvalue() == expected_output
