from microbit import *

FLASH = [
  Image('99999:99999:99999:99999:99999'),
  Image('77777:77777:77777:77777:77777'),
  Image('55555:55555:55555:55555:55555'),
  Image('33333:33333:33333:33333:33333'),
  Image('11111:11111:11111:11111:11111'),
  Image()
]
a = 0

while True:
  if button_a.was_pressed():
    display.show(FLASH, delay=100)
