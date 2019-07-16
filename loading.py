from sense_hat import SenseHat
from time import sleep

rainbow = [[255,0,0],[255,255,0],[0,255,0],[0,255,255],[0,0,255],[255,0,255]]
colorNum = 0

x = [0,0,255]
o = [0,0,0]


off = [	o,o,o,o,o,o,o,o,
	o,o,o,o,o,o,o,o,
	o,o,o,o,o,o,o,o,
	o,o,o,o,o,o,o,o,
	o,o,o,o,o,o,o,o,
	o,o,o,o,o,o,o,o,
	o,o,o,o,o,o,o,o,
	o,o,o,o,o,o,o,o]

sense = SenseHat()

for loop in range(100):
	colorNum = (colorNum+1)%6
	x = rainbow[colorNum]
	spiral = [[
		x,o,o,o,o,o,o,o,
		o,x,o,o,o,o,o,o,
		o,o,x,o,o,o,o,o,
		o,o,o,x,o,o,o,o,
		o,o,o,o,x,o,o,o,
		o,o,o,o,o,x,o,o,
		o,o,o,o,o,o,x,o,
		o,o,o,o,o,o,o,x],[
		o,x,o,o,o,o,o,o,
		o,x,o,o,o,o,o,o,
		o,o,x,o,o,o,o,o,
		o,o,o,x,o,o,o,o,
		o,o,o,o,x,o,o,o,
		o,o,o,o,o,x,o,o,
		o,o,o,o,o,o,x,o,
		o,o,o,o,o,o,x,o],[
		o,o,x,o,o,o,o,o,
		o,o,x,o,o,o,o,o,
		o,o,x,o,o,o,o,o,
		o,o,o,x,o,o,o,o,
		o,o,o,o,x,o,o,o,
		o,o,o,o,o,x,o,o,
		o,o,o,o,o,x,o,o,
		o,o,o,o,o,x,o,o],[
		o,o,o,x,o,o,o,o,
		o,o,o,x,o,o,o,o,
		o,o,o,x,o,o,o,o,
		o,o,o,x,o,o,o,o,
		o,o,o,o,x,o,o,o,
		o,o,o,o,x,o,o,o,
		o,o,o,o,x,o,o,o,
		o,o,o,o,x,o,o,o],[
		o,o,o,o,x,o,o,o,
		o,o,o,o,x,o,o,o,
		o,o,o,o,x,o,o,o,
		o,o,o,o,x,o,o,o,
		o,o,o,x,o,o,o,o,
		o,o,o,x,o,o,o,o,
		o,o,o,x,o,o,o,o,
		o,o,o,x,o,o,o,o],[
		o,o,o,o,o,x,o,o,
		o,o,o,o,o,x,o,o,
		o,o,o,o,o,x,o,o,
		o,o,o,o,x,o,o,o,
		o,o,o,x,o,o,o,o,
		o,o,x,o,o,o,o,o,
		o,o,x,o,o,o,o,o,
		o,o,x,o,o,o,o,o],[
		o,o,o,o,o,o,x,o,
		o,o,o,o,o,o,x,o,
		o,o,o,o,o,x,o,o,
		o,o,o,o,x,o,o,o,
		o,o,o,x,o,o,o,o,
		o,o,x,o,o,o,o,o,
		o,x,o,o,o,o,o,o,
		o,x,o,o,o,o,o,o],[
		o,o,o,o,o,o,o,x,
		o,o,o,o,o,o,x,o,
		o,o,o,o,o,x,o,o,
		o,o,o,o,x,o,o,o,
		o,o,o,x,o,o,o,o,
		o,o,x,o,o,o,o,o,
		o,x,o,o,o,o,o,o,
		x,o,o,o,o,o,o,o],[
		o,o,o,o,o,o,o,o,
		o,o,o,o,o,o,x,x,
		o,o,o,o,o,x,o,o,
		o,o,o,o,x,o,o,o,
		o,o,o,x,o,o,o,o,
		o,o,x,o,o,o,o,o,
		x,x,o,o,o,o,o,o,
		o,o,o,o,o,o,o,o],[
		o,o,o,o,o,o,o,o,
		o,o,o,o,o,o,o,o,
		o,o,o,o,o,x,x,x,
		o,o,o,o,x,o,o,o,
		o,o,o,x,o,o,o,o,
		x,x,x,o,o,o,o,o,
		o,o,o,o,o,o,o,o,
		o,o,o,o,o,o,o,o],[
		o,o,o,o,o,o,o,o,
		o,o,o,o,o,o,o,o,
		o,o,o,o,o,o,o,o,
		o,o,o,o,x,x,x,x,
		x,x,x,x,o,o,o,o,
		o,o,o,o,o,o,o,o,
		o,o,o,o,o,o,o,o,
		o,o,o,o,o,o,o,o],[
		o,o,o,o,o,o,o,o,
		o,o,o,o,o,o,o,o,
		o,o,o,o,o,o,o,o,
		x,x,x,x,o,o,o,o,
		o,o,o,o,x,x,x,x,
		o,o,o,o,o,o,o,o,
		o,o,o,o,o,o,o,o,
		o,o,o,o,o,o,o,o],[
		o,o,o,o,o,o,o,o,
		o,o,o,o,o,o,o,o,
		x,x,x,o,o,o,o,o,
		o,o,o,x,o,o,o,o,
		o,o,o,o,x,o,o,o,
		o,o,o,o,o,x,x,x,
		o,o,o,o,o,o,o,o,
		o,o,o,o,o,o,o,o],[
		o,o,o,o,o,o,o,o,
		x,x,o,o,o,o,o,o,
		o,o,x,o,o,o,o,o,
		o,o,o,x,o,o,o,o,
		o,o,o,o,x,o,o,o,
		o,o,o,o,o,x,o,o,
		o,o,o,o,o,o,x,x,
		o,o,o,o,o,o,o,o]]
	for repeat in range(2):
		for num in range(14):
			sense.set_pixels(spiral[num])
			sleep(.025)

sense.set_pixels(off)
