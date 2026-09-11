from pprint import pprint


# Complexity: O(2 ^ N)
def power_set[T](s: list[T]) -> list[list[T]]:
    if not s:
        return [[]]
    temp: list[list[T]] = power_set(s[:-1]) # butlast of s
    return temp + [e + [s[-1]] for e in temp]


if __name__ == '__main__':
    pprint(power_set([]))  # type: ignore
    pprint(power_set([1]))
    pprint(power_set(['a', 'b']))
    pprint(power_set(['a', 'b', 'c']))
    pprint(power_set(['a', 'b', 'c', 'd']))
