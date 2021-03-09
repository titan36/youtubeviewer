import webbrowser
import time
import os


url = raw_input("Enter YouTube URL : ")
refresh = raw_input("Enter refresh rate(seconds) : ")
brow = raw_input("Enter your default browser : ")

def OpenUrl():
	print("Successfully Viwed. ")
	os.system(" killall -9 " + brow)
	webbrowser.open(url)
	time.sleep(int(refresh))

for i in range(3):
	OpenUrl()
