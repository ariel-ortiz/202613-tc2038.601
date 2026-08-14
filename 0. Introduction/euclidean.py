def gcd2(a: int, b: int) -> int:
    while True:
        r: int = a % b
        if r == 0:
            return b
        a, b = b, r


def coprimes(a: int, b: int) -> bool:
    return gcd2(a, b) == 1


def gcd(a: int, b: int, *rest: int) -> int:
    result: int = gcd2(a, b)
    for n in rest:
        result = gcd2(result, n)
    return result


def lcm(a: int, b: int) -> int:
    return a * b // gcd2(a, b)


if __name__ == '__main__':
    print(f'{gcd2(45, 30) = }')
    print(f'{gcd2(6307, 1995) = }')
    print(f'{gcd2(42, 56) = }')
    print(f'{gcd2(99, 98) = }')
    print(f'{coprimes(99, 98) = }')
    print(f'{coprimes(42, 56) = }')
    print(f'{gcd(45, 30, 20, 100) = }')
    print(f'{lcm(15, 20) = }')
    print(f'{lcm(10, 20) = }')
