import pathlib
import json


class Paths:
    __paths = {
        "config_path": "./res/config.json",
        "syn_notes_path": "./res/syn_notes.json"
    }

    def get_path(self, file):
        return self.__paths[file]

    def set_path(self, file, new_path):
        self.__paths[file] = new_path


class Loader:
    @staticmethod
    def load(file):
        with open(pathlib.Path(file), encoding="utf-8") as new_file:
            return json.load(new_file)
