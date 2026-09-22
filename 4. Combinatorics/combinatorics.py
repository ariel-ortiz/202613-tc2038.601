from pprint import pprint


def nicely_sorted[T](s: list[list[T]]) -> list[list[T]]:

    def size_and_content(value: list[T]) -> tuple[int, list[T]]:
        return (len(value), value)

    return sorted(s, key=size_and_content)


# Complexity: O(2 ^ N)
def power_set[T](s: list[T]) -> list[list[T]]:
    if not s:
        return [[]]
    temp: list[list[T]] = power_set(s[:-1]) # butlast of s
    return temp + [e + [s[-1]] for e in temp]


def combinations[T](s: list[T], k: int) -> list[list[T]]:
    return [t for t in power_set(s) if len(t) == k]


def insert[T](x: T, s: list[T], i: int) -> list[T]:
    return s[:i] + [x] + s[i:]


def insert_everywhere[T](x: T, s: list[T]) -> list[list[T]]:
    return [insert(x, s, i) for i in range(len(s) + 1)]


def permute[T](s: list[T]) -> list[list[T]]:
    if not s:
        return [[]]
    empty: list[list[T]] = []
    return sum([insert_everywhere(s[-1], t) for t in permute(s[:-1])], empty)


if __name__ == '__main__':
    pprint(power_set([]))  # type: ignore
    pprint(power_set([1]))
    pprint(power_set(['a', 'b']))
    pprint(power_set(['a', 'b', 'c']))
    pprint(nicely_sorted(power_set(['a', 'b', 'c', 'd'])))
    pprint(sorted(combinations([1, 2, 3, 4], 2)))
    pprint(sorted(combinations([1, 2, 3, 4], 1)))
    pprint(sorted(combinations([1, 2, 3, 4], 3)))
    pprint(sorted(combinations([1, 2, 3, 4], 4)))
    pprint(insert(7, [1, 2, 3], 0))
    pprint(insert(7, [1, 2, 3], 1))
    pprint(insert(7, [1, 2, 3], 2))
    pprint(insert(7, [1, 2, 3], 3))
    pprint(insert_everywhere(7, [1, 2, 3, 4, 5, 6]))
    pprint(sorted(permute([1, 2, 3])))
    pprint(sorted(permute([1, 2, 3, 4])))
