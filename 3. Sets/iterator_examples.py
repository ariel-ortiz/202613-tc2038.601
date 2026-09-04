from collections.abc import Iterator

a: list[int] = [4, 8, 15, 16, 23, 42]
b: str = 'Hello'
c: tuple[float, ...] = (3.14, 2.78, 1.69, 1.41)

for elem in a:
    print(elem)

print()

it1: Iterator[int] = iter(a)
print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))
# print(next(it1))

print()

it2: Iterator[str] = iter(b)
try:
    while True:
        print(next(it2))
except StopIteration:
    ...

print()

for n in c:
    print(n)

print()

it3: Iterator[float] = iter(c)
try:
    while True:
        print(next(it3))
except StopIteration:
    ...

print()

class CountDown:

    current: int

    def __init__(self, value: int) -> None:
        self.current = value

    def __iter__(self) -> Iterator[int]:
        return self

    def __next__(self) -> int:
        if self.current < 0:
            raise StopIteration
        result: int = self.current
        self.current -= 1
        return result

it4: Iterator[int] = iter(CountDown(3))
print(next(it4))
print(next(it4))
print(next(it4))
print(next(it4))
# print(next(it4))

print()

for i in CountDown(10):
    print(i)

print()

def generator_example() -> Iterator[int]:
    x: int = 5
    yield x
    x *= 2
    yield x
    x += 1
    yield x

it5: Iterator[int] = generator_example()
print(next(it5))
print(next(it5))
print(next(it5))
# print(next(it5))

print()

for i in generator_example():
    print(i)

def count_down(value: int) -> Iterator[int]:
    while value >= 0:
        yield value
        value -= 1

print()

it6: Iterator[int] = count_down(3)
print(next(it6))
print(next(it6))
print(next(it6))
print(next(it6))
# print(next(it6))

for i in count_down(10):
    print(i)
