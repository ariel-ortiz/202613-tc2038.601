from typing import Any, Iterator
from collections import deque


type Tree = list[Any] | None


# Complexity: O(N)
def in_order(root: Tree) -> Iterator[Any]:
    if root is None:
        return
    # for e in in_order(root[1]):
    #     yield e
    yield from in_order(root[1])

    yield root[0]

    # for e in in_order(root[2]):
    #     yield e
    yield from in_order(root[2])


# Complexity: O(N)
def pre_order(root: Tree) -> Iterator[Any]:
    if root is None:
        return
    yield root[0]
    yield from pre_order(root[1])
    yield from pre_order(root[2])


# Complexity: O(N)
def post_order(root: Tree) -> Iterator[Any]:
    if root is None:
        return
    yield from post_order(root[1])
    yield from post_order(root[2])
    yield root[0]


# Complexity: O(N)
def level_order(root: Tree) -> Iterator[Any]:
    queue: deque[Tree] = deque()
    queue.append(root)
    while queue:
        current: Tree = queue.popleft()
        if current is not None:
            value, left, right = current
            yield value
            queue.append(left)
            queue.append(right)


if __name__ == '__main__':
    t: Tree = [5,
               [3, 
                [1, None, None],
                [4, None, None]],
               [8, 
                [7, 
                 [6, None, None],
                 None],
                [9, None, None]]]
    print(list(in_order(t)))
    print(list(pre_order(t)))
    print(list(post_order(t)))
    print(list(level_order(t)))