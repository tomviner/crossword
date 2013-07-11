from board import Board

from copy import copy

class Crossword(Board):
    pass
    # def __init__(self):
    #     Board.__init__(self, 10, 10)


    def __copy__(self):
        new = Crossword(self.height, self.width)
        new.table = self.table.copy()
        return new

    def __str__(self):
        s = []
        for i in range(self.height):
            for j in range(self.width):
                if self.get(i, j) is None:
                    s.append(' ')
                else:
                    s.append(self.get(i, j))
            s.append('\n')
        return ''.join(s)

    def place(self, word, x, y, is_hor=True):
        if self.check(word, x, y, is_hor):
            for i, letter in enumerate(word):
                if is_hor:
                    self.put(x, y+i, letter)
                else:
                    self.put(x+i, y, letter)
            return copy(self)
        else:
            raise ValueError('Word does not fit')

    def check(self, word, x, y, is_hor=True):
        for i, letter in enumerate(word):
            if is_hor:
                current = self.get(x, y+i)
            else:
                current = self.get(x+i, y)
            if current and current != letter:
                return False
        return True

def fit(board, words, solutions):
    print words
    try:
        word = words.pop()
    except IndexError:
        solutions.append(board)
        return

    for i in range(board.height):
        for j in range(board.width):
            for is_hor in [True, False]:
                try:
                    print word, i, j, is_hor
                    new = board.place(word, i, j, is_hor)
                    print new
                    # 1/0
                    fit(new, list(words), solutions)
                except (ValueError, IndexError):
                    pass
                # else:
                #     print board
                #     raw_input()


c = Crossword(10, 10)
words = [
    'window'
]

solutions = []
fit(c, ['test', 'eel', 'tee'], solutions)
# for s in solutions:
#     print s
#     print
