import pyxel


class App:
    def __init__(self):
        pyxel.init(160, 120, title="VM TEST")
        self.x = 72
        self.sx = 80
        self.sy = 0
        self.score = 0
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btn(pyxel.KEY_LEFT):
            self.x -= 2
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x += 2
        self.x = max(0, min(144, self.x))
        self.sy += 2
        if self.sy > 112:
            dx = self.sx - (self.x + 8)
            if -10 <= dx <= 10:
                self.score += 1
            self.sy = 0
            self.sx = pyxel.rndi(8, 152)

    def draw(self):
        pyxel.cls(1)
        pyxel.text(8, 8, "PYXEL VM TEST", 7)
        pyxel.text(8, 18, "SCORE " + str(self.score), 10)
        pyxel.rect(self.x, 110, 16, 4, 11)
        pyxel.circ(self.sx, self.sy, 3, 10)


App()
