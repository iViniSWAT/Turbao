#from tkinter import *
from guizero import *
import sys

volAleta = 1922223.16 #mm³

#def exitapp():
#    sys.exit()

def inputNumber(key):
    global displayString, operatorFlag
    if operatorFlag:
        displayString=''
        operatorFlag = False
    displayString = displayString + key
    display.value = displayString


def milhoVariaveis():
    tiposTrat = Window(app, title="Tipos de Tratamento", bg="#2d2e6f")
    tiposTrat.tk.attributes("-fullscreen", True)
    spacer2_Box = Box(tiposTrat, width="fill", height=100, border=True)

    tituloTrat_Box = Box(tiposTrat,width="fill", border=True)
    tituloTrat = Text(tituloTrat_Box, text="Selecione o tipo de Tratamento:",font="Geometria")
    tiposTrat.text_size = 20
    tiposTrat.text_color = "White"

    config_but_Box1 = Box(tiposTrat, width="fill", align="bottom", border=True)
    config_but = PushButton(config_but_Box1, image="/home/pi/Pictures/engrenagem.png",align="left")
    config_but.bg="#2d2e6f"

    spacer2_Box = Box(tiposTrat, width=100, height="fill", border=True, align="left")
    spacer3_Box = Box(tiposTrat, width=98, height="fill", border=True, align="right")

    buttons_Box1 = Box(tiposTrat, width="fill", height="fill", border=True, align="left", layout="grid")
    liq1po1_but = PushButton(buttons_Box1, espProd, text="1 Líquido 1 Pó", width="10", height="2", align="top", grid=[0,0])
    liq1po1_but.text_color="Black"
    liq1po1_but.text_size=20
    liq1po1_but.bg="white"
    liq1po1_but.font="Geometria"

    spacer2_Tex = Text(buttons_Box1, text="", width=11,grid=[1,0])

    liq1po2_but = PushButton(buttons_Box1, command=None, text="1 Líquido 2 Pós",grid=[2,0], width=10, height=2, enabled=False)
    liq1po2_but.text_color="Black"
    liq1po2_but.text_size=20
    liq1po2_but.bg="white"
    liq1po2_but.font="Geometria"

    spacer3_Tex = Text(buttons_Box1, text="", width=11,grid=[0,1])

    liq2po1_but = PushButton(buttons_Box1, command=None, text="2 Líquidos 1 Pó",grid=[0,2], width=10, height=2, enabled=False)
    liq2po1_but.text_color="Black"
    liq2po1_but.text_size=20
    liq2po1_but.bg="white"
    liq2po1_but.font="Geometria"

    liq2po2_but = PushButton(buttons_Box1, command=None, text="2 Líquidos 2 Pós",grid=[2,2], width=10, height=2, enabled=False)
    liq2po2_but.text_color="Black"
    liq2po2_but.text_size=20
    liq2po2_but.bg="white"
    liq2po2_but.font="Geometria"


    pesoEspMilho = 0.70 #Kg/m³ - 0,0007 g/cm3
    densEspMilho = 1.277 #g/cm³ - 1277 Kg/m³
    volEspMilho = 0.0007 #kg/cm³   0.000548159 #m3

#------------------------------------------------------------------------------#

#def soja():

#---------------------------------------------------------------#

