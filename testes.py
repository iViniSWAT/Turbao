from gpiozero import *

#sensor = InputDevice(26)
#pulsos = 0
#
#while True:
#    if sensor.is_active == 0:
#        pulsos = pulsos+1
#        print(pulsos)

motor = Motor(3,20)
sensor = Button(21)
count = 0

while True:
    #speed = input()
    #speed1=float(speed)
    #motor.forward(speed1)
    if sensor.is_pressed:
	    count += 1
	    print(count)