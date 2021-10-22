from guizero import *
from gpiozero import *
import time
import RPi.GPIO as GPIO
BUTTON_GPIO = 21
count=0
voltas=0
motor = Motor(3,20)

def pwm():
    speed = textBox_pwm.value
    print(speed)
    speed1=float(speed)
    motor.forward(speed1)




app = App(title="Mecmaq",bg="#2d2e6f")
app.tk.attributes("-fullscreen", True)

spacer_Box = Box(app, width="fill", height=100, border=True)

boxFuncoes = Box(app,width="fill", height="fill",border=True, grid=True)
textBox_pwm = TextBox(boxFuncoes, command=pwm, text="0", grid=[0,0] )
textBox_pwm.bg="white"
textPWM = Text(boxFuncoes, text="PWM", font="Geometria", grid=[0,1])
textPWM.text_color="White"

spacer_Text = Text(boxFuncoes, text="---------------", font="Geometria", grid=[1,0])

text_pulsos = Text(boxFuncoes, text=count, font="Geometria", grid=[2,0])
text_pulsos.text_color="white"
textVolta = Text(boxFuncoes, text=voltas, font="Geometria", grid=[2,1])
textVolta.text_color="White"


#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUTTON_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    pressed = False
    while True:
        # button is pressed when pin is LOW
        if not GPIO.input(BUTTON_GPIO):
            if not pressed:
                count=count+1
                voltas = count/7                
                #print(count," pulsos e", voltasConv," voltas.")
                pressed = True
        # button not pressed (or released)
        else:
            pressed = False
        time.sleep(0.1)


app.display()


