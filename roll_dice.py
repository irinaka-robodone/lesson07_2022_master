from microbit import *
import random

ONE = Image('00000:00000:00900:00000:00000')  # 1の出目のイメージ
TWO = Image('00000:00000:00900:00000:00000')
Three = Image('00000:00000:00900:00000:00000') 
Four = Image('00000:00000:00900:00000:00000') 
Five = Image('00000:00000:00900:00000:00000') 
Six = Image('00900:00900:00900:00900:00900') 
kazu=[ONE,TWO,Three,Four,Five,Six]
random.choice(kazu)
while True:
  if accelerometer.was_gesture("Nshake"):  # もし、振動したら次へ
    display.show(random.choice(kazu))             # ANGRYを表示する
    sleep(500)
    display.clear()

