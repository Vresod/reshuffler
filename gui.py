import PySimpleGUI as sg
import settings

# GUI TODO:
# make backend.py more modular
# add backend.py functionality
# make settings tab let you modify the settings
# make colors look nicer
# add icon, separate from python.exe, etc, basically just steal boilerplate from AUE-PY

settings_layout = sg.Tab(
	"Settings",
	[[sg.Text(i),sg.Push(),sg.Text(settings.Settings[i] if i != "client_secret" else "*" * len(settings.Settings[i]))] for i in settings.Settings]
)

layout=[[sg.TabGroup([[settings_layout]],"topleft")],
		[sg.Text("WIP")],
		[sg.Button("Ok"), sg.Button("Quit")]]

sg.theme("DarkGreen5")
window = sg.Window("Reshuffler", layout)

while True:
	event, values = window.read()
	if event == sg.WINDOW_CLOSED or event == "Quit":
		break

window.close()