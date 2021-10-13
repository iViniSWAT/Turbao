
from guizero import App, PushButton, Text, Window
from gpiozero import LED
import sys

led1 = LED(21)
led1.off()

led2 = LED(20)
led2.off()


led3 = LED(16)
led3.off()



def exitapp():
    sys.exit()


def toggleled1():
    led1.toggle()
    if led1.is_lit:
        ledButton1.text = 'LIGADO'
        ledButton1.bg = "Green"

    else:
        ledButton1.text = 'DESLIGADO'
        ledButton1.bg = "Red"

def toggleled2():
    led2.toggle()
    if led2.is_lit:
        ledButton2.text = 'LIGADO'
        ledButton2.bg = "Green"

    else:
        ledButton2.text = 'DESLIGADO'
        ledButton2.bg = "Red"

def toggleled3():
    led3.toggle()
    if led3.is_lit:
        ledButton3.text = 'LIGADO'
        ledButton3.bg = "Green"

    else:
        ledButton3.text = 'DESLIGADO'
        ledButton3.bg = "Red"

app = App(title='MecMaq',height=600, width=800)
#app = App(title='MecMaq',layout='grid')
app.tk.attributes("-fullscreen", True)


intro = Text(app, text = "Bem-Vindo ao novo sistema automatico da Turbão Dupla Nebulização!", align="top")
intro.text_size = 18

intro2 = Text(app, text = "Insira os dados para iniciar o processo de tratamento:", align="top")
intro2.text_size = 18

ledButton1 = PushButton(app, toggleled1, text='Desligado', align='left', width=10, height=2)
ledButton1.text_size = 20
ledButton1.bg = "Red"

ledButton2 = PushButton(app, toggleled2, text='Desligado', align='left', width=10, height=2)
ledButton2.text_size = 20
ledButton2.bg = "Red"

ledButton3 = PushButton(app, toggleled3, text='Desligado', align='left', width=10, height=2)
ledButton3.text_size = 20
ledButton3.bg = "Red"

exitButton = PushButton(app, exitapp, text='Sair', align='bottom', width=10, height=2)
exitButton.text_size = 10
exitButton.bg = 'Blue'
exitButton.text_color = 'Yellow'

app.display()
