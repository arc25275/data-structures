# Name: Alex Clark
# OSU Email: clarka8@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Assignment 5 - Minimum Heap
# Due Date: 3/3/2024
# Description: Implement a minimum heap data structure

from dynamic_array import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initialize a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        heap_data = [self._heap[i] for i in range(self._heap.length())]
        return 'HEAP ' + str(heap_data)

    def add(self, node: object) -> None:
        """Add a value to the minimum heap"""
        self._heap.append(node)
        node_index = self.size() - 1
        parent_index = parent(node_index)
        # Loop until parent is out of index
        while parent_index >= 0 and node < self._heap[parent_index]:
            swap(self._heap, node_index, parent_index)
            node_index = parent_index
            parent_index = parent(node_index)

    def is_empty(self) -> bool:
        """Check if heap is empty"""
        return True if self.size() == 0 else False

    def get_min(self) -> object:
        """Return minimum value"""
        if self.is_empty():
            raise MinHeapException
        return self._heap[0]

    def remove_min(self) -> object:
        """Remove minimum value from heap"""
        # Base cases
        if self.is_empty():
            raise MinHeapException
        if self.size() == 1:
            return self._heap.pop()
        # Swap first and last, and remove min
        swap(self._heap, 0, self.size()-1)
        value = self._heap.pop()
        _percolate_down(self._heap, 0, self.size())
        return value

    def build_heap(self, da: DynamicArray) -> None:
        """Turn an unsorted array into a heap"""
        self._heap = DynamicArray(da)
        # First non leaf
        index = self.size() // 2 - 1
        while index >= 0:
            _percolate_down(self._heap, index, da.length())
            index -= 1

    def size(self) -> int:
        """Return size of heap"""
        return self._heap.length()

    def clear(self) -> None:
        """Remove all values from heap"""
        self._heap = DynamicArray()


def swap(da: DynamicArray, index_1: int, index_2: int):
    temp = da[index_1]
    da[index_1] = da[index_2]
    da[index_2] = temp


def parent(i: int) -> int:
    """Return parent index"""
    return (i - 1) // 2


def left_child(i: int) -> int:
    """Return left child index"""
    return 2 * i + 1


def right_child(i: int) -> int:
    """Return left child index"""
    return 2 * i + 2


def _percolate_down(da: DynamicArray, index: int, end: int) -> None:
    """Percolate value downwards in heap"""
    value = da[index]
    while index < end:
        # Set index values of children
        left = left_child(index)
        right = right_child(index)
        # Make sure children are not out of bounds
        if left >= end:
            break
        # Find min child index, and swap value with it
        min_child = left
        if right < end and da[right] < da[left]:
            min_child = right
        if da[min_child] < value:
            swap(da, index, min_child)
            index = min_child
        else:
            break


def heapsort(da: DynamicArray) -> None:
    """
    TODO: Write this implementation
    """
    index = da.length() // 2 - 1
    while index >= 0:
        _percolate_down(da, index, da.length())
        index -= 1
    k = da.length() - 1
    while k >= 0:
        swap(da, 0, k)
        _percolate_down(da, 0, k)
        k -= 1



# ------------------- BASIC TESTING -----------------------------------------


if __name__ == '__main__':

    print("\nPDF - add example 1")
    print("-------------------")
    h = MinHeap()
    print(h, h.is_empty())
    for value in range(300, 200, -15):
        h.add(value)
        print(h)

    print("\nPDF - add example 2")
    print("-------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
        h.add(value)
        print(h)

    print("\nPDF - is_empty example 1")
    print("-------------------")
    h = MinHeap([2, 4, 12, 56, 8, 34, 67])
    print(h.is_empty())

    print("\nPDF - is_empty example 2")
    print("-------------------")
    h = MinHeap()
    print(h.is_empty())

    print("\nPDF - get_min example 1")
    print("-----------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    print(h.get_min(), h.get_min())

    print("\nPDF - remove_min example 1")
    print("--------------------------")
    h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    while not h.is_empty() and h.is_empty() is not None:
        print(h, end=' ')
        print(h.remove_min())

    print("\nPDF - build_heap example 1")
    print("--------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    h = MinHeap(['zebra', 'apple'])
    print(h)
    h.build_heap(da)
    print(h)

    print("--------------------------")
    print("Inserting 500 into input DA:")
    da[0] = 500
    print(da)

    print("Your MinHeap:")
    print(h)
    if h.get_min() == 500:
        print("Error: input array and heap's underlying DA reference same object in memory")

    print("\nPDF - heapsort example 1")
    print("------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")

    print("\nPDF - heapsort example 1")
    print("------------------------")
    da = DynamicArray([-84002, -76400, 52061, 5311, 78436])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")

    print("\nPDF - heapsort example 2")
    print("------------------------")
    da = DynamicArray(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")

    print("\nPDF - size example 1")
    print("--------------------")
    h = MinHeap([100, 20, 6, 200, 90, 150, 300])
    print(h.size())

    print("\nPDF - size example 2")
    print("--------------------")
    h = MinHeap([])
    print(h.size())

    print("\nPDF - clear example 1")
    print("---------------------")
    h = MinHeap(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    print(h)
    print(h.clear())
    print(h)
