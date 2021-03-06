"""Stage 5: Puzzle 6 of 10

Can you figure out how draw this triangle and square? Hint: Do the
triangle first, then figure out how much to turn before drawing the
square.

"""

import sys
sys.path.append('..')
import codestudio
artist = codestudio.load('s1level29')
a = artist

for count in range(3):
    a.fd(100)
    a.rt(120)
for count in range(1):
    a.lt(180)
for count in range(4):
    a.fd(100)
    a.rt(90)
    
artist.check()
