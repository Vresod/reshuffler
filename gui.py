import PySimpleGUI as sg
import settings

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