# Keymap Autogenerated by Pog do not edit
from kmk.keys import KC
from kmk.handlers.sequences import send_string, simple_key_sequence
from kmk.modules.combos import Chord, Sequence

import pog
import customkeys

keymap = [
    [KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.ESC, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.ESC, KC.TAB, KC.HT(KC.A, KC.LCTL, prefer_hold=False, tap_time=200), KC.HT(KC.S, KC.LGUI, prefer_hold=False, tap_time=200), KC.HT(KC.D, KC.LALT, prefer_hold=False, tap_time=200), KC.HT(KC.F, KC.LCTL, prefer_hold=False, tap_time=200), KC.G, KC.H, KC.J, KC.HT(KC.K, KC.RALT, prefer_hold=False, tap_time=200), KC.HT(KC.L, KC.RGUI, prefer_hold=False, tap_time=200), KC.HT(KC.SCLN, KC.RCTL, prefer_hold=False, tap_time=200), KC.QUOT, KC.LSFT, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMM, KC.DOT, KC.SLSH, KC.RSFT, KC.HT(KC.LCTL(KC.F2),KC.MO(1)), KC.HT(KC.SPC,KC.MO(2)), KC.HT(KC.ENT,KC.LSFT), KC.HT(KC.ENT,KC.RSFT), KC.HT(KC.SPC,KC.MO(1)), KC.HT(KC.F2,KC.MO(3)), KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS], [KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.NO, KC.LSFT(KC.DEL), KC.LCTL(KC.INSERT), KC.LSFT(KC.INSERT), KC.INSERT, KC.LCTL(KC.Y), KC.DEL, KC.CAPSWORD, KC.BSPC, KC.PGUP, KC.TRNS, KC.TRNS, KC.LCTL, KC.LGUI, KC.LALT, KC.LCTL, KC.LSFT, KC.LEFT, KC.DOWN, KC.UP, KC.RIGHT, KC.PGDOWN, KC.NO, KC.TRNS, KC.LCTL(KC.Z), KC.LCTL(KC.X), KC.LCTL(KC.C), KC.LCTL(KC.V), KC.LCTL(KC.Y), KC.NO, KC.HOME, KC.CAPS, KC.END, KC.BSLS, KC.TRNS, KC.NO, KC.SPC, KC.TRNS, KC.NO, KC.TRNS, KC.NO, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS], [KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.EQL, KC.LBRC, KC.RBRC, KC.LCBR, KC.RCBR, KC.MINS, KC.UNDERSCORE, KC.COMM, KC.DOT, KC.COLN, KC.TRNS, KC.TRNS, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.TRNS, KC.TRNS, KC.EXLM, KC.AT, KC.HASH, KC.DOLLAR, KC.PERCENT, KC.CIRCUMFLEX, KC.AMPERSAND, KC.ASTERISK, KC.LEFT_PAREN, KC.RIGHT_PAREN, KC.TRNS, KC.NO, KC.TRNS, KC.NO, KC.TRNS, KC.SPC, KC.RCTL, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS], [KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.F11, KC.F12, KC.PAUSE, KC.NO, KC.NO, KC.PSCREEN, KC.SCROLLLOCK, KC.NO, KC.NO, customkeys.ToggleDrive, KC.TRNS, KC.TRNS, KC.F1, KC.F2, KC.F3, KC.F4, KC.F5, KC.F6, KC.F7, KC.F8, KC.F9, KC.F10, KC.TRNS, KC.TRNS, KC.LCTL, KC.LGUI, KC.LALT, KC.NO, KC.NO, KC.NO, KC.NO, KC.RALT, KC.RGUI, KC.RCTL, KC.TRNS, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS]
]

encoderKeymap = []
for l, layer in enumerate(pog.config['encoderKeymap']):
    layerEncoders = []
    for e, encoder in enumerate(layer):
        layerEncoders.append(tuple(map(eval, encoder)))
    encoderKeymap.append(tuple(layerEncoders))
