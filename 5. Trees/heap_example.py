# type: ignore

from heapq import heappush, heappop  # Uses a min-heap
from heapq import heappush_max, heappop_max  # Uses a max-heap

# Complexity: O(N log N)
def heap_sort(data):

    # Create the heap
    heap = []
    for elem in data:
        heappush(heap, elem)

    # Remove one element at a time from the heap
    result = []
    while heap:
        result.append(heappop(heap))

    return result


# Complexity: O(N log N)
def heap_sort_reversed(data):

    # Create the heap
    heap = []
    for elem in data:
        heappush_max(heap, elem)

    # Remove one element at a time from the heap
    result = []
    while heap:
        result.append(heappop_max(heap))

    return result


if __name__ == '__main__':
    # heap = []
    # heappush(heap, 5)
    # print(heap)
    # heappush(heap, 1)
    # print(heap)
    # heappush(heap, 3)
    # print(heap)
    # heappush(heap, 2)
    # print(heap)
    # heappush(heap, 0)
    # print(heap)
    # print(heappop(heap))
    # print(heap)
    # print(heappop(heap))
    # print(heap)
    # print(heappop(heap))
    # print(heap)
    # print(heappop(heap))
    # print(heap)
    # print(heappop(heap))
    # print(heap)
    print(heap_sort([5, 13, 26, 17, 2, 8, 10, 1, 20]))
    print(heap_sort_reversed([5, 13, 26, 17, 2, 8, 10, 1, 20]))


