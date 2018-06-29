import serial
import Sliding_Windows as SWL
import pyautogui

ser = serial.Serial('COM4',9600,timeout=None)
dictionary = {'1':'crocin', '2':'digene', '3':'flagyl', '4':'norflox', '5':'wikoryl'}
size=[400,400]
steps=1500
def capture():
	pyautogui.hotkey('alt', 'tab')
	pyautogui.PAUSE=2.5
	pyautogui.click(x=590,y=234)
	pyautogui.PAUSE=4
	pyautogui.click(x=672,y=518)
	pyautogui.PAUSE=2.5
	pyautogui.click(x=1037,y=162)

def get_string_from_coords(coords):
	x = int((coords[0]/size[0])*steps)
	y = int((coords[1]/size[1])*steps)
	str = 'l'*x + 'd'*y + 'p' + 'r'*x + 'u'*y 
	return str

def getName():
	#name = dictionary[ser.read()]
	print("Awaiting Input...")
	inString = chr(int(ser.read(2)))
	print("Input received")
	return dictionary[inString]

def moveMotors(dir):
	i = 0
	for i in range(0, len(dir)):
		ser.write(dir[i].encode())
		print("Waiting for response from Arduino...")
		while (ser.in_waiting == 0):
			pass
		print("Arduino's response: ", ser.read(1))

if __name__ == "__main__":
	print("Extracting coorddinates")
	coords = SWL.main(getName())
	dir = get_string_from_coords(coords)
	print("Moving Arm")
	moveMotors(dir)
