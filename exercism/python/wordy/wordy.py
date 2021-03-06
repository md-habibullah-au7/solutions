from operator import add, sub, mul, floordiv
from functools import reduce

OPS = {'plus': add, 'minus': sub, 'divided': floordiv, 'multiplied': mul}


def calculate(question):
    words = [w for w in question[8:-1].split(' ') if w != 'by']
    try:
        fbs = [(OPS[op], int(n)) for op, n in zip(words[1::2], words[2::2])]
    except KeyError:
        raise ValueError
    return reduce(lambda a, (f, b): f(a, b), fbs, int(words[0]))
