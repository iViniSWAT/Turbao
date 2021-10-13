
from guizero import App, Combo, Text, PushButton
import sys

def exitapp():
    sys.exit()

def update_bg():
    app.bg = bg_combo.value

def update_text():
    app.text_color = text_combo.value

colors = ["Black", "White", "Red", "Green", "Blue", "Yellow"]

app = App()
app.bg = "Blue"
app.text_color = "Yellow"

title1 = Text(app, text="Cor de Fundo")
bg_combo = Combo(app, options=colors, selected=app.bg, command=update_bg)

title2 = Text(app, text="Cor do Texto")
text_combo = Combo(app, options=colors, selected=app.text_color, command=update_text)

exitButton = PushButton(app, exitapp, text='Sair', align='bottom', width=15, height=3)
exitButton.text_size = 36

app.display()
