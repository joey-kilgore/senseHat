import netifaces
from sense_hat import SenseHat

sense = SenseHat()
sense.clear()
sense.low_light = True

def getIP():
    iface = netifaces.gateways()['default'][netifaces.AF_INET][1]
    return netifaces.ifaddresses(iface)[netifaces.AF_INET][0]['addr']

IP = getIP()
print(IP)
#sense.show_message(str(IP))
while True:
    for event in sense.stick.get_events():
        if event.action == "pressed":
            sense.show_message(str(IP))
