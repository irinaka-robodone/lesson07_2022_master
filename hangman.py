from microbit import *
import music

HANGMAN = [
  Image(),
  Image('90000:90000:90000:90000:90000'),
  Image('99990:90000:90000:90000:90000'),
  Image('99990:90090:90000:90000:90000'),
  Image('99990:90090:90090:90000:90000'),
  Image('99990:90090:90990:90000:90000'),
  Image('99990:90090:90999:90000:90000'),
  Image('99990:90090:90999:90090:90000'),
  Image('99990:90090:90999:90090:90900'),
  Image('99990:90090:90999:90090:90909')
  ]
c = 0

while True:
  
  if button_a.was_pressed():
    c += 1
  elif c == 9:
    music.play(music.POWER_DOWN)
    display.clear()
    c = 0
  display.show(HANGMAN[c])
  sleep(1000)
  