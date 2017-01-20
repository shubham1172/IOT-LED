from flask import Flask, render_template, request, make_response
import RPi.GPIO as GPIO
import time

app = Flask(__name__)

def init():
	global RED, YELLOW, GREEN, stateRed, stateYellow, stateGreen
	RED = 12; stateRed = False
	YELLOW = 16; stateYellow = False 
	GREEN = 21; stateGreen = False

def setup():
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.setup(RED, GPIO.OUT)
	GPIO.setup(YELLOW, GPIO.OUT)
	GPIO.setup(GREEN, GPIO.OUT)
	GPIO.output(RED, GPIO.LOW)
	GPIO.output(GREEN, GPIO.LOW)
	GPIO.output(YELLOW, GPIO.LOW)

def glowLED(LED):
	GPIO.output(LED, GPIO.HIGH)
def dimLED(LED):
	GPIO.output(LED, GPIO.LOW)

#Home
@app.route('/')
def index():
	return make_response(render_template("home.html"),200)

#Task
@app.route('/task')
def task():
	headers = {'Content-Type': 'text/html'}
	return make_response(render_template("taskpage.html"),200,headers)

#GLOW
@app.route('/glow/<LED>')
def glow(LED):
	global stateRed, stateGreen, stateYellow
	if(LED=="R"):
		if(stateRed==False):
			glowLED(RED)
			stateRed = True
		else:
			dimLED(RED)
			stateRed = False
	elif(LED=="G"):
		if(stateGreen==False):
			glowLED(GREEN)
			stateGreen = True
		else:
			dimLED(GREEN)
			stateGreen = False
	elif(LED=="Y"):
		if(stateYellow==False):
			glowLED(YELLOW)
			stateYellow = True
		else:
			dimLED(YELLOW)
			stateYellow = False
	return "DONE"			

if(__name__=="__main__"):
	init()
	setup()
	app.run(host='0.0.0.0')
