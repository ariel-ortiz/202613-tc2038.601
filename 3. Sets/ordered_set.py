from typing import cast
from collections.abc import Iterator, Iterable


class OrderedSet[T]:

    class Node[N]:

        info: N
        prev: OrderedSet.Node[N]
        next: OrderedSet.Node[N]

        # Complexity: O(1)
        def __init__(self, value: N) -> None:
            self.info = value
            self.prev = self
            self.next = self

    __sentinel: OrderedSet.Node[T]
    __count: int

    # Complexity: O(N) where N = len(values)
    def __init__(self, values: Iterable[T] = ()) -> None:
        self.__sentinel = OrderedSet.Node(cast(T, None))
        self.__count = 0
        for elem in values:
            self.add(elem)

    # Complexity: O(1)
    def __len__(self) -> int:
        return self.__count

    # Complexity: O(N)
    def __repr__(self) -> str:
        return f'OrderedSet({list(self) if self else ""})'

    # Complexity: O(N)
    def add(self, value: T) -> None:
        if value in self:
            return
        self.__count += 1
        new_node: OrderedSet.Node[T] = OrderedSet.Node(value)
        new_node.prev = self.__sentinel.prev
        new_node.next = self.__sentinel
        self.__sentinel.prev.next = new_node
        self.__sentinel.prev = new_node

    # Complexity: O(N)
    def __iter__(self) -> Iterator[T]:
        current: OrderedSet.Node[T] = self.__sentinel.next
        while current is not self.__sentinel:
            yield current.info
            current = current.next

    # Complexity: O(N)
    def __contains__( self, value: object) -> bool:
        for elem in self:
            if elem == value:
                return True
        return False


if __name__ == '__main__':
    a: OrderedSet[int] = OrderedSet([4, 8, 15, 16, 23])
    print(len(a))
    print(a)
    for i in a:
        print(i)
    print(list(a))
    b: OrderedSet[str] = OrderedSet('hello')
    print(b)
    print(4 in b)
    print('e' in b)
