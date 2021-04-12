import music21
import eel
from common.guitar import guitar
from src.data.chord import guitar_chord_builder, chord


def convert_id_to_note(id_):
    id_ = id_[::-1]
    note_name = ""
    for ltr in id_:
        if ltr == "t":
            break
        note_name += ltr
    return music21.note.Note(note_name[::-1])


def convert_id_to_note_name(id_):
    id_ = id_[::-1]
    note_name = ""
    for ltr in id_:
        if ltr == "t":
            break
        note_name += ltr
    return note_name[::-1]


def get_string(fret_name):
    string_list = ["e", "B", "G", "D", "A", "E"]  # todo: make extensible
    to_ret = 0
    try:
        to_ret = string_list.index(fret_name[0])
    except IndexError:
        print("Error")
        return
    return to_ret


@eel.expose
def select_guitar_note(note):
    fret_nr = ""
    for ltr in convert_id_to_note_name(note):
        if ltr != convert_id_to_note_name(note)[0]:
            fret_nr += ltr
    guitar.guitar.get_string_by_id(get_string(convert_id_to_note_name(note))).select_fret(int(fret_nr))


@eel.expose
def get_info(obj, type_):
    pass


# @eel.expose
def search(index, type_):
    if type_ == "Chords":
        for obj in sorted(chord.ChordInterface.index(index)):
            eel.search_append(obj, type_)


@eel.expose
def display_lowest_chord(chord_name):
    print(chord_name)
    chord_ = chord.ChordInterface.get_chord(chord_name)
    print(chord_.root())
    # frets = guitar.guitar.get_lowest_caged_chord(chord_)[0]
    frets = guitar_chord_builder.get_lowest(guitar_chord_builder.GuitarChord(chord_, 4).get_shapes())
    print(frets)
    for i in range(len(frets)):  # [0, 2, 2, 1, 0, 0]
        if frets[5 - i] != "x":
            string_name = guitar.guitar.get_strings()[i].get_name()
            fret_name = f"{string_name}{frets[5 - i]}"
            eel.highlight_fret(get_js_fret_name(fret_name))


@eel.expose
def display_chord(chord_name, lowest_string):
    print(chord_name)
    chord_ = chord.ChordInterface.get_chord(chord_name)
    frets = guitar_chord_builder.GuitarChord(chord_, lowest_string).get_shapes()
    for i in range(len(frets)):
        if frets[5 - i] != "x":
            string_name = guitar.guitar.get_strings()[i].get_name()
            fret_name = f"{string_name}{frets[5 - i]}"
            eel.highlight_fret(get_js_fret_name(fret_name))


def get_js_fret_name(fret_name):
    return f"fret{fret_name}"
