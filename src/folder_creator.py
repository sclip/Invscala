import os


# TODO: refactor, make more dynamic!


def create_documents_folder():
    folder_path = os.path.expanduser('~/documents')
    if not os.path.exists(folder_path + "/Scale Finder"):
        os.makedirs(folder_path + "/Scale Finder")


def create_sub_folders():
    folder_path = os.path.expanduser('~/documents/Scale Finder')
    if not os.path.exists(folder_path + "/MIDI"):
        os.makedirs(folder_path + "/MIDI")
    if not os.path.exists(folder_path + "/logs"):
        os.makedirs(folder_path + "/logs")
    if not os.path.exists(folder_path + "/xml"):
        os.makedirs(folder_path + "/xml")


def init():
    create_documents_folder()
    create_sub_folders()
