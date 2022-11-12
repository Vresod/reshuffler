import json
import os
from typing import Union

__exports__ = ["Settings"]

class SettingsClass:
	def __init__(self,file_location:Union[str,os.PathLike]) -> None:
		self._file_location = file_location
		self._autosave = True
		try:
			open(self._file_location,"x")
			open(self._file_location,"w").write("{}")
		except FileExistsError: pass
		# self._file_handler = open(self._file_location,"r+") # we don't want it getting fucked with while we're working with it
		try:
			with open(self._file_location,"r") as file: settings:dict = json.load(file)
		except json.JSONDecodeError:
			open(self._file_location,"w").write("{}")
		self._autosave = False
		self.redirect_uri:str = settings.get("redirect_uri","http://127.0.0.1:9090")
		self.client_id:str = settings.get("client_id","")
		self.client_secret:str = settings.get("client_secret","")
		self.added_songs:int = settings.get("added_songs",90)
		self._autosave = True
	
	def __setattr__(self, __name: str, __value) -> None:
		super().__setattr__(__name,__value)
		if __name[0] == "_" or not self._autosave:
			return
		with open(self._file_location,"r") as file: settings:dict = json.load(file)
		settings.update({k:v for k,v in self.__dict__.items() if k[0] != "_"})
		settings[__name] = __value
		with open(self._file_location,"w") as file: json.dump(settings,file,indent=4)
	
	def __repr__(self) -> str:
		repr_str = f"<SettingsClass: "
		for key in [k for k in self.__dict__.keys() if k[0] != "_"]:
			repr_str += f"{key}={repr(self.__dict__[key])}, "
		repr_str += f"_file_location={repr(self._file_location)}>"
		return repr_str

Settings = SettingsClass("settings.json")

def main():
	print(Settings)
	Settings.added_songs = 45

if __name__ == "__main__":
	main()