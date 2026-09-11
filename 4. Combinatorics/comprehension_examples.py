from pprint import pprint
from typing import Iterator


# Example of a list comprehension
print([2 ** n for n in range(100) if 2 ** n < 100])

# The previous example is the same as:
result: list[int] = []
for n in range(100):
    if 2 ** n < 100:
        result.append(2 ** n)
print(result)

# Example of a set comprehension
print({c.upper() for c in 'Hello, World!' if c.isalpha()})

# Example of a dict comprehension
print({n: 2 ** n for n in range(11)})

# Example of a generator comprehension
g: Iterator[int] = (2 ** n for n in range(1_000_000_000))
print(next(g))
print(next(g))
print(next(g))
for i in g:
    if i > 100:
        break
    print(i)

a: list[int] = [1, 2, 3, 4]
b: list[str] = ['a', 'b', 'c']
pprint([(x, y) for x in a for y in b])

pprint([(x, y, z) for x in range(2) for y in range(2) for z in range(2)])

# Print all Pythagorean triples less of equal to 100
pprint([(a, b, c) for a in range(1, 101)
                  for b in range(1, 101)
                  for c in range(1, 101)
                  if a < b < c <= 100 and a ** 2 + b ** 2 == c ** 2])
