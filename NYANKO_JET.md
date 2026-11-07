# にゃんこジェット (Nyanko Jet) — Pyxel port

A Pyxel (Python) port of the 128×128 Earth-defense shooter originally built
in JavaScript/Excalibur. A kijitora cat on Earth's surface fires golden
koban up at waves of UFOs: 5 cycling wave patterns, aimed / cone / straight
enemy fire, a 20-bar NEON GROOVE BGM (E minor) transcribed from the JS
version, and jsfxr-style synthesized SFX rebuilt as Pyxel sound data.

## Play in the browser (Pyxel Web Launcher)

https://kitao.github.io/pyxel/wasm/launcher/?run=miyataka-dev.pyxel-star-test.nyanko_jet&gamepad=enabled

`nyanko_jet.html` in this repo is the standalone `pyxel app2html` build of
the same game (script + resources embedded).

## Controls

- Title: ↑/↓ (or ←/→) choose, Z / J / Space / Enter or click to confirm
  (OPTION is a deliberate no-op, as in the JS version)
- Game: ←/→ or A/D move, hold Z / J / Space to shoot, P pauses

## About the missing .pyxres

The game's resource file `nyanko_jet.pyxres` (image banks + sound/music
data) is binary and could not be uploaded through the available GitHub API
route, so it is not in this repo. That is fine: `nyanko_jet.py` first tries
to load `nyanko_jet.pyxres` next to it, and when the file is absent it
rebuilds byte-identical resources at startup from embedded pixel data and
programmatic audio builders. The launcher version above plays exactly the
same either way. The canonical `.pyxres` lives with the full project
sources (and inside the packaged `nyanko_jet.pyxapp`).

## Notes / deviations from the JS version

- BGM runs at 150 BPM instead of 144 (Pyxel note lengths are whole ticks;
  150 is the closest uniform tempo) and the 18% swing is omitted.
- The bass uses Pyxel's square tone (no sawtooth available); percussion
  note collisions resolve kick > snare > open hat > hat on the single
  percussion channel.
- SFX share two Pyxel channels (JS had 5 independent voices); per-type
  monophony is preserved.
- Pausing stops the music; on resume the BGM restarts from the top of the
  loop (Pyxel cannot resume music mid-loop).
