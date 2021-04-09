def get_real_chord_quality(chord):
    if chord.quality == "other":
        return chord.simplifyEnharmonics().quality
    return chord.quality


def get_real_chord(chord):
    return chord.simplifyEnharmonics()
