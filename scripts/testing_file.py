
def can_bar1():
    pass


def can_bar2():
    pass


def can_bar(base, a) -> bool:

    prev1 = None
    prev1_count = 0

    for n in a:
        if n not in [base, "x"]:
            if prev1 is None:
                prev1 = n
            if n == prev1:
                prev1_count += 1

    print(prev1_count)

    if prev1_count >= 3:
        return True
    return False
