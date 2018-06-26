import serial
import SlidingWindowV1_1 as SWL

ser = serial.Serial('COM4',9600,timeout=None)
dictionary = {'1':'crocin', '2':'digene', '3':'flagyl', '4':'norflox', '5':'wikoryl'}
size=[400,400]
steps=1500
def get_string_from_coords(coords):
	x = int((coords[0]/size[0])*steps)
	y = int((coords[1]/size[1])*steps)
	str = 'l'*x + 'd'*y + 'p' + 'r'*x + 'u'*y 
	return str
def getName():
	#name = dictionary[ser.read()]
	print("Awaiting Input...")
	inString = chr(int(ser.read(2)))
	print("Read Input")
	return dictionary[inString]

print("Extracting coorddinates")
coords = SWL.main(getName())
dir = get_string_from_coords(coords)
print("Moving Arm")
ser.print(dir)
