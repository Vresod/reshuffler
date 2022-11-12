import PySimpleGUI as sg

layout = [[sg.Text("WIP")],
		[sg.Button("Ok"), sg.Button("Quit")]]

sg.theme("DarkGreen5")
window = sg.Window("Reshuffler", layout)

while True:
	event, values = window.read()
	if event == sg.WINDOW_CLOSED or event == "Quit":
		break

window.close()