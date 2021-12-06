
class Lines:
    x1 = 0
    x2 = 0

    y1 = 0
    y2 = 0

    dots = []

    def __init__(self):
        (x, y)= input().split("->")
        (x1, y1) = [int(i) for i in x.split(",")]
        (x2, y2) = [int(i) for i in y.split(",")]

        self.x1 = x1
        self.x2 = x2

        self.y1 = y1
        self.y2 = y2

    def is_vertical(self):
        return self.x1 == self.x2

    def is_horizontal(self):
        return self.y1 == self.y2

    def show(self):
        print(self.x1,self.y1, "->", self.x2,self.y2)


lines = []

max_x = 0
max_y = 0

while True:
    try:
        tmp = Lines()

        # part 1: Only horizontal lines
        if tmp.is_horizontal() or tmp.is_vertical():
            lines.append(tmp)

    except EOFError:
        break
