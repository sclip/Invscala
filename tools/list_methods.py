def get_lowest_item(li):
    lowest = li[0]
    for item in li:
        if item < lowest:
            lowest = item
    return lowest
