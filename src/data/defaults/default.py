from src import config


class Settings:  # todo: unit test!
	__LAUNCH_SETTINGS = "data/res/launch_settings.json"
	__settings = {

	}
	loaded_settings = False

	def init(self):
		to_load = config.Loader.load(self.__LAUNCH_SETTINGS)
		for _file in to_load["to_load"]:
			loaded_file = config.Loader.load(_file)  # Load the file, this must be done before we edit _file

			# Remove everything before the / in the path, leaving you with the file name
			# print(_file)  # <- Output should be path/file_name.json
			_file2 = ""
			for letter in _file[::-1]:
				if letter == "/":
					break
				_file2 += letter
			_file = _file2[::-1]
			# print(_file)  # <- Output should be file_name.json
			# Remove the .json
			_file2 = ""
			for letter in _file:
				if letter == ".":
					break
				_file2 += letter
			_file = _file2
			# print(_file)  # <- Output should be file name

			# Create dictionaries for every settings file, giving us the {"a": {}, "b": {}} structure
			self.__settings.setdefault(str(_file), {})
			# print(self.__settings)  # <- Output should be {"a": {}, "b": {}}

			# Next we have to fill up this new dictionary. We access it by doing
			# self.__settings[_file]
			# print(self.__settings[_file])  # <- Test
			for obj in loaded_file:
				self.__settings[_file].setdefault(str(obj), loaded_file[obj])
			# print(self.__settings)
		print("Loaded Settings")

	def get_settings_file(self, settings_file):
		return self.__settings[settings_file]

	def get_setting(self, settings_file, setting):
		return self.__settings[settings_file][setting]


settings = Settings()


def init():
	settings.init()
