def to_roman(number):
    """Convert number into a roman numeral

    Returns a string
    Ex to_roman(5) -> "V"

    """
    num = [1, 4, 5, 9, 10, 40, 50, 90,
           100, 400, 500, 900, 1000]
    sym = ["I", "IV", "V", "IX", "X", "XL",
           "L", "XC", "C", "CD", "D", "CM", "M"]
    output = ""
    i = 12
    while number:
        div = number // num[i]
        number %= num[i]

        while div:
            output += sym[i]
            div -= 1
        i -= 1
    return output
