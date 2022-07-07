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
# print(len(HANGMAN))
a = 0
while True:

  if button_a.was_pressed():
    a += 1

  elif a == 9:
    music.play(music.POWER_DOWN)
    a = 0
  display.show(HANGMAN[a])




