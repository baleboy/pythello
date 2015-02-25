# Copyright (c) 2015 Francesco Balestrieri
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

import game
import unittest


def compareBoards(b1, b2):

    for i in range(8):
        for j in range(8):
            if b1[i][j] != b2[i][j]:
                return False

    return True


class TestStartingPosition(unittest.TestCase):

    def test_start_turn(self):
        g = game.Game()
        self.assertEqual(g.turn, game.black)


class TestInvalidMoves(unittest.TestCase):

    def setUp(self):
        self.game = game.Game()

    def test_not_empty(self):
        self.assertEqual(self.game.playMove('d', 4), False)

    def test_cannot_turn(self):
        self.assertEqual(self.game.playMove('c', 5), False)

    def test_lonely_square(self):
        self.assertEqual(self.game.playMove('a', 1), False)


class TestValidMoves(unittest.TestCase):

    def test_turn_one_file(self):

        g = game.Game()

        self.assertEqual(g.turn, game.black)
        g.playMove('c', 4)

        expected = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', '0', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', '0', '0', ' ', ' ', ' '],
            [' ', ' ', ' ', '0', 'O', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        ]

        self.assertEquals(compareBoards(g.board, expected), True)

    def test_turn_two_files(self):

        g = game.Game()
        g.turn = game.white

        g.board = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', 'O', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', '0', ' ', ' ', 'O', ' '],
            [' ', ' ', ' ', '0', '0', '0', ' ', ' '],
            [' ', ' ', ' ', '0', '0', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        ]

        expected = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', 'O', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', 'O', ' ', ' ', 'O', ' '],
            [' ', ' ', ' ', 'O', '0', 'O', ' ', ' '],
            [' ', ' ', ' ', 'O', 'O', ' ', ' ', ' '],
            [' ', ' ', ' ', 'O', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        ]

        g.playMove('f', 4)
        self.assertEquals(compareBoards(g.board, expected), True)


class TestGameOver(unittest.TestCase):

    def setUp(self):
        self.game = game.Game()

    def test_out_of_moves(self):

        self.game.board = [
            ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', 'O', 'O', ' '],
            ['O', 'O', 'O', 'O', 'O', 'O', ' ', ' '],
            ['O', 'O', 'O', 'O', 'O', 'O', ' ', '0'],
            ['O', 'O', 'O', 'O', 'O', 'O', ' ', ' '],
            ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']
        ]
        self.assertEqual(self.game.hasMovesAvailable(), False)

    def test_full_board(self):

        self.game.board = [
            ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', 'O', 'O', '0'],
            ['O', 'O', 'O', 'O', 'O', 'O', '0', '0'],
            ['O', 'O', 'O', 'O', 'O', 'O', '0', '0'],
            ['O', 'O', 'O', 'O', 'O', 'O', '0', '0'],
            ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']
        ]
        self.assertEqual(self.game.hasMovesAvailable(), False)


if __name__ == '__main__':
    unittest.main()
