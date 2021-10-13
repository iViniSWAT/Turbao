
from guizero import App, PushButton, Text, Box
from gpiozero import LED
import gpiozero
import sys

RELAY_PIN = 18

relay = gpiozero.OutputDevice(RELAY_PIN, active_high=False, initial_value=False)
#relay.close()

led1 = LED(21)
led1.off()

led2 = LED(20)
led2.off()


led3 = LED(16)
led3.off()

def togglerelay1():
    relay.close()
    if relay.is_lit:
        #relay.on()
        relayButton1.text = 'LIGADO'
        relayButton1.bg = "Green"

    else:
        #relay.close()
        relayButton1.text = 'DESLIGADO'
        relayButton1.bg = "Red"



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

#app = App(title='MecMaq',height=600, width=800)
app = App(title='MecMaq', height=600, width=800)

intro_box = Box(app, width="fill", align="top")
intro = Text(intro_box, text = 'Bem-Vindo ao novo sistema automatico da Turbão Dupla Nebulização!', align='top')
intro.text_size = 18
intro2 = Text(intro_box, text = "Insira os dados para iniciar o processo de tratamento:", align='top')
intro2.text_size = 18

button_box = Box(app, width='fill', layout='grid', align='top')
#ledButton1 = PushButton(app, toggleled1, text='DESLIGADO', align='center', width=10, height=2)
#ledButton1.text_size = 20
#ledButton1.bg = "Red"

ledButton1 = PushButton(button_box, toggleled1, text='DESLIGADO', grid=[0,0], align='left',)
ledButton1.text_size = 20
ledButton1.bg = "Red"

#ledButton2 = PushButton(app, toggleled2, text='DESLIGADO', align='center', width=10, height=2)
#ledButton2.text_size = 20
#ledButton2.bg = "Red"

ledButton2 = PushButton(button_box, toggleled2, text='DESLIGADO', grid=[1,0], align='left')
ledButton2.text_size = 20
ledButton2.bg = "Red"

#ledButton3 = PushButton(app, toggleled3, text='DESLIGADO', align='center', width=10, height=2)
#ledButton3.text_size = 20
#ledButton3.bg = "Red"

ledButton3 = PushButton(button_box, toggleled3, text='DESLIGADO', grid=[2,0], align='left')
ledButton3.text_size = 20
ledButton3.bg = "Red"

relayButton1 = PushButton(button_box, togglerelay1, text='DESLIGADO', grid=[3,0], align='left',)
relayButton1.text_size = 20
relayButton1.bg = "Red"

#exitButton = PushButton(app, exitapp, text='Sair', align='bottom', width=10, height=2)
#exitButton.text_size = 10
#exitButton.bg = 'Blue'
#exitButton.text_color = 'Yellow'

exit_box = Box(app, width="fill", align="bottom")
exitButton = PushButton(exit_box, exitapp, text='Sair', align='right')
exitButton.text_size = 20
exitButton.bg = 'Blue'
exitButton.text_color = 'Yellow'

app.display()



