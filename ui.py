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


class Ui:

    def __init__(self, game):
        self.game = game

    def divider(self):
        return '  ' + '='*17

    def show(self):

        print "   1 2 3 4 5 6 7 8"
        print self.divider()
        i = 0
        for row in self.game.board:
            line = chr(ord('a') + i) + " |"
            i += 1
            for square in row:
                line += square + '|'
            print line
        print self.divider()

        print "White: " + str(self.game.score[game.white])
        print "Black: " + str(self.game.score[game.black])

    def printColor(self, square):
        if square == game.white:
            return "White"
        elif square == game.black:
            return "Black"
        else:
            return "Empty"

    def getInput(self):

        while True:
            cmd = raw_input("{0} to move (\"q\" to exit) ".format(
                self.printColor(self.game.turn)
                )
            )
            if cmd == "q":
                return False
            else:
                if not self.game.playMove(cmd[0], int(cmd[1])):
                    print "Invalid move"
                else:
                    break
        return True
