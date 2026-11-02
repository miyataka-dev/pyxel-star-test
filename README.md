# pyxel-star-test

Pyxel sample game (star catcher, 160x120) used to test playing a Pyxel
game in a web browser via GitHub.

## Play

- **Pyxel Web Launcher** (runs `star.py` directly, no setup):
  https://kitao.github.io/pyxel/wasm/launcher/?run=miyataka-dev.pyxel-star-test.star&gamepad=enabled
- **GitHub Pages** (serves `index.html`, the `pyxel app2html` output):
  https://miyataka-dev.github.io/pyxel-star-test/
  (Pages must be enabled once in Settings > Pages: branch `main`, folder `/ (root)`)

Click the game screen once after loading, then move the paddle with
the left/right arrow keys (or the virtual gamepad) and catch the
falling stars.

## Files

- `star.py` — the game source (Python / Pyxel)
- `index.html` — standalone HTML converted from the packaged
  `.pyxapp` with `pyxel app2html` (game data embedded, Pyxel 2.9.9
  runtime loaded from CDN)
