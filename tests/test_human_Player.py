import sys
from StringIO import StringIO

import pytest
from mock import patch

from human_player import HumanPlayer
from board import Board
from console_ui import ConsoleUi

@pytest.fixture(scope='function')
def ui():
    return ConsoleUi(StringIO())

@patch('sys.stdin', StringIO('3\n'))
def test_it_gets_3_first_time(ui):
    b = Board()

    human_player = HumanPlayer('O', ui)
    opponent = HumanPlayer('X', ui)

    human_move = human_player.get_move(b, opponent)
    assert human_move == 3

@patch('sys.stdin', StringIO('3\n5\n6\n'))
def test_it_rejects_3_and_5_accepts_6(ui):
    expected_output = open('fixtures/get_human_move_expected_output.txt', 'r').read()

    _input = [[None, None, None], ['X', 'X', 'O'], [None, None, None]]
    b = Board(_input)

    human_player = HumanPlayer('O', ui)
    opponent = HumanPlayer('X', ui)

    human_move = human_player.get_move(b, opponent)

    assert ui._out_stream.getvalue() == expected_output

