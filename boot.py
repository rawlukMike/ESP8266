import network
import time
from machine import Pin
import _thread

LED = Pin(2,Pin.OUT)
wifiConnection = network.WLAN(network.STA_IF)

def discoLED(counter):
	global LED
	for x in range(1,counter):
		LED.value(0)
		time.sleep(0.2)
		LED.value(1)
		time.sleep(0.5)
		LED.value(0)

def neton():
	global wifiConnection
	global LED
	discoLED(3)
	if not wifiConnection.isconnected():
		print('connecting to network AP...')
		wifiConnection.active(True)
		wifiConnection.connect('###AP NAME###', '###PASSWORD###)
		while not wifiConnection.isconnected():
			pass
	else:
		print('Already Connected')
	print('network config:', wifiConnection.ifconfig())
	LED.value(1)

def netoff():
	global wifiConnection
	global LED
	discoLED(3)
	if wifiConnection.isconnected():
		print('Disconneting from AP...')
		wifiConnection.active(False)
	else:
		print('Already Disconnected')
	print('Network config:', wifiConnection.ifconfig())
	LED.value(0)
	
def chknet():
	global wifiConnection
	print('network config:', wifiConnection.ifconfig())
