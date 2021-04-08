from src.gui import gui, setup
from src.data.note import note
from src.data.chord import chord
from src.data.defaults import syn_notes, octave, chord_types, notes, chord_shapes, default, chords
from src import folder_creator


def setup_gui():
    gui.init()


def setup_default():
    # Setup notes
    default.init()

    ln = default.settings.get_setting("config", "Lowest Note")
    hn = default.settings.get_setting("config", "Highest Note")
    notes_ = note.NoteInterface.generate(lowest=ln, highest=hn)
    notes.notes.set_notes(notes_)

    notes_ = note.NoteInterface.generate_octave()
    octave.octave.set_octave(notes_)

    syn_notes_ = default.settings.get_settings_file("syn_notes")
    syn_notes.syn_notes.set_syn_notes(syn_notes_)

    chord_shapes.chord_shapes.set_chord_shapes(default.settings.get_settings_file("chord_shapes"))


def setup_data():
    # Setup chords
    chord_types.chord_types.set_chord_types(default.settings.get_settings_file("chord_types"))
    chord.ChordInterface.init()

    chords.chords.set_chords(chord.all_chords)


def setup_plugins(priority):
    if priority == "abc":  # Todo
        modules_to_import = []  # json
        modules = map(__import__, modules_to_import)
        # modules.init()


def setup_common():
    pass


if __name__ == '__main__':
    # setup_plugins("High Priority")  # Todo
    folder_creator.init()
    setup_default()
    setup_data()
    # setup_common()
    # setup_plugins("Low Priority")
    setup.load()
    setup_gui()
