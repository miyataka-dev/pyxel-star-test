import pyxel


class App:
    def __init__(self):
        pyxel.init(160, 120, title="VM TEST v2")
        # sound 0: catch jingle, sound 1: miss buzz
        pyxel.sounds[0].set("c4e4g4a4", "s", "6", "n", 12)
        pyxel.sounds[1].set("c3g2", "t", "5", "n", 15)
        self.x = 72
        self.sx = 80
        self.sy = 0
        self.score = 0
        self.misses = 0
        pyxel.run(self.update, self.draw)

    def update(self):
        # keyboard
        if pyxel.btn(pyxel.KEY_LEFT):
            self.x -= 2
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x += 2
        # gamepad d-pad
        if pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_LEFT):
            self.x -= 2
        if pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT):
            self.x += 2
        # gamepad left stick
        stick = pyxel.btnv(pyxel.GAMEPAD1_AXIS_LEFTX)
        if stick > 8000:
            self.x += 2
        elif stick < -8000:
            self.x -= 2
        self.x = max(0, min(144, self.x))

        self.sy += 2
        if self.sy > 112:
            dx = self.sx - (self.x + 8)
            if -10 <= dx <= 10:
                self.score += 1
                pyxel.play(0, 0)
            else:
                self.misses += 1
                pyxel.play(1, 1)
            self.sy = 0
            self.sx = pyxel.rndi(8, 152)

    def draw(self):
        pyxel.cls(1)
        pyxel.text(8, 8, "PYXEL VM TEST V2", 7)
        pyxel.text(8, 18, "SCORE " + str(self.score), 10)
        pyxel.text(8, 28, "MISS " + str(self.misses), 8)
        pyxel.rect(self.x, 110, 16, 4, 11)
        pyxel.circ(self.sx, self.sy, 3, 10)


App()
