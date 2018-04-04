#! /bin/env python

import pymedia.player
import time

player = pymedia.player.Player()

player.start()
player.startPlayback("C:\Users\Javier\SONIDOS\ANTENA 3\ATRAPA UN MILLON\BSO Atrapa un millon - Cabecera.mp3")

while player.isPlaying():
    time.sleep(0.01)
