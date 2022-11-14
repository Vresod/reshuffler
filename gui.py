import PySimpleGUI as sg
import sys
import ctypes
from settings import Settings
import backend

# GUI TODO:
# make backend.py more modular
# add backend.py functionality
# make settings tab let you modify the settings
# make colors look nicer
# add icon, separate from python.exe, etc, basically just steal boilerplate from AUE-PY

__version__ = "v0.1"

settings_layout = sg.Tab(
	"Settings",
	[[sg.Text(i),sg.Push(),sg.Input(Settings[i],password_char="" if i != "client_secret" else "*" * len(Settings[i]),key=f"{i}",enable_events=True)] for i in Settings]
)

queue_randomizer_layout = sg.Tab(
	"Queue Manager",layout=[
		[sg.Text("Playlist:"),sg.Combo(values=[i['name'] for i in backend.list_playlists()])],
		# [sg.Combo(values=[[i['name']] for i in backend.list_playlists()])]
])

if sys.platform == 'win32' and not sys.argv[0].endswith('.exe'):
	ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(f'Vresod.Reshuffler.{__version__}') # string is arbitrary

layout=[[sg.TabGroup([[queue_randomizer_layout,settings_layout]],"topleft",key="TabGroup")],
		[sg.Text("WIP")],
		[sg.Button("Quit")]]

sg.theme("DarkGreen5")
window = sg.Window("Reshuffler", layout)

while True:
	event, values = window.read()
	if event == sg.WINDOW_CLOSED or event == "Quit":
		break
	print(event,values)
	if values['TabGroup'] == "Settings":
		Settings[event] = values[event]
		print(Settings[event])

window.close()