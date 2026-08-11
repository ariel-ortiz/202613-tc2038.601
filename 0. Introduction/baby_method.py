def sqrt(s: float, guess: float, delta: float) -> float:
    if s < 0:
        raise ValueError(f'Cannot compute square root of negative number: {s}')
    prev: float = guess
    while True:
        guess = (prev + s / prev) / 2
        if abs(guess - prev) <= delta:
            return guess
        prev = guess


print(f'{__name__ = }')


if __name__ == '__main__':
    try:
        sqrt(-1, 0, 0.0001)
        assert False
    except ValueError:
        ...
    print(f'{sqrt(50, 7, 0.0001) = }')
    print(f'{sqrt(100, 1, 0.0001) = }')
    print(f'{sqrt(2, 1, 0.0001) = }')
