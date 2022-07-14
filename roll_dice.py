from microbit import *
import random

ONE = Image('00000:00000:00900:00000:00000')  # 1の出目のイメージ
TWO = Image('90000:00000:00000:00000:00009')                       
THREE = Image('00009:00000:00900:00000:90000')
FOUR = Image('90009:00000:00000:00000:90009')
FIVE = Image('90009:00000:00900:00000:90009')
SIX = Image('90009:00000:90009:00000:90009')
dice = [ONE,TWO,THREE,FOUR,FIVE,SIX]
while True:
  if accelerometer.was_gesture("shake"):  # もし、振動したら次へ
    display.show(random.choice(dice))             # ANGRYを表示する
    sleep(500)
    display.clear()