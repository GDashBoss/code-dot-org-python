"""Stage 7: Puzzle 1 of 11

Can you draw a triangle (with edges of 100 pixels) with only 3
lines of code? Hint: use a repeat (for) loop.

"""

import sys
sys.path.append('..')
import codestudio
artist = codestudio.load('s1level35')
a = artist
a.fd(100)
a.rt(120)
a.fd(100)
a.rt(120)
a.fd(100)

artist.check()