def espProd():
    especificProd = Window(app, title="Especificação dos Produtos", bg="#2d2e6f")
    especificProd.tk.attributes("-fullscreen", True)

    spacer4_Box = Box(especificProd, width="fill", height=25, border=True)

    especificProd_Box = Box(especificProd, width="fill", border=True)
    especificProd_Text = Text(especificProd_Box, text="Insira as especificações dos Produtos", font="Geometria")
    especificProd_Text.text_color = "White"
    especificProd_Text.text_size = 20

    spacer5_Box = Box(especificProd, width="fill", height=20, border=True)

    spacer6_Box = Box(especificProd, width=50, height="fill", align="left", border=True)

    keyboard_buttons = Box(especificProd,width="fill", height="fill", align="right", layout="grid", border=True)
    labelspacer1 = Text(keyboard_buttons, grid=[0,1],text="                ")
    btn7 = PushButton(keyboard_buttons, command=inputNumber, args=['7'], text='7', grid=[1,1],width=5,height=4)
    btn8 = PushButton(keyboard_buttons, command=inputNumber, args=['8'], text='8', grid=[2,1],width=5,height=4)
    btn9 = PushButton(keyboard_buttons, command=inputNumber, args=['9'], text='9', grid=[3,1],width=5,height=4)
    btn4 = PushButton(keyboard_buttons, command=inputNumber, args=['4'], text='4', grid=[1,2],width=5,height=4)
    btn5 = PushButton(keyboard_buttons, command=inputNumber, args=['5'], text='5', grid=[2,2],width=5,height=4)
    btn6 = PushButton(keyboard_buttons, command=inputNumber, args=['6'], text='6', grid=[3,2],width=5,height=4)
    btn1 = PushButton(keyboard_buttons, command=inputNumber, args=['1'], text='1', grid=[1,3],width=5,height=4)
    btn2 = PushButton(keyboard_buttons, command=inputNumber, args=['2'], text='2', grid=[2,3],width=5,height=4)
    btn3 = PushButton(keyboard_buttons, command=inputNumber, args=['3'], text='3', grid=[3,3],width=5,height=4)
    btn0 = PushButton(keyboard_buttons, command=inputNumber, args=['0'], text='0', grid=[2,4],width=5,height=4)
    #btnDec = PushButton(keyboard_buttons, command=inputNumber, args=['.'], text=' .', grid=[3,4],width=5,height=4)
    
    btn7.bg="White"
    btn8.bg="white"
    btn9.bg="White"
    btn4.bg="White"
    btn5.bg="White"
    btn6.bg="White"
    btn1.bg="White"
    btn2.bg="White"
    btn3.bg="White"
    btn0.bg="White"
    #btnDec.bg="White"

    formsBox = Box(especificProd, width="fill", height="fill", layout="grid",border=True)

    calda1_Box = Box(formsBox, width="fill", border=True, layout="grid", grid=[0,0])
    densidadecalda1_Text = Text(calda1_Box, text="Densidade da Calda 1     ", font="Geometria", grid=[0,0])
    densidadecalda1_Text.text_color = "White"
    densidadecalda1_Text.text_size = 15
    densidadecalda1_TextBox = TextBox(calda1_Box, grid=[1,0])
    ## densidadecalda1_TextBox.append("kg/m³")
    densidadecalda1_TextBox.bg = "White"
    densidadecalda1Final_Text = Text(calda1_Box, text="kg/m³", font="Geometria", grid=[2,0])
    densidadecalda1Final_Text.text_color = "White"
    densidadecalda1Final_Text.text_size = 15

    spacer7_Box = Box(calda1_Box, width="fill", height=5, grid=[0,1], align="left", border=True)

    quantidadecalda1_Text = Text(calda1_Box, text=" Quantidade da Calda 1     ", font="Geometria", grid=[0,2])
    quantidadecalda1_Text.text_color = "White"
    quantidadecalda1_Text.text_size = 15
    quantidadecalda1_TextBox = TextBox(calda1_Box, grid=[1,2])
    ## quantidadecalda1_TextBox.append("kg/m³")
    quantidadecalda1_TextBox.bg = "White"
    quantidadecalda1Final_Text = Text(calda1_Box, text="ml/Kg", font="Geometria", grid=[2,2])
    quantidadecalda1Final_Text.text_color = "White"
    quantidadecalda1Final_Text.text_size = 15

    spacer8_Box = Box(formsBox, width="fill", height= 20, grid=[0,1], align="left", border=True)

    po1_Box = Box(formsBox, width="fill", height="fill", grid=[0,2], layout="grid", align="left", border=True)
    po1quantidade_Text = Text(po1_Box, text="Quantidade do Pó 1            ", font="Geometria", grid=[0,0])
    po1quantidade_Text.text_color="White"
    po1quantidade_Text.text_size=15
    po1quantidade_TextBox = TextBox(po1_Box, grid=[1,0])
    po1quantidade_TextBox.bg = "White"
    po1quantidadeFinal_Text = Text(po1_Box, text="g/kg", grid=[2,0], font="Geometria")
    po1quantidadeFinal_Text.text_color = "white"
    po1quantidadeFinal_Text.text_size = 15



#----------------------------------------------------------#

app = App(title="Mecmaq",bg="#2d2e6f")
app.tk.attributes("-fullscreen", True)
#app.image("icone")
#picture = Picture(app, image="/home/pi/Pictures/TELA AUTOMAÇÃO FUNDO.png")

spacer_Box = Box(app, width="fill", height=180, border=True)

intro_Box = Box(app, width="fill", border=True)
intro = Text(intro_Box, text = "Selecione a cultura a ser tratada:",font="Geometria")
intro.text_size = 20
intro.text_color="white"

config_but_Box = Box(app, width="fill", align="bottom", border=True)
config_but = PushButton(config_but_Box, image="/home/pi/Pictures/engrenagem.png",align="left")
config_but.bg="#2d2e6f"

spacer1_Box = Box(app, width=100, height="fill", border=True, align="left")

buttons_Box = Box(app, width="fill", height="fill", border=True, align="left", layout="grid")
milho_but = PushButton(buttons_Box, milhoVariaveis, text="Milho", width="10", height="2", align="top", grid=[0,0])
milho_but.text_color="Black"
milho_but.text_size=20
milho_but.bg="white"
milho_but.font="Geometria"

spacer_text = Text(buttons_Box, text="",width=20, grid=[1,0])

soja_but = PushButton(buttons_Box, text="Soja", width="10", height="2",align="right", grid=[2,0])
soja_but.text_size=20
soja_but.text_color="Black"
soja_but.bg="white"
soja_but.font="Geometria"
#-------------------------------------------------------------------------#


app.display()