import random


def rng_return(chance):
    if chance < 0 or chance > 100:
        raise ValueError(chance)
    if random.randint(0, 100) <= chance:
        return True
    else:
        return False
