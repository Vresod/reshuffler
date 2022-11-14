import json
import os
from typing import Union

__all__ = ["Settings"]

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
			settings = {}
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
		for key in self:
			repr_str += f"{key}={repr(self.__dict__[key])}, "
		repr_str += f"_file_location={repr(self._file_location)}>"
		return repr_str
	
	def __iter__(self):
		for i in self.__dict__.keys():
			if i[0] == "_": continue
			yield i
	
	def __getitem__(self,item):
		if item[0] != "_":
			return self.__dict__[item]
		raise KeyError(repr(item))
	
	def __setitem__(self,key,value):
		self.__setattr__(key,value)

Settings = SettingsClass("settings.json")

def assert_default_settings(settings:SettingsClass):
	assert settings.added_songs == 90
	assert settings.client_id == ""
	assert settings.client_secret == ""
	assert settings.redirect_uri == "http://127.0.0.1:9090"

def main():
	# i wrote this function because I wanted to feel productive while doing nothing productive at all
	# it did end up making the code a little less shit but not in any meaningful way
	"""
	resets your settings and performs some code tests
	"""
	f = "settings.json"

	# test __init__ from a corrupted state
	with open(f,"w") as file: file.write("{")
	Settings = SettingsClass(f)
	assert_default_settings(Settings)
	
	# test __init__ from a non-blank state
	Settings = SettingsClass(f)
	assert_default_settings(Settings)
	
	# test __init__ from a blank state
	os.remove(f)
	Settings = SettingsClass(f)
	assert_default_settings(Settings)

	# test __setattr__
	Settings.added_songs = 45
	assert Settings.added_songs == 45 # seems stupid but considering we do fuck with the __setattr__ function I believe it is a good test

	# test __iter__
	assert 'added_songs' in Settings
	assert '_file_location' not in Settings

	# test __repr__
	print(Settings) # tell me if it looks good, that's about all I can say

	# test __getitem__
	assert Settings['added_songs'] == 45
	try: # can't assert that an error will happen but we can error if it does
		Settings['_file_location']
		raise AssertionError
	except KeyError: pass

	Settings.added_songs = 90 # assuming everything else went well this will set it back to the default value

if __name__ == "__main__":
	main()