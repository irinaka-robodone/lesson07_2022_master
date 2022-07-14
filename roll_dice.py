from microbit import *
import random

ONE = Image('00000:00000:00900:00000:00000')  # 1の出目のイメージ
Two = Image('90000:00000:00000:00000:00009')
Three = Image('00009:00000:00900:00000:90000')
Four = Image('90009:00000:00000:00000:90009')
Five = Image('90009:00000:00900:00000:90009')
Six = Image('90009:90009:90009:90009:90009')
dice = [ONE,Two,Three,Four,Five,Six]
while True:
  if accelerometer.was_gesture("shake"):  # もし、振動したら次へ
    display.show(random.choice(dice))             # ANGRYを表示する
    sleep(500)
    display.clear()

