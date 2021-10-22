import RPi.GPIO as GPIO
from gpiozero import *

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(26,GPIO.IN)
pulsos = 0
cont = 0 
while True:
    if (GPIO.input(26)==0):
        cont=cont + 1
        print("sim", cont)
    else:
        print("não")