from board import Board

class Crossword(Board):
    pass
    # def __init__(self):
    #     Board.__init__(self, 10, 10)

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

    def place(self, word, x, y, is_hor):
        for i, letter in enumerate(word):
            if is_hor:
                c.put(x, y+i, letter)
            else:
                c.put(x+i, y, letter)


c = Crossword(10, 10)
c.place('testing', 2, 0, True)
c.place('test', 2, 3, False)
print c