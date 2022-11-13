import PySimpleGUI as sg
import sys
import ctypes
from settings import Settings

# GUI TODO:
# make backend.py more modular
# add backend.py functionality
# make settings tab let you modify the settings
# make colors look nicer
# add icon, separate from python.exe, etc, basically just steal boilerplate from AUE-PY

__version__ = "v0.1"

settings_layout = sg.Tab(
	"Settings",
	[[sg.Text(i),sg.Push(),sg.Input(Settings[i],password_char="" if i != "client_secret" else "*" * len(Settings[i]))] for i in Settings]
)

if sys.platform == 'win32' and not sys.argv[0].endswith('.exe'):
	ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(f'Vresod.Reshuffler.{__version__}') # string is arbitrary

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