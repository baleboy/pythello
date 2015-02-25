
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

EMPTY = ' '
BLACK = '0'
WHITE = 'O'

directions = [
    (-1, 1), (-1, 0), (0, 1), (1, 1), (0, 1), (1, 0), (-1, -1), (0, -1)
    ]


class Game:

    def __init__(self):
        self.board = [[EMPTY]*8 for i in range(8)]
        self.board[3][3] = WHITE
        self.board[3][4] = BLACK
        self.board[4][3] = BLACK
        self.board[4][4] = WHITE

        self.turn = BLACK

        self.score = {BLACK: 2, WHITE: 2}

    def opposite(self):
        return WHITE if self.turn == BLACK else BLACK

    def scanDirection(self, row, col, direction, color):

        curRow = row + direction[0]
        curCol = col + direction[1]

        piecesToTurn = 0
        while curRow >= 0 and curRow <= 7 and curCol >= 0 and curCol <= 7:
            if self.board[curRow][curCol] != self.opposite():
                break
            piecesToTurn += 1
            curRow += direction[0]
            curCol += direction[1]

        if (curRow >= 0 and curRow <= 7 and curCol >= 0 and
                curCol <= 7 and piecesToTurn > 0):
            if self.board[curRow][curCol] == color:
                return piecesToTurn
            else:
                return 0

    def playMove(self, letter, number):

        row = ord(letter) - ord('a')
        col = number - 1

        if row > 7 or row < 0:
            return False

        if self.board[row][col] != EMPTY:
            return False

        validMove = False

        for direction in directions:
            piecesToTurn = self.scanDirection(
                row, col,
                direction, self.turn
            )
            if piecesToTurn > 0:
                if not validMove:
                    validMove = True
                curRow = row
                curCol = col
                for i in range(piecesToTurn + 1):
                    self.board[curRow][curCol] = self.turn
                    curRow += direction[0]
                    curCol += direction[1]
                self.score[self.turn] += piecesToTurn
                self.score[self.opposite()] -= piecesToTurn

        if validMove:
            self.score[self.turn] += 1
            self.turn = self.opposite()

        return validMove

    def playerCanMove(self):

        row = 0
        col = 0
        res = False

        for row in range(8):
            for col in range(8):
                if self.board[row][col] == EMPTY:
                    for dir in directions:
                        if self.scanDirection(row, col, dir, self.turn) > 0:
                            res = True
                            break
                if res:
                    break
            if res:
                break
        return res

    def hasMovesAvailable(self):

        if self.score[WHITE] + self.score[BLACK] == 64:
            return False

        if self.playerCanMove():
            return True

        self.turn = self.opposite()

        return self.playerCanMove()
