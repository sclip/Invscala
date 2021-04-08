def remove_up_to(string, up_to):
    """remove_up_to() -> string

    :param string: String to remove from
    :param up_to: Character to remove up to
    :return: String without all characters before and including 'up_to'
    """
    my_str = string
    my_str2 = ""

    for letter in my_str[::-1]:
        if letter == up_to:
            break
        my_str2 += letter
    my_str2 = my_str2[::-1]

    return my_str2
