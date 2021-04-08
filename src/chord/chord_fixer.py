import music21

my_chord = music21.chord.Chord("C F- A--")


def get_real_chord_quality(chord):
    if chord.quality == "other":
        return chord.simplifyEnharmonics().quality
    return chord.quality


def get_real_chord(chord):
    return chord.simplifyEnharmonics()


my_chord.simplifyEnharmonics(inPlace=True)
print(my_chord.pitchedCommonName)
print(my_chord.quality)
print(my_chord.normalOrder)
# print(my_chord.inversionName())
print(get_real_chord_quality(my_chord.simplifyEnharmonics()))
