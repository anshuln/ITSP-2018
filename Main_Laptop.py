import serial
import Sliding_Windows as SWL
import pyautogui
import imaplib
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
def read_input_from_email():
	imapObj=imaplib.IMAP4_SSL('imap.gmail.com',993)
	imapObj.login('ITSP35@gmail.com','ITSP35')
	imapObj.select('INBOX')
	unread_msg_nums=[]
	while len(unread_msg_nums)==0:
		status, response = imap.search(None, 'INBOX', '(UNSEEN)')
		unread_msg_nums = response[0].split()
		time.sleep(3)
	for id in unread_msg_nums:
		_, response = imap.fetch(id, '(UID BODY[TEXT])')
		imap.store(id, '+FLAGS', '\Seen')
	print(response[0][1])
	return(response[0][1])
	
def get_string_from_coords(coords):
	x = int((coords[0]/size[0])*steps)
	y = int((coords[1]/size[1])*steps)
	str = 'l'*x + 'd'*y + 'p' + 'r'*x + 'u'*y 
	return str

def getName():
	#name = dictionary[ser.read()]
	print("Awaiting Input...")
# 	inString = chr(int(ser.read(2)))
	inString=read_input_from_email()
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
	print("Give Input")
	name=getName()
	print("Capturing Image...")
	capture()
	path=''	#Fix path here
	print("Extracting coordinates")
	coords = SWL.main(path,name)
	os.remove(path)
	dir = get_string_from_coords(coords)
	print("Moving Arm")
	moveMotors(dir)
