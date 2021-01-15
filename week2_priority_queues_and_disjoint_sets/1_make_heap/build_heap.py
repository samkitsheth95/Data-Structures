import math
from typing import List


def leftChild(i: int) -> int:
    return 2 * i + 1


def rightChild(i: int) -> int:
    return 2 * i + 2


def shiftDown(data: List[int], i: int, swaps: List[List[int]], n: int) -> None:
    minIndex = i
    l = leftChild(i)
    r = rightChild(i)
    if l < n and data[l] < data[minIndex]:
        minIndex = l
    if r < n and data[r] < data[minIndex]:
        minIndex = r
    if minIndex != i:
        data[i], data[minIndex] = data[minIndex], data[i]
        swaps.append([i, minIndex])
        shiftDown(data, minIndex, swaps, n)


def build_heap(data: List[int]) -> List[List[int]]:
    """Build a heap from ``data`` inplace.
    Returns a sequence of swaps performed by the algorithm.
    """
    n = len(data)
    swaps = []
    for i in range(int((n-1)/2), -1, -1):
        shiftDown(data, i, swaps, n)
    return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
