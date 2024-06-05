# Keymap Autogenerated by Pog do not edit
from kmk.keys import KC
from kmk.handlers.sequences import send_string, simple_key_sequence
from kmk.modules.combos import Chord, Sequence

import pog
import customkeys

keymap = [
    [KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.ESC, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.RESET, KC.TAB, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SCLN, KC.QUOT, KC.LSFT, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMM, KC.DOT, KC.SLSH, KC.RSFT, KC.LCTL(KC.F2), KC.SPC, KC.ENT, KC.ENT, KC.SPC, KC.F2, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS]
]

encoderKeymap = []
for l, layer in enumerate(pog.config['encoderKeymap']):
    layerEncoders = []
    for e, encoder in enumerate(layer):
        layerEncoders.append(tuple(map(eval, encoder)))
    encoderKeymap.append(tuple(layerEncoders))