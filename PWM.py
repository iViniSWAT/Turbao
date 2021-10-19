from gpiozero import *
import time

motor = Motor(20,21)


while True:
    speed = input()
    speed1=float(speed)
    motor.forward(speed1)