import serial
import SlidingWindowV1_1 as SWL

ser = serial.Serial('COM4',9600,timeout=None)
dictionary = {'1':'crocin', '2':'digene', '3':'flagyl', '4':'norflox', '5':'wikoryl'}

def getName():
	#name = dictionary[ser.read()]
	inString = chr(int(ser.read(2)))
	return dictionary[inString]

SWL.main(getName())