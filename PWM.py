from gpiozero import *
import time

motor = Motor(2,20)

while True:
    speed = input()
    speed1=float(speed)
    motor.forward(speed1)