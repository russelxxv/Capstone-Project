import serial
import time
import shlex
import subprocess
import RPi.GPIO as GPIO

redLed = 21
greenLed = 20
blueLed = 16

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(redLed,GPIO.OUT)
GPIO.setup(greenLed,GPIO.OUT)
GPIO.setup(blueLed,GPIO.OUT)

tmeSleep = 0.2

cmd_end = 'aplay voice.wav'
ser = serial.Serial('/dev/ttyACM0', 38400)

welcome = 'pico2wave -l en-US -w voice.wav "Welcome! to Speaking Glove!, You can now start!"'
frmt_welcome = shlex.split(welcome)
subprocess.call(frmt_welcome, stdout=subprocess.PIPE)
subprocess.call(cmd_end, shell=True)

GPIO.output(21,GPIO.HIGH)
time.sleep(tmeSleep)
GPIO.output(21,GPIO.LOW)
time.sleep(tmeSleep)
GPIO.output(21,GPIO.HIGH)
time.sleep(tmeSleep)
GPIO.output(21,GPIO.LOW)
time.sleep(tmeSleep)
GPIO.output(21,GPIO.HIGH)
time.sleep(tmeSleep)
GPIO.output(21,GPIO.LOW)
GPIO.output(20,GPIO.LOW)
GPIO.output(16,GPIO.LOW)

while True:
    try:
        text = ser.readline().decode("ASCII")#.strip('\r\n')
        #print(text)
        try:
            int(text)
            print(text);
            if int(text) == 255:
                GPIO.output(blueLed,GPIO.HIGH)
                GPIO.output(redLed,GPIO.HIGH)
                GPIO.output(greenLed,GPIO.LOW)
            elif int(text) == 256:
                GPIO.output(greenLed,GPIO.LOW)
                GPIO.output(redLed,GPIO.HIGH)
                GPIO.output(blueLed,GPIO.LOW)
            elif int(text) == 155:
                GPIO.output(redLed,GPIO.LOW)
                GPIO.output(greenLed,GPIO.HIGH)
                GPIO.output(blueLed,GPIO.LOW)
            elif int(text) == 355:
                GPIO.output(greenLed,GPIO.LOW)
        except ValueError:
                raw_command = 'pico2wave -l en-US -w voice.wav "%s"'%(text)
                formatted_command = shlex.split(raw_command)
                
                print(text)
                
                subprocess.call(formatted_command, stdout=subprocess.PIPE)
                subprocess.call(cmd_end, shell=True)
    except: ValueError

