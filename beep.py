import RPi.GPIO as GPIO
import time
from ultrasonic_sensor import distance

BuzzerPin = 7

CL = [0, 131, 147, 165, 175, 196, 211, 248] # Low C Note Frequency
CM = [0, 262, 294, 330, 350, 393, 441, 495] # Middle C Note Frequency
CH = [0, 525, 589, 661, 700, 786, 882, 990] # High C Note Frequency

song_1 = [ CM[1], CM[1], CM[2], CM[1], CM[4], CM[3], CM[1], CM[1],
CM[2], CM[1], CM[5], CM[4], CM[1], CM[1], CH[1], CM[6], CM[4],
CM[3], CM[2], 468, 468, CM[6], CM[4], CM[5], CM[4] ]

beat_1 = [ 1, .5, 2, 2, 2, 4, 1, .5,
2, 2, 2, 4, 1, .5, 2, 2, 2,
2, 4, 1, .5, 2, 2, 2, 2 ]

def setup():
  GPIO.setmode(GPIO.BOARD) # Numbers GPIOs by physical location
  GPIO.setup(BuzzerPin, GPIO.OUT) # Set pins' mode is output
  global Buzz # Assign a global variable to replace GPIO.PWM
  Buzz = GPIO.PWM(BuzzerPin, 440) # 440 is initial frequency.

def loop():
  print '\n Playing Happy Birthday...'
  for i in range(0, len(song_1)): # Play Happy Birthday
    Buzz.start(50)
    Buzz.ChangeFrequency(song_1[i]) # Change the frequency along the song note
    time.sleep(beat_1[i] * .25) # delay a note for beat * 0.25s
    Buzz.stop()
    time.sleep(.1)
  time.sleep(1) # Wait a second for next song.

def destory():
  print("\nend.")
  Buzz.stop() # Stop the BuzzerPin
  GPIO.output(BuzzerPin, 1) # Set BuzzerPin pin to High
  GPIO.cleanup() # Release resource

if __name__ == '__main__': # Program start from here
  setup()
  try:
    while True:
      dist = distance()
      
  except KeyboardInterrupt:
    destory()
