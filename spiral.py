from sense_hat import SenseHat
from time import sleep
import random
sense = SenseHat()
sense.clear()
sense.low_light = True

def turnOnLED(x,y):
	color =[random.randint(50,200), random.randint(50,200), random.randint(50,200)]
	sense.set_pixel(x,y, color)
	#print(str(x) + ',' + str(y))
	sleep(waitTime)

def spiral():
	x = 0	# initial coordinates
	y = 0
	xmax = 7
	ymax = 7
	xmin = 0
	ymin = 1
	turnOnLED(x,y)

	while xmax>xmin:
		# draw top line
		while x<xmax:
			x = x+1
			turnOnLED(x,y)
		xmax = xmax-1

		# first side
		while y<ymax:
			y = y+1
			turnOnLED(x,y)
		ymax = ymax-1

		# bottom line
		while x>xmin:
			x = x-1
			turnOnLED(x,y)
		xmin = xmin+1

		# last side
		while y>ymin:
			y = y-1
			turnOnLED(x,y)
		ymin = ymin+1

try:
	waitTime = .1
	for num in range(10):
		#waitTime = waitTime -.05
		spiral()
		sense.clear()
except:
	sense.clear()
