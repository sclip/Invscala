import music21
from src.data.defaults import syn_notes

syn_notes_ = {
	"A#": "Bb",
	"C#": "Db",
	"D#": "Eb",
	"F#": "Gb",
	"G#": "Ab"
}
syn_notes.syn_notes.set_syn_notes(syn_notes_)


strings = []


def gen_string(root_note) -> list:
	root = music21.note.Note(root_note)
	# String in this case is *NOT* a str, a piece of text, but a guitar string.
	string = [tuple([root.transpose(n), n]) for n in range(24)]
	return string


[strings.append(gen_string(note)) for note in ["E4", "B3", "G3", "D3", "A2", "E2"]]


def is_syn(note_a, note_b) -> bool:
	return syn_notes.syn_notes.is_syn_note(note_a, note_b)


c = music21.chord.Chord("C E G")


def get_chord_note_positions(chord):
	new_strings = []
	for i in range(len(strings)):
		new_strings.append([n for n in strings[i] if any([is_syn(x, strings[i][strings[i].index(n)][0]) for x in chord.notes])])
	return new_strings


chord_pos = get_chord_note_positions(c)
[print([n[1] for n in x]) for x in chord_pos]

#
#
#


open_fret = 0
max_frets = 24
string_count = 6


def get_frets_on_string(bass_fret, previous, string_id, max_add=4, possible_frets=None, thumb=False) -> list:
	"""

	:param bass_fret:               Fret of the bass note in the chord
	:param previous:                Previous frets
	:param string_id:               The string to get the fret on
	:param max_add:                 Max added frets from last fret value
	:param possible_frets:          Possible frets to use, None for all
	:return:
	"""

	if possible_frets is None:
		possible_frets = chord_pos[string_id]

	if thumb:  # If the thumb is allowed then we have 5 fingers to work with
		fingers = 5
	else:
		fingers = 4

	for fret in previous:
		if fret > open_fret:
			fingers -= 1

	valid_frets = []
	for frets in this_string:

		if bass_fret[1] == 0:  # if the bass fret is open then we are a bit more free, can start anywhere actually
			valid_frets.append(frets)

		# if this fret is less than a distance of 2 from the previous fret, and at most a distance of max_add from bass
		if frets[1] < previous_fret[1] + 2 or frets[1] < bass_fret[1] + max_add:
			if frets[1] > bass_fret[1] - 1 or frets[1] == open_fret:
				valid_frets.append(frets)

	# Return muted string
	if len(valid_frets) == 0:
		return [("x", "x")]

	return valid_frets


# Frets use the format (note object, fret number)
# fret[1] will therefore give you the fret number
# fret[0] will get you the note object, workable with music21
f_1 = strings[0][0]
f_2 = strings[1][3]
t_s = strings[2]

a = [n[1] for n in get_frets_on_string(f_1, f_2, 2)]
print(a)
