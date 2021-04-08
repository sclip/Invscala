def index(dictionary, k):
    i = 0
    if dictionary.__contains__(k) is False:
        raise KeyError(k)
    for val in dictionary:
        if val == k:
            return i
        i += 1


def get_id(dictionary, k):
    for i in dictionary:
        if k == index(dictionary, i):
            return i
