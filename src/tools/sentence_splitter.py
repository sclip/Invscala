def split(sentence):
    """

    :param sentence: Sentence to split into words
    :return: List of words
    """
    words = []
    new_word = ""
    for letter in sentence:
        if letter == " ":
            if len(new_word) > 0:
                words.append(new_word)
            new_word = ""
        else:
            new_word += letter
    words.append(new_word)
    return words
