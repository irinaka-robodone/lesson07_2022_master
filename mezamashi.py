from microbit import *
import music
taima=0
while True:
  if button_a.was_pressed():
      taima +=1
  if button_b.was_pressed():
    break

display.show(Image.ASLEEP)
sleep(taima*1000)
display.clear()
music.play(music.RINGTONE)
