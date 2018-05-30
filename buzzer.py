import RPi.GPIO as GPIO
import time

BuzzerPin = 7

CL = [0, 131, 147, 165, 175, 196, 211, 248] # Low C Note Frequency
CM = [0, 262, 294, 330, 350, 393, 441, 495] # Middle C Note Frequency
CH = [0, 525, 589, 661, 700, 786, 882, 990] # High C Note Frequency

song_3 = [ CM[1], CM[1], CM[2], CM[1], CM[4], CM[3], CM[1], CM[1],
CM[2], CM[1], CM[5], CM[4], CM[1], CM[1], CH[1], CM[6], CM[4],
CM[3], CM[2], 468, 468, CM[6], CM[4], CM[5], CM[4] ]

beat_3 = [ 1, .5, 2, 2, 2, 4, 1, .5,
2, 2, 2, 4, 1, .5, 2, 2, 2,
2, 4, 1, .5, 2, 2, 2, 2 ]

song_1 = [ CM[3], CM[5], CM[6], CM[3], CM[2], CM[3], CM[5], CM[6], # Sound Notes 1
CH[1], CM[6], CM[5], CM[1], CM[3], CM[2], CM[2], CM[3],
CM[5], CM[2], CM[3], CM[3], CL[6], CL[6], CL[6], CM[1],
CM[2], CM[3], CM[2], CL[7], CL[6], CM[1], CL[5] ]

beat_1 = [ 1, 1, 3, 1, 1, 3, 1, 1, # Beats of song 1, 1 means 1/8 beats
1, 1, 1, 1, 1, 1, 3, 1,
1, 3, 1, 1, 1, 1, 1, 1,
1, 2, 1, 1, 1, 1, 1, 1,
1, 1, 3 ]

song_2 = [ CM[1], CM[1], CM[1], CL[5], CM[3], CM[3], CM[3], CM[1], # Sound Notes 2
CM[1], CM[3], CM[5], CM[5], CM[4], CM[3], CM[2], CM[2],
CM[3], CM[4], CM[4], CM[3], CM[2], CM[3], CM[1], CM[1],
CM[3], CM[2], CL[5], CL[7], CM[2], CM[1] ]

beat_2 = [ 1, 1, 2, 2, 1, 1, 2, 2, # Beats of song 2, 1 means 1/8 beats
1, 1, 2, 2, 1, 1, 3, 1,
1, 2, 2, 1, 1, 2, 2, 1,
1, 2, 2, 1, 1, 3 ]

def setup():
  GPIO.setmode(GPIO.BOARD) # Numbers GPIOs by physical location
  GPIO.setup(BuzzerPin, GPIO.OUT) # Set pins' mode is output
  global Buzz # Assign a global variable to replace GPIO.PWM
  Buzz = GPIO.PWM(BuzzerPin, 440) # 440 is initial frequency.
  Buzz.start(50) # Start BuzzerPin pin with 50% duty ration

def loop():
  while True:
    print '\n Playing song 3...'
    for i in range(0, len(song_3)): # Play song 3
      Buzz.start(50)
      Buzz.ChangeFrequency(song_3[i]) # Change the frequency along the song note
      time.sleep(beat_3[i] * .25) # delay a note for beat * 0.5s
      Buzz.stop()
      time.sleep(.1)
    time.sleep(1) # Wait a second for next song.
    Buzz.start(50)

    print '\n Playing song 1...'
    for i in range(1, len(song_1)): # Play song 1
      Buzz.ChangeFrequency(song_1[i]) # Change the frequency along the song note
      time.sleep(beat_1[i] * 0.5) # delay a note for beat * 0.5s
    time.sleep(1) # Wait a second for next song.

    print '\n\n Playing song 2...'
    for i in range(1, len(song_2)): # Play song 1
      Buzz.ChangeFrequency(song_2[i]) # Change the frequency along the song note
      time.sleep(beat_2[i] * 0.5) # delay a note for beat * 0.5s

def destory():
  print("\nend.")
  Buzz.stop() # Stop the BuzzerPin
  GPIO.output(BuzzerPin, 1) # Set BuzzerPin pin to High
  GPIO.cleanup() # Release resource

if __name__ == '__main__': # Program start from here
  setup()
  try:
    loop()
  except KeyboardInterrupt:
    destory()
